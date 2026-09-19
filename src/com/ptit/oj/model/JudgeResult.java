package com.ptit.oj.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/** Tong hop ket qua cham cua mot bai nop. */
public class JudgeResult {

    private final Submission submission;
    private final List<TestCaseResult> testResults = new ArrayList<>();
    private Verdict globalVerdict;      // CE / IE: loi chung, khong chay test nao
    private String globalMessage = "";
    private long judgeTimeMs;

    public JudgeResult(Submission submission) {
        this.submission = submission;
    }

    public void addTestResult(TestCaseResult r) {
        testResults.add(r);
    }

    /** Danh dau loi toan cuc (bien dich loi, thieu compiler...). */
    public void markGlobal(Verdict verdict, String message) {
        this.globalVerdict = verdict;
        this.globalMessage = message == null ? "" : message;
    }

    public List<TestCaseResult> getTestResults() {
        return Collections.unmodifiableList(testResults);
    }

    /** Verdict cuoi cung: uu tien loi toan cuc, roi den loi nang nhat trong cac test. */
    public Verdict getOverallVerdict() {
        if (globalVerdict != null) return globalVerdict;
        if (testResults.isEmpty()) return Verdict.IE;
        Verdict worst = Verdict.AC;
        for (TestCaseResult r : testResults) {
            if (r.getVerdict().getSeverity() > worst.getSeverity()) worst = r.getVerdict();
        }
        return worst;
    }

    public int getPassedCount() {
        int c = 0;
        for (TestCaseResult r : testResults) if (r.getVerdict().isAccepted()) c++;
        return c;
    }

    public int getTotalTests() {
        return submission.getProblem().getTestCases().size();
    }

    public double getScore() {
        double s = 0;
        for (TestCaseResult r : testResults) s += r.getEarnedPoints();
        return s;
    }

    public long getMaxRuntimeMs() {
        long m = 0;
        for (TestCaseResult r : testResults) m = Math.max(m, r.getRuntimeMs());
        return m;
    }

    public Submission getSubmission() { return submission; }
    public String getGlobalMessage() { return globalMessage; }

    /**
     * Gan lai thong bao chung khi dung lai ket qua tu CSDL, ma khong dat
     * globalVerdict (vi verdict cua ban ghi cu van suy ra duoc tu danh sach test).
     */
    public void setGlobalMessage(String globalMessage) {
        this.globalMessage = globalMessage == null ? "" : globalMessage;
    }

    public long getJudgeTimeMs() { return judgeTimeMs; }
    public void setJudgeTimeMs(long judgeTimeMs) { this.judgeTimeMs = judgeTimeMs; }

    @Override
    public String toString() {
        return String.format("%s  %d/%d test  %.1f/%.1f điểm  test lâu nhất %d ms",
                getOverallVerdict().getCode(), getPassedCount(), getTotalTests(),
                getScore(), submission.getProblem().getMaxPoints(), getMaxRuntimeMs());
    }
}
