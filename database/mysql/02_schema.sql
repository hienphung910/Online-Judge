-- =====================================================================
--  PTIT Online Judge - luoc do bang cho MySQL 8
-- =====================================================================
--  Day la BAN THAM CHIEU, giong het nhung gi lop
--  com.ptit.oj.database.MySqlSchemaInitializer tu chay luc khoi dong.
--  Chay tay cung duoc (khong bat buoc):
--
--      mysql -u oj_app -p online_judge < database/mysql/02_schema.sql
--
--  Chay lai bao nhieu lan cung an toan va KHONG lam mat du lieu cu:
--  bang dung CREATE TABLE IF NOT EXISTS, view thi kiem tra truoc khi tao.
--  Index duoc khai bao ngay trong CREATE TABLE, vi MySQL khong ho tro
--  CREATE INDEX IF NOT EXISTS.
-- =====================================================================

-- Tren Windows, mysql.exe mac dinh khai bao charset ket noi la codepage cua
-- console (cp850/cp437). Khi do MySQL gan nhan charset do cho moi chuoi trong
-- file, va CHECK_CLAUSE se luu thanh _cp850'STUDENT' thay vi 'STUDENT'.
-- Khong sai ket qua nhung ban do lech charset va co the gay loi so sanh
-- collation ve sau. Mot dong SET NAMES sua dut diem.
SET NAMES utf8mb4;

-- ---------------------------------------------------------------------
--  users - tai khoan he thong
-- ---------------------------------------------------------------------
--  username dung collation utf8mb4_0900_ai_ci (accent-insensitive,
--  case-insensitive) nen rang buoc UNIQUE tu dong coi "Admin" va "admin"
--  la trung nhau - thay cho COLLATE NOCASE cua SQLite.
CREATE TABLE IF NOT EXISTS users (
    id                  VARCHAR(64)  NOT NULL,
    username            VARCHAR(32)  NOT NULL,
    full_name           VARCHAR(150) NOT NULL,
    role                VARCHAR(20)  NOT NULL,
    student_code        VARCHAR(30)      NULL,
    class_name          VARCHAR(50)      NULL,
    department          VARCHAR(150)     NULL,
    password_hash       VARCHAR(255) NOT NULL,
    password_salt       VARCHAR(255) NOT NULL,
    password_iterations INT UNSIGNED NOT NULL,
    created_at          DATETIME(6)  NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    PRIMARY KEY (id),
    UNIQUE KEY uq_users_username (username),
    CONSTRAINT chk_users_role CHECK (role IN ('STUDENT', 'TEACHER', 'ADMIN'))
) ENGINE = InnoDB
  DEFAULT CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;

-- ---------------------------------------------------------------------
--  submissions - lich su nop bai
-- ---------------------------------------------------------------------
--  problem_title va max_points la BAN CHUP tai thoi diem nop: de bai co
--  doi ten hay bi xoa khoi data/problems/ thi lich su cu van doc dung.
--  source_code luu ma nguon that nen xoa file goc van xem lai duoc.
CREATE TABLE IF NOT EXISTS submissions (
    id             VARCHAR(64)         NOT NULL,
    user_id        VARCHAR(64)         NOT NULL,
    problem_id     VARCHAR(30)         NOT NULL,
    problem_title  VARCHAR(255)        NOT NULL,
    language       VARCHAR(40)         NOT NULL,
    file_name      VARCHAR(255)        NOT NULL,
    source_code    LONGTEXT            NOT NULL,
    submitted_at   DATETIME(6)         NOT NULL,
    verdict        VARCHAR(20)         NOT NULL,
    score          DECIMAL(12,4)       NOT NULL DEFAULT 0,
    max_points     DECIMAL(12,4)       NOT NULL DEFAULT 0,
    max_runtime_ms BIGINT UNSIGNED     NOT NULL DEFAULT 0,
    judge_time_ms  BIGINT UNSIGNED     NOT NULL DEFAULT 0,
    global_message TEXT                NOT NULL,
    PRIMARY KEY (id),
    KEY idx_submissions_user_time    (user_id, submitted_at),
    KEY idx_submissions_user_solved  (user_id, verdict, problem_id),
    KEY idx_submissions_problem      (problem_id),
    KEY idx_submissions_verdict      (verdict),
    KEY idx_submissions_time         (submitted_at),
    CONSTRAINT fk_submissions_user
        FOREIGN KEY (user_id) REFERENCES users (id)
        ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;

-- ---------------------------------------------------------------------
--  test_case_results - ket qua cham cua tung test
-- ---------------------------------------------------------------------
--  ON DELETE CASCADE: xoa mot bai nop la ket qua test bay theo, khong con
--  ban ghi mo coi. InnoDB thuc thi rang buoc nay that su (khac SQLite,
--  noi phai bat PRAGMA foreign_keys o tung ket noi).
CREATE TABLE IF NOT EXISTS test_case_results (
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
    CONSTRAINT fk_test_results_submission
        FOREIGN KEY (submission_id) REFERENCES submissions (id)
        ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;

-- ---------------------------------------------------------------------
--  user_stats - so bai da giai, tinh lai tu du lieu that
-- ---------------------------------------------------------------------
--  CO Y khong them cot solved_count vao bang users: mot cot nhu the phai
--  cap nhat bang tay o moi cho ghi du lieu va se lech ngay khi quen mot cho.
--  VIEW nay tinh lai moi lan doc nen luon dung theo dinh nghia:
--      so bai da giai = COUNT(DISTINCT problem_id) voi verdict = 'AC'
--  => nop AC 5 lan cho cung mot bai van chi tinh la 1.
--  MySQL khong co "CREATE VIEW IF NOT EXISTS", con "CREATE OR REPLACE VIEW"
--  lai doi hoi quyen DROP - ma tai khoan oj_app CO Y khong duoc cap quyen do
--  tren CSDL that. Vi vay hoi information_schema truoc roi chi tao khi thieu.
--  Lop MySqlSchemaInitializer trong Java lam dung y het nhu doan nay.
SET @user_stats_exists = (
    SELECT COUNT(*) FROM information_schema.views
     WHERE table_schema = DATABASE() AND table_name = 'user_stats');

SET @create_user_stats = IF(@user_stats_exists > 0,
    'DO 0',
    'CREATE VIEW user_stats AS
     SELECT u.id       AS user_id,
            u.username AS username,
            (SELECT COUNT(DISTINCT s.problem_id)
               FROM submissions s
              WHERE s.user_id = u.id
                AND s.verdict = ''AC'')  AS solved_count,
            (SELECT COUNT(*)
               FROM submissions s
              WHERE s.user_id = u.id)    AS submission_count
       FROM users u');

PREPARE stmt FROM @create_user_stats;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
