package com.ptit.oj.repository;

import com.ptit.oj.database.MySqlDatabaseManager;
import com.ptit.oj.exception.DataAccessException;
import com.ptit.oj.language.Language;
import com.ptit.oj.language.LanguageRegistry;
import com.ptit.oj.model.JudgeResult;
import com.ptit.oj.model.Problem;
import com.ptit.oj.model.Submission;
import com.ptit.oj.model.TestCase;
import com.ptit.oj.model.TestCaseResult;
import com.ptit.oj.model.User;
import com.ptit.oj.model.Verdict;

import java.math.BigDecimal;
import java.nio.file.Paths;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.EnumMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

/**
 * Kho lich su nop bai luu trong MySQL 8.
 *
 * Diem dang chu y:
 *  - saveWithResults() ghi bang submissions va test_case_results trong MOT
 *    transaction: hoac ca hai cung vao, hoac rollback sach. Khong bao gio ton tai
 *    bai nop thieu mat ket qua test.
 *  - Khi doc lai, bai nop duoc dung lai thanh doi tuong Submission + JudgeResult
 *    day du, nen ScoreboardService / ApiServer khong can biet du lieu tu dau ra.
 *  - Neu de bai da bi xoa khoi o dia, van dung lai duoc mot Problem tu ban chup
 *    (problem_title, max_points, danh sach test da cham) de lich su cu khong vo.
 *
 * Ghi chu ve MySQL:
 *  - Ghi de bang INSERT ... ON DUPLICATE KEY UPDATE (khong phai ON CONFLICT).
 *  - Sap xep bang (submitted_at, id) - MySQL khong co rowid an nhu SQLite.
 *  - DECIMAL doc/ghi bang BigDecimal, DATETIME(6) bang LocalDateTime,
 *    BOOLEAN bang setBoolean/getBoolean, COUNT va BIGINT bang long.
 */
public class MySqlSubmissionRepository implements SubmissionRepository {

    /** So tham so toi da cho mot cau IN (...) - chia lo de khong dung gioi han cua may chu. */
    private static final int IN_CHUNK = 400;

    private static final String COLUMNS =
            "id, user_id, problem_id, problem_title, language, file_name, source_code, "
          + "submitted_at, verdict, score, max_points, max_runtime_ms, judge_time_ms, global_message";

    private final MySqlDatabaseManager database;
    private final Repository<Problem> problems;
    private final UserRepository users;
    private final LanguageRegistry languages;

    public MySqlSubmissionRepository(MySqlDatabaseManager database,
                                     Repository<Problem> problems,
                                     UserRepository users,
                                     LanguageRegistry languages) {
        this.database = database;
        this.problems = problems;
        this.users = users;
        this.languages = languages;
    }

    // ------------------------------------------------------------------ ghi

    @Override
    public void save(Submission submission) {
        saveWithResults(submission);
    }

