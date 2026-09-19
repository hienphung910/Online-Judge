package com.ptit.oj.repository;

import com.ptit.oj.model.Submission;
import com.ptit.oj.model.Verdict;

import java.util.ArrayList;
import java.util.Collections;
import java.util.EnumMap;
import java.util.List;
import java.util.Map;

/**
 * Kho lich su nop bai trong bo nho - dung cho --demo / --selftest.
 * Khong co transaction that vi tat ca nam trong mot cau truc du lieu duy nhat.
 */
public class InMemorySubmissionRepository extends InMemoryRepository<Submission>
        implements SubmissionRepository {

    @Override
    public void saveWithResults(Submission submission) {
        save(submission);
    }

    @Override
    public List<Submission> findAllNewestFirst() {
        List<Submission> all = findAll();
        Collections.reverse(all);
        return all;
    }

    @Override
    public List<Submission> findByUserId(String userId) {
        List<Submission> mine = new ArrayList<>();
        for (Submission s : findAllNewestFirst()) {
            if (s.getAuthor().getId().equals(userId)) mine.add(s);
        }
        return mine;
    }

    @Override
    public Map<Verdict, Integer> countByVerdict() {
        Map<Verdict, Integer> counter = new EnumMap<>(Verdict.class);
        for (Submission s : findAll()) {
            if (!s.isJudged()) continue;
            counter.merge(s.getResult().getOverallVerdict(), 1, Integer::sum);
        }
        return counter;
    }
}
