package com.ptit.oj.service;

import com.ptit.oj.model.Verdict;
import com.ptit.oj.repository.SubmissionRepository;

import java.util.EnumMap;
import java.util.Map;

/**
 * Thong ke verdict tren TOAN BO lich su nop bai.
 *
 * Truoc day so lieu lay tu StatisticsListener nen chi dem duoc phien dang chay:
 * tat chuong trinh la ve 0. Nay doc thang tu kho du lieu nen mo lai van dung.
 */
public class StatisticsService {

    private final SubmissionRepository submissions;

    public StatisticsService(SubmissionRepository submissions) {
        this.submissions = submissions;
    }

    public Map<Verdict, Integer> countByVerdict() {
        return new EnumMap<>(submissions.countByVerdict());
    }

    public int getTotalSubmissions() {
        return submissions.count();
    }

    /** Ban bao cao dang van ban cho giao dien console. */
    public String report() {
        int total = getTotalSubmissions();
        if (total == 0) return "Chưa có bài nộp nào được chấm.";
        StringBuilder sb = new StringBuilder("Tổng số bài nộp: " + total);
        for (Map.Entry<Verdict, Integer> e : countByVerdict().entrySet()) {
            sb.append(System.lineSeparator())
              .append(String.format("  %-4s %-22s %d lần",
                      e.getKey().getCode(), e.getKey().getDisplay(), e.getValue()));
        }
        return sb.toString();
    }
}
