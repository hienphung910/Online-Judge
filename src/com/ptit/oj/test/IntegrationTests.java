package com.ptit.oj.test;

import com.ptit.oj.database.DatabaseConfig;
import com.ptit.oj.database.MySqlDatabaseManager;
import com.ptit.oj.database.MySqlSchemaInitializer;
import com.ptit.oj.model.Admin;
import com.ptit.oj.service.JudgeService;
import com.ptit.oj.web.ApiServer;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.StandardCopyOption;
import java.nio.file.attribute.BasicFileAttributes;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

/**
 * Bo kiem thu tich hop cho phan MySQL + xac thuc + quan tri de bai.
 *
 * Chay bang:  run-tests.ps1  /  run-tests.bat  /  ./run-tests.sh
 * hoac:       java -cp "out;lib/*" com.ptit.oj.Main --apitest
 *
 * AN TOAN DU LIEU - hai lop bao ve:
 *   1. Ket noi lay tu bo bien moi truong RIENG (OJ_TEST_DB_URL / _USER / _PASSWORD),
 *      khong dung chung voi CSDL that.
 *   2. Ten CSDL BAT BUOC ket thuc bang "_test". Neu khong, bo kiem thu dung ngay
 *      va khong chay bat ky lenh ghi nao.
 * De bai thi duoc copy sang mot thu muc tam nen data/problems/ that khong bi dong toi.
 *
 * Khong dung JUnit vi bai tap lon chi cho phep thu vien chuan + mysql-connector-j.
 */
public final class IntegrationTests {

    private static final String STUDENT_A = "sv_alpha";
    private static final String STUDENT_B = "sv_beta";
    private static final String PASSWORD = "MatKhau@2026";
    private static final String ADMIN_USER = "admin_test";
    private static final String ADMIN_PASSWORD = "Admin@2026!";

    /** Cap gia tri CHI xuat hien trong test AN cua bai P900 do bo kiem thu tao ra. */
    private static final String HIDDEN_IN = "987654321 864297531";
    private static final String HIDDEN_OUT = "1851951852";

    private static int passed;
    private static int failed;
    private static final List<String> FAILURES = new ArrayList<>();

    private IntegrationTests() { }

    /** Chay toan bo kiem thu. Tra ve so ca that bai (0 = tat ca dat). */
    public static int runAll(Path sourceDataDir) {
        Path workspace = null;
        try {
            DatabaseConfig config = DatabaseConfig.fromTestEnvironment();
            MySqlDatabaseManager database = MySqlDatabaseManager.from(config);
            String schema = database.getDatabaseName();

            // ---- Lop bao ve: chi cho phep chay tren CSDL co ten ket thuc bang _test ----
            if (!schema.toLowerCase(Locale.ROOT).endsWith("_test")) {
                System.out.println("DUNG KIEM THU: " + DatabaseConfig.ENV_TEST_URL
                        + " phải trỏ tới một cơ sở dữ liệu có tên kết thúc bằng \"_test\""
                        + " (đang trỏ tới \"" + schema + "\").");
                System.out.println("Bộ kiểm thử sẽ xoá sạch bảng trước khi chạy nên"
                        + " không bao giờ được phép chạy trên cơ sở dữ liệu thật.");
                return 1;
            }

            workspace = Files.createTempDirectory("oj-apitest-");
            Path dataDir = workspace.resolve("data");
            Files.createDirectories(dataDir);
            copyDirectory(sourceDataDir.resolve("problems"), dataDir.resolve("problems"));

            System.out.println("==================================================");
            System.out.println("  KIEM THU TICH HOP - PTIT Online Judge (MySQL)");
            System.out.println("  CSDL kiem thu : " + database.getSafeUrl());
            System.out.println("  De bai tam    : " + dataDir);
            System.out.println("==================================================");
            System.out.println();

            // 1. Ket noi MySQL
            database.testConnection();
            check("1. Kết nối được MySQL bằng cấu hình kiểm thử", true, "");

            // 2. Khoi tao schema (chay 2 lan de chung minh idempotent)
            new MySqlSchemaInitializer(database).initialize();
            new MySqlSchemaInitializer(database).initialize();
            check("2. Khởi tạo lược đồ MySQL (chạy lại lần 2 vẫn an toàn)",
                    tablesExist(database), "Thiếu bảng sau khi khởi tạo lược đồ");

            cleanTables(database);
            runScenarios(dataDir, database);
        } catch (DatabaseConfig.MissingConfigException e) {
            failed++;
            FAILURES.add("Thiếu cấu hình MySQL cho kiểm thử");
            System.out.println(e.getMessage());
        } catch (Exception e) {
            failed++;
            FAILURES.add("Ngoại lệ ngoài dự kiến: " + e);
            e.printStackTrace(System.out);
        } finally {
            deleteRecursively(workspace);
        }

        System.out.println();
        System.out.println("==================================================");
        System.out.printf("  KET QUA: %d dat / %d that bai%n", passed, failed);
        for (String f : FAILURES) System.out.println("  x " + f);
        System.out.println("==================================================");
        return failed;
    }

