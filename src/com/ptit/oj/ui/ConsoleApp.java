package com.ptit.oj.ui;

import com.ptit.oj.core.ConsoleJudgeListener;
import com.ptit.oj.language.Language;
import com.ptit.oj.model.JudgeResult;
import com.ptit.oj.model.Problem;
import com.ptit.oj.model.Submission;
import com.ptit.oj.model.TestCase;
import com.ptit.oj.model.TestCaseResult;
import com.ptit.oj.model.User;
import com.ptit.oj.service.AuthService;
import com.ptit.oj.service.JudgeService;
import com.ptit.oj.service.ScoreboardService;
import com.ptit.oj.util.TextUtils;

import java.io.Console;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;
import java.util.Scanner;

/**
 * Tang giao dien console: chi lo doc/ghi man hinh, moi xu ly nghiep vu
 * deu goi xuong JudgeService.
 *
 * Che do tuong tac BAT BUOC dang nhap bang mat khau. Che do --demo / --selftest
 * chay tren kho du lieu trong bo nho voi tai khoan mau nen khong can dang nhap,
 * khong can MySQL va cung khong dong toi CSDL that.
 */
public class ConsoleApp {

    private final JudgeService service;
    private final Scanner scanner = new Scanner(System.in);
    private User currentUser;

    /** Nhan JudgeService tu ben ngoai de Main quyet dinh dung MySQL hay bo nho. */
    public ConsoleApp(JudgeService service) {
        this.service = service;
        this.service.addJudgeListener(new ConsoleJudgeListener(true));
    }

    public void loadData() {
        service.loadData();
        System.out.printf("Đã nạp %d bài tập, %d tài khoản.%n",
                service.getProblems().size(), service.getUsers().size());
    }

    /** Dat san nguoi dung cho che do tu dong (--demo / --selftest). */
    public void useAccount(User user) {
        this.currentUser = user;
    }

    // ------------------------------------------------------------------ menu

    public void runInteractive() {
        printBanner();
        if (!authenticate()) {
            System.out.println("Chưa đăng nhập được, kết thúc chương trình.");
            return;
        }
        boolean running = true;
        while (running) {
            printMenu();
            String choice = ask("Chọn");
            if (choice == null) {          // het du lieu tren stdin -> thoat, khong lap vo han
                System.out.println("(Không còn dữ liệu nhập, kết thúc chương trình)");
                break;
            }
            System.out.println();
            switch (choice.trim()) {
                case "1": listProblems(); break;
                case "2": showProblemDetail(); break;
                case "3": submitFromInput(); break;
                case "4": listMySubmissions(); break;
                case "5": printScoreboard(); break;
                case "6": System.out.println(service.getStatistics().report()); break;
                case "7": checkEnvironment(); break;
                case "8": running = !switchAccount(); break;
                case "0": running = false; break;
                default: System.out.println("Lựa chọn không hợp lệ, mời chọn lại."); break;
            }
        }
        System.out.println("Kết thúc. Cảm ơn!");
    }

    private void printBanner() {
        System.out.println("==================================================");
        System.out.println("   PTIT ONLINE JUDGE - Trình chấm bài tự động");
        System.out.println("   Bài tập lớn môn Lập trình hướng đối tượng");
        System.out.println("==================================================");
    }

    private void printMenu() {
        System.out.println();
        System.out.println("--- Đang đăng nhập: " + currentUser.describe()
                + " | đã giải " + service.getSolvedCount(currentUser) + " bài ---");
        System.out.println("1. Danh sách bài tập");
        System.out.println("2. Xem chi tiết một bài");
        System.out.println("3. Nộp bài từ file mã nguồn");
        System.out.println("4. Lịch sử nộp bài");
        System.out.println("5. Bảng xếp hạng");
        System.out.println("6. Thống kê verdict");
        System.out.println("7. Kiểm tra môi trường biên dịch");
        System.out.println("8. Đăng xuất / đổi tài khoản");
        System.out.println("0. Thoát");
    }

    // -------------------------------------------------------------- dang nhap

    /** Man hinh dang nhap / dang ky. Tra ve true neu da co nguoi dung hop le. */
    private boolean authenticate() {
        while (true) {
            System.out.println();
            System.out.println("1. Đăng nhập");
            System.out.println("2. Đăng ký tài khoản học sinh");
            System.out.println("0. Thoát");
            String choice = ask("Chọn");
            if (choice == null) return false;
            switch (choice.trim()) {
                case "1":
                    if (doLogin()) return true;
                    break;
                case "2":
                    doRegister();
                    break;
                case "0":
                    return false;
                default:
                    System.out.println("Lựa chọn không hợp lệ.");
            }
        }
    }

