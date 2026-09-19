package com.ptit.oj.database;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Doc cau hinh ket noi MySQL tu BIEN MOI TRUONG (khong bao gio hard-code trong ma nguon).
 *
 *   OJ_DB_URL       jdbc:mysql://localhost:3306/online_judge?...
 *   OJ_DB_USER      oj_app
 *   OJ_DB_PASSWORD  (mat khau cua tai khoan tren)
 *
 * Che do kiem thu dung bo bien rieng de khong bao gio cham vao CSDL that:
 *
 *   OJ_TEST_DB_URL / OJ_TEST_DB_USER / OJ_TEST_DB_PASSWORD
 *
 * Cho tien khi phat trien, lop nay cung doc file `.env` o thu muc goc neu co.
 * Bien moi truong that LUON duoc uu tien hon file `.env`, va `.env` da nam trong
 * .gitignore nen mat khau khong bao gio bi day len git.
 */
public final class DatabaseConfig {

    public static final String ENV_URL = "OJ_DB_URL";
    public static final String ENV_USER = "OJ_DB_USER";
    public static final String ENV_PASSWORD = "OJ_DB_PASSWORD";

    public static final String ENV_TEST_URL = "OJ_TEST_DB_URL";
    public static final String ENV_TEST_USER = "OJ_TEST_DB_USER";
    public static final String ENV_TEST_PASSWORD = "OJ_TEST_DB_PASSWORD";

    /** Gia tri goi y khi nguoi dung chua dat bien moi truong - chi de in ra huong dan. */
    public static final String SAMPLE_URL =
            "jdbc:mysql://localhost:3306/online_judge"
          + "?useUnicode=true&characterEncoding=UTF-8&serverTimezone=UTC"
          + "&useSSL=false&allowPublicKeyRetrieval=true";

    private static Map<String, String> dotEnv;

    private final String url;
    private final String user;
    private final String password;

    private DatabaseConfig(String url, String user, String password) {
        this.url = url;
        this.user = user;
        this.password = password;
    }

    public String getUrl() { return url; }
    public String getUser() { return user; }
    public String getPassword() { return password; }

    /** Bao thieu cau hinh, kem huong dan dat bien moi truong. */
    public static class MissingConfigException extends RuntimeException {
        public MissingConfigException(String message) {
            super(message);
        }
    }

    /** Cau hinh cho che do chay that. */
    public static DatabaseConfig fromEnvironment() {
        return read(ENV_URL, ENV_USER, ENV_PASSWORD, "chạy ứng dụng");
    }

    /** Cau hinh cho che do --apitest. */
    public static DatabaseConfig fromTestEnvironment() {
        return read(ENV_TEST_URL, ENV_TEST_USER, ENV_TEST_PASSWORD, "chạy kiểm thử tích hợp");
    }

    private static DatabaseConfig read(String urlKey, String userKey, String passwordKey, String purpose) {
        String url = value(urlKey);
        String user = value(userKey);
        String password = value(passwordKey);

        if (isBlank(url) || isBlank(user)) {
            throw new MissingConfigException(
                    "Thiếu cấu hình MySQL để " + purpose + ".\n"
                  + "  Hãy đặt biến môi trường " + urlKey + " và " + userKey
                  + " (và " + passwordKey + " nếu tài khoản có mật khẩu),\n"
                  + "  hoặc chép .env.example thành .env rồi điền vào đó.\n"
                  + "  Ví dụ " + urlKey + ":\n    " + SAMPLE_URL);
        }
        return new DatabaseConfig(url.trim(), user.trim(), password == null ? "" : password);
    }

    /** Cho phep truyen thang URL qua tham so --db-url (mat khau van lay tu biến moi truong). */
    public DatabaseConfig withUrl(String overrideUrl) {
        return isBlank(overrideUrl) ? this : new DatabaseConfig(overrideUrl.trim(), user, password);
    }

    /** Bien moi truong that truoc, sau do moi den file .env. */
    private static String value(String key) {
        String fromEnv = System.getenv(key);
        if (!isBlank(fromEnv)) return fromEnv;
        String fromProperty = System.getProperty(key);
        if (!isBlank(fromProperty)) return fromProperty;
        return dotEnv().get(key);
    }

    /**
     * Doc file `.env` mot lan. Cu phap don gian: KEY=VALUE, bo qua dong trong va dong
     * bat dau bang '#'. Khong ho tro chuoi nhieu dong - du dung cho vai bien cau hinh.
     */
    private static synchronized Map<String, String> dotEnv() {
        if (dotEnv != null) return dotEnv;
        dotEnv = new LinkedHashMap<>();
        Path file = Path.of(".env");
        if (!Files.isRegularFile(file)) return dotEnv;
        try {
            List<String> lines = Files.readAllLines(file, StandardCharsets.UTF_8);
            for (String raw : lines) {
                String line = raw.trim();
                if (line.isEmpty() || line.startsWith("#")) continue;
                int eq = line.indexOf('=');
                if (eq <= 0) continue;
                String key = line.substring(0, eq).trim();
                String val = line.substring(eq + 1).trim();
                if (val.length() >= 2
                        && ((val.startsWith("\"") && val.endsWith("\""))
                         || (val.startsWith("'") && val.endsWith("'")))) {
                    val = val.substring(1, val.length() - 1);
                }
                dotEnv.put(key, val);
            }
        } catch (IOException e) {
            // Khong doc duoc .env thi coi nhu khong co - bien moi truong van dung binh thuong.
            System.err.println("Không đọc được file .env: " + e.getMessage());
        }
        return dotEnv;
    }

    private static boolean isBlank(String s) {
        return s == null || s.trim().isEmpty();
    }

    /** Khong bao gio in mat khau. */
    @Override
    public String toString() {
        return "DatabaseConfig{user=" + user + ", url=" + MySqlDatabaseManager.maskUrl(url) + "}";
    }
}
