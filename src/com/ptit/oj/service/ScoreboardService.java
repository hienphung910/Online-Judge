package com.ptit.oj.service;

import com.ptit.oj.model.Problem;
import com.ptit.oj.model.Submission;
import com.ptit.oj.model.User;
import com.ptit.oj.repository.Repository;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Tinh bang xep hang: moi nguoi lay diem CAO NHAT tren tung bai, roi cong lai.
 * Tang lop service chi lam nghiep vu, khong lam I/O va khong lam cham bai.
 */
public class ScoreboardService {

    private final Repository<Submission> submissions;
    private final Repository<Problem> problems;

    public ScoreboardService(Repository<Submission> submissions, Repository<Problem> problems) {
        this.submissions = submissions;
        this.problems = problems;
    }

    /** Mot dong trong bang xep hang. */
    public static class Row {
        private final User user;
        private final Map<String, Double> bestPerProblem;
        private final int attempts;
        private final int solved;
        private final double total;

        Row(User user, Map<String, Double> bestPerProblem, int attempts, int solved, double total) {
            this.user = user;
            this.bestPerProblem = bestPerProblem;
            this.attempts = attempts;
            this.solved = solved;
            this.total = total;
        }

        public User getUser() { return user; }
        public Map<String, Double> getBestPerProblem() { return bestPerProblem; }
        public int getAttempts() { return attempts; }
        public int getSolved() { return solved; }
        public double getTotal() { return total; }
    }

    /**
     * Sai so cho phep khi so sanh "da dat diem toi da chua".
     *
     * Vi sao khong dung 1e-9: diem tung test luu trong MySQL o kieu DECIMAL(12,4),
     * nen mot bai 100 diem chia cho 3 test se thanh 3 x 33.3333 = 99.9999 khi doc
     * lai - lech 0.0001 so voi 100. Voi sai so 1e-9 thi bai da giai tron ven lai bi
     * dem thanh CHUA giai. Moi test lech toi da 0.00005, gioi han 200 test/bai
     * (xem ProblemAdminService.MAX_TESTS) nen 0.01 la nguong an toan va vẫn du chat
     * de khong nham mot bai thieu diem thanh dat diem toi da.
     */
    private static final double SCORE_EPSILON = 0.01;

    public List<Row> buildScoreboard() {
        Map<User, Map<String, Double>> best = new LinkedHashMap<>();
        Map<User, Integer> attempts = new HashMap<>();

        for (Submission s : submissions.findAll()) {
            if (!s.isJudged()) continue;
            User u = s.getAuthor();
            best.putIfAbsent(u, new LinkedHashMap<>());
            attempts.merge(u, 1, Integer::sum);

            String pid = s.getProblem().getId();
            double score = s.getResult().getScore();
            Double current = best.get(u).get(pid);
            if (current == null || score > current) {
                best.get(u).put(pid, score);
            }
        }

        List<Row> rows = new ArrayList<>();
        for (Map.Entry<User, Map<String, Double>> e : best.entrySet()) {
            double total = 0;
            int solved = 0;
            for (Map.Entry<String, Double> p : e.getValue().entrySet()) {
                total += p.getValue();
                Problem problem = problems.findById(p.getKey()).orElse(null);
                if (problem != null && p.getValue() >= problem.getMaxPoints() - SCORE_EPSILON) solved++;
            }
            rows.add(new Row(e.getKey(), e.getValue(), attempts.getOrDefault(e.getKey(), 0), solved, total));
        }

        rows.sort((a, b) -> {
            int byScore = Double.compare(b.getTotal(), a.getTotal());
            if (byScore != 0) return byScore;
            int byAttempts = Integer.compare(a.getAttempts(), b.getAttempts());  // it lan nop hon thi xep truoc
            if (byAttempts != 0) return byAttempts;
            return a.getUser().getUsername().compareTo(b.getUser().getUsername());
        });
        return rows;
    }
}
