package com.ptit.oj.web;

import com.ptit.oj.exception.DataAccessException;
import com.ptit.oj.language.Language;
import com.ptit.oj.model.JudgeResult;
import com.ptit.oj.model.Problem;
import com.ptit.oj.model.Submission;
import com.ptit.oj.model.TestCase;
import com.ptit.oj.model.TestCaseResult;
import com.ptit.oj.model.User;
import com.ptit.oj.model.Verdict;
import com.ptit.oj.repository.ProblemDraft;
import com.ptit.oj.service.AuthService;
import com.ptit.oj.service.JudgeService;
import com.ptit.oj.service.ProblemAdminService;
import com.ptit.oj.service.ScoreboardService;
import com.ptit.oj.service.SessionService;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * May chu HTTP cho giao dien web, dung com.sun.net.httpserver co san trong JDK.
 *
 * Nhiem vu:
 *  - Cung cap REST API doc/ghi du lieu cua JudgeService (tang nghiep vu).
 *  - Kiem tra dang nhap va phan quyen cho tung endpoint.
 *  - Phuc vu file tinh cua frontend da build (frontend/dist).
 *
 * An toan: chi lang nghe tren 127.0.0.1. Vi may chu nay bien dich va chay ma
 * nguon tuy y nen KHONG duoc mo ra mang LAN.
 *
 * Nguyen tac phan quyen: KHONG BAO GIO tin du lieu client gui len.
 *  - nguoi nop bai lay tu token, khong lay tu truong "username" trong body,
 *  - hoc sinh chi doc duoc lich su cua chinh minh,
 *  - endpoint /api/admin/* kiem tra vai tro o backend, khong dua vao viec
 *    frontend co hien nut hay khong.
 */
public class ApiServer {

    private static final DateTimeFormatter ISO = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss");
    private static final int MAX_BODY_BYTES = 512 * 1024;        // 512 KB, du cho mot bai nop
    private static final int MAX_ADMIN_BODY_BYTES = 8 * 1024 * 1024;  // de bai + test co the lon hon

    private final JudgeService service;
    private final int port;
    private final Path webRoot;

    /**
     * Cham bai tuan tu: neu hai request cham cung luc, hai tien trinh se tranh CPU
     * lam thoi gian do duoc sai lech, de bi TLE oan.
     */
    private final Object judgeLock = new Object();

    private HttpServer server;
    private ExecutorService pool;

    public ApiServer(JudgeService service, int port, Path webRoot) {
        this.service = service;
        this.port = port;
        this.webRoot = webRoot;
    }

    public void start() throws IOException {
        server = HttpServer.create(new InetSocketAddress(InetAddress.getLoopbackAddress(), port), 0);
        pool = Executors.newFixedThreadPool(4);
        server.setExecutor(pool);
        server.createContext("/api/", this::handleApi);
        server.createContext("/", this::handleStatic);
        server.start();

        System.out.println("Máy chủ web đã chạy: http://localhost:" + getPort());
        if (Files.isDirectory(webRoot)) {
            System.out.println("Giao diện web: " + webRoot.toAbsolutePath());
        } else {
            System.out.println("Chưa có frontend đã build tại " + webRoot.toAbsolutePath());
            System.out.println("  -> chạy: cd frontend && npm install && npm run build");
            System.out.println("  -> hoặc dùng chế độ dev: cd frontend && npm run dev");
        }
        System.out.println("Nhấn Ctrl+C để dừng.");
    }

    public void stop() {
        if (server != null) server.stop(0);
        if (pool != null) pool.shutdownNow();
    }

    /** Cong thuc su dang lang nghe (huu ich khi truyen port = 0 de he dieu hanh tu chon). */
    public int getPort() {
        return server == null ? port : server.getAddress().getPort();
    }

    // --------------------------------------------------------------- REST API

