package com.ptit.oj.database;

import com.ptit.oj.exception.DataAccessException;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Locale;

/**
 * Quan ly ket noi toi MySQL 8.
 *
 * Nguyen tac:
 *  - KHONG giu mot Connection dung chung toan cuc. Moi thao tac tu mo mot ket noi
 *    roi dong ngay bang try-with-resources, nen HttpServer chay nhieu thread song song
 *    khong bao gio dam nhau tren cung mot ket noi.
 *  - KHONG BAO GIO ghi mat khau ra log hay ra thong bao loi (xem maskUrl()).
 *  - Moi SQLException duoc boc thanh DataAccessException voi thong bao tieng Viet
 *    de nguoi dung biet phai sua gi, thay vi doc stack trace cua driver.
 */
public class MySqlDatabaseManager {

    private final String url;
    private final String user;
    private final String password;

    public MySqlDatabaseManager(String url, String user, String password) {
        if (url == null || url.trim().isEmpty()) {
            throw new IllegalArgumentException("Thiếu URL kết nối MySQL");
        }
        if (user == null || user.trim().isEmpty()) {
            throw new IllegalArgumentException("Thiếu tên đăng nhập MySQL");
        }
        this.url = url.trim();
        this.user = user.trim();
        this.password = password == null ? "" : password;
        loadDriver();
    }

    public static MySqlDatabaseManager from(DatabaseConfig config) {
        return new MySqlDatabaseManager(config.getUrl(), config.getUser(), config.getPassword());
    }

    private void loadDriver() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            throw new DataAccessException(
                    "Không tìm thấy trình điều khiển MySQL (mysql-connector-j). "
                  + "Hãy chạy lại bằng run.ps1 / run.sh để script tự tải thư viện về thư mục lib/, "
                  + "hoặc chạy: mvn -q dependency:copy-dependencies -DoutputDirectory=lib", e);
        }
    }

    /**
     * Mo mot ket noi moi. Nguoi goi PHAI dong bang try-with-resources.
     * Ket noi mac dinh o che do autocommit; noi nao can transaction thi tu tat.
     */
    public Connection open() {
        try {
            return DriverManager.getConnection(url, user, password);
        } catch (SQLException e) {
            throw new DataAccessException(friendlyMessage(e), e);
        }
    }

    /** Kiem tra ket noi bang SELECT 1 - goi luc khoi dong de bao loi som va rõ ràng. */
    public void testConnection() {
        try (Connection c = open();
             Statement st = c.createStatement();
             ResultSet rs = st.executeQuery("SELECT 1")) {
            if (!rs.next() || rs.getInt(1) != 1) {
                throw new DataAccessException("MySQL trả về kết quả không mong đợi cho SELECT 1");
            }
        } catch (SQLException e) {
            throw new DataAccessException(friendlyMessage(e), e);
        }
    }

    /** Ten CSDL lay tu URL, vi du "online_judge". Rong neu URL khong chi ro. */
    public String getDatabaseName() {
        return databaseNameOf(url);
    }

    /** URL da che phan nhay cam - dung khi in ra man hinh hoac ghi log. */
    public String getSafeUrl() {
        return maskUrl(url);
    }

    public String getUser() {
        return user;
    }

    @Override
    public String toString() {
        return "MySqlDatabaseManager{user=" + user + ", url=" + getSafeUrl() + "}";
    }

    // ------------------------------------------------------------- tien ich

    /** Doc ten CSDL tu chuoi jdbc:mysql://host:port/<ten>?tham-so */
    public static String databaseNameOf(String jdbcUrl) {
        if (jdbcUrl == null) return "";
        int question = jdbcUrl.indexOf('?');
        String withoutQuery = question < 0 ? jdbcUrl : jdbcUrl.substring(0, question);
        int lastSlash = withoutQuery.lastIndexOf('/');
        if (lastSlash < 0 || lastSlash == withoutQuery.length() - 1) return "";
        // Bo qua dau "//" cua phan host
        if (lastSlash > 0 && withoutQuery.charAt(lastSlash - 1) == '/') return "";
        return withoutQuery.substring(lastSlash + 1);
    }

    /**
     * Xoa moi tham so co the chua thong tin nhay cam (password, user) khoi URL
     * truoc khi in ra. Chi giu lai phan host/port/ten CSDL.
     */
    public static String maskUrl(String jdbcUrl) {
        if (jdbcUrl == null) return "";
        int question = jdbcUrl.indexOf('?');
        String base = question < 0 ? jdbcUrl : jdbcUrl.substring(0, question);
        return question < 0 ? base : base + "?...";
    }

    /** Bien loi cua driver thanh cau tieng Viet noi ro phai sua gi. */
    private String friendlyMessage(SQLException e) {
        String state = e.getSQLState() == null ? "" : e.getSQLState();
        String raw = e.getMessage() == null ? "" : e.getMessage().toLowerCase(Locale.ROOT);
        String where = " (" + getSafeUrl() + ", user=" + user + ")";

        if ("28000".equals(state) || raw.contains("access denied")) {
            return "MySQL từ chối đăng nhập" + where
                 + ". Kiểm tra lại " + DatabaseConfig.ENV_USER + " / " + DatabaseConfig.ENV_PASSWORD
                 + ", và tài khoản đã được GRANT quyền trên CSDL này chưa.";
        }
        if ("42000".equals(state) || raw.contains("unknown database")) {
            return "MySQL không có cơ sở dữ liệu này" + where
                 + ". Hãy chạy database/mysql/01_create_database.sql trước.";
        }
        if ("08S01".equals(state) || state.startsWith("08") || raw.contains("communications link failure")
                || raw.contains("connection refused")) {
            return "Không kết nối được tới máy chủ MySQL" + where
                 + ". Kiểm tra dịch vụ MySQL đã chạy chưa và đúng host/port trong "
                 + DatabaseConfig.ENV_URL + " chưa.";
        }
        return "Lỗi khi làm việc với MySQL" + where + ": " + e.getMessage();
    }
}
