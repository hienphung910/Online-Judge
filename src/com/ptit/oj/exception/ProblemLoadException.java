package com.ptit.oj.exception;

/** Nem ra khi doc de bai / bo test tu o dia bi loi. */
public class ProblemLoadException extends RuntimeException {
    private static final long serialVersionUID = 1L;

    public ProblemLoadException(String message, Throwable cause) { super(message, cause); }
    public ProblemLoadException(String message) { super(message); }
}
