package com.ptit.oj.model;

/** Mot bo test: input + output mong doi + diem. */
public class TestCase extends Entity {

    private final String input;
    private final String expectedOutput;
    private final double points;
    private final boolean sample;

    public TestCase(String id, String input, String expectedOutput, double points, boolean sample) {
        super(id);
        this.input = input == null ? "" : input;
        this.expectedOutput = expectedOutput == null ? "" : expectedOutput;
        this.points = points;
        this.sample = sample;
    }

    public String getInput() { return input; }
    public String getExpectedOutput() { return expectedOutput; }
    public double getPoints() { return points; }
    public boolean isSample() { return sample; }

    @Override
    public String describe() {
        return "Test " + getId() + (sample ? " (ví dụ)" : "") + " - " + points + " điểm";
    }
}