    private static void runScenarios(Path dataDir, MySqlDatabaseManager database) throws Exception {
        // ---------------------------------------------------- vong doi thu nhat
        JudgeService service = JudgeService.mysql(dataDir, database);
        service.loadData();
        // Tao san mot tai khoan quan tri de kiem thu (khong dung bootstrap ngau nhien
        // vi test can biet truoc mat khau).
        service.getAuth().createAccount(
                new Admin("U-ADMIN-TEST", ADMIN_USER, "Quản trị kiểm thử"), ADMIN_PASSWORD);

        ApiServer server = new ApiServer(service, 0, dataDir.resolve("no-frontend"));
        server.start();
        String base = "http://localhost:" + server.getPort();

        String tokenA;
        String tokenB;
        String tokenAdmin;
        String subBId;
        try {
            // 3. Dang ky hoc sinh thanh cong
            Response r = post(base + "/api/auth/register", null, json(
                    "username", STUDENT_A, "password", PASSWORD,
                    "fullName", "Nguyễn Văn Alpha", "studentCode", "B24DCCN001", "className", "D24CQCN01"));
            check("3. Đăng ký học sinh thành công", r.status == 201,
                    "HTTP " + r.status + " - " + r.body);

            post(base + "/api/auth/register", null, json(
                    "username", STUDENT_B, "password", PASSWORD,
                    "fullName", "Trần Thị Beta", "studentCode", "B24DCCN002", "className", "D24CQCN01"));

            // 4. Username trung bi tu choi ke ca khac chu hoa/thuong
            r = post(base + "/api/auth/register", null, json(
                    "username", STUDENT_A.toUpperCase(Locale.ROOT), "password", PASSWORD,
                    "fullName", "Kẻ trùng tên", "studentCode", "B24DCCN003", "className", "D24CQCN02"));
            check("4. Username trùng bị từ chối (409, không phân biệt hoa thường)", r.status == 409,
                    "HTTP " + r.status + " - " + r.body);

            r = post(base + "/api/auth/register", null, json(
                    "username", "ke_gia_mao", "password", PASSWORD, "fullName", "Kẻ giả mạo",
                    "studentCode", "B24DCCN004", "className", "D24CQCN02", "role", "ADMIN"));
            check("4b. Gửi kèm role=ADMIN khi đăng ký vẫn ra STUDENT",
                    r.status == 201 && r.body.contains("\"role\":\"STUDENT\""),
                    "HTTP " + r.status + " - " + r.body);

            // 5. Dang nhap dung / sai mat khau
            r = post(base + "/api/auth/login", null, json("username", STUDENT_A, "password", "sai-mat-khau"));
            check("5a. Đăng nhập sai mật khẩu bị từ chối (401)", r.status == 401,
                    "HTTP " + r.status + " - " + r.body);

            r = post(base + "/api/auth/login", null, json("username", STUDENT_A, "password", PASSWORD));
            check("5b. Đăng nhập đúng mật khẩu thành công",
                    r.status == 200 && r.body.contains("\"token\""), "HTTP " + r.status + " - " + r.body);
            tokenA = extract(r.body, "token");

            check("5c. Phản hồi đăng nhập không chứa hash/salt mật khẩu",
                    !r.body.contains("password") && !r.body.contains("salt") && !r.body.contains("hash"),
                    r.body);

            tokenB = extract(post(base + "/api/auth/login", null,
                    json("username", STUDENT_B, "password", PASSWORD)).body, "token");
            tokenAdmin = extract(post(base + "/api/auth/login", null,
                    json("username", ADMIN_USER, "password", ADMIN_PASSWORD)).body, "token");

            r = get(base + "/api/problems", null);
            check("5d. Gọi /api/problems khi chưa đăng nhập bị 401", r.status == 401,
                    "HTTP " + r.status + " - " + r.body);

            // 6. CSDL khong chua mat khau dang van ban
            check("6. MySQL không chứa mật khẩu dạng plaintext",
                    !databaseContainsPlaintext(database, PASSWORD),
                    "Tìm thấy chuỗi mật khẩu trong bảng users");

            // 7. Student goi API admin nhan 403
            r = post(base + "/api/admin/problems", tokenA, adminProblemBody("P900"));
            check("7. Student gọi API admin nhận 403", r.status == 403, "HTTP " + r.status + " - " + r.body);

            // 8. Admin them bai thanh cong
            r = post(base + "/api/admin/problems", tokenAdmin, adminProblemBody("P900"));
            check("8a. Admin tạo bài thành công (201)", r.status == 201, "HTTP " + r.status + " - " + r.body);
            check("8b. Bài mới ghi đúng cấu trúc thư mục trên ổ đĩa",
                    Files.isRegularFile(dataDir.resolve("problems/P900/problem.properties"))
                            && Files.isRegularFile(dataDir.resolve("problems/P900/statement.txt"))
                            && Files.isRegularFile(dataDir.resolve("problems/P900/tests/sample01.in"))
                            && Files.isRegularFile(dataDir.resolve("problems/P900/tests/sample01.out"))
                            && Files.isRegularFile(dataDir.resolve("problems/P900/tests/01.in"))
                            && Files.isRegularFile(dataDir.resolve("problems/P900/tests/01.out")),
                    "Thiếu file trong data/problems/P900");

            r = get(base + "/api/problems", tokenA);
            check("8c. Bài mới xuất hiện ngay, không cần khởi động lại", r.body.contains("\"P900\""), r.body);

            r = post(base + "/api/admin/problems", tokenAdmin, adminProblemBody("P900"));
            check("8d. Mã bài trùng bị từ chối (409)", r.status == 409, "HTTP " + r.status + " - " + r.body);

            for (String evil : new String[]{"../evil", "..", "P9/../../x", "P9\\..\\x", "p9 01"}) {
                Response bad = post(base + "/api/admin/problems", tokenAdmin, adminProblemBody(evil));
                check("8e. Mã bài \"" + evil + "\" bị từ chối (400)", bad.status == 400,
                        "HTTP " + bad.status + " - " + bad.body);
            }

            r = get(base + "/api/problems", tokenA);
            check("8f. GET /api/problems không còn trường testCount", !r.body.contains("testCount"), r.body);
            check("8g. GET /api/problems không lộ input/output của test ẩn",
                    !r.body.contains(HIDDEN_IN) && !r.body.contains(HIDDEN_OUT),
                    "Nội dung test ẩn bị lộ trong danh sách bài");

            // 9. Student A khong xem duoc submission cua Student B
            Response subB = post(base + "/api/submit", tokenB,
                    json("problemId", "P001", "language", "Java", "code", sumSolution()));
            check("9a. Student B nộp bài thành công", subB.status == 200,
                    "HTTP " + subB.status + " - " + subB.body);
            subBId = extract(subB.body, "id");

            r = get(base + "/api/submissions/" + subBId, tokenA);
            check("9b. Student A xem submission của Student B bị 403", r.status == 403,
                    "HTTP " + r.status + " - " + r.body);

            r = get(base + "/api/submissions", tokenA);
            check("9c. Danh sách lịch sử của A không chứa bài của B", !r.body.contains(subBId), r.body);

            r = get(base + "/api/submissions/" + subBId, tokenAdmin);
            check("9d. Admin xem được submission của mọi người", r.status == 200,
                    "HTTP " + r.status + " - " + r.body);

            // 10. Transaction luu du ca submission lan test results
            check("10. Transaction lưu đủ submission và toàn bộ test results",
                    testResultCount(database, subBId) == 4,
                    "Số dòng test_case_results của " + subBId + " = " + testResultCount(database, subBId)
                            + " (kỳ vọng 4 - bài P001 có 4 test)");

            // 12 + 13. solvedCount
            check("12a. Nộp AC lần 1 cho P001", verdictOf(post(base + "/api/submit", tokenA,
                    json("problemId", "P001", "language", "Java", "code", sumSolution()))).equals("AC"),
                    "Không nhận được verdict AC");
            check("12b. Nộp AC lần 2 cho cùng bài P001", verdictOf(post(base + "/api/submit", tokenA,
                    json("problemId", "P001", "language", "Java", "code", sumSolution()))).equals("AC"),
                    "Không nhận được verdict AC");

            r = get(base + "/api/auth/me", tokenA);
            check("12c. Nộp AC nhiều lần cùng một bài -> solvedCount = 1",
                    r.body.contains("\"solvedCount\":1"), r.body);

            check("13a. Nộp AC cho bài thứ hai P003", verdictOf(post(base + "/api/submit", tokenA,
                    json("problemId", "P003", "language", "Java", "code", avgSolution()))).equals("AC"),
                    "Không nhận được verdict AC");

            r = get(base + "/api/auth/me", tokenA);
            check("13b. AC hai bài khác nhau -> solvedCount = 2",
                    r.body.contains("\"solvedCount\":2"), r.body);

            // Mot bai WA de kiem tra thong ke verdict sau khi khoi dong lai
            post(base + "/api/submit", tokenA,
                    json("problemId", "P001", "language", "Java", "code", wrongSolution()));
        } finally {
            server.stop();
        }

        int submissionsBefore = service.getSubmissions().size();

        // ---------------------------------------------- khoi dong lai may chu
        JudgeService restarted = JudgeService.mysql(dataDir, database);
        restarted.loadData();
        ApiServer server2 = new ApiServer(restarted, 0, dataDir.resolve("no-frontend"));
        server2.start();
        String base2 = "http://localhost:" + server2.getPort();
        try {
            String freshTokenA = extract(post(base2 + "/api/auth/login", null,
                    json("username", STUDENT_A, "password", PASSWORD)).body, "token");

            // 11. Lich su van con sau khi khoi dong lai
            check("11a. Tài khoản cũ vẫn đăng nhập được sau khi khởi động lại",
                    freshTokenA != null && !freshTokenA.isEmpty(), "Không lấy được token");

            Response r = get(base2 + "/api/submissions", freshTokenA);
            check("11b. Lịch sử nộp bài vẫn còn sau khi khởi động lại",
                    restarted.getSubmissions().size() == submissionsBefore && r.body.contains("\"P001\""),
                    "Trước: " + submissionsBefore + ", sau: " + restarted.getSubmissions().size());

            check("11c. Mã nguồn đã nộp vẫn đọc lại được từ MySQL",
                    detailHasSourceCode(base2, freshTokenA, r.body), "Không thấy sourceCode trong chi tiết");

            // 14. Scoreboard va stats van dung sau khi khoi dong lai
            r = get(base2 + "/api/auth/me", freshTokenA);
            check("14a. solvedCount vẫn đúng sau khi khởi động lại (= 2)",
                    r.body.contains("\"solvedCount\":2"), r.body);

            r = get(base2 + "/api/scoreboard", freshTokenA);
            check("14b. Bảng xếp hạng đọc được dữ liệu cũ",
                    r.status == 200 && r.body.contains(STUDENT_A), "HTTP " + r.status + " - " + r.body);

            r = get(base2 + "/api/stats", freshTokenA);
            check("14c. Thống kê verdict tính trên toàn bộ lịch sử",
                    r.body.contains("\"AC\":") && r.body.contains("\"WA\":")
                            && !r.body.contains("\"totalSubmissions\":0"),
                    r.body);

            r = get(base2 + "/api/problems", freshTokenA);
            check("14d. Bài do admin tạo vẫn còn sau khi khởi động lại", r.body.contains("\"P900\""), r.body);

            // 16. Ma bai nop khong trung
            check("16. Mã bài nộp không bị trùng qua các lần khởi động", noDuplicateIds(database),
                    "Có mã bài nộp bị trùng");
        } finally {
            server2.stop();
        }

        // 15. ON DELETE CASCADE - xoa submission thi test results bay theo,
        //     xoa user thi ca submission lan test results bay theo.
        int beforeDelete = testResultCount(database, subBId);
        restarted.getSubmissions();
        boolean deleted = deleteSubmission(database, subBId);
        check("15a. Xoá submission -> test_case_results bay theo (ON DELETE CASCADE)",
                deleted && beforeDelete > 0 && testResultCount(database, subBId) == 0,
                "Trước khi xoá có " + beforeDelete + " dòng, sau khi xoá còn "
                        + testResultCount(database, subBId));

        String userAId = userIdOf(database, STUDENT_A);
        int subsOfA = submissionCountOfUser(database, userAId);
        deleteUser(database, userAId);
        check("15b. Xoá user -> submissions và test_case_results bay theo",
                subsOfA > 0 && submissionCountOfUser(database, userAId) == 0
                        && orphanTestResultCount(database) == 0,
                "Còn " + submissionCountOfUser(database, userAId) + " bài nộp và "
                        + orphanTestResultCount(database) + " dòng test mồ côi");
    }

