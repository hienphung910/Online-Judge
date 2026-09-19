package com.ptit.oj.language;

import com.ptit.oj.runner.ExecutionResult;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class JavaLanguage extends Language {

    @Override public String getName() { return "Java"; }
    @Override public String getFileExtension() { return ".java"; }
    @Override public long getStartupOverheadMs() { return 400; }    // JVM khoi dong cham
    @Override public boolean supportsMemoryLimit() { return true; }
    @Override public String getMemoryLimitNote() { return "có, bằng -Xmx"; }

    /** Ten class trong ma nguon, de dat ten file cho khop (yeu cau cua javac). */
    private static final Pattern CLASS_NAME = Pattern.compile(
            "(?m)^\\s*(?:public\\s+)?(?:final\\s+|abstract\\s+)?class\\s+([A-Za-z_$][\\w$]*)");

    @Override
    protected List<String> getVersionCommand() {
        return Arrays.asList("javac", "-version");
    }

    /**
     * Java bat buoc ten file trung ten class public, va lenh chay cung dung
     * ten file lam ten class -> phai doc ten class tu ma nguon.
     * Han che: chi bat class dau tien khai bao o dau dong, du cho bai nop thong thuong.
     */
    @Override
    public String defaultFileName(String sourceCode) {
        if (sourceCode != null) {
            Matcher m = CLASS_NAME.matcher(sourceCode);
            if (m.find()) return m.group(1) + getFileExtension();
        }
        return "Main" + getFileExtension();
    }

    @Override
    public CompileResult compile(Path source, Path workDir) throws IOException, InterruptedException {
        ExecutionResult r = runTool(workDir,
                "javac", "-encoding", "UTF-8", "-d", workDir.toString(), source.toString());
        if (r.isTimedOut()) return CompileResult.fail("Biên dịch quá lâu (> 20s)");
        if (r.getExitCode() != 0) {
            String msg = r.getStderr().isEmpty() ? r.getStdout() : r.getStderr();
            return CompileResult.fail(msg.trim());
        }
        return CompileResult.ok();
    }

    @Override
    public List<String> buildRunCommand(Path source, Path workDir, int memoryLimitMb) {
        return Arrays.asList("java",
                "-Xmx" + memoryLimitMb + "m",
                "-Dfile.encoding=UTF-8",
                "-cp", workDir.toString(),
                baseName(source));
    }
}
