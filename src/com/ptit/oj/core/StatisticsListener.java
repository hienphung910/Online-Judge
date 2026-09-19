package com.ptit.oj.core;

import com.ptit.oj.model.JudgeResult;
import com.ptit.oj.model.Submission;
import com.ptit.oj.model.Verdict;

import java.util.EnumMap;
import java.util.Map;

/** Observer thu hai: dem so lan xuat hien cua tung verdict trong ca phien lam viec. */
public class StatisticsListener implements JudgeListener {

    private final Map<Verdict, Integer> counter = new EnumMap<>(Verdict.class);
    private int totalSubmissions;

    @Override
    public void onJudgeFinished(Submission submission, JudgeResult result) {
        totalSubmissions++;
        Verdict v = result.getOverallVerdict();
        counter.merge(v, 1, Integer::sum);
    }

    public int getTotalSubmissions() { return totalSubmissions; }

    public Map<Verdict, Integer> getCounter() { return new EnumMap<>(counter); }

    public String report() {
        if (totalSubmissions == 0) return "Chưa có bài nộp nào được chấm.";
        StringBuilder sb = new StringBuilder("Tổng số bài nộp: " + totalSubmissions);
        for (Map.Entry<Verdict, Integer> e : counter.entrySet()) {
            sb.append(System.lineSeparator())
              .append(String.format("  %-4s %-22s %d lần",
                      e.getKey().getCode(), e.getKey().getDisplay(), e.getValue()));
        }
        return sb.toString();
    }
}
