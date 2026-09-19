package com.ptit.oj.runner;

/** Ket qua thuc thi mot tien trinh con: ma thoat, stdout, stderr, thoi gian. */
public class ExecutionResult {

    private final int exitCode;
    private final String stdout;
    private final String stderr;
    private final long elapsedMs;
    private final boolean timedOut;

    public ExecutionResult(int exitCode, String stdout, String stderr, long elapsedMs, boolean timedOut) {
        this.exitCode = exitCode;
        this.stdout = stdout;
        this.stderr = stderr;
        this.elapsedMs = elapsedMs;
        this.timedOut = timedOut;
    }

    public int getExitCode() { return exitCode; }
    public String getStdout() { return stdout; }
    public String getStderr() { return stderr; }
    public long getElapsedMs() { return elapsedMs; }
    public boolean isTimedOut() { return timedOut; }
    public boolean isSuccess() { return !timedOut && exitCode == 0; }
}
