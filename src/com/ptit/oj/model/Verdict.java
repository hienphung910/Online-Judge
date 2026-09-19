package com.ptit.oj.model;

/** Ket qua cham cua mot test / mot bai nop. */
public enum Verdict {
    AC("AC", "Accepted", 0),
    PE("PE", "Presentation Error", 1),
    WA("WA", "Wrong Answer", 2),
    TLE("TLE", "Time Limit Exceeded", 3),
    MLE("MLE", "Memory Limit Exceeded", 4),
    RE("RE", "Runtime Error", 5),
    CE("CE", "Compile Error", 6),
    IE("IE", "Internal Error", 7);

    private final String code;
    private final String display;
    private final int severity;

    Verdict(String code, String display, int severity) {
        this.code = code;
        this.display = display;
        this.severity = severity;
    }

    public String getCode() { return code; }
    public String getDisplay() { return display; }
    public int getSeverity() { return severity; }

    public boolean isAccepted() { return this == AC; }
}
