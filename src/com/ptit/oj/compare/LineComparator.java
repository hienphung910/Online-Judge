package com.ptit.oj.compare;

import java.util.ArrayList;
import java.util.List;

/**
 * So sanh theo tung DONG - danh cho bai ve hinh bang ky tu.
 *
 * TokenComparator khong dung duoc cho bai ve hinh vi no bo qua moi khoang trang:
 * tam giac can le trai va can le phai se bi coi la giong nhau. ExactComparator
 * thi qua kho voi hoc sinh nho (thua mot dau cach cuoi dong hay thieu dau xuong
 * dong cuoi cung la sai). Lop nay o giua:
 *   - khoang trang DAU dong duoc giu nguyen (no la mot phan cua hinh ve),
 *   - khoang trang CUOI dong va cac dong trong o cuoi output duoc bo qua.
 */
public class LineComparator implements OutputComparator {

    @Override
    public String getName() { return "lines"; }

    @Override
    public boolean matches(String expected, String actual) {
        return lines(expected).equals(lines(actual));
    }

    /** Cong khai: chi noi lech o dong nao va thi sinh da in gi o dong do. */
    @Override
    public String explain(String expected, String actual) {
        List<String> e = lines(expected);
        List<String> a = lines(actual);
        if (e.size() != a.size()) {
            return "Số dòng không khớp: nhận được " + a.size() + " dòng";
        }
        int i = firstMismatch(e, a);
        if (i < 0) return "Khớp";
        return "Lệch tại dòng thứ " + (i + 1) + ": nhận được [" + a.get(i) + "]";
    }

    @Override
    public String explainDetailed(String expected, String actual) {
        List<String> e = lines(expected);
        List<String> a = lines(actual);
        if (e.size() != a.size()) {
            return "Sai số dòng: kỳ vọng " + e.size() + ", nhận được " + a.size();
        }
        int i = firstMismatch(e, a);
        if (i < 0) return "Khớp";
        return "Lệch tại dòng thứ " + (i + 1) + ": kỳ vọng [" + e.get(i) + "], nhận được [" + a.get(i) + "]";
    }

    /** Tach dong, cat khoang trang cuoi moi dong, bo cac dong trong o cuoi. */
    private List<String> lines(String s) {
        List<String> result = new ArrayList<>();
        if (s == null) return result;
        for (String line : s.replace("\r\n", "\n").replace("\r", "\n").split("\n", -1)) {
            result.add(line.stripTrailing());
        }
        while (!result.isEmpty() && result.get(result.size() - 1).isEmpty()) {
            result.remove(result.size() - 1);
        }
        return result;
    }

    private int firstMismatch(List<String> e, List<String> a) {
        for (int i = 0; i < e.size(); i++) {
            if (!e.get(i).equals(a.get(i))) return i;
        }
        return -1;
    }
}