    private void handleApi(HttpExchange ex) throws IOException {
        String path = ex.getRequestURI().getPath();
        String method = ex.getRequestMethod();
        try {
            route(ex, method, path);
        } catch (ApiException e) {
            sendError(ex, e.getStatus(), e.getMessage());
        } catch (AuthService.AuthException e) {
            sendError(ex, e.getHttpStatus(), e.getMessage());
        } catch (ProblemAdminService.ProblemAdminException e) {
            sendError(ex, e.getHttpStatus(), e.getMessage());
        } catch (IllegalArgumentException e) {
            sendError(ex, 400, e.getMessage());
        } catch (DataAccessException e) {
            // Khong lo chi tiet SQL / duong dan CSDL ra ngoai, nhung van ghi log de sua.
            System.err.println("Lỗi CSDL khi xử lý " + method + " " + path + ": " + e);
            sendError(ex, 500, "Lỗi truy cập cơ sở dữ liệu");
        } catch (RuntimeException e) {
            // Khong de mot request loi lam sap ca may chu, cung khong tra stack trace ve client.
            System.err.println("Lỗi khi xử lý " + method + " " + path + ": " + e);
            sendError(ex, 500, "Lỗi máy chủ nội bộ");
        }
    }

    private void route(HttpExchange ex, String method, String path) throws IOException {
        // ---- cong khai (chua can dang nhap) ----
        if ("GET".equals(method) && path.equals("/api/health")) {
            sendJson(ex, 200, Json.obj().put("ok", true)
                    .put("problems", service.getProblems().size()).build());
            return;
        }
        if ("GET".equals(method) && path.equals("/api/languages")) {
            sendJson(ex, 200, languagesJson());
            return;
        }
        if ("POST".equals(method) && path.equals("/api/auth/register")) {
            handleRegister(ex);
            return;
        }
        if ("POST".equals(method) && path.equals("/api/auth/login")) {
            handleLogin(ex);
            return;
        }
        if ("POST".equals(method) && path.equals("/api/auth/logout")) {
            handleLogout(ex);
            return;
        }

        // ---- can dang nhap ----
        if ("GET".equals(method) && path.equals("/api/auth/me")) {
            sendJson(ex, 200, userJson(requireUser(ex), true));
            return;
        }
        if ("GET".equals(method) && path.equals("/api/problems")) {
            requireUser(ex);
            sendJson(ex, 200, problemsJson());
            return;
        }
        if ("GET".equals(method) && path.equals("/api/submissions")) {
            sendJson(ex, 200, submissionsJson(requireUser(ex)));
            return;
        }
        if ("GET".equals(method) && path.startsWith("/api/submissions/")) {
            handleSubmissionDetail(ex, requireUser(ex), path.substring("/api/submissions/".length()));
            return;
        }
        if ("GET".equals(method) && path.equals("/api/scoreboard")) {
            requireUser(ex);
            sendJson(ex, 200, scoreboardJson());
            return;
        }
        if ("GET".equals(method) && path.equals("/api/stats")) {
            requireUser(ex);
            sendJson(ex, 200, statsJson());
            return;
        }
        if ("POST".equals(method) && path.equals("/api/submit/stream")) {
            handleSubmitStream(ex, requireUser(ex));
            return;
        }
        if ("POST".equals(method) && path.equals("/api/submit")) {
            handleSubmit(ex, requireUser(ex));
            return;
        }

        // ---- chi ADMIN ----
        if ("POST".equals(method) && path.equals("/api/admin/problems")) {
            handleCreateProblem(ex, requireAdmin(ex));
            return;
        }

        if ("GET".equals(method) || "POST".equals(method)) {
            throw ApiException.notFound("Không có endpoint " + path);
        }
        throw new ApiException(405, "Phương thức không hỗ trợ: " + method);
    }

    // ------------------------------------------------------------ xac thuc

    /** Lay tai khoan tu header Authorization. Nem 401 neu chua dang nhap. */
    private User requireUser(HttpExchange ex) {
        String token = SessionService.extractBearerToken(ex.getRequestHeaders().getFirst("Authorization"));
        Optional<User> user = service.getAuth().authenticate(token);
        if (!user.isPresent()) {
            throw ApiException.unauthorized("Bạn cần đăng nhập để dùng chức năng này");
        }
        return user.get();
    }

