package com.ptit.oj.model;

/**
 * Ket qua cham cua dung mot test.
 *
 * Co HAI thong bao, muc do lo thong tin khac nhau:
 *   message         - cong khai: gui ve thi sinh, luu vao CSDL. Khong bao gio chua dap an.
 *   detailedMessage - kem dap an (voi verdict WA): chi de in ra terminal cua nguoi cham,
 *                     KHONG luu, KHONG gui di. Khi doc lai tu CSDL thi khong co, va roi
 *                     ve message.
 */
public class TestCaseResult {

    private final TestCase testCase;
    private final Verdict verdict;
    private final long runtimeMs;
    private final double earnedPoints;
    private final String message;
    private final String detailedMessage;

    /** Dung khi khong co ban chi tiet rieng (TLE/RE/MLE/AC, hoac doc lai tu CSDL). */
    public TestCaseResult(TestCase testCase, Verdict verdict, long runtimeMs,
                          double earnedPoints, String message) {
        this(testCase, verdict, runtimeMs, earnedPoints, message, null);
    }

    public TestCaseResult(TestCase testCase, Verdict verdict, long runtimeMs,
                          double earnedPoints, String message, String detailedMessage) {
        this.testCase = testCase;
        this.verdict = verdict;
        this.runtimeMs = runtimeMs;
        this.earnedPoints = earnedPoints;
        this.message = message == null ? "" : message;
        this.detailedMessage = detailedMessage == null || detailedMessage.isEmpty()
                ? this.message : detailedMessage;
    }

    public TestCase getTestCase() { return testCase; }
    public Verdict getVerdict() { return verdict; }
    public long getRuntimeMs() { return runtimeMs; }
    public double getEarnedPoints() { return earnedPoints; }

    /** Thong bao cong khai - an toan de gui cho thi sinh va luu tru. */
    public String getMessage() { return message; }

    /** Thong bao day du kem dap an - CHI cho nguoi cham xem tren terminal. */
    public String getDetailedMessage() { return detailedMessage; }

    @Override
    public String toString() {
        return String.format("Test %-9s %-4s %5d ms  %s",
                testCase.getId(), verdict.getCode(), runtimeMs, message);
    }
}
