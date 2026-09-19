package com.ptit.oj.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/** Mot bai tap tren he thong. */
public class Problem extends Entity {

    private final String title;
    private final String statement;
    private final long timeLimitMs;
    private final int memoryLimitMb;
    private final String comparatorSpec;   // "exact" | "token" | "float:1e-6"
    private final List<TestCase> testCases = new ArrayList<>();

    public Problem(String id, String title, String statement,
                   long timeLimitMs, int memoryLimitMb, String comparatorSpec) {
        super(id);
        this.title = title;
        this.statement = statement == null ? "" : statement;
        this.timeLimitMs = timeLimitMs;
        this.memoryLimitMb = memoryLimitMb;
        this.comparatorSpec = comparatorSpec == null ? "token" : comparatorSpec;
    }

    public void addTestCase(TestCase tc) {
        testCases.add(tc);
    }

    /** Tra ve ban sao khong sua duoc -> bao ve trang thai noi bo (encapsulation). */
    public List<TestCase> getTestCases() {
        return Collections.unmodifiableList(testCases);
    }

    public String getTitle() { return title; }
    public String getStatement() { return statement; }
    public long getTimeLimitMs() { return timeLimitMs; }
    public int getMemoryLimitMb() { return memoryLimitMb; }
    public String getComparatorSpec() { return comparatorSpec; }

    public double getMaxPoints() {
        double sum = 0;
        for (TestCase tc : testCases) sum += tc.getPoints();
        return sum;
    }

    /** Khong cong bo so luong test: thi sinh chi can biet gioi han va tong diem. */
    @Override
    public String describe() {
        return String.format("[%s] %s | %d ms | %d MB | %.0f điểm",
                getId(), title, timeLimitMs, memoryLimitMb, getMaxPoints());
    }
}