    /**
     * Ghi bai nop + toan bo ket qua test trong MOT giao dich.
     *
     * Cac buoc: mo ket noi -> setAutoCommit(false) -> ghi submissions ->
     * xoa het ket qua test cu cua bai nop nay (bo cac test khong con ton tai)
     * -> ghi lai toan bo ket qua test moi -> commit. Bat ky loi nao cung rollback.
     */
    @Override
    public void saveWithResults(Submission submission) {
        if (submission == null) throw new IllegalArgumentException("Không được lưu entity null");

        String insertSubmission = "INSERT INTO submissions (" + COLUMNS + ") "
                + "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?) "
                + "ON DUPLICATE KEY UPDATE "
                + "  problem_title = VALUES(problem_title),"
                + "  language = VALUES(language),"
                + "  file_name = VALUES(file_name),"
                + "  source_code = VALUES(source_code),"
                + "  verdict = VALUES(verdict),"
                + "  score = VALUES(score),"
                + "  max_points = VALUES(max_points),"
                + "  max_runtime_ms = VALUES(max_runtime_ms),"
                + "  judge_time_ms = VALUES(judge_time_ms),"
                + "  global_message = VALUES(global_message)";

        String deleteOldTests = "DELETE FROM test_case_results WHERE submission_id = ?";

        String insertTest = "INSERT INTO test_case_results "
                + "(submission_id, test_case_id, ordinal, sample, verdict, runtime_ms, earned_points, message) "
                + "VALUES (?,?,?,?,?,?,?,?) "
                + "ON DUPLICATE KEY UPDATE "
                + "  ordinal = VALUES(ordinal),"
                + "  sample = VALUES(sample),"
                + "  verdict = VALUES(verdict),"
                + "  runtime_ms = VALUES(runtime_ms),"
                + "  earned_points = VALUES(earned_points),"
                + "  message = VALUES(message)";

        JudgeResult result = submission.getResult();
        Connection c = null;
        try {
            c = database.open();
            c.setAutoCommit(false);                     // mo transaction

            try (PreparedStatement ps = c.prepareStatement(insertSubmission)) {
                ps.setString(1, submission.getId());
                ps.setString(2, submission.getAuthor().getId());
                ps.setString(3, submission.getProblem().getId());
                ps.setString(4, submission.getProblem().getTitle());
                ps.setString(5, submission.getLanguage().getName());
                ps.setString(6, String.valueOf(submission.getSourcePath().getFileName()));
                ps.setString(7, submission.getSourceCode() == null ? "" : submission.getSourceCode());
                ps.setObject(8, submission.getSubmittedAt());
                ps.setString(9, result == null ? "PENDING" : result.getOverallVerdict().getCode());
                ps.setBigDecimal(10, decimal(result == null ? 0 : result.getScore()));
                ps.setBigDecimal(11, decimal(submission.getProblem().getMaxPoints()));
                ps.setLong(12, result == null ? 0 : Math.max(0, result.getMaxRuntimeMs()));
                ps.setLong(13, result == null ? 0 : Math.max(0, result.getJudgeTimeMs()));
                ps.setString(14, result == null ? "" : result.getGlobalMessage());
                ps.executeUpdate();
            }

            // Bo cac ket qua test cu khong con ton tai (vi du bai duoc cham lai voi bo test khac).
            try (PreparedStatement ps = c.prepareStatement(deleteOldTests)) {
                ps.setString(1, submission.getId());
                ps.executeUpdate();
            }

            if (result != null && !result.getTestResults().isEmpty()) {
                try (PreparedStatement ps = c.prepareStatement(insertTest)) {
                    int ordinal = 0;
                    for (TestCaseResult tr : result.getTestResults()) {
                        ps.setString(1, submission.getId());
                        ps.setString(2, tr.getTestCase().getId());
                        ps.setInt(3, ordinal++);
                        ps.setBoolean(4, tr.getTestCase().isSample());
                        ps.setString(5, tr.getVerdict().getCode());
                        ps.setLong(6, Math.max(0, tr.getRuntimeMs()));
                        ps.setBigDecimal(7, decimal(tr.getEarnedPoints()));
                        ps.setString(8, tr.getMessage());
                        ps.addBatch();
                    }
                    ps.executeBatch();
                }
            }

            c.commit();
        } catch (SQLException e) {
            rollbackQuietly(c);
            throw new DataAccessException("Không lưu được bài nộp " + submission.getId(), e);
        } finally {
            closeQuietly(c);
        }
    }

    @Override
    public boolean deleteById(String id) {
        // test_case_results co ON DELETE CASCADE nen tu bay theo (InnoDB thuc thi that su).
        try (Connection c = database.open();
             PreparedStatement ps = c.prepareStatement("DELETE FROM submissions WHERE id = ?")) {
            ps.setString(1, id);
            return ps.executeUpdate() > 0;
        } catch (SQLException e) {
            throw new DataAccessException("Không xoá được bài nộp " + id, e);
        }
    }

    // ------------------------------------------------------------------ doc

    @Override
    public Optional<Submission> findById(String id) {
        if (id == null) return Optional.empty();
        List<Submission> found = query("SELECT " + COLUMNS + " FROM submissions WHERE id = ?", id);
        return found.isEmpty() ? Optional.empty() : Optional.of(found.get(0));
    }

    @Override
    public List<Submission> findAll() {
        return query("SELECT " + COLUMNS + " FROM submissions ORDER BY submitted_at, id", null);
    }

    @Override
    public List<Submission> findAllNewestFirst() {
        return query("SELECT " + COLUMNS + " FROM submissions ORDER BY submitted_at DESC, id DESC", null);
    }

    @Override
    public List<Submission> findByUserId(String userId) {
        if (userId == null) return new ArrayList<>();
        return query("SELECT " + COLUMNS + " FROM submissions WHERE user_id = ? "
                   + "ORDER BY submitted_at DESC, id DESC", userId);
    }

    @Override
    public int count() {
        try (Connection c = database.open();
             PreparedStatement ps = c.prepareStatement("SELECT COUNT(*) FROM submissions");
             ResultSet rs = ps.executeQuery()) {
            return rs.next() ? (int) rs.getLong(1) : 0;
        } catch (SQLException e) {
            throw new DataAccessException("Không đếm được số bài nộp", e);
        }
    }

