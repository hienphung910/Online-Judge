package com.ptit.oj.language;

import com.ptit.oj.runner.ExecutionResult;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class CppLanguage extends Language {

    @Override public String getName() { return "C++"; }
    @Override public String getFileExtension() { return ".cpp"; }

    @Override
    protected List<String> getVersionCommand() {
        return Arrays.asList("g++", "--version");
    }

    private Path executablePath(Path source, Path workDir) {
        return workDir.resolve(baseName(source) + (isWindows() ? ".exe" : ".bin"));
    }

    @Override
    public CompileResult compile(Path source, Path workDir) throws IOException, InterruptedException {
        Path exe = executablePath(source, workDir);
        ExecutionResult r = runTool(workDir,
                "g++", "-O2", "-std=c++17", "-o", exe.toString(), source.toString());
        if (r.isTimedOut()) return CompileResult.fail("Biên dịch quá lâu (> 20s)");
        if (r.getExitCode() != 0) {
            String msg = r.getStderr().isEmpty() ? r.getStdout() : r.getStderr();
            return CompileResult.fail(msg.trim());
        }
        return CompileResult.ok();
    }

    @Override
    public List<String> buildRunCommand(Path source, Path workDir, int memoryLimitMb) {
        // Khong ep duoc bo nho o muc tien trinh -> chi phat hien MLE qua std::bad_alloc.
        return Collections.singletonList(executablePath(source, workDir).toString());
    }
}
