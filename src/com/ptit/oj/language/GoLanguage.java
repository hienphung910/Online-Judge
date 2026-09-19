package com.ptit.oj.language;

import com.ptit.oj.runner.ExecutionResult;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Ngon ngu Go. Bai nop phai la mot file duy nhat co "package main" va "func main()".
 * Bien dich: go build -o <exe> <source>  (khong can go.mod cho file don le).
 */
public class GoLanguage extends Language {

    @Override public String getName() { return "Go"; }
    @Override public String getFileExtension() { return ".go"; }

    @Override
    protected List<String> getVersionCommand() {
        return Arrays.asList("go", "version");
    }

    private Path executablePath(Path source, Path workDir) {
        return workDir.resolve(baseName(source) + (isWindows() ? ".exe" : ".bin"));
    }

    @Override
    public CompileResult compile(Path source, Path workDir) throws IOException, InterruptedException {
        Path exe = executablePath(source, workDir);
        ExecutionResult r = runTool(workDir, "go", "build", "-o", exe.toString(), source.toString());
        if (r.isTimedOut()) return CompileResult.fail("Biên dịch quá lâu (> 20s)");
        if (r.getExitCode() != 0) {
            String msg = r.getStderr().isEmpty() ? r.getStdout() : r.getStderr();
            return CompileResult.fail(msg.trim());
        }
        return CompileResult.ok();
    }

    @Override
    public List<String> buildRunCommand(Path source, Path workDir, int memoryLimitMb) {
        // Go khong co tham so gioi han heap kieu -Xmx -> chi phat hien MLE qua thong bao runtime.
        return Collections.singletonList(executablePath(source, workDir).toString());
    }
}
