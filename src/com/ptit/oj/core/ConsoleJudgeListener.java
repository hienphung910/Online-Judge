package com.ptit.oj.core;

import com.ptit.oj.model.JudgeResult;
import com.ptit.oj.model.Submission;
import com.ptit.oj.model.TestCaseResult;
import com.ptit.oj.model.Verdict;

/**
 * Observer cu the: in tien trinh cham ra man hinh.
 *
 * Day la terminal cua NGUOI CHAM nen duoc in ban chi tiet kem dap an
 * (getDetailedMessage) - khac voi SseJudgeListener gui ve trinh duyet thi sinh,
 * chi duoc dung ban cong khai (getMessage).
 */
public class ConsoleJudgeListener implements JudgeListener {

    private final boolean verbose;

    public ConsoleJudgeListener(boolean verbose) {
        this.verbose = verbose;
    }

    @Override
    public void onJudgeStarted(Submission s) {
        System.out.printf("%n>>> Chấm %s | bài %s (%s) | ngôn ngữ %s | file %s%n",
                s.getId(), s.getProblem().getId(), s.getProblem().getTitle(),
                s.getLanguage().getName(), s.getSourcePath().getFileName());
    }

    @Override
    public void onCompiled(Submission s, boolean success, String message) {
        if (success) {
            System.out.println("    Biên dịch: OK");
        } else {
            System.out.println("    Biên dịch: THẤT BẠI");
            if (verbose && !message.isEmpty()) {
                System.out.println(indent(message));
            }
        }
    }

    @Override
    public void onTestCaseFinished(Submission s, int index, int total, TestCaseResult r) {
        System.out.printf("    Test %2d/%-2d  %-4s  %5d ms   %s%n",
                index, total, r.getVerdict().getCode(), r.getRuntimeMs(),
                r.getVerdict().isAccepted() ? "" : shorten(r.getDetailedMessage()));
    }

    @Override
    public void onJudgeFinished(Submission s, JudgeResult result) {
        Verdict v = result.getOverallVerdict();
        System.out.printf("    => %s (%s) | %d/%d test | %.1f/%.1f điểm | tổng %d ms%n",
                v.getCode(), v.getDisplay(), result.getPassedCount(), result.getTotalTests(),
                result.getScore(), s.getProblem().getMaxPoints(), result.getJudgeTimeMs());
        // Loi bien dich da in o onCompiled roi -> khong in lai.
        if (verbose && v != Verdict.CE && !result.getGlobalMessage().isEmpty()) {
            System.out.println(indent(result.getGlobalMessage()));
        }
    }

    private static String shorten(String msg) {
        if (msg == null) return "";
        String one = msg.replace("\r", " ").replace("\n", " ").trim();
        return one.length() <= 90 ? one : one.substring(0, 87) + "...";
    }

    /** Thut le va them gach dau dong cho khoi thong bao nhieu dong cua compiler. */
    private static String indent(String text) {
        StringBuilder sb = new StringBuilder();
        String[] lines = text.split("\r?\n");
        for (int i = 0; i < lines.length; i++) {
            if (i > 0) sb.append(System.lineSeparator());
            sb.append("        | ").append(lines[i]);
        }
        return sb.toString();
    }
}