    private boolean doLogin() {
        String username = ask("Tên đăng nhập");
        if (username == null) return false;
        String password = askPassword("Mật khẩu");
        if (password == null) return false;
        try {
            AuthService.LoginResult result = service.getAuth().login(username, password);
            currentUser = result.getUser();
            System.out.println("Xin chào " + currentUser.describe());
            return true;
        } catch (AuthService.AuthException e) {
            System.out.println("Đăng nhập thất bại: " + e.getMessage());
            return false;
        }
    }

    private void doRegister() {
        String username = ask("Tên đăng nhập (3-32 ký tự, chữ/số/._)");
        if (username == null) return;
        String fullName = ask("Họ tên");
        if (fullName == null) return;
        String studentCode = ask("Mã sinh viên");
        if (studentCode == null) return;
        String className = ask("Lớp");
        if (className == null) return;
        String password = askPassword("Mật khẩu (ít nhất 8 ký tự)");
        if (password == null) return;
        String confirm = askPassword("Nhập lại mật khẩu");
        if (confirm == null) return;
        if (!password.equals(confirm)) {
            System.out.println("Hai lần nhập mật khẩu không khớp.");
            return;
        }
        try {
            User created = service.getAuth().register(username, password, fullName, studentCode, className);
            System.out.println("Đã tạo tài khoản " + created.describe() + ". Mời đăng nhập.");
        } catch (AuthService.AuthException | IllegalArgumentException e) {
            System.out.println("Đăng ký thất bại: " + e.getMessage());
        }
    }

    /** Tra ve true neu nguoi dung chon thoat han thay vi dang nhap lai. */
    private boolean switchAccount() {
        currentUser = null;
        System.out.println("Đã đăng xuất.");
        return !authenticate();
    }

    // ------------------------------------------------------------- chuc nang

    private void listProblems() {
        System.out.println("DANH SÁCH BÀI TẬP");
        for (Problem p : service.getProblems()) {
            System.out.println("  " + p.describe() + "  [so sánh: " + p.getComparatorSpec() + "]");
        }
    }

    private void showProblemDetail() {
        String id = ask("Mã bài (ví dụ P001)");
        if (id == null) return;
        Optional<Problem> found = service.findProblem(id);
        if (!found.isPresent()) {
            System.out.println("Không tìm thấy bài này.");
            return;
        }
        Problem p = found.get();
        System.out.println("=== " + p.getId() + " - " + p.getTitle() + " ===");
        if (!p.getStatement().isEmpty()) System.out.println(p.getStatement());
        System.out.printf("Giới hạn: %d ms, %d MB. Tổng điểm: %.0f%n",
                p.getTimeLimitMs(), p.getMemoryLimitMb(), p.getMaxPoints());
        System.out.println("Test ví dụ:");
        for (TestCase tc : p.getTestCases()) {
            if (!tc.isSample()) continue;
            System.out.println("  Input : " + tc.getInput().trim().replace("\n", " | "));
            System.out.println("  Output: " + tc.getExpectedOutput().trim().replace("\n", " | "));
        }
    }

    private void submitFromInput() {
        String id = ask("Mã bài");
        if (id == null) return;
        Optional<Problem> found = service.findProblem(id);
        if (!found.isPresent()) {
            System.out.println("Không tìm thấy bài này.");
            return;
        }
        String raw = ask("Đường dẫn file mã nguồn (.java/.cpp/.py/.go/.js/.rs)");
        if (raw == null) return;
        Path source = Paths.get(raw.trim().replace("\"", ""));
        if (!Files.isRegularFile(source)) {
            System.out.println("Không tìm thấy file: " + source.toAbsolutePath());
            return;
        }
        submitAndJudge(found.get(), currentUser, source);
    }

    /** Nop + cham mot bai, kem cac kiem tra dau vao. Tra ve null neu khong cham duoc. */
    private JudgeResult submitAndJudge(Problem problem, User author, Path source) {
        Optional<Language> language = service.detectLanguage(source);
        if (!language.isPresent()) {
            System.out.println("Không hỗ trợ đuôi file của " + source.getFileName());
            return null;
        }
        return service.submitFile(problem, author, source, language.get());
    }

    // -------------------------------------------------------------- bo demo

