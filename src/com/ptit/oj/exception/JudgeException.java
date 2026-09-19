package com.ptit.oj.exception;

/** Ngoai le chung cua qua trinh cham bai (checked exception tu dinh nghia). */
public class JudgeException extends Exception {
    private static final long serialVersionUID = 1L;

    public JudgeException(String message) { super(message); }
    public JudgeException(String message, Throwable cause) { super(message, cause); }
}
