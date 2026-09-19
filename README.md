# PTIT Online Judge — Trình chấm bài tự động

Bài tập lớn môn **Lập trình hướng đối tượng**. Backend viết bằng **Java thuần** (JDK 11+) với **đúng một thư viện ngoài duy nhất là `com.mysql:mysql-connector-j`** — máy chủ HTTP, bộ xử lý JSON, băm mật khẩu và quản lý phiên đều tự viết trên API chuẩn của JDK, dùng **JDBC trực tiếp** (không Spring Boot, không Hibernate, không ORM). Giao diện có 2 lựa chọn: **console** và **web** (React 19 + TypeScript, thiết kế từ Figma Make).

Tài khoản, mật khẩu (đã băm), lịch sử nộp bài, mã nguồn, kết quả từng test, bảng xếp hạng, thống kê verdict và số bài đã giải được lưu trong **MySQL 8**. Đề bài và testcase vẫn nằm trong `data/problems/`.

Hệ thống nhận mã nguồn của thí sinh, biên dịch, chạy trên từng test với giới hạn thời gian, so sánh output với đáp án và trả về verdict: **AC / WA / TLE / MLE / RE / CE**.

## Yêu cầu

| Thành phần | Bắt buộc? | Ghi chú |
|---|---|---|
| **JDK 11+** | có | biên dịch và chạy backend |
| **MySQL 8.0+** | chỉ khi cần lưu lâu dài | `--demo`, `--selftest` và `--no-db` chạy hoàn toàn trong RAM nên không cần — xem [Demo không cần MySQL](#demo-không-cần-mysql) |
| **Node.js + npm** | chỉ khi dùng giao diện web | build frontend |
| **Maven** | không | có thì tiện; không có thì script tự tải Connector/J về `lib/` |

## Cài đặt lần đầu

### 1. Tạo cơ sở dữ liệu và tài khoản ứng dụng

Mở `database/mysql/01_create_database.sql`, **đổi `THAY_MAT_KHAU_NAY` thành mật khẩu thật của bạn**, rồi chạy bằng tài khoản quản trị MySQL:

```bash
mysql -u root -p < database/mysql/01_create_database.sql
```

Script tạo:

- `online_judge` — cơ sở dữ liệu thật, `utf8mb4` / `utf8mb4_0900_ai_ci`;
- `online_judge_test` — cơ sở dữ liệu riêng cho `--apitest`;
- tài khoản **`oj_app`** với đúng những quyền cần dùng (`SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, INDEX, REFERENCES, CREATE VIEW`).

Ứng dụng **không bao giờ chạy bằng `root`**.

Bảng và VIEW thì **không cần tạo tay**: lớp `MySqlSchemaInitializer` tự tạo lúc khởi động, chạy lại bao nhiêu lần cũng an toàn và không xoá dữ liệu cũ. Bản SQL tham chiếu nằm ở `database/mysql/02_schema.sql` nếu bạn muốn xem hoặc chạy tay.

### 2. Cấu hình biến môi trường

Chép file mẫu rồi điền mật khẩu vừa đặt ở bước 1:

```bash
cp .env.example .env
```

Trên Windows PowerShell:

```bash
Copy-Item .env.example .env
```

Nội dung cần sửa trong `.env`:

| Biến | Dùng để |
|---|---|
| `OJ_DB_URL` | URL JDBC tới `online_judge` |
| `OJ_DB_USER` | `oj_app` |
| `OJ_DB_PASSWORD` | mật khẩu đặt ở bước 1 |
| `OJ_TEST_DB_URL` | URL JDBC tới `online_judge_test` (tên **bắt buộc** kết thúc bằng `_test`) |
| `OJ_TEST_DB_USER` / `OJ_TEST_DB_PASSWORD` | tài khoản cho cơ sở dữ liệu kiểm thử |
| `OJ_ADMIN_PASSWORD` | mật khẩu admin lần đầu (bỏ trống thì hệ thống tự sinh) |
| `OJ_SEED_PASSWORD` | mật khẩu chung của 4 tài khoản mẫu |

URL mẫu cho máy local:

```
jdbc:mysql://localhost:3306/online_judge?useUnicode=true&characterEncoding=UTF-8&serverTimezone=UTC&useSSL=false&allowPublicKeyRetrieval=true
```

`.env` đã nằm trong `.gitignore`. **Không có mật khẩu nào được hard-code trong Java, `pom.xml`, script hay README.** Nếu thích, bạn có thể bỏ hẳn `.env` và dùng biến môi trường thật (`export` / `$env:`) — biến môi trường luôn được ưu tiên hơn file `.env`.

## Chạy nhanh

| Hệ điều hành | Console | Web | Toàn bộ kiểm thử |
|---|---|---|---|
| Windows PowerShell | `run.ps1` | `run-web.ps1` | `run-tests.ps1` |
| Windows cmd | `run.bat` | `run-web.bat` | `run-tests.bat` |
| Linux / macOS | `./run.sh` | `./run-web.sh` | `./run-tests.sh` |

Windows:

```bash
powershell -ExecutionPolicy Bypass -File run-web.ps1
```

Linux / macOS (lần đầu cần cấp quyền thực thi):

```bash
chmod +x run.sh run-web.sh run-tests.sh && ./run-web.sh
```

Rồi mở http://localhost:8080. Đổi cổng: `./run-web.sh 9000` hoặc `run-web.ps1 -Port 9000`.

### Demo không cần MySQL

Cờ `--no-db` cho **đầy đủ tính năng** — đăng ký, đăng nhập, phân quyền, nộp bài, chấm, bảng xếp hạng, thống kê verdict, quản trị đề bài — mà không mở một kết nối cơ sở dữ liệu nào:

| Hệ điều hành | Console | Web |
|---|---|---|
| Windows PowerShell | `run.ps1 --no-db` | `run-web.ps1 -NoDb` |
| Windows cmd | `run.bat --no-db` | `run-web.bat --no-db` |
| Linux / macOS | `./run.sh --no-db` | `./run-web.sh --no-db` |

Đánh đổi duy nhất: tài khoản và lịch sử nộp bài nằm trong RAM nên **mất khi tắt chương trình**. Đề bài vẫn đọc và ghi ở `data/problems/` nên còn nguyên, kể cả bài do admin tạo lúc đang chạy.

Mật khẩu vẫn băm bằng PBKDF2 **120 000 vòng** như bản chạy thật — chỉ `--demo` và `--selftest` hạ xuống 1 000 vòng cho nhanh, vì hai chế độ đó không ai đăng nhập. Do bảng tài khoản trống ở mỗi lần chạy, hệ thống tạo lại 4 tài khoản mẫu (mật khẩu `ptit@2026`) và in mật khẩu admin **mới mỗi lần**. Muốn cố định thì đặt biến môi trường trước khi chạy:

```bash
$env:OJ_ADMIN_PASSWORD = "MatKhauCuaBan@2026"
```

Dùng khi nào: demo trên máy chưa cài MySQL, hoặc làm phương án dự phòng nếu MySQL không lên được đúng lúc bảo vệ. Riêng `--apitest` **không** chạy được với `--no-db` (thoát với mã 2) vì nó kiểm thử đúng cái tầng JDBC vừa bị bỏ đi.

Chỗ này cũng là ví dụ sống của Repository pattern: `ConsoleApp` và `ApiServer` chỉ phụ thuộc `JudgeService`, nên đổi kho dữ liệu chỉ là đổi `JudgeService.mysql()` thành `JudgeService.inMemory()` tại **một chỗ duy nhất** trong `Main.java` — không sửa một dòng nào trong hai tầng giao diện.

Lần chạy đầu tiên script tự tải `mysql-connector-j` về thư mục `lib/` (ưu tiên Maven nếu máy có cài, không thì tải thẳng từ Maven Central). Tải một lần rồi các lần sau chạy được offline.

Cài toolchain trên Ubuntu/Debian nếu muốn chấm đủ 6 ngôn ngữ:

```bash
sudo apt install default-jdk nodejs npm g++ python3 golang rustc
```

### Các chế độ của backend

| Tham số | Ý nghĩa | Cần MySQL? |
|---|---|---|
| *(không có)* | Menu console — **bắt buộc đăng nhập bằng mật khẩu** | có (`online_judge`) |
| `--no-db` | **Đầy đủ tính năng** (menu console, hoặc giao diện web nếu kèm `--serve`) nhưng tài khoản và lịch sử nộp bài nằm trong RAM | không (RAM) |
| `--demo` | Tự động chấm loạt bài nộp mẫu theo `data/submissions/demo-plan.txt` | không (RAM) |
| `--selftest` | Như `--demo` nhưng **đối chiếu verdict thực tế với verdict kỳ vọng**, exit code 0 nếu tất cả khớp | không (RAM) |
| `--apitest` | Bộ kiểm thử tích hợp: MySQL + đăng ký / đăng nhập / phân quyền / quản trị đề / khởi động lại | có (`*_test`) |
| `--serve` / `--serve=9000` | Mở REST API + giao diện web tại `http://localhost:8080` | có (`online_judge`), trừ khi kèm `--no-db` |
| `--data=...`, `--web=...` | Trỏ tới thư mục dữ liệu / thư mục frontend đã build khác | |
| `--db-url=jdbc:mysql://...` | Ghi đè `OJ_DB_URL` cho một lần chạy | |

**Mật khẩu không bao giờ nhận qua dòng lệnh** (để không lọt vào lịch sử shell hay danh sách tiến trình) — chỉ qua biến môi trường / `.env`.

`--demo` và `--selftest` dùng kho dữ liệu **trong bộ nhớ**, không mở kết nối MySQL nào, nên chạy bao nhiêu lần cũng không làm bẩn dữ liệu thật.

Máy chủ nạp đề bài **một lần lúc khởi động** (trừ bài do admin tạo qua API — bài đó được nạp ngay lập tức), nên sửa tay `statement.txt` hoặc thêm test thì phải khởi động lại mới thấy.

## Maven và thư viện MySQL

Project có `pom.xml` nhưng **giữ nguyên cấu trúc thư mục cũ** thay vì ép theo chuẩn Maven:

```xml
<sourceDirectory>src</sourceDirectory>     <!-- không phải src/main/java -->
<outputDirectory>out</outputDirectory>     <!-- đúng thư mục các script vẫn dùng -->
<maven.compiler.release>11</maven.compiler.release>
```

Dependency ngoài **duy nhất**:

```xml
<dependency>
  <groupId>com.mysql</groupId>
  <artifactId>mysql-connector-j</artifactId>
  <version>8.4.0</version>
</dependency>
```

Bản 8.4.0 là bản ổn định, chạy tốt trên JDK 11 và MySQL 8.x, và không kéo theo thư viện bắt buộc nào khác (`protobuf` chỉ cần cho X DevAPI nên ở phạm vi `provided`) — classpath khi chạy chỉ có đúng một file jar.

Ba cách lấy thư viện — chọn cách nào cũng được. Có Maven thì:

```bash
mvn -q clean compile
```

Chỉ muốn tải thư viện, không biên dịch:

```bash
mvn -q dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime
```

Hoặc **không cần cài Maven** — đây là cách mặc định, script tự lo:

```bash
powershell -ExecutionPolicy Bypass -File run.ps1
```

Chạy tay sau khi đã biên dịch:

```bash
java -Dfile.encoding=UTF-8 -cp "out;lib/*" com.ptit.oj.Main --serve
```

Trên Linux/macOS đổi `;` thành `:` trong classpath.

## Cơ sở dữ liệu MySQL

Kết nối do `MySqlDatabaseManager` quản lý. Lớp này **không giữ một `Connection` toàn cục**: mỗi thao tác tự mở một kết nối bằng `DriverManager` rồi đóng ngay bằng try-with-resources, nên `HttpServer` chạy nhiều thread song song không bao giờ đâm nhau. Lúc khởi động, `testConnection()` chạy `SELECT 1` để báo lỗi sớm và rõ ràng thay vì để hỏng giữa chừng. Mọi `SQLException` được bọc thành `DataAccessException` với thông báo tiếng Việt nói rõ phải sửa gì, và **không bao giờ in mật khẩu**.

### Lược đồ

```sql
CREATE TABLE users (
    id                  VARCHAR(64)  NOT NULL,
    username            VARCHAR(32)  NOT NULL,
    full_name           VARCHAR(150) NOT NULL,
    role                VARCHAR(20)  NOT NULL,
    student_code        VARCHAR(30)      NULL,   -- chỉ STUDENT
    class_name          VARCHAR(50)      NULL,   -- chỉ STUDENT
    department          VARCHAR(150)     NULL,   -- chỉ TEACHER
    password_hash       VARCHAR(255) NOT NULL,   -- PBKDF2-HMAC-SHA256, Base64
    password_salt       VARCHAR(255) NOT NULL,   -- 16 byte ngẫu nhiên, Base64
    password_iterations INT UNSIGNED NOT NULL,
    created_at          DATETIME(6)  NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    PRIMARY KEY (id),
    UNIQUE KEY uq_users_username (username),
    CONSTRAINT chk_users_role CHECK (role IN ('STUDENT','TEACHER','ADMIN'))
) ENGINE = InnoDB
  DEFAULT CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE submissions (
    id             VARCHAR(64)     NOT NULL,     -- "SUB-" + UUID
    user_id        VARCHAR(64)     NOT NULL,
    problem_id     VARCHAR(30)     NOT NULL,
    problem_title  VARCHAR(255)    NOT NULL,     -- bản chụp tên đề tại lúc nộp
    language       VARCHAR(40)     NOT NULL,
    file_name      VARCHAR(255)    NOT NULL,
    source_code    LONGTEXT        NOT NULL,     -- mã nguồn thật
    submitted_at   DATETIME(6)     NOT NULL,
    verdict        VARCHAR(20)     NOT NULL,
    score          DECIMAL(12,4)   NOT NULL DEFAULT 0,
    max_points     DECIMAL(12,4)   NOT NULL DEFAULT 0,
    max_runtime_ms BIGINT UNSIGNED NOT NULL DEFAULT 0,
    judge_time_ms  BIGINT UNSIGNED NOT NULL DEFAULT 0,
    global_message TEXT            NOT NULL,
    PRIMARY KEY (id),
    KEY idx_submissions_user_time   (user_id, submitted_at),
    KEY idx_submissions_user_solved (user_id, verdict, problem_id),
    KEY idx_submissions_problem     (problem_id),
    KEY idx_submissions_verdict     (verdict),
    KEY idx_submissions_time        (submitted_at),
    CONSTRAINT fk_submissions_user FOREIGN KEY (user_id)
        REFERENCES users (id) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE test_case_results (
    submission_id VARCHAR(64)     NOT NULL,
    test_case_id  VARCHAR(100)    NOT NULL,
    ordinal       INT UNSIGNED    NOT NULL,
    sample        BOOLEAN         NOT NULL DEFAULT FALSE,
    verdict       VARCHAR(20)     NOT NULL,
    runtime_ms    BIGINT UNSIGNED NOT NULL DEFAULT 0,
    earned_points DECIMAL(12,4)   NOT NULL DEFAULT 0,
    message       TEXT            NOT NULL,
    PRIMARY KEY (submission_id, test_case_id),
    KEY idx_test_results_order (submission_id, ordinal),
    CONSTRAINT fk_test_results_submission FOREIGN KEY (submission_id)
        REFERENCES submissions (id) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;

CREATE VIEW user_stats AS
SELECT u.id       AS user_id,
       u.username AS username,
       (SELECT COUNT(DISTINCT s.problem_id) FROM submissions s
         WHERE s.user_id = u.id AND s.verdict = 'AC') AS solved_count,
       (SELECT COUNT(*) FROM submissions s
         WHERE s.user_id = u.id)                      AS submission_count
  FROM users u;
```

Vài điểm cần biết:

- **`username` không phân biệt hoa thường** nhờ collation `utf8mb4_0900_ai_ci`, nên `UNIQUE` tự động coi `Admin` và `admin` là trùng nhau.
- **Khoá ngoại được InnoDB thực thi thật sự** — không cần bật gì thêm ở từng kết nối. Xoá một bài nộp thì kết quả test bay theo; xoá một tài khoản thì cả bài nộp lẫn kết quả test bay theo.
- **`DATETIME(6)` đọc/ghi bằng `LocalDateTime`** (`setObject` / `getObject`) chứ không phải `Timestamp`: `Timestamp` là một mốc thời gian tuyệt đối nên driver sẽ quy đổi theo `serverTimezone` và làm lệch giờ hiển thị, còn `LocalDateTime` giữ đúng giá trị như trong cơ sở dữ liệu.
- **`DECIMAL(12,4)` đọc/ghi bằng `BigDecimal`**, `BOOLEAN` bằng `setBoolean`/`getBoolean`, `COUNT` và `BIGINT` bằng `long`.
- **Ghi đè bằng `INSERT ... ON DUPLICATE KEY UPDATE`**, sắp xếp bằng `(submitted_at, id)` — MySQL không có `rowid` ẩn như SQLite.
- Index khai báo ngay trong `CREATE TABLE` vì MySQL **không hỗ trợ `CREATE INDEX IF NOT EXISTS`**. VIEW thì hỏi `information_schema` trước rồi mới tạo, vì `CREATE OR REPLACE VIEW` đòi quyền `DROP` mà tài khoản ứng dụng cố ý không được cấp.

### Quy tắc tính "số bài đã giải"

```sql
solvedCount = COUNT(DISTINCT problem_id) WHERE verdict = 'AC'
```

Cố ý **không có cột `solved_count`** trong bảng `users`: một cột như thế phải cập nhật bằng tay ở mọi nơi ghi dữ liệu và sẽ lệch ngay khi quên một chỗ. Thay vào đó VIEW `user_stats` tính lại từ bảng `submissions` mỗi lần đọc, nên con số **luôn đúng theo định nghĩa**:

- nộp AC **5 lần cho cùng một bài** → vẫn tính là **1** (nhờ `DISTINCT`);
- AC hai bài khác nhau → **2**;
- nộp WA rồi mới AC → tính 1 (đã từng AC là được).

Phân biệt với cột **AC** trên bảng xếp hạng: cột đó đếm số bài đạt **điểm tối đa**, còn `solvedCount` đếm số bài **từng có ít nhất một lần nộp AC**.

### Giao dịch (transaction)

`MySqlSubmissionRepository.saveWithResults()` ghi một bài nộp trong **một transaction duy nhất**:

1. mở `Connection`, `setAutoCommit(false)`;
2. `INSERT ... ON DUPLICATE KEY UPDATE` vào `submissions`;
3. `DELETE FROM test_case_results WHERE submission_id = ?` — bỏ các kết quả test cũ không còn tồn tại;
4. `executeBatch()` ghi lại toàn bộ `test_case_results`;
5. `commit()` nếu thành công, `rollback()` nếu bất kỳ bước nào lỗi;
6. đóng `Connection` trong `finally`.

Vì thế **không bao giờ tồn tại bài nộp thiếu mất kết quả test**. Mọi câu lệnh đều dùng `PreparedStatement` (chống SQL injection) và `try-with-resources`.

### Không đưa cấu hình lên git

`.env` chứa mật khẩu cơ sở dữ liệu nên đã nằm trong `.gitignore`, cùng với `lib/`, `out/`, `target/`. Bản mẫu **không có mật khẩu thật** là `.env.example` (file này thì có commit).

## Đăng nhập, đăng ký và phân quyền

### Ba vai trò

| Vai trò | Nộp bài | Xem lịch sử | Tạo đề bài | Cách có tài khoản |
|---|---|---|---|---|
| `STUDENT` | có | **chỉ của chính mình** | không | tự đăng ký ở màn hình đăng nhập |
| `TEACHER` | có | toàn hệ thống (chỉ đọc) | không | do quản trị tạo sẵn (tài khoản mẫu `gvthanh`) |
| `ADMIN` | có | toàn hệ thống | **có** | tạo tự động lần đầu chạy máy chủ |

Chỉ `Admin.canCreateProblem()` trả `true`; `Student` và `Teacher` kế thừa `false` từ `User`. Backend kiểm tra vai trò ở **mọi** endpoint `/api/admin/*` — ẩn nút trên frontend chỉ cho gọn mắt, không phải biện pháp bảo mật.

### Lấy mật khẩu admin lần đầu

Lần đầu chạy `run-web.ps1` (hoặc `run.ps1`), nếu trong CSDL **chưa có tài khoản ADMIN nào**, chương trình tạo tài khoản `admin` và in mật khẩu ra terminal **đúng một lần**:

```
==================================================
 ĐÃ TẠO TÀI KHOẢN QUẢN TRỊ
   Tên đăng nhập: admin
   Mật khẩu     : dnhH0V66sEOKYQyJbb3iyil0
   (chỉ hiện DUY NHẤT lần này - hãy chép lại ngay;
    cơ sở dữ liệu chỉ lưu chuỗi băm, không lưu mật khẩu)
==================================================
```

Chép lại ngay. Muốn tự chọn mật khẩu thì đặt biến môi trường **trước** lần chạy đầu tiên. PowerShell:

```bash
$env:OJ_ADMIN_PASSWORD = "MatKhauCuaBan@2026"
```

Linux / macOS:

```bash
export OJ_ADMIN_PASSWORD="MatKhauCuaBan@2026"
```

Những lần chạy sau **không bao giờ đặt lại** mật khẩu admin. Lỡ quên thì xoá dòng admin trong bảng `users` rồi chạy lại:

```bash
mysql -u oj_app -p online_judge -e "DELETE FROM users WHERE role = 'ADMIN';"
```

### Tài khoản mẫu

Khi bảng `users` còn hoàn toàn trống, hệ thống tạo 4 tài khoản mẫu để giữ được bộ demo cũ: `hiennm`, `lananh`, `tuanpv` (STUDENT) và `gvthanh` (TEACHER). Mật khẩu chung mặc định là **`ptit@2026`**, đổi được bằng biến môi trường `OJ_SEED_PASSWORD`. Bốn tài khoản này dùng chung một mật khẩu nhưng **muối băm khác nhau** nên `password_hash` trong CSDL hoàn toàn khác nhau.

### Cách mật khẩu được bảo vệ

| Yêu cầu | Cách làm |
|---|---|
| Không lưu plaintext | `PasswordService` chỉ trả về `Credentials` (hash + salt + số vòng lặp) |
| Thuật toán | `PBKDF2WithHmacSHA256`, **120 000 vòng**, khoá 256 bit |
| Muối | 16 byte từ `SecureRandom`, **riêng cho từng tài khoản** → chống rainbow table |
| Lưu trữ | hash và salt mã hoá **Base64** |
| So sánh | `MessageDigest.isEqual()` — thời gian hằng số, không rò rỉ qua thời gian phản hồi |
| Độ dài | tối thiểu **8**, tối đa **128** ký tự (chặn trên để request không bắt máy chủ băm chuỗi khổng lồ) |
| Dọn bộ nhớ | `Arrays.fill(..., 0)` mảng byte/char sau khi băm xong |

Sai tên đăng nhập và sai mật khẩu trả về **cùng một thông báo** để không lộ tài khoản nào đang tồn tại.

### Phiên đăng nhập

Token sinh bằng `SecureRandom` 32 byte, mã hoá Base64-URL, **hết hạn sau 8 giờ**, lưu trong `ConcurrentHashMap` (`SessionService`). Frontend giữ token trong `sessionStorage` và `api.ts` tự gắn header `Authorization: Bearer <token>` vào mọi request; nhận 401 thì tự đăng xuất.

Đây là ứng dụng chạy cục bộ nên phiên nằm trong RAM: tắt máy chủ là mọi người phải đăng nhập lại — nhưng **tài khoản và lịch sử vẫn còn nguyên** vì nằm trong MySQL.

## Sáu ngôn ngữ được hỗ trợ

| Ngôn ngữ | Biên dịch | Giới hạn bộ nhớ | Cần cài |
|---|---|---|---|
| **Java** (chính) | `javac -encoding UTF-8` | có, bằng `-Xmx` | JDK |
| C++ | `g++ -O2 -std=c++17` | không (chỉ bắt qua `bad_alloc`) | MinGW / MSYS2 |
| Python | `py_compile` (kiểm tra cú pháp) | không | Python 3 |
| **Go** | `go build` | không | [go.dev/dl](https://go.dev/dl/) |
| **JavaScript** | `node --check` | có, bằng `--max-old-space-size` | Node.js |
| **Rust** | `rustc -O` | không | [rustup.rs](https://rustup.rs) |

Thêm ngôn ngữ = **một lớp con `Language` + một dòng `register()`** trong `LanguageRegistry`. Máy nào chưa cài toolchain thì ngôn ngữ đó hiện `KHÔNG CÓ`, dòng demo tương ứng tự **BỎ QUA**, và API trả lỗi rõ ràng — phần demo Java không bị ảnh hưởng.

## Kiến trúc

```
com.ptit.oj
├── model/        Entity, User→Student/Teacher/Admin, Problem, TestCase,
│                 Submission, TestCaseResult, JudgeResult, Verdict (enum), Credentials
├── language/     Language (abstract) → Java / C++ / Python / Go / JavaScript / Rust
│                 LanguageRegistry (factory/registry)
├── compare/      OutputComparator (interface) → Exact / Token / Float
│                 ComparatorFactory
├── runner/       ProcessRunner  — chạy tiến trình con, bơm stdin, timeout, kill
├── core/         Judge          — bộ chấm; JudgeListener → Console / Statistics
├── database/     DatabaseConfig         — đọc OJ_DB_* từ biến môi trường / .env
│                 MySqlDatabaseManager   — mở Connection, testConnection(), che mật khẩu
│                 SchemaInitializer  — tạo bảng + VIEW user_stats
├── repository/   Repository<T extends Entity>            (interface generic)
│                 ├── InMemoryRepository<T>               (dùng cho --demo/--selftest)
│                 ├── UserRepository        → InMemoryUserRepository | MySqlUserRepository
│                 └── SubmissionRepository  → InMemory...  | MySqlSubmissionRepository
│                 ProblemLoader / ProblemWriter / ProblemDraft  (đọc-ghi đề bài trên ổ đĩa)
├── service/      JudgeService        — tầng nghiệp vụ dùng chung cho cả 2 giao diện
│                 AuthService         — đăng ký / đăng nhập / bootstrap admin
│                 PasswordService     — PBKDF2 + SecureRandom + MessageDigest.isEqual
│                 SessionService      — token có hạn, ConcurrentHashMap
│                 ProblemAdminService — kiểm tra hợp lệ rồi tạo đề bài mới
│                 ScoreboardService   — bảng xếp hạng
│                 StatisticsService   — thống kê verdict trên toàn bộ lịch sử
├── web/          ApiServer    — REST API + xác thực + phục vụ file tĩnh
│                 Json         — sinh/đọc JSON tự viết (có bộ đọc đệ quy cho object/array lồng)
│                 ApiException — lỗi kèm mã HTTP
├── test/         IntegrationTests — bộ kiểm thử tích hợp (chạy bằng --apitest)
├── util/         TextUtils — lọc BOM của file do Notepad tạo
└── ui/           ConsoleApp — menu console (có đăng nhập)

frontend/         React 19 + Vite + TypeScript (thiết kế từ Figma Make)
├── src/api.ts             gọi REST API, tự gắn Authorization: Bearer
├── src/components/ui.tsx  badge verdict, thẻ thống kê, dropdown... (giữ đúng thiết kế gốc)
└── src/pages/             Login · Problems · Submit · Submissions · Leaderboard · AdminProblems
```

Hai giao diện dùng **chung một tầng nghiệp vụ**, và tầng nghiệp vụ **không tự tạo kho dữ liệu** — kho được tiêm vào qua constructor:

```
ConsoleApp ─┐                    ┌─ Judge ─→ Language.compile() / ProcessRunner.run()
            ├─→ JudgeService ────┤              └─→ OutputComparator.matches()
ApiServer ──┘        │           └─ AuthService / ProblemAdminService / ScoreboardService
                     │
                     └─→ Repository ──┬─→ MySQL 8    (chế độ thật)
                                      └─→ bộ nhớ RAM (--demo / --selftest)
```

```java
// JudgeService.persistent(...)  hoặc  JudgeService.inMemory(...)
public JudgeService(Path dataDir, Repository<Problem> problems,
                    UserRepository users, SubmissionRepository submissions,
                    PasswordService passwords)
```

Nhờ đó `--selftest` chạy hoàn toàn trong RAM, còn `--serve` dùng MySQL, mà **không có một dòng `if` nào về chế độ nằm trong tầng nghiệp vụ**. Chuyển từ SQLite sang MySQL chỉ cần viết hai lớp repository mới và sửa đúng một hàm factory — `JudgeService`, `ApiServer`, `ConsoleApp` và toàn bộ lõi `Judge` không đổi một dòng nào.

Không có câu SQL nào nằm ngoài package `repository` / `database`.

## REST API

Trừ 4 endpoint đầu, **mọi endpoint đều cần** header `Authorization: Bearer <token>`.

| Method | Đường dẫn | Quyền | Trả về |
|---|---|---|---|
| GET | `/api/health` | công khai | trạng thái máy chủ |
| GET | `/api/languages` | công khai | 6 ngôn ngữ + máy có toolchain hay chưa |
| POST | `/api/auth/register` | công khai | `{username, password, fullName, studentCode, className}` → tạo tài khoản **STUDENT** |
| POST | `/api/auth/login` | công khai | `{username, password}` → `{token, user}` |
| POST | `/api/auth/logout` | đã đăng nhập | huỷ token hiện tại |
| GET | `/api/auth/me` | đã đăng nhập | `{id, username, fullName, role, roleName, canCreateProblem, solvedCount}` |
| GET | `/api/problems` | đã đăng nhập | danh sách bài + đề + **chỉ test ví dụ** |
| GET | `/api/submissions` | đã đăng nhập | STUDENT: chỉ của mình · TEACHER/ADMIN: tất cả |
| GET | `/api/submissions/{id}` | chủ sở hữu / TEACHER / ADMIN | chi tiết: verdict từng test + mã nguồn |
| GET | `/api/scoreboard` | đã đăng nhập | bảng xếp hạng |
| GET | `/api/stats` | đã đăng nhập | thống kê verdict trên **toàn bộ** lịch sử |
| POST | `/api/submit` | đã đăng nhập | `{problemId, language, code}` → chấm ngay, trả kết quả đầy đủ |
| POST | `/api/submit/stream` | đã đăng nhập | như trên nhưng trả **Server-Sent Events**: mỗi test xong là gửi ngay một sự kiện |
| POST | `/api/admin/problems` | **chỉ ADMIN** | tạo bài tập mới, ghi ra `data/problems/<id>/` |

`POST /api/submit` **không còn nhận trường `username`**: người nộp luôn lấy từ token, nên không thể mạo danh người khác. Trường `role` gửi kèm khi đăng ký cũng bị bỏ qua — `register()` luôn tạo STUDENT.

### Mã lỗi HTTP

| Mã | Khi nào |
|---|---|
| 400 | dữ liệu không hợp lệ (JSON sai, mật khẩu ngắn, mã bài sai định dạng, tên test có ký tự đường dẫn…) |
| 401 | chưa đăng nhập, token sai hoặc hết hạn |
| 403 | đã đăng nhập nhưng không đủ quyền (học sinh gọi API admin, xem bài nộp của người khác) |
| 404 | không có bài / mã nộp / endpoint |
| 409 | trùng tên đăng nhập hoặc trùng mã bài |
| 500 | lỗi nội bộ — **chỉ trả về câu chung**, stack trace và thông tin CSDL chỉ in ra log máy chủ |

### Ví dụ dòng lệnh

Đăng nhập lấy token:

```bash
curl -X POST http://localhost:8080/api/auth/login -H "Content-Type: application/json" -d "{\"username\":\"hiennm\",\"password\":\"ptit@2026\"}"
```

Nộp bài bằng token vừa lấy:

```bash
curl -X POST http://localhost:8080/api/submit -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d "{\"problemId\":\"P001\",\"language\":\"Python\",\"code\":\"import sys\\nd=sys.stdin.read().split()\\nprint(int(d[0])+int(d[1]))\\n\"}"
```

### Chấm trực tiếp: `POST /api/submit/stream`

`POST /api/submit` chặn cho đến khi chấm xong rồi mới trả kết quả một cục. Bản stream trả về `text/event-stream` và đẩy sự kiện ngay khi từng test chạy xong:

| Sự kiện | Dữ liệu |
|---|---|
| `started` | `{submissionId, problemId, language, total}` — biết trước tổng số test để vẽ thanh tiến trình |
| `compiled` | `{success, message}` — thất bại thì `message` là nguyên văn thông báo của trình biên dịch |
| `test` | `{index, total, id, sample, verdict, runtimeMs, points, message}` — **một sự kiện cho mỗi test** |
| `finished` | `{verdict, passed, total, score}` |
| `done` | nguyên bản ghi bài nộp, giống hệt cái `/api/submit` trả về |
| `error` | `{error}` — chỉ dùng cho lỗi xảy ra **sau** khi header đã gửi, lúc đó không đặt được mã HTTP nữa |

Mọi kiểm tra đầu vào (bài không tồn tại, chưa đăng nhập, ngôn ngữ chưa cài) đều chạy **trước** khi mở luồng, nên vẫn trả về mã HTTP 4xx và JSON bình thường.

Xem thẳng bằng `curl -N` (`-N` để không gom bộ đệm):

```bash
curl -N -X POST http://localhost:8080/api/submit/stream -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d "{\"problemId\":\"P001\",\"language\":\"Java\",\"code\":\"...\"}"
```

Cài đặt là `SseJudgeListener` — **một lớp con `JudgeListener` nữa, không sửa một dòng nào trong `Judge`**. Listener được gắn trước khi chấm và gỡ trong `finally`, nên không sống lâu hơn request đã sinh ra nó.

Frontend không dùng `EventSource` của trình duyệt vì `EventSource` chỉ gọi được GET, mà nộp bài thì phải POST kèm mã nguồn; thay vào đó `api.submitStream()` đọc thẳng thân phản hồi bằng `ReadableStream` rồi tự tách khung SSE.

Admin tạo bài mới:

```bash
curl -X POST http://localhost:8080/api/admin/problems -H "Content-Type: application/json" -H "Authorization: Bearer $ADMIN_TOKEN" -d "{\"id\":\"P004\",\"title\":\"Nhan hai so\",\"statement\":\"Tich a*b\",\"timeLimitMs\":1000,\"memoryLimitMb\":64,\"comparator\":\"token\",\"totalPoints\":100,\"tests\":[{\"name\":\"sample01\",\"input\":\"3 4\\n\",\"output\":\"12\\n\",\"sample\":true},{\"name\":\"01\",\"input\":\"111 222\\n\",\"output\":\"24642\\n\",\"sample\":false}]}"
```

## Quản trị đề bài

`POST /api/admin/problems` nhận body JSON có mảng `tests` lồng bên trong. Bộ đọc JSON cũ chỉ hiểu object phẳng nên `Json` được bổ sung **bộ đọc đệ quy đầy đủ** (`Json.parse` / `Json.parseObject` → `Json.Value`) hỗ trợ object và array lồng nhau, có chặn độ sâu (32 mức) và kích thước — không cắt chuỗi thủ công.

### Kiểm tra hợp lệ ở backend

| Trường | Ràng buộc |
|---|---|
| `id` | khớp `[A-Z0-9_-]{1,32}`, **cấm** `..`, `/`, `\`; không trùng bài đã có |
| `title`, `statement` | không rỗng (tối đa 200 / 200 000 ký tự) |
| `timeLimitMs` | 100 – 60 000 |
| `memoryLimitMb` | 8 – 2048 |
| `totalPoints` | > 0 và ≤ 100 000 |
| `comparator` | phải được `ComparatorFactory` chấp nhận (`exact` / `token` / `float` / `float:1e-9`) |
| `tests` | ít nhất 1, tối đa 200 |
| `tests[].name` | khớp `[A-Za-z0-9_-]{1,64}`, không trùng nhau (không phân biệt hoa thường vì Windows như vậy) |
| `tests[].input` / `output` | đều bắt buộc, không rỗng |
| test ví dụ | `sample: true` ⇒ tên **phải** bắt đầu bằng `sample`, và ngược lại |

### Ghi ra ổ đĩa an toàn

`ProblemWriter` ghi theo kiểu "tất cả hoặc không có gì": tạo thư mục tạm `_tmp_xxxxxxxx` **ngay bên trong `data/problems/`** (cùng ổ đĩa nên đổi tên là thao tác nguyên tử), ghi đầy đủ mọi file bằng UTF-8, rồi mới `Files.move(..., ATOMIC_MOVE)` sang tên thật. Lỗi giữa chừng thì thư mục tạm bị xoá, không để lại bài dở dang. `ProblemLoader` cũng bỏ qua mọi thư mục có tiền tố `_tmp_`.

Tạo xong, bài được **nạp lại bằng chính `ProblemLoader`** rồi đưa vào repository — nên dữ liệu trên ổ đĩa và trong bộ nhớ luôn khớp nhau, và frontend thấy bài mới **ngay lập tức, không cần khởi động lại máy chủ**.

Trang **Thêm bài tập** trên web chỉ hiện với tài khoản ADMIN, cho nhập metadata, thêm/xoá nhiều test, mỗi test có tên · input · output · ô tick *Test ví dụ*, và báo lỗi ngay trên trình duyệt trước khi gửi đi (backend vẫn kiểm tra lại toàn bộ).

## OOP và design pattern — bảng đối chiếu để viết báo cáo

| Khái niệm | Thể hiện trong code |
|---|---|
| **Encapsulation** | `Problem.testCases` là `private`, `getTestCases()` trả `unmodifiableList`; `Credentials` bất biến và `toString()` **không in hash/salt**; mọi field đều private + getter |
| **Inheritance** | `Entity` → `Problem`/`Submission`/`User`/`TestCase`; `User` → `Student`/`Teacher`/**`Admin`**; `FloatComparator extends TokenComparator`; `MySqlUserRepository implements UserRepository extends Repository<User>` |
| **Polymorphism** | `Judge` gọi `language.compile()` và `comparator.matches()` mà không biết lớp cụ thể; **`canCreateProblem()` chỉ `Admin` ghi đè thành `true`** nên chỗ kiểm tra quyền không cần `if (role == ...)`; `Language.defaultFileName()` chỉ Java ghi đè |
| **Abstraction** | `Language`, `User`, `Entity` là abstract class; `OutputComparator`, `Repository<T>`, `UserRepository`, `SubmissionRepository`, `JudgeListener` là interface |
| **Strategy** | `OutputComparator`: đổi cách so sánh (exact / token / float ε) mà không sửa `Judge` |
| **Factory** | `ComparatorFactory.create("float:1e-6")`, `LanguageRegistry.detect(file)`, `JudgeService.persistent()` / `JudgeService.inMemory()` |
| **Observer** | `JudgeListener` có **ba** bản cài đặt: `ConsoleJudgeListener` in tiến trình ra terminal, `StatisticsListener` đếm verdict, `SseJudgeListener` đẩy từng test về trình duyệt. Cả ba được thêm vào mà **không sửa một dòng nào trong `Judge`** — đây là ví dụ Open/Closed rõ nhất của project |
| **Generic** | `Repository<T extends Entity>` dùng chung cho mọi entity; hai bản cài đặt RAM và MySQL thay nhau được |
| **Dependency Injection** | `JudgeService` **nhận** kho dữ liệu qua constructor, không `new` bên trong → `--selftest` chạy RAM, `--serve` chạy MySQL mà tầng nghiệp vụ không biết khác biệt |
| **Phân tầng** | UI (console/web) → service → repository → database. Không có câu SQL nào nằm ngoài package `repository`; `Judge` và `ConsoleApp` không biết MySQL tồn tại |
| **Exception tự định nghĩa** | `JudgeException`, `CompileErrorException`, `ProblemLoadException`, `DataAccessException`, `ApiException`, `AuthException`, `ProblemAdminException` |
| **Enum có hành vi** | `Verdict` mang `code`, `display`, `severity`, `isAccepted()` |
| **Đa luồng** | `ProcessRunner` dùng 3 thread (bơm stdin, đọc stdout, đọc stderr) tránh deadlock khi buffer OS đầy; `InMemoryRepository` synchronized; `SessionService` dùng `ConcurrentHashMap`; `MySqlDatabaseManager` mở một `Connection` riêng cho mỗi thao tác thay vì dùng chung một kết nối; chấm bài nối tiếp qua `judgeLock` để đo thời gian không bị nhiễu |
| **Bảo mật** | PBKDF2 + `SecureRandom` + `MessageDigest.isEqual`; `PreparedStatement` cho mọi câu SQL; kiểm tra quyền ở backend; chống path traversal ở cả mã bài lẫn tên test |
| **SOLID** | *S*: `PasswordService` chỉ lo băm, `SessionService` chỉ lo phiên, `ProblemWriter` chỉ lo ghi đĩa · *O*: thêm ngôn ngữ/kiểu so sánh/observer/kho dữ liệu đều không sửa lớp cũ · *L*: đổi `InMemoryUserRepository` ↔ `MySqlUserRepository` không ảnh hưởng nơi gọi · *I*: `UserRepository` và `SubmissionRepository` tách riêng · *D*: `Judge` phụ thuộc trừu tượng `Language`/`OutputComparator`, `JudgeService` phụ thuộc interface `Repository` |

## Định dạng dữ liệu

Một bài tập = một thư mục trong `data/problems/`:

```
P001/
├── problem.properties    id, title, timeLimitMs, memoryLimitMb, comparator, totalPoints
├── statement.txt         đề bài (tùy chọn)
└── tests/
    ├── sample01.in / sample01.out    (tên bắt đầu bằng "sample" = test ví dụ, chạy trước)
    ├── 02.in / 02.out
    └── 03.in / 03.out
```

`comparator` nhận: `exact` (đúng từng ký tự), `token` (bỏ qua khoảng trắng thừa — mặc định), `float` hoặc `float:1e-9` (sai số cho phép). Điểm chia đều cho các test nên bài sai một phần vẫn có điểm từng phần.

**Số lượng test không được công bố:** danh sách bài (`GET /api/problems`, cột trên trang *Bài tập*, và `Problem.describe()` trên console) **không hiển thị số test** nữa. Test vẫn nằm nguyên trong model và `ProblemLoader`, bộ chấm vẫn chạy đủ mọi test, test ví dụ vẫn hiện, và sau khi chấm vẫn báo `passed/total` trong kết quả lẫn lịch sử.

`data/submissions/demo-plan.txt` — kịch bản demo, mỗi dòng: `mãBài | username | file | verdict kỳ vọng`.

## Bài nộp mẫu: đủ 6 verdict bằng Java

| File | Verdict | Nguyên nhân |
|---|---|---|
| `SumAC.java` | AC | đúng hoàn toàn |
| `SumWA.java` | WA | tính `a - b` |
| `SumTLE.java` | TLE | vòng lặp vô hạn, bị cưỡng chế dừng |
| `SumMLE.java` | MLE | cấp phát không ngừng, vượt `-Xmx64m` |
| `SumRE.java` | RE | chia cho 0 |
| `SumCE.java` | CE | thiếu dấu `;` |

Thêm `sum_ac.cpp`, `sum_ac.py`, `sum_ac.js`, `sum_ac.go`, `sum_ac.rs`, `avg_ac.py`, `prime_wa.js` cho phần đa ngôn ngữ.

## Kiểm thử

```bash
powershell -ExecutionPolicy Bypass -File run-tests.ps1
```

Script chạy 4 bước: biên dịch backend → `--selftest` → `--apitest` → `npm run build`, và trả exit code khác 0 nếu có bước nào hỏng. Chưa cấu hình `OJ_TEST_DB_*` thì bước `--apitest` được **bỏ qua** chứ không báo lỗi, để máy không có MySQL vẫn chạy được ba bước còn lại.

`--apitest` (`com.ptit.oj.test.IntegrationTests`) chạy trên **MySQL thật** với hai lớp bảo vệ dữ liệu:

1. kết nối lấy từ bộ biến môi trường **riêng** `OJ_TEST_DB_URL` / `OJ_TEST_DB_USER` / `OJ_TEST_DB_PASSWORD`, không dùng chung với cơ sở dữ liệu thật;
2. tên cơ sở dữ liệu **bắt buộc kết thúc bằng `_test`** — nếu không, bộ kiểm thử in cảnh báo và dừng ngay, **không chạy một câu lệnh ghi nào**.

Đề bài thì được copy sang thư mục temp nên `data/problems/` thật cũng không bị đụng tới. Các tình huống được kiểm tra:

| Nhóm | Nội dung |
|---|---|
| Đăng ký | tạo học sinh thành công (201) · trùng username → 409 (không phân biệt hoa thường) · gửi kèm `role: ADMIN` vẫn ra STUDENT |
| Đăng nhập | sai mật khẩu → 401 · đúng mật khẩu → token · phản hồi không chứa hash/salt · không token → 401 |
| Mật khẩu | đọc thẳng bảng `users` bằng JDBC, khẳng định **không có chuỗi plaintext** |
| Phân quyền | học sinh gọi `/api/admin/problems` → 403 · học sinh A xem bài nộp của B → 403 · danh sách của A không chứa bài của B · admin xem được tất cả |
| Quản trị đề | admin tạo bài → 201 · file ghi đúng cấu trúc trên ổ đĩa · bài mới hiện ngay không cần restart · trùng mã → 409 · các mã `../evil`, `..`, `P9/../../x`, `P9\..\x`, `p9 01` → 400 · tên test dạng đường dẫn → 400 · payload độc hại không tạo thư mục nào |
| Ẩn test | `GET /api/problems` không còn `testCount`, không lộ input/output của test ẩn, vẫn hiện test ví dụ |
| Không lộ đáp án qua kết quả chấm | thông báo WA gửi về client (`message`) chỉ nói **lệch ở vị trí nào và thí sinh in ra gì**, không bao giờ kèm "kỳ vọng" — nếu không, nộp bừa vài lần đọc đáp án từng test rồi hardcode là qua hết. Giao diện web còn không liệt kê từng test nữa — chỉ báo "WA on test mấy"; bản kèm đáp án (`explainDetailed`) chỉ in ra terminal người chấm, không lưu, không gửi |
| Kết nối & lược đồ | `SELECT 1` thành công · chạy `MySqlSchemaInitializer` **hai lần liên tiếp** vẫn an toàn và đủ 4 đối tượng (3 bảng + VIEW) |
| Transaction | sau khi nộp một bài, số dòng `test_case_results` khớp đúng số test của đề — không có bài nộp nào thiếu kết quả test |
| Khoá ngoại | xoá một submission → `test_case_results` bay theo · xoá một user → cả submissions lẫn test results bay theo, không còn dòng mồ côi (`ON DELETE CASCADE` của InnoDB) |
| Bền vững | nộp bài → dừng máy chủ → mở lại trên cùng cơ sở dữ liệu: tài khoản vẫn đăng nhập được, lịch sử còn nguyên, mã bài nộp không trùng, mã nguồn đọc lại được, bảng xếp hạng và thống kê verdict vẫn đúng, bài do admin tạo vẫn còn |
| solvedCount | AC 2 lần cùng một bài → **1** · AC hai bài khác nhau → **2** · vẫn đúng sau khi khởi động lại |

`--selftest` giữ nguyên vai trò cũ: chấm lại toàn bộ `demo-plan.txt` và đối chiếu verdict thực tế với verdict kỳ vọng.

## Kịch bản demo

**Phần 1 — chứng minh hệ thống chạy đúng (console):**

1. `run-tests.ps1` — chạy cả kiểm thử tích hợp lẫn bộ chấm, in bảng ĐÚNG/LỆCH. Đây là bằng chứng kết quả không dựng sẵn.
2. `run.ps1` → đăng nhập `hiennm` / `ptit@2026` → menu **7** để xem máy có toolchain nào. Thử gõ sai mật khẩu để thấy bị từ chối.

**Phần 2 — giao diện web:**

3. `run-web.ps1`, **chép mật khẩu admin in ra terminal**, mở http://localhost:8080.
4. Màn hình đăng nhập → bấm *Chưa có tài khoản?* → đăng ký một học sinh mới ngay tại chỗ, rồi đăng nhập bằng tài khoản đó.
5. Tab **Bài tập**: bảng **không còn cột "Test"**. Bấm vào dòng P003 — chuyển sang khung nộp bài, đề bài và test ví dụ nằm ngay cột bên trái khung code.
6. Bấm *Chèn code mẫu A+B*, đổi ngôn ngữ (Java → Python → JavaScript), bấm *Nộp và chấm* — badge nhấp nháy chờ, dòng **"Đúng k/N test"** và thanh tiến trình 25% → 50% → 75% → 100% nhích theo từng test máy chủ vừa chấm xong, số **"đã giải"** trên thanh trên cùng tự tăng, terminal in song song đúng tiến trình đó. Muốn thấy rõ hơn thì nộp một bài cố tình TLE: mỗi test mất hơn 1 giây, và dòng **"TLE on test 1 (ví dụ)"** hiện ra ngay khi test đầu trượt, chưa cần đợi chấm hết.
7. Sửa code thành `a - b` rồi nộp lại → **"WA on test 1 (ví dụ), 2, 3, 4"** kiểu Codeforces — không liệt kê từng test, **không hiện đáp án**. Terminal của bạn thì in đủ "Lệch tại giá trị thứ 1: kỳ vọng [8], nhận được [-2]" (xem bảng bảo mật bên dưới). Xoá một dấu `;` rồi nộp → CE: badge đỏ kèm nguyên thông báo `javac`, không có dòng "Đúng k/N" vì test chưa chạy.
8. Tab **Lịch sử nộp**: học sinh **chỉ thấy bài của chính mình**. Đăng xuất, đăng nhập bằng `admin` → thấy bài nộp của tất cả mọi người, và có thêm tab **Thêm bài tập**.
9. Tab **Thêm bài tập**: nhập mã bài, đề, các test (tick *Test ví dụ* cho test công khai) → *Tạo bài tập*. Bài xuất hiện ngay ở tab **Bài tập** và trong `data/problems/`. Thử nhập mã `../evil` để thấy backend từ chối.
10. **Tắt máy chủ bằng Ctrl+C rồi chạy lại** → lịch sử, bảng xếp hạng, thống kê verdict và số bài đã giải vẫn còn nguyên; mật khẩu admin **không** bị in lại. Mở MySQL Workbench xem thẳng bảng `submissions` và VIEW `user_stats` để chứng minh dữ liệu nằm thật trong cơ sở dữ liệu.

> **Phương án dự phòng:** nếu MySQL không lên được đúng lúc bảo vệ, `run-web.ps1 -NoDb` cho chạy trọn Phần 2 trừ bước 10 (bước đó cần dữ liệu còn lại sau khi tắt). Xem [Demo không cần MySQL](#demo-không-cần-mysql).

**Phần 3 — chỉ code:** `Judge.java` (lõi), `OutputComparator.java` (Strategy), `Language.java` + `LanguageRegistry` (Factory + đa hình 6 ngôn ngữ), `JudgeListener` (Observer), `JudgeService` (tiêm phụ thuộc + tầng dùng chung 2 giao diện), `PasswordService` (PBKDF2), `MySqlSubmissionRepository.saveWithResults()` (transaction), `ProblemAdminService` (kiểm tra hợp lệ) và `ProblemWriter` (ghi nguyên tử).

Câu hỏi thường gặp và chỗ trả lời: *"Chống lặp vô hạn?"* → `ProcessRunner.run()` dùng `waitFor(timeout)` + `destroyForcibly()`. *"Output khổng lồ?"* → `OUTPUT_CAP_BYTES = 1MB`. *"Thêm ngôn ngữ mất bao lâu?"* → 1 lớp con + 1 dòng `register()`. *"Học sinh sửa `role` trong request được không?"* → không, `register()` luôn tạo `Student`. *"Đoán mã bài nộp để xem code người khác?"* → 403, kiểm tra ở `handleSubmissionDetail()`. *"Ẩn nút Thêm bài tập là đủ chưa?"* → không, `requireAdmin()` chặn ở backend.

## Giới hạn đã biết (nên nói rõ khi bảo vệ)

1. **Giới hạn bộ nhớ chỉ là xấp xỉ.** Java ép bằng `-Xmx`, JavaScript bằng `--max-old-space-size`; C++/Python/Go/Rust chỉ suy ra MLE khi runtime báo hết bộ nhớ (`bad_alloc`, `MemoryError`, `out of memory`…). Muốn đo chính xác phải dùng cgroups (Linux) hoặc Job Object (Windows) — vượt phạm vi bài tập lớn.
2. **Không có sandbox thật.** Code thí sinh chạy bằng quyền người dùng hiện tại. Vì vậy máy chủ web **chỉ lắng nghe trên 127.0.0.1**, không mở ra LAN, và không bật CORS (frontend dev đi qua proxy của Vite). Chỉ chấm bài nộp mà bạn tin cậy. Đăng nhập giải quyết chuyện *ai nộp bài*, **không** biến hệ thống thành an toàn để mở ra Internet.
3. **Phiên đăng nhập nằm trong RAM.** Tắt máy chủ là mọi người phải đăng nhập lại (tài khoản và lịch sử thì vẫn còn). Không có "ghi nhớ đăng nhập", không có refresh token, không giới hạn số lần thử sai mật khẩu.
4. **Không có HTTPS.** Token đi qua HTTP thuần — chấp nhận được vì chỉ chạy trên `localhost`.
5. **Chưa có chức năng sửa/xoá đề bài và đổi mật khẩu** qua giao diện; hiện chỉ có tạo mới. Quên mật khẩu admin thì phải sửa trực tiếp CSDL.
6. **Mỗi test bắt buộc có cả input lẫn output khác rỗng** khi tạo bài qua API, nên không tạo được bài "không có input" bằng giao diện quản trị (vẫn tạo tay trong `data/problems/` được).
7. **Điểm chia đều cho các test.** API tạo bài chưa cho đặt điểm riêng từng test.
8. **`findAll()` của kho MySQL đọc toàn bộ lịch sử vào bộ nhớ** mỗi lần dựng bảng xếp hạng, và mỗi thao tác mở một kết nối mới (chưa có connection pool). Quy mô một lớp học thì không sao; hệ thống thật cần pool + phân trang + tính điểm bằng SQL.
9. **Thời gian đo là wall-clock**, gồm cả thời gian khởi động JVM/interpreter (đã bù bằng `getStartupOverheadMs()`), nên số ms dao động giữa các lần chạy.
10. **Chấm tuần tự.** Web nhận nhiều request nhưng khoá lại chấm lần lượt để số đo thời gian không bị nhiễu. Muốn nhanh hơn: hàng đợi + `ExecutorService`.

## Ô soạn mã nguồn

Trang **Nộp bài** dùng **CodeMirror 6** thay cho `<textarea>`: có số dòng, tô màu cú pháp cho cả 6 ngôn ngữ, so khớp ngoặc, và phím `Tab` thụt dòng thay vì nhảy ra khỏi ô. Bảng màu tô cú pháp **không lấy theme có sẵn** mà đặt lại theo đúng biến CSS trong `index.css`, để ô code không lạc lõng giữa các panel xung quanh.

Sáu bộ phân tích cú pháp cộng lại nặng gần 800 kB nên chúng được **nạp động**: `CodeEditor.tsx` gọi `import()` cho đúng ngôn ngữ đang chọn, Vite tách mỗi ngôn ngữ thành một file riêng (30–104 kB), và đổi ngôn ngữ chỉ thay phần cấu hình đó qua `Compartment` chứ không dựng lại cả editor. Nhờ vậy file khởi động vẫn ~247 kB, gần bằng bản chưa có editor.

Trang **Lịch sử nộp** dùng lại đúng component này ở chế độ chỉ xem (`readOnly`), nên mã nguồn đã nộp cũng được tô màu theo ngôn ngữ của bài — không có bộ hiển thị thứ hai để phải giữ đồng bộ màu.

## Nguồn gốc giao diện

Thiết kế lấy từ file Figma Make `Competitive Programming Platform.make` (giữ trong thư mục gốc làm bản gốc thiết kế). Bản Figma chỉ là prototype dùng dữ liệu random giả; khi đưa vào project, toàn bộ dữ liệu giả đã được thay bằng REST API thật, thêm trang **Nộp bài**, và bỏ trang *Contests* vì backend chưa có khái niệm kỳ thi. Bảng màu, font và bộ component (badge verdict, thẻ thống kê, dropdown, thanh thời gian) giữ đúng bản thiết kế; Tailwind được thay bằng CSS variable thuần để bớt phụ thuộc lúc build.

## Lưu ý về mã hóa ký tự

Chuỗi hiển thị là tiếng Việt có dấu, lưu UTF-8. Vì vậy luôn biên dịch với `javac -encoding UTF-8` (các script đã làm sẵn), và trong IDE đặt project encoding là UTF-8. Chương trình tự ép `System.out` sang UTF-8 (`Main.forceUtf8Output()`) và tự lọc BOM của file do Notepad tạo (`TextUtils.stripBom()`).