    /** Nem 401 neu chua dang nhap, 403 neu dang nhap nhung khong phai quan tri. */
    private User requireAdmin(HttpExchange ex) {
        User user = requireUser(ex);
        if (!User.ROLE_ADMIN.equals(user.getRoleCode())) {
            throw ApiException.forbidden("Chỉ tài khoản quản trị mới được dùng chức năng này");
        }
        return user;
    }

    /** ADMIN va giang vien xem duoc toan bo lich su; hoc sinh chi xem cua minh. */
    private boolean canSeeEveryone(User user) {
        return User.ROLE_ADMIN.equals(user.getRoleCode())
                || User.ROLE_TEACHER.equals(user.getRoleCode());
    }

    private void handleRegister(HttpExchange ex) throws IOException {
        Json.Value body = Json.parseObject(readBody(ex, MAX_BODY_BYTES));
        // Cho du client co gui "role": "ADMIN" thi cung bi bo qua: register() luon tao STUDENT.
        User created = service.getAuth().register(
                body.getString("username"),
                body.getString("password"),
                body.getString("fullName"),
                body.getString("studentCode"),
                body.getString("className"));
        sendJson(ex, 201, Json.obj()
                .put("message", "Đăng ký thành công, mời bạn đăng nhập")
                .putRaw("user", userJson(created, false))
                .build());
    }

    private void handleLogin(HttpExchange ex) throws IOException {
        Json.Value body = Json.parseObject(readBody(ex, MAX_BODY_BYTES));
        AuthService.LoginResult result = service.getAuth()
                .login(body.getString("username"), body.getString("password"));
        sendJson(ex, 200, Json.obj()
                .put("token", result.getToken())
                .putRaw("user", userJson(result.getUser(), true))
                .build());
    }

    private void handleLogout(HttpExchange ex) throws IOException {
        String token = SessionService.extractBearerToken(ex.getRequestHeaders().getFirst("Authorization"));
        service.getAuth().logout(token);
        // Luon tra ve 200: dang xuat mot token da het han khong phai la loi.
        sendJson(ex, 200, Json.obj().put("ok", true).build());
    }

    /** JSON cua mot tai khoan - KHONG BAO GIO kem password_hash hay password_salt. */
    private String userJson(User user, boolean withStats) {
        Json.Obj o = Json.obj()
                .put("id", user.getId())
                .put("username", user.getUsername())
                .put("fullName", user.getFullName())
                .put("role", user.getRoleCode())
                .put("roleName", user.getRole())
                .put("canCreateProblem", user.canCreateProblem());
        if (withStats) {
            o.put("solvedCount", service.getSolvedCount(user));
        }
        return o.build();
    }

    // ------------------------------------------------------------- du lieu

    private String languagesJson() {
        List<String> items = new ArrayList<>();
        for (Language l : service.getLanguages()) {
            items.add(Json.obj()
                    .put("name", l.getName())
                    .put("extension", l.getFileExtension())
                    .put("available", l.isAvailable())
                    .put("memoryLimitNote", l.getMemoryLimitNote())
                    .build());
        }
        return Json.array(items);
    }

    /**
     * Danh sach bai tap. KHONG tra ve so luong test, va chi tra ve input/output
     * cua test VI DU - test an khong bao gio roi xuong trinh duyet.
     */
    private String problemsJson() {
        List<String> items = new ArrayList<>();
        for (Problem p : service.getProblems()) {
            List<String> samples = new ArrayList<>();
            for (TestCase tc : p.getTestCases()) {
                if (!tc.isSample()) continue;
                samples.add(Json.obj()
                        .put("input", tc.getInput())
                        .put("output", tc.getExpectedOutput())
                        .build());
            }
            items.add(Json.obj()
                    .put("id", p.getId())
                    .put("title", p.getTitle())
                    .put("statement", p.getStatement())
                    .put("timeLimitMs", p.getTimeLimitMs())
                    .put("memoryLimitMb", p.getMemoryLimitMb())
                    .put("comparator", p.getComparatorSpec())
                    .put("maxPoints", p.getMaxPoints())
                    .putRaw("samples", Json.array(samples))
                    .build());
        }
        return Json.array(items);
    }

