package com.ptit.oj.core;

import com.ptit.oj.compare.ComparatorFactory;
import com.ptit.oj.compare.OutputComparator;
import com.ptit.oj.exception.CompileErrorException;
import com.ptit.oj.exception.JudgeException;
import com.ptit.oj.language.CompileResult;
import com.ptit.oj.language.Language;
import com.ptit.oj.model.JudgeResult;
import com.ptit.oj.model.Problem;
import com.ptit.oj.model.Submission;
import com.ptit.oj.model.TestCase;
import com.ptit.oj.model.TestCaseResult;
import com.ptit.oj.model.Verdict;
import com.ptit.oj.runner.ExecutionResult;
import com.ptit.oj.runner.ProcessRunner;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.Comparator;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.stream.Stream;

/**
 * Bo cham bai - lop trung tam cua he thong.
 *
 * Quy trinh: tao thu muc lam viec -> bien dich -> chay lan luot tung test
 * -> so sanh output bang Strategy -> tong hop verdict -> don dep.
 *
 * Judge KHONG biet ngon ngu nao dang duoc dung (Language) cung khong biet
 * cach so sanh nao dang ap dung (OutputComparator) => phu thuoc vao truu tuong,
 * khong phu thuoc vao lop cu the (Dependency Inversion).
 */
public class Judge {

    private final ProcessRunner runner = new ProcessRunner();
    /**
     * CopyOnWriteArrayList chu khong phai ArrayList: listener cua web (SseJudgeListener)
     * duoc gan va go theo tung request, nen danh sach nay co the bi sua trong khi mot
     * vong lap thong bao dang chay. Ban copy-on-write cho phep duyet an toan ma khong
     * phai khoa gi them.
     */
    private final List<JudgeListener> listeners = new CopyOnWriteArrayList<>();

    /** True: dung ngay khi gap test sai (giong ICPC). False: cham het de tinh diem tung phan. */
    private boolean stopOnFirstFailure = false;

    public void addListener(JudgeListener listener) {
        listeners.add(listener);
    }

    /**
     * Go mot observer ra.
     *
     * Can cho nhung listener song ngan hon Judge: SseJudgeListener chi ton tai trong
     * mot request nop bai, gan truoc khi cham va go trong finally. Khong go thi danh
     * sach phinh them sau moi lan nop, va lan cham sau se co gang ghi vao ket noi da dong.
     */
    public void removeListener(JudgeListener listener) {
        listeners.remove(listener);
    }

    public void setStopOnFirstFailure(boolean stopOnFirstFailure) {
        this.stopOnFirstFailure = stopOnFirstFailure;
    }

    public JudgeResult judge(Submission submission) {
        Problem problem = submission.getProblem();
        Language language = submission.getLanguage();
        JudgeResult result = new JudgeResult(submission);
        long startedAt = System.currentTimeMillis();

        for (JudgeListener l : listeners) l.onJudgeStarted(submission);

        Path workDir = null;
        try {
            if (!Files.isRegularFile(submission.getSourcePath())) {
                throw new JudgeException("Không tìm thấy file mã nguồn: " + submission.getSourcePath());
            }
            if (!language.isAvailable()) {
                throw new JudgeException("Máy này chưa cài toolchain cho " + language.getName());
            }
            if (problem.getTestCases().isEmpty()) {
                throw new JudgeException("Bài " + problem.getId() + " chưa có test nào");
            }

            workDir = Files.createTempDirectory("oj-judge-");
            Path source = workDir.resolve(submission.getSourcePath().getFileName());
            Files.copy(submission.getSourcePath(), source, StandardCopyOption.REPLACE_EXISTING);

            CompileResult compile = language.compile(source, workDir);
            for (JudgeListener l : listeners) {
                l.onCompiled(submission, compile.isSuccess(), compile.getMessage());
            }
            if (!compile.isSuccess()) {
                throw new CompileErrorException(compile.getMessage());
            }

            OutputComparator comparator = ComparatorFactory.create(problem.getComparatorSpec());
            List<TestCase> tests = problem.getTestCases();

            for (int i = 0; i < tests.size(); i++) {
                TestCaseResult tcResult = runSingleTest(
                        problem, language, source, workDir, tests.get(i), comparator);
                result.addTestResult(tcResult);
                for (JudgeListener l : listeners) {
                    l.onTestCaseFinished(submission, i + 1, tests.size(), tcResult);
                }
                if (stopOnFirstFailure && !tcResult.getVerdict().isAccepted()) {
                    break;
                }
            }

        } catch (CompileErrorException e) {
            result.markGlobal(Verdict.CE, e.getMessage());
        } catch (JudgeException e) {
            result.markGlobal(Verdict.IE, e.getMessage());
        } catch (IOException e) {
            result.markGlobal(Verdict.IE, "Lỗi vào/ra khi chấm: " + e.getMessage());
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();   // ton trong co ngat cua thread
            result.markGlobal(Verdict.IE, "Quá trình chấm bị ngắt");
        } finally {
            deleteRecursively(workDir);
            result.setJudgeTimeMs(System.currentTimeMillis() - startedAt);
            submission.setResult(result);
            for (JudgeListener l : listeners) l.onJudgeFinished(submission, result);
        }
        return result;
    }

