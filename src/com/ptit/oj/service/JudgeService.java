package com.ptit.oj.service;

import com.ptit.oj.core.Judge;
import com.ptit.oj.core.JudgeListener;
import com.ptit.oj.core.StatisticsListener;
import com.ptit.oj.database.MySqlDatabaseManager;
import com.ptit.oj.database.MySqlSchemaInitializer;
import com.ptit.oj.language.Language;
import com.ptit.oj.language.LanguageRegistry;
import com.ptit.oj.model.JudgeResult;
import com.ptit.oj.model.Problem;
import com.ptit.oj.model.Submission;
import com.ptit.oj.model.User;
import com.ptit.oj.model.Verdict;
import com.ptit.oj.repository.InMemoryRepository;
import com.ptit.oj.repository.InMemorySubmissionRepository;
import com.ptit.oj.repository.InMemoryUserRepository;
import com.ptit.oj.repository.ProblemDraft;
import com.ptit.oj.repository.ProblemLoader;
import com.ptit.oj.repository.Repository;
import com.ptit.oj.repository.MySqlSubmissionRepository;
import com.ptit.oj.repository.MySqlUserRepository;
import com.ptit.oj.repository.SubmissionRepository;
import com.ptit.oj.repository.UserRepository;
import com.ptit.oj.util.TextUtils;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Optional;

/**
 * Tang nghiep vu trung tam: giu du lieu (bai tap, bai nop, nguoi dung) va dieu phoi Judge.
 *
 * Vi sao can lop nay: ca giao dien console (ConsoleApp) va giao dien web (ApiServer)
 * deu dung chung mot bo du lieu va mot bo cham. Neu de logic trong ConsoleApp thi
 * web phai copy lai => tach ra day, hai tang giao dien chi con viec hien thi.
 *
 * Cac kho du lieu duoc TIEM VAO qua constructor chu khong tao san ben trong, nho vay:
 *   - che do binh thuong dung MySQL   -> du lieu con nguyen sau khi tat may,
 *   - che do --demo / --selftest dung kho trong bo nho -> khong lam ban CSDL that.
 */
public class JudgeService {

    /** So vong PBKDF2 cho --demo / --selftest: du lieu tam nen uu tien toc do. */
    private static final int DEMO_PBKDF2_ITERATIONS = 1000;

    private final Path dataDir;
    private final Repository<Problem> problems;
    private final UserRepository users;
    private final SubmissionRepository submissions;
    private final LanguageRegistry languages = new LanguageRegistry();
    private final StatisticsListener stats = new StatisticsListener();
    private final Judge judge = new Judge();

    private final ScoreboardService scoreboard;
    private final StatisticsService statistics;
    private final PasswordService passwords;
    private final SessionService sessionService = new SessionService();
    private final AuthService auth;
    private final ProblemAdminService problemAdmin;

    public JudgeService(Path dataDir,
                        Repository<Problem> problems,
                        UserRepository users,
                        SubmissionRepository submissions,
                        PasswordService passwords) {
        this.dataDir = dataDir;
        this.problems = problems;
        this.users = users;
        this.submissions = submissions;
        this.passwords = passwords;
        this.scoreboard = new ScoreboardService(submissions, problems);
        this.statistics = new StatisticsService(submissions);
        this.auth = new AuthService(users, passwords, sessionService);
        this.problemAdmin = new ProblemAdminService(problems, dataDir.resolve("problems"));
        judge.addListener(stats);
    }

    // ------------------------------------------------------- cach tao san co

    /**
     * Che do that: tai khoan va lich su nop bai nam trong MySQL, con nguyen sau
     * khi tat chuong trinh. De bai va testcase van doc tu data/problems/.
     *
     * Luoc do duoc tao neu chua co (an toan khi goi lai, khong xoa du lieu cu).
     * JudgeService chi biet cac interface UserRepository / SubmissionRepository -
     * doi sang CSDL khac chi can viet lop cai dat moi va sua dung ham nay.
     */
    public static JudgeService mysql(Path dataDir, MySqlDatabaseManager database) {
        new MySqlSchemaInitializer(database).initialize();

        Repository<Problem> problems = new InMemoryRepository<>();   // de bai van doc tu o dia
        MySqlUserRepository users = new MySqlUserRepository(database);
        LanguageRegistry languages = new LanguageRegistry();
        MySqlSubmissionRepository submissions =
                new MySqlSubmissionRepository(database, problems, users, languages);
        return new JudgeService(dataDir, problems, users, submissions, new PasswordService());
    }

