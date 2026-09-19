package com.ptit.oj.language;

import com.ptit.oj.runner.ExecutionResult;

import java.io.IOException;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

public class PythonLanguage extends Language {

    private String interpreter;   // "python" hoac "python3" tuy may

    @Override public String getName() { return "Python"; }
    @Override public String getFileExtension() { return ".py"; }
    @Override public long getStartupOverheadMs() { return 300; }

    private String getInterpreter() {
        if (interpreter == null) {
            interpreter = isWindows() ? "python" : "python3";
        }
        return interpreter;
    }

    @Override
    protected List<String> getVersionCommand() {
        return Arrays.asList(getInterpreter(), "--version");
    }

    /** Thu ca hai ten interpreter truoc khi ket luan may khong co Python. */
    @Override
    public boolean isAvailable() {
        if (super.isAvailable()) return true;
        interpreter = isWindows() ? "python3" : "python";
        try {
            ExecutionResult r = runner.run(getVersionCommand(), currentDir(), "", 10_000);
            return r.isSuccess();
        } catch (IOException | InterruptedException e) {
            return false;
        }
    }

    /** Python la ngon ngu thong dich: chi kiem tra loi cu phap thay vi bien dich. */
    @Override
    public CompileResult compile(Path source, Path workDir) throws IOException, InterruptedException {
        ExecutionResult r = runTool(workDir, getInterpreter(), "-m", "py_compile", source.toString());
        if (r.isTimedOut()) return CompileResult.fail("Kiểm tra cú pháp quá lâu");
        if (r.getExitCode() != 0) {
            String msg = r.getStderr().isEmpty() ? r.getStdout() : r.getStderr();
            return CompileResult.fail(msg.trim());
        }
        return CompileResult.ok();
    }

    @Override
    public List<String> buildRunCommand(Path source, Path workDir, int memoryLimitMb) {
        return Arrays.asList(getInterpreter(), source.toString());
    }
}