    /** Chay dung mot test va quy ra verdict. */
    private TestCaseResult runSingleTest(Problem problem, Language language, Path source,
                                         Path workDir, TestCase test, OutputComparator comparator)
            throws IOException, InterruptedException {

        List<String> command = language.buildRunCommand(source, workDir, problem.getMemoryLimitMb());
        long limit = problem.getTimeLimitMs() + language.getStartupOverheadMs();

        ExecutionResult exec = runner.run(command, workDir, test.getInput(), limit);

        if (exec.isTimedOut()) {
            return new TestCaseResult(test, Verdict.TLE, exec.getElapsedMs(), 0,
                    "Chạy quá " + problem.getTimeLimitMs() + " ms");
        }
        if (looksLikeOutOfMemory(exec.getStderr())) {
            return new TestCaseResult(test, Verdict.MLE, exec.getElapsedMs(), 0,
                    "Vượt giới hạn " + problem.getMemoryLimitMb() + " MB");
        }
        if (exec.getExitCode() != 0) {
            return new TestCaseResult(test, Verdict.RE, exec.getElapsedMs(), 0,
                    "Exit code " + exec.getExitCode() + ": " + firstLine(exec.getStderr()));
        }
        if (comparator.matches(test.getExpectedOutput(), exec.getStdout())) {
            return new TestCaseResult(test, Verdict.AC, exec.getElapsedMs(), test.getPoints(), "");
        }
        // Hai ban giai thich: cong khai (gui thi sinh, luu CSDL - khong co dap an)
        // va chi tiet (chi in terminal nguoi cham). Xem OutputComparator.
        return new TestCaseResult(test, Verdict.WA, exec.getElapsedMs(), 0,
                comparator.explain(test.getExpectedOutput(), exec.getStdout()),
                comparator.explainDetailed(test.getExpectedOutput(), exec.getStdout()));
    }

    /**
     * Nhan biet loi tran bo nho qua thong bao cua runtime.
     * Han che: day la cach xap xi. Muon do bo nho chinh xac phai dung
     * cgroups (Linux) hoac Job Object (Windows) - vuot pham vi bai tap lon.
     */
    private boolean looksLikeOutOfMemory(String stderr) {
        if (stderr == null || stderr.isEmpty()) return false;
        String s = stderr.toLowerCase();
        return s.contains("outofmemoryerror")            // Java
                || s.contains("bad_alloc")               // C++
                || s.contains("memoryerror")             // Python
                || s.contains("heap out of memory")      // JavaScript (Node)
                || s.contains("out of memory")           // Go: runtime: out of memory
                || s.contains("memory allocation of")    // Rust: memory allocation of N bytes failed
                || s.contains("cannot allocate memory");
    }

    private String firstLine(String text) {
        if (text == null || text.isEmpty()) return "(không có thông báo)";
        String[] lines = text.split("\r?\n");
        for (String line : lines) {
            if (!line.trim().isEmpty()) return line.trim();
        }
        return "(không có thông báo)";
    }

    /** Xoa thu muc lam viec tam (bao gom file .class / .exe da sinh ra). */
    private void deleteRecursively(Path dir) {
        if (dir == null || !Files.exists(dir)) return;
        try (Stream<Path> walk = Files.walk(dir)) {
            walk.sorted(Comparator.reverseOrder()).forEach(p -> {
                try {
                    Files.deleteIfExists(p);
                } catch (IOException ignored) {
                    // file .exe co the con bi khoa tren Windows -> bo qua
                }
            });
        } catch (IOException ignored) {
            // khong xoa duoc thi de OS don dep thu muc temp
        }
    }
}