    // ------------------------------------------------------------ kiem tra

    private static boolean tablesExist(MySqlDatabaseManager db) {
        String sql = "SELECT COUNT(*) FROM information_schema.tables "
                   + "WHERE table_schema = DATABASE() AND table_name IN "
                   + "('users','submissions','test_case_results','user_stats')";
        try (Connection c = db.open();
             PreparedStatement ps = c.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            return rs.next() && rs.getLong(1) == 4;
        } catch (SQLException e) {
            throw new IllegalStateException("Không kiểm tra được danh sách bảng", e);
        }
    }

    /** Don sach bang truoc khi chay - chi lam tren CSDL co duoi _test (da kiem tra o runAll). */
    private static void cleanTables(MySqlDatabaseManager db) {
        try (Connection c = db.open(); Statement st = c.createStatement()) {
            st.executeUpdate("DELETE FROM test_case_results");
            st.executeUpdate("DELETE FROM submissions");
            st.executeUpdate("DELETE FROM users");
        } catch (SQLException e) {
            throw new IllegalStateException("Không dọn được bảng kiểm thử", e);
        }
    }

    private static boolean databaseContainsPlaintext(MySqlDatabaseManager db, String password) {
        String sql = "SELECT username, full_name, password_hash, password_salt FROM users";
        try (Connection c = db.open();
             PreparedStatement ps = c.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                for (int i = 1; i <= 4; i++) {
                    String value = rs.getString(i);
                    if (value != null && value.contains(password)) return true;
                }
            }
        } catch (SQLException e) {
            throw new IllegalStateException("Không đọc được bảng users", e);
        }
        return false;
    }

    private static boolean noDuplicateIds(MySqlDatabaseManager db) {
        String sql = "SELECT COUNT(*) - COUNT(DISTINCT id) FROM submissions";
        try (Connection c = db.open();
             PreparedStatement ps = c.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            return rs.next() && rs.getLong(1) == 0;
        } catch (SQLException e) {
            throw new IllegalStateException("Không kiểm tra được mã bài nộp", e);
        }
    }

    private static int testResultCount(MySqlDatabaseManager db, String submissionId) {
        return countBy(db, "SELECT COUNT(*) FROM test_case_results WHERE submission_id = ?", submissionId);
    }

    private static int submissionCountOfUser(MySqlDatabaseManager db, String userId) {
        return countBy(db, "SELECT COUNT(*) FROM submissions WHERE user_id = ?", userId);
    }

    /** Dong test_case_results khong con submission cha - phai luon bang 0. */
    private static int orphanTestResultCount(MySqlDatabaseManager db) {
        String sql = "SELECT COUNT(*) FROM test_case_results t "
                   + "LEFT JOIN submissions s ON s.id = t.submission_id WHERE s.id IS NULL";
        try (Connection c = db.open();
             PreparedStatement ps = c.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            return rs.next() ? (int) rs.getLong(1) : -1;
        } catch (SQLException e) {
            throw new IllegalStateException("Không đếm được dòng test mồ côi", e);
        }
    }

    private static int countBy(MySqlDatabaseManager db, String sql, String param) {
        try (Connection c = db.open(); PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setString(1, param);
            try (ResultSet rs = ps.executeQuery()) {
                return rs.next() ? (int) rs.getLong(1) : -1;
            }
        } catch (SQLException e) {
            throw new IllegalStateException("Không thực hiện được truy vấn đếm", e);
        }
    }

    private static String userIdOf(MySqlDatabaseManager db, String username) {
        try (Connection c = db.open();
             PreparedStatement ps = c.prepareStatement("SELECT id FROM users WHERE username = ?")) {
            ps.setString(1, username);
            try (ResultSet rs = ps.executeQuery()) {
                return rs.next() ? rs.getString(1) : null;
            }
        } catch (SQLException e) {
            throw new IllegalStateException("Không tìm được tài khoản " + username, e);
        }
    }

    private static boolean deleteSubmission(MySqlDatabaseManager db, String id) {
        return executeDelete(db, "DELETE FROM submissions WHERE id = ?", id);
    }

    private static void deleteUser(MySqlDatabaseManager db, String id) {
        executeDelete(db, "DELETE FROM users WHERE id = ?", id);
    }

    private static boolean executeDelete(MySqlDatabaseManager db, String sql, String param) {
        try (Connection c = db.open(); PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setString(1, param);
            return ps.executeUpdate() > 0;
        } catch (SQLException e) {
            throw new IllegalStateException("Không xoá được bản ghi", e);
        }
    }

    private static boolean detailHasSourceCode(String base, String token, String listBody) throws IOException {
        String id = extract(listBody, "id");
        if (id == null) return false;
        Response detail = get(base + "/api/submissions/" + id, token);
        return detail.status == 200 && detail.body.contains("\"sourceCode\"")
                && detail.body.contains("class Solution");
    }

    private static String verdictOf(Response r) {
        String v = extract(r.body, "verdict");
        return v == null ? "?" : v;
    }

    // ------------------------------------------------------ du lieu kiem thu

    /**
     * Payload tao bai tap. Test an dung mot cap so rat dac biet (HIDDEN_IN / HIDDEN_OUT)
     * de neu chuoi do xuat hien trong phan hoi API thi chac chan la bi lo, chu khong
     * phai trung ngau nhien voi noi dung cua bai khac.
     */
    private static String adminProblemBody(String id) {
        return "{"
             + "\"id\":" + quote(id) + ","
             + "\"title\":\"Bài kiểm thử tự động\","
             + "\"statement\":\"Cộng hai số.\","
             + "\"timeLimitMs\":1000,"
             + "\"memoryLimitMb\":64,"
             + "\"comparator\":\"token\","
             + "\"totalPoints\":100,"
             + "\"tests\":["
             + "{\"name\":\"sample01\",\"input\":\"1 2\\n\",\"output\":\"3\\n\",\"sample\":true},"
             + "{\"name\":\"01\",\"input\":\"" + HIDDEN_IN + "\\n\",\"output\":\"" + HIDDEN_OUT + "\\n\",\"sample\":false}"
             + "]}";
    }

    private static String sumSolution() {
        return "import java.util.Scanner;\n"
             + "public class Solution {\n"
             + "    public static void main(String[] args) {\n"
             + "        Scanner sc = new Scanner(System.in);\n"
             + "        long a = sc.nextLong();\n"
             + "        long b = sc.nextLong();\n"
             + "        System.out.println(a + b);\n"
             + "    }\n"
             + "}\n";
    }

    private static String wrongSolution() {
        return "import java.util.Scanner;\n"
             + "public class Solution {\n"
             + "    public static void main(String[] args) {\n"
             + "        Scanner sc = new Scanner(System.in);\n"
             + "        long a = sc.nextLong();\n"
             + "        long b = sc.nextLong();\n"
             + "        System.out.println(a - b);\n"
             + "    }\n"
             + "}\n";
    }

    private static String avgSolution() {
        return "import java.util.Locale;\n"
             + "import java.util.Scanner;\n"
             + "public class Solution {\n"
             + "    public static void main(String[] args) {\n"
             + "        Scanner sc = new Scanner(System.in);\n"
             + "        int n = sc.nextInt();\n"
             + "        double sum = 0;\n"
             + "        for (int i = 0; i < n; i++) sum += sc.nextLong();\n"
             + "        System.out.printf(Locale.US, \"%.6f%n\", sum / n);\n"
             + "    }\n"
             + "}\n";
    }

    // --------------------------------------------------------- HTTP toi gian

    private static final class Response {
        private final int status;
        private final String body;

        private Response(int status, String body) {
            this.status = status;
            this.body = body;
        }
    }

    private static Response get(String url, String token) throws IOException {
        return send("GET", url, token, null);
    }

    private static Response post(String url, String token, String body) throws IOException {
        return send("POST", url, token, body);
    }

    private static Response send(String method, String url, String token, String body) throws IOException {
        HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
        conn.setRequestMethod(method);
        conn.setConnectTimeout(10_000);
        conn.setReadTimeout(120_000);           // cham bai Java co the mat vai giay
        conn.setRequestProperty("Content-Type", "application/json; charset=utf-8");
        if (token != null) conn.setRequestProperty("Authorization", "Bearer " + token);
        if (body != null) {
            conn.setDoOutput(true);
            byte[] data = body.getBytes(StandardCharsets.UTF_8);
            conn.setFixedLengthStreamingMode(data.length);
            try (OutputStream os = conn.getOutputStream()) {
                os.write(data);
            }
        }
        int status = conn.getResponseCode();
        InputStream in = status >= 400 ? conn.getErrorStream() : conn.getInputStream();
        String text = in == null ? "" : readAll(in);
        conn.disconnect();
        return new Response(status, text);
    }

    private static String readAll(InputStream in) throws IOException {
        java.io.ByteArrayOutputStream out = new java.io.ByteArrayOutputStream();
        byte[] buf = new byte[8192];
        int n;
        while ((n = in.read(buf)) != -1) out.write(buf, 0, n);
        in.close();
        return new String(out.toByteArray(), StandardCharsets.UTF_8);
    }

    /** Doc gia tri chuoi dau tien cua mot khoa trong JSON - du dung cho kiem thu. */
    private static String extract(String json, String key) {
        String needle = "\"" + key + "\":\"";
        int at = json.indexOf(needle);
        if (at < 0) return null;
        int start = at + needle.length();
        StringBuilder sb = new StringBuilder();
        for (int i = start; i < json.length(); i++) {
            char c = json.charAt(i);
            if (c == '\\' && i + 1 < json.length()) {
                sb.append(json.charAt(++i));
                continue;
            }
            if (c == '"') break;
            sb.append(c);
        }
        return sb.toString();
    }

    private static String json(String... keyValues) {
        StringBuilder sb = new StringBuilder("{");
        for (int i = 0; i + 1 < keyValues.length; i += 2) {
            if (i > 0) sb.append(',');
            sb.append(quote(keyValues[i])).append(':').append(quote(keyValues[i + 1]));
        }
        return sb.append('}').toString();
    }

    private static String quote(String s) {
        return com.ptit.oj.web.Json.quote(s);
    }

    // ------------------------------------------------------------- tien ich

    private static void check(String name, boolean condition, String detail) {
        if (condition) {
            passed++;
            System.out.println("  [ĐẠT ] " + name);
        } else {
            failed++;
            FAILURES.add(name + " -> " + shorten(detail));
            System.out.println("  [LỖI ] " + name + " -> " + shorten(detail));
        }
    }

    private static String shorten(String text) {
        if (text == null) return "";
        String one = text.replace("\n", " ").trim();
        return one.length() > 300 ? one.substring(0, 300) + "..." : one;
    }

    private static void copyDirectory(Path from, Path to) throws IOException {
        Files.walkFileTree(from, new SimpleFileVisitor<Path>() {
            @Override
            public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs) throws IOException {
                Files.createDirectories(to.resolve(from.relativize(dir).toString()));
                return FileVisitResult.CONTINUE;
            }

            @Override
            public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                Files.copy(file, to.resolve(from.relativize(file).toString()),
                        StandardCopyOption.REPLACE_EXISTING);
                return FileVisitResult.CONTINUE;
            }
        });
    }

    private static void deleteRecursively(Path dir) {
        if (dir == null || !Files.exists(dir)) return;
        try (java.util.stream.Stream<Path> walk = Files.walk(dir)) {
            walk.sorted(java.util.Comparator.reverseOrder()).forEach(p -> {
                try {
                    Files.deleteIfExists(p);
                } catch (IOException ignored) {
                    // don dep het suc; file con lai nam trong thu muc temp cua he dieu hanh
                }
            });
        } catch (IOException ignored) {
            // bo qua
        }
    }
}
