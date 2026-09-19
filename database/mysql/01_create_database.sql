-- =====================================================================
--  PTIT Online Judge - tao co so du lieu va tai khoan ung dung
-- =====================================================================
--  Chay MOT LAN bang tai khoan quan tri MySQL (root), vi day la cac lenh
--  cap he thong. Sau buoc nay, UNG DUNG chay bang tai khoan 'oj_app'
--  chu KHONG dung root.
--
--  Cach chay:
--      mysql -u root -p < database/mysql/01_create_database.sql
--
--  QUAN TRONG: hay doi THAY_MAT_KHAU_NAY thanh mat khau that cua ban
--  TRUOC khi chay, va dat dung mat khau do vao bien moi truong
--  OJ_DB_PASSWORD (xem .env.example). Khong luu mat khau that vao file
--  nay roi commit len git.
-- =====================================================================

CREATE DATABASE IF NOT EXISTS online_judge
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_0900_ai_ci;

-- CSDL rieng cho bo kiem thu tich hop (--apitest).
-- Ten BAT BUOC ket thuc bang _test: chuong trinh se tu choi chay kiem thu
-- neu URL khong tro toi mot CSDL co duoi _test, de khong bao gio xoa nham
-- du lieu that.
CREATE DATABASE IF NOT EXISTS online_judge_test
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_0900_ai_ci;

CREATE USER IF NOT EXISTS 'oj_app'@'localhost'
    IDENTIFIED BY 'THAY_MAT_KHAU_NAY';

-- CREATE USER IF NOT EXISTS KHONG doi mat khau cua tai khoan da ton tai.
-- Neu chay lai script nay voi mat khau khac, khong co dong ALTER USER duoi day
-- thi MySQL van giu mat khau cu -> ung dung bao "Access denied" rat kho hieu.
-- ALTER USER lam script chay lai bao nhieu lan cung dat dung mat khau.
ALTER USER 'oj_app'@'localhost'
    IDENTIFIED BY 'THAY_MAT_KHAU_NAY';

GRANT SELECT, INSERT, UPDATE, DELETE,
      CREATE, ALTER, INDEX, REFERENCES
    ON online_judge.*
    TO 'oj_app'@'localhost';

-- Bo kiem thu con can DROP de don sach bang giua cac lan chay.
GRANT SELECT, INSERT, UPDATE, DELETE,
      CREATE, ALTER, INDEX, REFERENCES, DROP, CREATE VIEW
    ON online_judge_test.*
    TO 'oj_app'@'localhost';

-- CREATE VIEW can cho VIEW user_stats o 02_schema.sql
GRANT CREATE VIEW, SHOW VIEW ON online_judge.* TO 'oj_app'@'localhost';
GRANT SHOW VIEW ON online_judge_test.* TO 'oj_app'@'localhost';

FLUSH PRIVILEGES;