    /**
     * Cham lan luot cac bai nop trong data/submissions/demo-plan.txt.
     * @param checkExpectations true -> doi chieu verdict thuc te voi verdict ky vong
     * @return so truong hop lech ky vong (0 = tat ca dung nhu du kien)
     */
    public int runDemoPlan(boolean checkExpectations) {
        List<String> badLines = new ArrayList<>();
        List<JudgeService.DemoEntry> entries;
        try {
            entries = service.readDemoPlan(badLines);
        } catch (IOException e) {
            System.out.println("Lỗi đọc demo-plan.txt: " + e.getMessage());
            return 1;
        }
        for (String bad : badLines) {
            System.out.println("Bỏ qua dòng sai cú pháp: " + bad);
        }

        int judged = 0, skipped = 0, mismatch = 0;
        List<String> report = new ArrayList<>();

        for (JudgeService.DemoEntry e : entries) {
            Optional<Problem> problem = service.findProblem(e.getProblemId());
            Optional<User> author = service.findUser(e.getUsername());
            String skipReason = checkEntry(e, problem, author);

            if (skipReason != null) {
                skipped++;
                System.out.println();
                System.out.println(">>> BỎ QUA " + e.getSource().getFileName() + " (" + skipReason + ")");
                report.add(String.format("  %-18s %-6s %s", e.getSource().getFileName(), "SKIP", skipReason));
                continue;
            }

            JudgeResult result = submitAndJudge(problem.get(), author.get(), e.getSource());
            judged++;
            if (checkExpectations) {
                String actual = result == null ? "?" : result.getOverallVerdict().getCode();
                boolean ok = e.getExpectedVerdict() == null || e.getExpectedVerdict().equals(actual);
                if (!ok) mismatch++;
                report.add(String.format("  %-18s %-6s %s",
                        e.getSource().getFileName(),
                        ok ? "ĐÚNG" : "LỆCH",
                        e.getExpectedVerdict() == null
                                ? "không khai báo kỳ vọng (thực tế " + actual + ")"
                                : "kỳ vọng " + e.getExpectedVerdict() + ", thực tế " + actual));
            }
        }

        System.out.printf("%nĐã chấm %d bài nộp mẫu", judged);
        System.out.println(skipped > 0 ? ", bỏ qua " + skipped + " bài." : ".");
        System.out.println(service.getStatistics().report());

        if (checkExpectations) {
            System.out.println();
            System.out.println("TỰ KIỂM TRA KẾT QUẢ CHẤM");
            for (String line : report) System.out.println(line);
            System.out.println(mismatch == 0
                    ? "=> Tất cả verdict đúng như kỳ vọng."
                    : "=> Có " + mismatch + " trường hợp lệch kỳ vọng!");
        }
        return mismatch;
    }

    /** Tra ve ly do phai bo qua dong demo, hoac null neu cham duoc. */
    private String checkEntry(JudgeService.DemoEntry e, Optional<Problem> problem, Optional<User> author) {
        if (!problem.isPresent()) return "không có bài " + e.getProblemId();
        if (!author.isPresent()) return "không có người dùng " + e.getUsername();
        if (!Files.isRegularFile(e.getSource())) return "thiếu file " + e.getSource().getFileName();

        Optional<Language> lang = service.detectLanguage(e.getSource());
        if (!lang.isPresent()) return "không hỗ trợ đuôi file";
        // May demo co the chi cai JDK -> bo qua chu khong bao loi he thong
        if (!lang.get().isAvailable()) return "máy chưa cài " + lang.get().getName();
        return null;
    }

    /** Lich su nop bai: hoc sinh chi thay bai cua chinh minh, quan tri thay tat ca. */
    private void listMySubmissions() {
        boolean seesAll = User.ROLE_ADMIN.equals(currentUser.getRoleCode())
                || User.ROLE_TEACHER.equals(currentUser.getRoleCode());
        List<Submission> all = seesAll ? service.getSubmissionsNewestFirst()
                                       : service.getSubmissionsOf(currentUser);
        System.out.println(seesAll ? "LỊCH SỬ NỘP BÀI (toàn hệ thống)" : "LỊCH SỬ NỘP BÀI CỦA BẠN");
        if (all.isEmpty()) {
            System.out.println("  (chưa có bài nộp nào - hãy dùng chức năng 3 trước)");
            return;
        }
        for (Submission s : all) {
            System.out.println("  " + s.describe());
        }
        String id = ask("Xem chi tiết mã nộp nào (Enter để bỏ qua)");
        if (id == null || id.trim().isEmpty()) return;
        Optional<Submission> found = service.findSubmission(id);
        if (!found.isPresent()) {
            System.out.println("Không có mã nộp này.");
            return;
        }
        // Chan doan ma nop de xem bai cua nguoi khac, giong het API web.
        if (!seesAll && !found.get().getAuthor().getId().equals(currentUser.getId())) {
            System.out.println("Bạn chỉ được xem bài nộp của chính mình.");
            return;
        }
        printSubmissionDetail(found.get());
    }

