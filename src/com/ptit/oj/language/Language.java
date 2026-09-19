package com.ptit.oj.language;

import com.ptit.oj.runner.ExecutionResult;
import com.ptit.oj.runner.ProcessRunner;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;

/**
 * Lop truu tuong cho mot ngon ngu lap trinh duoc ho tro.
 * Day la khung chung (template): lop con chi khai bao lenh bien dich / lenh chay.
 */
public abstract class Language {

    protected static final long COMPILE_TIME_LIMIT_MS = 20_000;
    protected final ProcessRunner runner = new ProcessRunner();

    private Boolean availableCache;

    public abstract String getName();

    /** Duoi file tuong ung, vi du ".java". */
    public abstract String getFileExtension();

    /** Lenh kiem tra toolchain co san khong, vi du javac -version. */
    protected abstract List<String> getVersionCommand();

    /** Bien dich ma nguon trong workDir. Ngon ngu thong dich chi can tra ve ok(). */
    public abstract CompileResult compile(Path source, Path workDir) throws IOException, InterruptedException;

    /** Lenh chay chuong trinh cua thi sinh. */
    public abstract List<String> buildRunCommand(Path source, Path workDir, int memoryLimitMb);

    /** Thoi gian cong them cho ngon ngu khoi dong cham (JVM, Python interpreter...). */
    public long getStartupOverheadMs() { return 0; }

    /** Ngon ngu nay co gioi han bo nho thuc su khong (de bao cao trung thuc). */
    public boolean supportsMemoryLimit() { return false; }

    /**
     * Mo ta cach gioi han bo nho cua rieng ngon ngu nay.
     * Lop con nao ep duoc bo nho thi ghi de de bao cao dung ten tham so.
     */
    public String getMemoryLimitNote() {
        return "không (chỉ phát hiện qua lỗi runtime)";
    }

    /** Kiem tra compiler/interpreter co ton tai tren may khong (ket qua duoc cache). */
    public boolean isAvailable() {
        if (availableCache == null) {
            availableCache = probe();
        }
        return availableCache;
    }

    private boolean probe() {
        try {
            ExecutionResult r = runner.run(getVersionCommand(), currentDir(), "", 10_000);
            return !r.isTimedOut();
        } catch (IOException | InterruptedException e) {
            return false;
        }
    }

    protected static Path currentDir() {
        return Paths.get(System.getProperty("user.dir"));
    }

    /** Tien ich: chay mot lenh cua toolchain (compiler) va gom stdout + stderr. */
    protected ExecutionResult runTool(Path workDir, String... command) throws IOException, InterruptedException {
        return runner.run(Arrays.asList(command), workDir, "", COMPILE_TIME_LIMIT_MS);
    }

    /**
     * Ten file nen dat khi thi sinh dan code truc tiep tren web (khong upload file).
     * Mac dinh la "solution" + duoi file; Java phai ghi de vi ten file
     * bat buoc trung ten class.
     */
    public String defaultFileName(String sourceCode) {
        return "solution" + getFileExtension();
    }

    /** Ten file khong co duoi, dung lam ten class / ten file thuc thi. */
    protected static String baseName(Path source) {
        String name = source.getFileName().toString();
        int dot = name.lastIndexOf('.');
        return dot < 0 ? name : name.substring(0, dot);
    }

    protected static boolean isWindows() {
        return System.getProperty("os.name").toLowerCase().contains("win");
    }

    @Override
    public String toString() { return getName(); }
}
