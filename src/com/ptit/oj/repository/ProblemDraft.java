package com.ptit.oj.repository;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Ban thao mot bai tap sap duoc ghi ra o dia (do admin gui len).
 *
 * Day chi la tui du lieu - moi phep kiem tra hop le do ProblemAdminService lam
 * TRUOC khi giao cho ProblemWriter, nen writer khong bao gio ghi du lieu ban.
 */
public class ProblemDraft {

    private String id;
    private String title;
    private String statement;
    private long timeLimitMs = 2000;
    private int memoryLimitMb = 256;
    private String comparator = "token";
    private double totalPoints = 100;
    private final List<TestDraft> tests = new ArrayList<>();

    /** Mot bo test trong ban thao. */
    public static class TestDraft {
        private final String name;
        private final String input;
        private final String output;
        private final boolean sample;

        public TestDraft(String name, String input, String output, boolean sample) {
            this.name = name;
            this.input = input;
            this.output = output;
            this.sample = sample;
        }

        public String getName() { return name; }
        public String getInput() { return input; }
        public String getOutput() { return output; }
        public boolean isSample() { return sample; }
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getStatement() { return statement; }
    public void setStatement(String statement) { this.statement = statement; }

    public long getTimeLimitMs() { return timeLimitMs; }
    public void setTimeLimitMs(long timeLimitMs) { this.timeLimitMs = timeLimitMs; }

    public int getMemoryLimitMb() { return memoryLimitMb; }
    public void setMemoryLimitMb(int memoryLimitMb) { this.memoryLimitMb = memoryLimitMb; }

    public String getComparator() { return comparator; }
    public void setComparator(String comparator) { this.comparator = comparator; }

    public double getTotalPoints() { return totalPoints; }
    public void setTotalPoints(double totalPoints) { this.totalPoints = totalPoints; }

    public void addTest(TestDraft test) { tests.add(test); }

    public List<TestDraft> getTests() { return Collections.unmodifiableList(tests); }
}