    private void printSubmissionDetail(Submission s) {
        JudgeResult r = s.getResult();
        if (r == null) {
            System.out.println("Bài nộp này chưa được chấm.");
            return;
        }
        System.out.println("=== Chi tiết " + s.getId() + " ===");
        System.out.println("Bài " + s.getProblem().getId() + " - " + s.getProblem().getTitle()
                + " | " + s.getLanguage().getName() + " | " + s.getSourcePath().getFileName());
        System.out.println(r.toString());
        if (!r.getGlobalMessage().isEmpty()) {
            System.out.println("Thông báo: " + r.getGlobalMessage());
        }
        for (TestCaseResult tr : r.getTestResults()) {
            System.out.println("  " + tr);
        }
    }

    private void printScoreboard() {
        List<ScoreboardService.Row> rows = service.buildScoreboard();
        System.out.println("BẢNG XẾP HẠNG");
        if (rows.isEmpty()) {
            System.out.println("  (chưa có dữ liệu - hãy nộp một bài trước)");
            return;
        }
        System.out.printf("%-5s %-12s %-22s %8s %6s %8s%n",
                "Hạng", "Username", "Họ tên", "Điểm", "AC", "Số lần");
        int rank = 1;
        for (ScoreboardService.Row row : rows) {
            System.out.printf("%-5d %-12s %-22s %8.1f %6d %8d%n",
                    rank++, row.getUser().getUsername(), row.getUser().getFullName(),
                    row.getTotal(), row.getSolved(), row.getAttempts());
        }
    }

    private void checkEnvironment() {
        System.out.println("MÔI TRƯỜNG BIÊN DỊCH");
        for (Language l : service.getLanguages()) {
            System.out.printf("  %-11s %-6s %-10s | giới hạn bộ nhớ: %s%n",
                    l.getName(), l.getFileExtension(),
                    l.isAvailable() ? "CÓ SẴN" : "KHÔNG CÓ",
                    l.getMemoryLimitNote());
        }
    }

    /** Doc mot dong tu ban phim. Tra ve null khi stdin da het (tranh vong lap vo han). */
    private String ask(String prompt) {
        System.out.print(prompt + ": ");
        System.out.flush();
        try {
            // stripBom: file input tao bang Notepad co BOM se lam lenh dau tien bi sai
            return scanner.hasNextLine() ? TextUtils.stripBom(scanner.nextLine()) : null;
        } catch (NoSuchElementException | IllegalStateException e) {
            return null;
        }
    }

    /**
     * Doc mat khau. Dung System.console() de KHONG hien ky tu tren man hinh;
     * khi chay trong IDE (console null) thi danh doc thuong va bao truoc cho nguoi dung.
     */
    private String askPassword(String prompt) {
        Console console = System.console();
        if (console != null) {
            char[] chars = console.readPassword("%s: ", prompt);
            if (chars == null) return null;
            String value = new String(chars);
            java.util.Arrays.fill(chars, '\0');
            return value;
        }
        System.out.println("(Terminal này không ẩn được ký tự - mật khẩu sẽ hiện khi gõ)");
        return ask(prompt);
    }

    // ---------------------------------------------------- che do chay tu dong

    /** Che do --demo: khong can nhap tay, dung de chay thu / quay video bao cao. */
    public void runDemoMode() {
        printBanner();
        checkEnvironment();
        System.out.println();
        listProblems();
        runDemoPlan(false);
        System.out.println();
        printScoreboard();
    }

    /** Che do --selftest: chay demo va doi chieu voi verdict ky vong. Tra ve so ca lech. */
    public int runSelfTest() {
        printBanner();
        checkEnvironment();
        System.out.println();
        return runDemoPlan(true);
    }

    /** Cho che do --serve dung lai dung mot bo du lieu voi console. */
    public JudgeService getService() {
        return service;
    }
}
