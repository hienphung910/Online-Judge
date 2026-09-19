package com.ptit.oj.repository;

import com.ptit.oj.database.MySqlDatabaseManager;
import com.ptit.oj.exception.DataAccessException;
import com.ptit.oj.model.Admin;
import com.ptit.oj.model.Credentials;
import com.ptit.oj.model.Student;
import com.ptit.oj.model.Teacher;
import com.ptit.oj.model.User;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

/**
 * Kho tai khoan luu trong MySQL 8.
 *
 * Moi cau lenh deu dung PreparedStatement (chong SQL injection) va
 * try-with-resources (khong ro ri Connection / Statement / ResultSet).
 *
 * Ghi chu ve MySQL:
 *  - Ghi dung mot ban ghi bang INSERT ... ON DUPLICATE KEY UPDATE
 *    (khong phai ON CONFLICT ... DO UPDATE nhu SQLite).
 *  - Cot username dung collation utf8mb4_0900_ai_ci nen phep so sanh "=" va
 *    rang buoc UNIQUE tu dong khong phan biet hoa thuong - khong can COLLATE NOCASE.
 *  - created_at la DATETIME(6): dung setObject/getObject voi LocalDateTime de
 *    gia tri luu trong CSDL dung y nguyen gio dia phuong, khong bi lech mui gio
 *    nhu khi dung setTimestamp (Timestamp la mot moc thoi gian tuyet doi nen
 *    driver se quy doi theo serverTimezone).
 */
public class MySqlUserRepository implements UserRepository {

    private static final String COLUMNS =
            "id, username, full_name, role, student_code, class_name, department, "
          + "password_hash, password_salt, password_iterations, created_at";

    private final MySqlDatabaseManager database;

    public MySqlUserRepository(MySqlDatabaseManager database) {
        this.database = database;
    }

    // ------------------------------------------------------------------ ghi

    /** Luu tai khoan nhung GIU NGUYEN mat khau cu (dung khi chi sua ho ten...). */
    @Override
    public void save(User user) {
        if (user == null) throw new IllegalArgumentException("Không được lưu entity null");
        Optional<Credentials> existing = findCredentials(user.getId());
        if (!existing.isPresent()) {
            throw new DataAccessException("Tài khoản " + user.getUsername()
                    + " chưa có mật khẩu - hãy dùng saveWithCredentials()");
        }
        saveWithCredentials(user, existing.get());
    }

    @Override
    public void saveWithCredentials(User user, Credentials credentials) {
        if (user == null || credentials == null) {
            throw new IllegalArgumentException("Thiếu thông tin tài khoản hoặc mật khẩu");
        }
        String sql = "INSERT INTO users (" + COLUMNS + ") VALUES (?,?,?,?,?,?,?,?,?,?,?) "
                   + "ON DUPLICATE KEY UPDATE "
                   + "  username = VALUES(username),"
                   + "  full_name = VALUES(full_name),"
                   + "  role = VALUES(role),"
                   + "  student_code = VALUES(student_code),"
                   + "  class_name = VALUES(class_name),"
                   + "  department = VALUES(department),"
                   + "  password_hash = VALUES(password_hash),"
                   + "  password_salt = VALUES(password_salt),"
                   + "  password_iterations = VALUES(password_iterations)";
        try (Connection c = database.open(); PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setString(1, user.getId());
            ps.setString(2, user.getUsername());
            ps.setString(3, user.getFullName());
            ps.setString(4, user.getRoleCode());
            ps.setString(5, user instanceof Student ? ((Student) user).getStudentCode() : null);
            ps.setString(6, user instanceof Student ? ((Student) user).getClassName() : null);
            ps.setString(7, user instanceof Teacher ? ((Teacher) user).getDepartment() : null);
            ps.setString(8, credentials.getHashBase64());
            ps.setString(9, credentials.getSaltBase64());
            ps.setInt(10, credentials.getIterations());
            ps.setObject(11, LocalDateTime.now());
            ps.executeUpdate();
        } catch (SQLException e) {
            throw new DataAccessException("Không lưu được tài khoản " + user.getUsername(), e);
        }
    }

    /** Xoa tai khoan; bai nop cua ho bay theo nho ON DELETE CASCADE cua InnoDB. */
    @Override
    public boolean deleteById(String id) {
        try (Connection c = database.open();
             PreparedStatement ps = c.prepareStatement("DELETE FROM users WHERE id = ?")) {
            ps.setString(1, id);
            return ps.executeUpdate() > 0;
        } catch (SQLException e) {
            throw new DataAccessException("Không xoá được tài khoản " + id, e);
        }
    }

