package com.ptit.oj.compare;

/**
 * FACTORY METHOD: tao Strategy so sanh tu chuoi cau hinh trong file de bai.
 * Cu phap: "exact" | "token" | "float" | "float:1e-9"
 */
public final class ComparatorFactory {

    private ComparatorFactory() { }

    public static OutputComparator create(String spec) {
        if (spec == null || spec.trim().isEmpty()) return new TokenComparator();
        String s = spec.trim().toLowerCase();

        if (s.equals("exact")) return new ExactComparator();
        if (s.equals("token")) return new TokenComparator();
        if (s.startsWith("float")) {
            double eps = 1e-6;
            int colon = s.indexOf(':');
            if (colon >= 0) {
                try {
                    eps = Double.parseDouble(s.substring(colon + 1).trim());
                } catch (NumberFormatException ignored) {
                    // giu epsilon mac dinh
                }
            }
            return new FloatComparator(eps);
        }
        throw new IllegalArgumentException("Kiểu so sánh không hỗ trợ: " + spec);
    }
}
