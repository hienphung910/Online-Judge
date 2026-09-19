package com.ptit.oj.language;

import com.ptit.oj.runner.ExecutionResult;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

/**
 * Ngon ngu JavaScript, chay bang Node.js.
 * La ngon ngu thong dich nen "bien dich" chi la kiem tra cu phap (node --check).
 * Day la ngon ngu thong dich duy nhat ep duoc bo nho: --max-old-space-size.
 */
public class JavaScriptLanguage extends Language {

    @Override public String getName() { return "JavaScript"; }
    @Override public String getFileExtension() { return ".js"; }
    @Override public long getStartupOverheadMs() { return 250; }
    @Override public boolean supportsMemoryLimit() { return true; }
    @Override public String getMemoryLimitNote() { return "có, bằng --max-old-space-size"; }

    @Override
    protected List<String> getVersionCommand() {
        return Arrays.asList("node", "--version");
    }

    @Override
    public CompileResult compile(Path source, Path workDir) throws IOException, InterruptedException {
        ExecutionResult r = runTool(workDir, "node", "--check", source.toString());
        if (r.isTimedOut()) return CompileResult.fail("Kiểm tra cú pháp quá lâu");
        if (r.getExitCode() != 0) {
            String msg = r.getStderr().isEmpty() ? r.getStdout() : r.getStderr();
            return CompileResult.fail(msg.trim());
        }
        return CompileResult.ok();
    }

    @Override
    public List<String> buildRunCommand(Path source, Path workDir, int memoryLimitMb) {
        return Arrays.asList("node",
                "--max-old-space-size=" + memoryLimitMb,
                source.toString());
    }
}