    private String submissionsJson(User viewer) {
        List<Submission> list = canSeeEveryone(viewer)
                ? service.getSubmissionsNewestFirst()
                : service.getSubmissionsOf(viewer);
        List<String> items = new ArrayList<>();
        for (Submission s : list) {
            items.add(submissionJson(s, false));
        }
        return Json.array(items);
    }

    private void handleSubmissionDetail(HttpExchange ex, User viewer, String id) throws IOException {
        Optional<Submission> found = service.findSubmission(id);
        if (!found.isPresent()) {
            throw ApiException.notFound("Không có mã nộp " + id);
        }
        Submission s = found.get();
        // Chan viec doan ma nop de doc ma nguon cua nguoi khac.
        if (!canSeeEveryone(viewer) && !s.getAuthor().getId().equals(viewer.getId())) {
            throw ApiException.forbidden("Bạn chỉ được xem bài nộp của chính mình");
        }
        sendJson(ex, 200, submissionJson(s, true));
    }

    /** @param detail true -> kem ket qua tung test va ma nguon */
    private String submissionJson(Submission s, boolean detail) {
        JudgeResult r = s.getResult();
        Json.Obj o = Json.obj()
                .put("id", s.getId())
                .put("submittedAt", s.getSubmittedAt().format(ISO))
                .put("author", s.getAuthor().getUsername())
                .put("authorName", s.getAuthor().getFullName())
                .putRaw("problem", Json.obj()
                        .put("id", s.getProblem().getId())
                        .put("title", s.getProblem().getTitle())
                        .build())
                .put("language", s.getLanguage().getName())
                .put("fileName", String.valueOf(s.getSourcePath().getFileName()))
                .put("maxPoints", s.getProblem().getMaxPoints());

        if (r == null) {
            o.put("verdict", "PENDING").put("verdictName", "Chờ chấm")
             .putNull("execTimeMs").putNull("score")
             .put("passed", 0).put("total", s.getProblem().getTestCases().size());
        } else {
            Verdict v = r.getOverallVerdict();
            o.put("verdict", v.getCode())
             .put("verdictName", v.getDisplay())
             .put("execTimeMs", r.getMaxRuntimeMs())
             .put("judgeTimeMs", r.getJudgeTimeMs())
             .put("score", r.getScore())
             .put("passed", r.getPassedCount())
             .put("total", r.getTotalTests())
             .put("message", r.getGlobalMessage());
        }

        if (detail) {
            List<String> tests = new ArrayList<>();
            if (r != null) {
                for (TestCaseResult tr : r.getTestResults()) {
                    // Chi tra ve ket qua cham, khong tra ve input/output cua test an.
                    // message la ban CONG KHAI cua comparator (khong chua dap an) - xem
                    // OutputComparator.explain(); ban kem dap an chi co tren terminal.
                    tests.add(Json.obj()
                            .put("id", tr.getTestCase().getId())
                            .put("sample", tr.getTestCase().isSample())
                            .put("verdict", tr.getVerdict().getCode())
                            .put("runtimeMs", tr.getRuntimeMs())
                            .put("points", tr.getEarnedPoints())
                            .put("message", tr.getMessage())
                            .build());
                }
            }
            o.putRaw("tests", Json.array(tests));
            if (s.getSourceCode() != null) o.put("sourceCode", s.getSourceCode());
        }
        return o.build();
    }