    // ------------------------------------------------------------------ doc

    @Override
    public Optional<User> findById(String id) {
        if (id == null) return Optional.empty();
        return queryOne("SELECT " + COLUMNS + " FROM users WHERE id = ?", id);
    }

    /** Collation utf8mb4_0900_ai_ci lo viec so sanh khong phan biet hoa thuong. */
    @Override
    public Optional<User> findByUsername(String username) {
        if (username == null) return Optional.empty();
        return queryOne("SELECT " + COLUMNS + " FROM users WHERE username = ?", username.trim());
    }

    @Override
    public boolean existsByUsername(String username) {
        return findByUsername(username).isPresent();
    }

    @Override
    public List<User> findAll() {
        List<User> users = new ArrayList<>();
        String sql = "SELECT " + COLUMNS + " FROM users ORDER BY created_at, id";
        try (Connection c = database.open();
             PreparedStatement ps = c.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) users.add(map(rs));
        } catch (SQLException e) {
            throw new DataAccessException("Không đọc được danh sách tài khoản", e);
        }
        return users;
    }

    @Override
    public int count() {
        try (Connection c = database.open();
             PreparedStatement ps = c.prepareStatement("SELECT COUNT(*) FROM users");
             ResultSet rs = ps.executeQuery()) {
            return rs.next() ? (int) rs.getLong(1) : 0;
        } catch (SQLException e) {
            throw new DataAccessException("Không đếm được số tài khoản", e);
        }
    }

    @Override
    public Optional<Credentials> findCredentials(String userId) {
        if (userId == null) return Optional.empty();
        String sql = "SELECT password_hash, password_salt, password_iterations FROM users WHERE id = ?";
        try (Connection c = database.open(); PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setString(1, userId);
            try (ResultSet rs = ps.executeQuery()) {
                if (!rs.next()) return Optional.empty();
                return Optional.of(new Credentials(
                        rs.getString("password_hash"),
                        rs.getString("password_salt"),
                        rs.getInt("password_iterations")));
            }
        } catch (SQLException e) {
            throw new DataAccessException("Không đọc được thông tin xác thực", e);
        }
    }

    // ------------------------------------------------------------- thong ke

    /** Doc tu VIEW user_stats -> dinh nghia "so bai da giai" chi nam o mot cho duy nhat. */
    @Override
    public int countSolvedProblems(String userId) {
        if (userId == null) return 0;
        String sql = "SELECT solved_count FROM user_stats WHERE user_id = ?";
        try (Connection c = database.open(); PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setString(1, userId);
            try (ResultSet rs = ps.executeQuery()) {
                return rs.next() ? (int) rs.getLong(1) : 0;
            }
        } catch (SQLException e) {
            throw new DataAccessException("Không đếm được số bài đã giải", e);
        }
    }

    @Override
    public Map<String, Integer> solvedCountByUser() {
        Map<String, Integer> result = new LinkedHashMap<>();
        try (Connection c = database.open();
             PreparedStatement ps = c.prepareStatement("SELECT user_id, solved_count FROM user_stats");
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) result.put(rs.getString(1), (int) rs.getLong(2));
        } catch (SQLException e) {
            throw new DataAccessException("Không đọc được bảng thống kê người dùng", e);
        }
        return result;
    }

    // ------------------------------------------------------------- tien ich

    private Optional<User> queryOne(String sql, String param) {
        try (Connection c = database.open(); PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setString(1, param);
            try (ResultSet rs = ps.executeQuery()) {
                return rs.next() ? Optional.of(map(rs)) : Optional.empty();
            }
        } catch (SQLException e) {
            throw new DataAccessException("Không đọc được tài khoản", e);
        }
    }

    /** Dua mot dong CSDL ve dung lop con cua User (Student / Teacher / Admin). */
    private User map(ResultSet rs) throws SQLException {
        String id = rs.getString("id");
        String username = rs.getString("username");
        String fullName = rs.getString("full_name");
        String role = rs.getString("role");

        if (User.ROLE_ADMIN.equals(role)) {
            return new Admin(id, username, fullName);
        }
        if (User.ROLE_TEACHER.equals(role)) {
            return new Teacher(id, username, fullName, orEmpty(rs.getString("department")));
        }
        return new Student(id, username, fullName,
                orEmpty(rs.getString("student_code")), orEmpty(rs.getString("class_name")));
    }

    private String orEmpty(String value) {
        return value == null ? "" : value;
    }
}