    /**
     * Che do --demo / --selftest: moi thu trong RAM, khong can MySQL va khong dong
     * toi CSDL that, nen chay bao nhieu lan cung cho ket qua giong nhau.
     * So vong lap PBKDF2 ha xuong cho nhanh vi day chi la du lieu tam.
     */
    public static JudgeService inMemory(Path dataDir) {
        return inMemory(dataDir, new PasswordService(DEMO_PBKDF2_ITERATIONS));
    }

    /**
     * Nhu inMemory(Path) nhung tu chon bo bam mat khau.
     *
     * Che do --no-db dung ham nay voi PasswordService() mac dinh (120 000 vong)
     * de phan dang nhap chay dung nhu ban that, chi khac cho luu la RAM. Con
     * --demo / --selftest dung ban 1000 vong cho nhanh vi khong ai dang nhap.
     *
     * Ca ConsoleApp va ApiServer chi biet JudgeService nen doi kho du lieu o day
     * la du - hai tang giao dien khong phai sua mot dong nao.
     */
    public static JudgeService inMemory(Path dataDir, PasswordService passwords) {
        Repository<Problem> problems = new InMemoryRepository<>();
        InMemoryUserRepository users = new InMemoryUserRepository();
        InMemorySubmissionRepository submissions = new InMemorySubmissionRepository();
        users.setSubmissionRepository(submissions);
        return new JudgeService(dataDir, problems, users, submissions, passwords);
    }

    /** Gan them observer cho qua trinh cham (vi du: in tien trinh ra console). */
    public void addJudgeListener(JudgeListener listener) {
        judge.addListener(listener);
    }

    /** Go observer ra - dung cho listener chi song trong mot request (xem SseJudgeListener). */
    public void removeJudgeListener(JudgeListener listener) {
        judge.removeListener(listener);
    }

    /** Nap de bai tu o dia. Tai khoan KHONG con hard-code o day nua - xem AuthService. */
    public void loadData() {
        for (Problem p : new ProblemLoader(dataDir.resolve("problems")).loadAll()) {
            problems.save(p);
        }
    }

    // ------------------------------------------------------------- truy van

    public Path getDataDir() { return dataDir; }

    public List<Problem> getProblems() { return problems.findAll(); }

    public Optional<Problem> findProblem(String id) {
        return id == null ? Optional.empty() : problems.findById(id.trim().toUpperCase());
    }

    public List<Submission> getSubmissions() { return submissions.findAll(); }

    /** Bai nop moi nhat truoc (dung cho bang lich su tren web). */
    public List<Submission> getSubmissionsNewestFirst() { return submissions.findAllNewestFirst(); }

    /** Lich su cua rieng mot nguoi - dung de hoc sinh chi thay bai cua chinh minh. */
    public List<Submission> getSubmissionsOf(User user) {
        return user == null ? new ArrayList<>() : submissions.findByUserId(user.getId());
    }

    public Optional<Submission> findSubmission(String id) {
        return id == null ? Optional.empty() : submissions.findById(id.trim().toUpperCase());
    }

    public List<User> getUsers() { return users.findAll(); }

    public Optional<User> findUser(String username) { return users.findByUsername(username); }

    public int getSolvedCount(User user) { return auth.solvedCount(user); }

    public Map<String, Integer> getSolvedCountByUser() { return users.solvedCountByUser(); }

    public List<Language> getLanguages() { return languages.all(); }

    public Optional<Language> detectLanguage(Path source) { return languages.detect(source); }

    public Optional<Language> findLanguage(String name) { return languages.byName(name); }

    /** Thong ke cua rieng phien dang chay (observer minh hoa mau Observer). */
    public StatisticsListener getStats() { return stats; }

    /** Thong ke doc tu kho du lieu - dung cho ca lich su cu truoc khi khoi dong lai. */
    public StatisticsService getStatistics() { return statistics; }

    public Map<Verdict, Integer> getVerdictCounts() { return statistics.countByVerdict(); }

    public List<ScoreboardService.Row> buildScoreboard() { return scoreboard.buildScoreboard(); }

    public AuthService getAuth() { return auth; }

    public SessionService getSessions() { return sessionService; }