    private String scoreboardJson() {
        Map<String, Integer> solvedByUser = service.getSolvedCountByUser();
        List<String> rows = new ArrayList<>();
        int rank = 1;
        for (ScoreboardService.Row row : service.buildScoreboard()) {
            List<String> perProblem = new ArrayList<>();
            for (Map.Entry<String, Double> e : row.getBestPerProblem().entrySet()) {
                perProblem.add(Json.obj().put("problemId", e.getKey()).put("score", e.getValue()).build());
            }
            rows.add(Json.obj()
                    .put("rank", rank++)
                    .put("username", row.getUser().getUsername())
                    .put("fullName", row.getUser().getFullName())
                    .put("role", row.getUser().getRoleCode())
                    .put("roleName", row.getUser().getRole())
                    .put("total", row.getTotal())
                    .put("solved", row.getSolved())
                    .put("solvedCount", solvedByUser.getOrDefault(row.getUser().getId(), 0))
                    .put("attempts", row.getAttempts())
                    .putRaw("perProblem", Json.array(perProblem))
                    .build());
        }
        return Json.array(rows);
    }

    /** Thong ke doc tu CSDL nen bao gom ca lich su truoc khi khoi dong lai may chu. */
    private String statsJson() {
        Map<String, Long> counts = new LinkedHashMap<>();
        for (Map.Entry<Verdict, Integer> e : service.getVerdictCounts().entrySet()) {
            counts.put(e.getKey().getCode(), (long) e.getValue());
        }
        Json.Obj byVerdict = Json.obj();
        for (Map.Entry<String, Long> e : counts.entrySet()) {
            byVerdict.put(e.getKey(), e.getValue());
        }
        return Json.obj()
                .put("totalSubmissions", service.getStatistics().getTotalSubmissions())
                .putRaw("byVerdict", byVerdict.build())
                .build();
    }

    /**
     * POST /api/submit  body: {problemId, language, code}
     *
     * Truong "username" (neu client van gui) bi BO QUA hoan toan: nguoi nop luon
     * lay tu token dang nhap nen khong the mao danh nguoi khac.
     */
    private void handleSubmit(HttpExchange ex, User author) throws IOException {
        SubmitRequest req = readSubmitRequest(ex);

        Submission submission;
        synchronized (judgeLock) {          // cham tuan tu de do thoi gian chinh xac
            JudgeResult result = service.submitCode(req.problem, author, req.language, req.code);
            submission = result.getSubmission();
        }
        sendJson(ex, 200, submissionJson(submission, true));
    }

    /**
     * POST /api/submit/stream - giong /api/submit nhung tra ket qua TUNG TEST ngay khi
     * chay xong, thay vi doi cham het moi tra mot cuc.
     *
     * Ban dong bo (/api/submit) van giu nguyen khong doi, nen frontend cu hay cong cu
     * dong lenh nao dang dung no khong bi anh huong.
     *
     * Trat tu quan trong: MOI kiem tra dau vao phai xong TRUOC sendResponseHeaders,
     * vi sau khi header da di roi thi khong dat lai duoc ma HTTP nua - luc do loi chi
     * bao ve duoc qua mot su kien "error".
     */
    private void handleSubmitStream(HttpExchange ex, User author) throws IOException {
        SubmitRequest req = readSubmitRequest(ex);   // nem ApiException => tra 4xx binh thuong

        ex.getResponseHeaders().set("Content-Type", "text/event-stream; charset=utf-8");
        ex.getResponseHeaders().set("Cache-Control", "no-store");
        ex.getResponseHeaders().set("X-Accel-Buffering", "no");   // proxy dung gom bo dem
        ex.sendResponseHeaders(200, 0);                           // 0 = chunked, giu ket noi mo

        try (OutputStream os = ex.getResponseBody()) {
            SseJudgeListener sse = new SseJudgeListener(os);
            try {
                Submission submission;
                synchronized (judgeLock) {
                    service.addJudgeListener(sse);
                    try {
                        JudgeResult result =
                                service.submitCode(req.problem, author, req.language, req.code);
                        submission = result.getSubmission();
                    } finally {
                        // Go trong finally: cham loi hay khong thi listener cung khong
                        // duoc phep o lai trong Judge sau khi request nay ket thuc.
                        service.removeJudgeListener(sse);
                    }
                }
                sse.sendDone(submissionJson(submission, true));
            } catch (IOException | RuntimeException e) {
                System.err.println("Lỗi khi chấm bài (stream): " + e);
                sse.sendError("Lỗi máy chủ khi chấm bài");
            }
        }
    }

