package com.ptit.oj.compare;

/** So sanh tuyet doi tung ky tu (chi chuan hoa ky tu xuong dong Windows/Unix). */
public class ExactComparator implements OutputComparator {

    @Override
    public String getName() { return "exact"; }

    @Override
    public boolean matches(String expected, String actual) {
        return normalize(expected).equals(normalize(actual));
    }

    private String normalize(String s) {
        return s == null ? "" : s.replace("\r\n", "\n").replace("\r", "\n");
    }
}