    /** Dem theo verdict tren toan bo lich su - de SQL GROUP BY lam thay vi duyet trong Java. */
    @Override
    public Map<Verdict, Integer> countByVerdict() {
        Map<Verdict, Integer> counter = new EnumMap<>(Verdict.class);
        String sql = "SELECT verdict, COUNT(*) FROM submissions GROUP BY verdict";
        try (Connection c = database.open();
             PreparedStatement ps = c.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                Verdict v = parseVerdict(rs.getString(1));
                if (v != null) counter.merge(v, (int) rs.getLong(2), Integer::sum);
            }
        } catch (SQLException e) {
            throw new DataAccessException("Không thống kê được verdict", e);
        }
        return counter;
    }

    // --------------------------------------------------------- dung lai object

    /**
     * Doc CSDL roi dung lai doi tuong. Lam hai buoc de khong mo ResultSet long nhau:
     *   1. doc het bang submissions vao danh sach Row,
     *   2. doc mot lan toan bo test_case_results cua cac bai nop do (tranh N+1 query).
     */
    private List<Submission> query(String sql, String param) {
        List<Row> rows = new ArrayList<>();
        try (Connection c = database.open(); PreparedStatement ps = c.prepareStatement(sql)) {
            if (param != null) ps.setString(1, param);
            try (ResultSet rs = ps.executeQuery()) {
                while (rs.next()) rows.add(readRow(rs));
            }
        } catch (SQLException e) {
            throw new DataAccessException("Không đọc được lịch sử nộp bài", e);
        }

        List<String> ids = new ArrayList<>(rows.size());
        for (Row r : rows) ids.add(r.id);
        Map<String, List<TestRow>> testsBySubmission = loadTestRows(ids);

        List<Submission> list = new ArrayList<>(rows.size());
        for (Row r : rows) {
            Submission s = build(r, testsBySubmission.getOrDefault(r.id, Collections.emptyList()));
            if (s != null) list.add(s);
        }
        return list;
    }

    private Submission build(Row row, List<TestRow> testRows) {
        User author = users.findById(row.userId).orElse(null);
        if (author == null) return null;        // tai khoan da bi xoa -> bo qua dong nay

        Problem problem = problems.findById(row.problemId)
                .orElseGet(() -> rebuildProblem(row, testRows));

        Language language = languages.byName(row.language).orElseGet(() -> languages.all().get(0));

        Submission s = new Submission(row.id, problem, author, language,
                Paths.get(row.fileName), row.submittedAt);
        s.setSourceCode(row.sourceCode);

        JudgeResult result = new JudgeResult(s);
        result.setJudgeTimeMs(row.judgeTimeMs);
        result.setGlobalMessage(row.globalMessage);

        for (TestRow t : testRows) {
            TestCase tc = findTestCase(problem, t.testCaseId);
            if (tc == null) {
                // De bai da doi ten test -> dung lai mot TestCase toi thieu de van xem duoc lich su.
                tc = new TestCase(t.testCaseId, "", "", t.earnedPoints, t.sample);
            }
            result.addTestResult(new TestCaseResult(tc, t.verdict, t.runtimeMs, t.earnedPoints, t.message));
        }

        if (testRows.isEmpty()) {
            // CE / IE: khong chay test nao nen verdict la loi toan cuc.
            result.markGlobal(row.verdict == null ? Verdict.IE : row.verdict, row.globalMessage);
        } else if (row.verdict != null && result.getOverallVerdict() != row.verdict) {
            // Du lieu cu bi sua tay: lay verdict trong CSDL lam chuan.
            result.markGlobal(row.verdict, row.globalMessage);
        }

        s.setResult(result);
        return s;
    }

    /**
     * De bai khong con tren o dia -> dung lai tu ban chup de bang diem va lich su
     * van hien thi dung ten bai va tong diem cu.
     */
    private Problem rebuildProblem(Row row, List<TestRow> testRows) {
        Problem p = new Problem(row.problemId, row.problemTitle, "", 0, 0, "token");
        int n = testRows.size();
        double perTest = n == 0 ? 0 : row.maxPoints / n;
        for (TestRow t : testRows) {
            p.addTestCase(new TestCase(t.testCaseId, "", "", perTest, t.sample));
        }
        return p;
    }

    /** Doc ket qua test cua nhieu bai nop bang mot so it cau IN (...) thay vi moi bai mot cau. */
    private Map<String, List<TestRow>> loadTestRows(List<String> submissionIds) {
        Map<String, List<TestRow>> byId = new LinkedHashMap<>();
        if (submissionIds.isEmpty()) return byId;

        for (int from = 0; from < submissionIds.size(); from += IN_CHUNK) {
            List<String> chunk = submissionIds.subList(from, Math.min(from + IN_CHUNK, submissionIds.size()));
            StringBuilder sql = new StringBuilder(
                    "SELECT submission_id, test_case_id, sample, verdict, runtime_ms, earned_points, message "
                  + "FROM test_case_results WHERE submission_id IN (");
            for (int i = 0; i < chunk.size(); i++) sql.append(i == 0 ? "?" : ",?");
            sql.append(") ORDER BY submission_id, ordinal, test_case_id");

            try (Connection c = database.open(); PreparedStatement ps = c.prepareStatement(sql.toString())) {
                for (int i = 0; i < chunk.size(); i++) ps.setString(i + 1, chunk.get(i));
                try (ResultSet rs = ps.executeQuery()) {
                    while (rs.next()) {
                        TestRow t = new TestRow();
                        String sid = rs.getString("submission_id");
                        t.testCaseId = rs.getString("test_case_id");
                        t.sample = rs.getBoolean("sample");
                        Verdict v = parseVerdict(rs.getString("verdict"));
                        t.verdict = v == null ? Verdict.IE : v;
                        t.runtimeMs = rs.getLong("runtime_ms");
                        t.earnedPoints = toDouble(rs.getBigDecimal("earned_points"));
                        t.message = orEmpty(rs.getString("message"));
                        byId.computeIfAbsent(sid, k -> new ArrayList<>()).add(t);
                    }
                }
            } catch (SQLException e) {
                throw new DataAccessException("Không đọc được kết quả test", e);
            }
        }
        return byId;
    }

    private Row readRow(ResultSet rs) throws SQLException {
        Row r = new Row();
        r.id = rs.getString("id");
        r.userId = rs.getString("user_id");
        r.problemId = rs.getString("problem_id");
        r.problemTitle = orEmpty(rs.getString("problem_title"));
        r.language = rs.getString("language");
        r.fileName = orEmpty(rs.getString("file_name"));
        r.sourceCode = orEmpty(rs.getString("source_code"));
        r.submittedAt = readDateTime(rs, "submitted_at");
        r.verdict = parseVerdict(rs.getString("verdict"));
        r.maxPoints = toDouble(rs.getBigDecimal("max_points"));
        r.judgeTimeMs = rs.getLong("judge_time_ms");
        r.globalMessage = orEmpty(rs.getString("global_message"));
        return r;
    }

    private TestCase findTestCase(Problem problem, String testId) {
        for (TestCase tc : problem.getTestCases()) {
            if (tc.getId().equals(testId)) return tc;
        }
        return null;
    }

    /** Mot dong cua bang submissions, doc thoi ra khoi ResultSet. */
    private static final class Row {
        private String id;
        private String userId;
        private String problemId;
        private String problemTitle;
        private String language;
        private String fileName;
        private String sourceCode;
        private LocalDateTime submittedAt;
        private Verdict verdict;
        private double maxPoints;
        private long judgeTimeMs;
        private String globalMessage;
    }

    /** Mot dong cua bang test_case_results. */
    private static final class TestRow {
        private String testCaseId;
        private boolean sample;
        private Verdict verdict;
        private long runtimeMs;
        private double earnedPoints;
        private String message;
    }

    // ------------------------------------------------------------- tien ich

    /**
     * DATETIME(6) doc bang LocalDateTime chu khong phai Timestamp: Timestamp la
     * mot moc thoi gian tuyet doi nen driver se quy doi theo serverTimezone va
     * lam lech gio hien thi; LocalDateTime giu dung gia tri nhu trong CSDL.
     */
    private static LocalDateTime readDateTime(ResultSet rs, String column) throws SQLException {
        LocalDateTime value = rs.getObject(column, LocalDateTime.class);
        return value == null ? LocalDateTime.now() : value;
    }

    private static BigDecimal decimal(double value) {
        if (Double.isNaN(value) || Double.isInfinite(value)) return BigDecimal.ZERO;
        return BigDecimal.valueOf(value).setScale(4, java.math.RoundingMode.HALF_UP);
    }

    private static double toDouble(BigDecimal value) {
        return value == null ? 0 : value.doubleValue();
    }

    private static Verdict parseVerdict(String code) {
        if (code == null) return null;
        for (Verdict v : Verdict.values()) {
            if (v.getCode().equalsIgnoreCase(code.trim())) return v;
        }
        return null;
    }

    private static String orEmpty(String value) {
        return value == null ? "" : value;
    }

    private void rollbackQuietly(Connection c) {
        if (c == null) return;
        try {
            c.rollback();
        } catch (SQLException ignored) {
            // ket noi da hong thi cung khong con gi de cuu
        }
    }

    private void closeQuietly(Connection c) {
        if (c == null) return;
        try {
            c.setAutoCommit(true);
        } catch (SQLException ignored) {
            // bo qua
        }
        try {
            c.close();
        } catch (SQLException ignored) {
            // bo qua
        }
    }
}