    /** Ba truong da kiem tra hop le cua mot yeu cau nop bai. */
    private static final class SubmitRequest {
        final Problem problem;
        final Language language;
        final String code;

        SubmitRequest(Problem problem, Language language, String code) {
            this.problem = problem;
            this.language = language;
            this.code = code;
        }
    }

    /** Doc va kiem tra than request nop bai - dung chung cho ban dong bo va ban stream. */
    private SubmitRequest readSubmitRequest(HttpExchange ex) throws IOException {
        Json.Value body = Json.parseObject(readBody(ex, MAX_BODY_BYTES));

        String problemId = body.getString("problemId");
        String languageName = body.getString("language");
        String code = body.getString("code");

        Optional<Problem> problem = service.findProblem(problemId);
        if (!problem.isPresent()) {
            throw ApiException.notFound("Không có bài " + problemId);
        }
        Optional<Language> language = service.findLanguage(languageName);
        if (!language.isPresent()) {
            throw ApiException.badRequest("Không hỗ trợ ngôn ngữ " + languageName);
        }
        if (!language.get().isAvailable()) {
            throw ApiException.badRequest("Máy này chưa cài toolchain cho " + language.get().getName());
        }
        if (code == null || code.trim().isEmpty()) {
            throw ApiException.badRequest("Mã nguồn rỗng");
        }
        return new SubmitRequest(problem.get(), language.get(), code);
    }

    /** POST /api/admin/problems - tao bai tap moi, chi ADMIN. */
    private void handleCreateProblem(HttpExchange ex, User admin) throws IOException {
        Json.Value body = Json.parseObject(readBody(ex, MAX_ADMIN_BODY_BYTES));

        ProblemDraft draft = new ProblemDraft();
        draft.setId(body.getString("id"));
        draft.setTitle(body.getString("title"));
        draft.setStatement(body.getString("statement"));
        draft.setTimeLimitMs(body.getLong("timeLimitMs", 2000));
        draft.setMemoryLimitMb((int) body.getLong("memoryLimitMb", 256));
        draft.setComparator(body.getString("comparator", "token"));
        draft.setTotalPoints(body.getDouble("totalPoints", 100));

        if (!body.get("tests").isArray()) {
            throw ApiException.badRequest("Thiếu danh sách test (\"tests\" phải là một mảng)");
        }
        for (Json.Value t : body.getArray("tests")) {
            if (!t.isObject()) throw ApiException.badRequest("Mỗi phần tử của \"tests\" phải là một object");
            draft.addTest(new ProblemDraft.TestDraft(
                    t.getString("name"),
                    t.getString("input"),
                    t.getString("output"),
                    t.getBoolean("sample", false)));
        }

        Problem created = service.createProblem(admin, draft);
        sendJson(ex, 201, Json.obj()
                .put("message", "Đã tạo bài " + created.getId())
                .putRaw("problem", Json.obj()
                        .put("id", created.getId())
                        .put("title", created.getTitle())
                        .put("timeLimitMs", created.getTimeLimitMs())
                        .put("memoryLimitMb", created.getMemoryLimitMb())
                        .put("comparator", created.getComparatorSpec())
                        .put("maxPoints", created.getMaxPoints())
                        .build())
                .build());
    }

