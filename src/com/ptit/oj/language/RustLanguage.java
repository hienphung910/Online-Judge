package com.ptit.oj.language;

import com.ptit.oj.runner.ExecutionResult;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Ngon ngu Rust. Bai nop la mot file duy nhat co "fn main()".
 * Bien dich truc tiep bang rustc (khong dung cargo, vi khong can Cargo.toml).
 */
public class RustLanguage extends Language {

    @Override public String getName() { return "Rust"; }
    @Override public String getFileExtension() { return ".rs"; }

    @Override
    protected List<String> getVersionCommand() {
        return Arrays.asList("rustc", "--version");
    }

    private Path executablePath(Path source, Path workDir) {
        return workDir.resolve(baseName(source) + (isWindows() ? ".exe" : ".bin"));
    }

    @Override
    public CompileResult compile(Path source, Path workDir) throws IOException, InterruptedException {
        Path exe = executablePath(source, workDir);
        // -O bat toi uu, tuong duong -C opt-level=2
        ExecutionResult r = runTool(workDir, "rustc", "-O", "-o", exe.toString(), source.toString());
        if (r.isTimedOut()) return CompileResult.fail("Biên dịch quá lâu (> 20s)");
        if (r.getExitCode() != 0) {
            String msg = r.getStderr().isEmpty() ? r.getStdout() : r.getStderr();
            return CompileResult.fail(msg.trim());
        }
        return CompileResult.ok();
    }

    @Override
    public List<String> buildRunCommand(Path source, Path workDir, int memoryLimitMb) {
        return Collections.singletonList(executablePath(source, workDir).toString());
    }
}