    public PasswordService getPasswords() { return passwords; }

    // ------------------------------------------------------------- nghiep vu

    /** Nop bai bang file co san tren o dia (giao dien console). */
    public JudgeResult submitFile(Problem problem, User author, Path source, Language language) {
        Submission submission = new Submission(problem, author, language, source.toAbsolutePath());
        submission.setSourceCode(readSourceQuietly(source));
        JudgeResult result = judge.judge(submission);
        submissions.saveWithResults(submission);
        return result;
    }

    /**
     * Nop bai bang ma nguon dang van ban (nguoi dung dan code tren web).
     * Ma nguon duoc ghi ra file tam de bien dich, sau do xoa file va giu lai
     * noi dung trong CSDL de xem lai duoc sau nay.
     */
    public JudgeResult submitCode(Problem problem, User author, Language language, String code)
            throws IOException {
        String cleaned = TextUtils.stripBom(code == null ? "" : code);
        Path tempDir = Files.createTempDirectory("oj-upload-");
        Path source = tempDir.resolve(language.defaultFileName(cleaned));
        Files.write(source, cleaned.getBytes(StandardCharsets.UTF_8));

        Submission submission = new Submission(problem, author, language, source);
        submission.setSourceCode(cleaned);
        try {
            JudgeResult result = judge.judge(submission);
            // Luu SAU khi cham xong: bai nop va ket qua tung test vao CSDL
            // trong cung mot transaction, khong bao gio con ban ghi do dang.
            submissions.saveWithResults(submission);
            return result;
        } finally {
            deleteQuietly(source);
            deleteQuietly(tempDir);
        }
    }

    /** Tao bai tap moi - chi tai khoan ADMIN goi duoc (kiem tra trong ProblemAdminService). */
    public Problem createProblem(User actor, ProblemDraft draft) {
        return problemAdmin.createProblem(actor, draft);
    }

    private String readSourceQuietly(Path source) {
        try {
            return TextUtils.stripBom(new String(Files.readAllBytes(source), StandardCharsets.UTF_8));
        } catch (IOException e) {
            return "";   // khong doc duoc thi van cham binh thuong, chi la khong luu duoc ma nguon
        }
    }

    private void deleteQuietly(Path path) {
        try {
            Files.deleteIfExists(path);
        } catch (IOException ignored) {
            // file tam se do he dieu hanh don
        }
    }

    // ------------------------------------------------------- kich ban demo

    /** Mot dong trong data/submissions/demo-plan.txt. */
    public static class DemoEntry {
        private final String problemId;
        private final String username;
        private final Path source;
        private final String expectedVerdict;

        DemoEntry(String problemId, String username, Path source, String expectedVerdict) {
            this.problemId = problemId;
            this.username = username;
            this.source = source;
            this.expectedVerdict = expectedVerdict;
        }

        public String getProblemId() { return problemId; }
        public String getUsername() { return username; }
        public Path getSource() { return source; }
        public String getExpectedVerdict() { return expectedVerdict; }
    }

    /**
     * Doc kich ban demo. Cu phap moi dong:
     *   maBai | username | duong dan tuong doi | verdict ky vong (tuy chon)
     * @param badLines noi de ghi lai cac dong sai cu phap (co the null)
     */
    public List<DemoEntry> readDemoPlan(List<String> badLines) throws IOException {
        Path plan = dataDir.resolve("submissions").resolve("demo-plan.txt");
        List<DemoEntry> entries = new ArrayList<>();
        if (!Files.isRegularFile(plan)) {
            throw new IOException("Không tìm thấy " + plan.toAbsolutePath());
        }
        for (String raw : Files.readAllLines(plan, StandardCharsets.UTF_8)) {
            String line = TextUtils.stripBom(raw).trim();
            if (line.isEmpty() || line.startsWith("#")) continue;
            String[] parts = line.split("\\|");
            if (parts.length < 3) {
                if (badLines != null) badLines.add(line);
                continue;
            }
            String expected = parts.length >= 4 ? parts[3].trim().toUpperCase() : "";
            entries.add(new DemoEntry(
                    parts[0].trim().toUpperCase(),
                    parts[1].trim(),
                    dataDir.resolve("submissions").resolve(parts[2].trim()),
                    expected.isEmpty() ? null : expected));
        }
        return entries;
    }
}