    private String readBody(HttpExchange ex, int maxBytes) throws IOException {
        try (InputStream in = ex.getRequestBody()) {
            byte[] buf = new byte[8192];
            java.io.ByteArrayOutputStream out = new java.io.ByteArrayOutputStream();
            int n;
            while ((n = in.read(buf)) != -1) {
                out.write(buf, 0, n);
                if (out.size() > maxBytes) {
                    throw ApiException.badRequest("Dữ liệu gửi lên quá lớn (> " + (maxBytes / 1024) + " KB)");
                }
            }
            return new String(out.toByteArray(), StandardCharsets.UTF_8);
        }
    }

    // ------------------------------------------------------------ file tinh

    private void handleStatic(HttpExchange ex) throws IOException {
        if (!"GET".equals(ex.getRequestMethod())) {
            sendError(ex, 405, "Chỉ hỗ trợ GET cho file tĩnh");
            return;
        }
        String urlPath = ex.getRequestURI().getPath();
        if (urlPath.endsWith("/")) urlPath += "index.html";

        Path file = safeResolve(urlPath);
        // SPA: duong dan khong co duoi file va khong ton tai -> tra ve index.html
        if (file == null || !Files.isRegularFile(file)) {
            Path index = webRoot.resolve("index.html");
            if (!Files.isRegularFile(index)) {
                sendText(ex, 404, "Chưa build frontend. Chạy: cd frontend && npm install && npm run build");
                return;
            }
            file = index;
        }
        byte[] data = Files.readAllBytes(file);
        ex.getResponseHeaders().set("Content-Type", contentType(file.getFileName().toString()));
        ex.sendResponseHeaders(200, data.length);
        try (OutputStream os = ex.getResponseBody()) {
            os.write(data);
        }
    }

    /** Chong duong dan vuot ra ngoai webRoot (path traversal). */
    private Path safeResolve(String urlPath) {
        String relative = urlPath.startsWith("/") ? urlPath.substring(1) : urlPath;
        if (relative.isEmpty()) relative = "index.html";
        Path resolved = webRoot.resolve(relative).normalize().toAbsolutePath();
        return resolved.startsWith(webRoot.toAbsolutePath().normalize()) ? resolved : null;
    }

    private String contentType(String fileName) {
        String n = fileName.toLowerCase();
        if (n.endsWith(".html")) return "text/html; charset=utf-8";
        if (n.endsWith(".js") || n.endsWith(".mjs")) return "text/javascript; charset=utf-8";
        if (n.endsWith(".css")) return "text/css; charset=utf-8";
        if (n.endsWith(".json")) return "application/json; charset=utf-8";
        if (n.endsWith(".svg")) return "image/svg+xml";
        if (n.endsWith(".png")) return "image/png";
        if (n.endsWith(".jpg") || n.endsWith(".jpeg")) return "image/jpeg";
        if (n.endsWith(".ico")) return "image/x-icon";
        if (n.endsWith(".woff2")) return "font/woff2";
        return "application/octet-stream";
    }

    // ------------------------------------------------------------- tien ich

    private void sendJson(HttpExchange ex, int status, String json) throws IOException {
        byte[] data = json.getBytes(StandardCharsets.UTF_8);
        ex.getResponseHeaders().set("Content-Type", "application/json; charset=utf-8");
        ex.getResponseHeaders().set("Cache-Control", "no-store");
        ex.sendResponseHeaders(status, data.length);
        try (OutputStream os = ex.getResponseBody()) {
            os.write(data);
        }
    }

    private void sendError(HttpExchange ex, int status, String message) throws IOException {
        String text = message == null || message.trim().isEmpty() ? "Yêu cầu không hợp lệ" : message;
        sendJson(ex, status, Json.obj().put("error", text).build());
    }

    private void sendText(HttpExchange ex, int status, String text) throws IOException {
        byte[] data = text.getBytes(StandardCharsets.UTF_8);
        ex.getResponseHeaders().set("Content-Type", "text/plain; charset=utf-8");
        ex.sendResponseHeaders(status, data.length);
        try (OutputStream os = ex.getResponseBody()) {
            os.write(data);
        }
    }
}
