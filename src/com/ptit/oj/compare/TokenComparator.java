package com.ptit.oj.compare;

import java.util.Arrays;
import java.util.List;

/**
 * So sanh theo tung token, bo qua khoang trang / xuong dong thua.
 * Day la kieu so sanh mac dinh cua hau het cac Online Judge (Codeforces, LeetCode...).
 *
 * Toan bo vong lap so sanh nam o day va di qua tokenEquals(); lop con (FloatComparator)
 * chi ghi de phep so sanh MOT token va cach goi ten cho lech - khong copy lai vong lap.
 */
public class TokenComparator implements OutputComparator {

    @Override
    public String getName() { return "token"; }

    @Override
    public boolean matches(String expected, String actual) {
        List<String> e = tokens(expected);
        List<String> a = tokens(actual);
        return e.size() == a.size() && firstMismatch(e, a) < 0;
    }

    protected List<String> tokens(String s) {
        if (s == null) return Arrays.asList();
        String trimmed = s.trim();
        if (trimmed.isEmpty()) return Arrays.asList();
        return Arrays.asList(trimmed.split("\\s+"));
    }

    /** So sanh MOT token. FloatComparator ghi de de chap nhan sai so. */
    protected boolean tokenEquals(String expected, String actual) {
        return expected.equals(actual);
    }

    /** Cach goi ten mot cho lech trong thong bao; FloatComparator doi thanh "Lệch quá sai số". */
    protected String mismatchLabel() {
        return "Lệch";
    }

    /** Vi tri token dau tien khong khop, hoac -1 neu khop het. Gia su hai danh sach cung do dai. */
    protected int firstMismatch(List<String> e, List<String> a) {
        for (int i = 0; i < e.size(); i++) {
            if (!tokenEquals(e.get(i), a.get(i))) return i;
        }
        return -1;
    }

    /** Cong khai: noi vi tri lech va gia tri thi sinh in ra - khong noi gia tri dung la gi. */
    @Override
    public String explain(String expected, String actual) {
        List<String> e = tokens(expected);
        List<String> a = tokens(actual);
        if (e.size() != a.size()) {
            return "Số lượng giá trị không khớp: nhận được " + a.size();
        }
        int i = firstMismatch(e, a);
        if (i < 0) return "Khớp";
        return mismatchLabel() + " tại giá trị thứ " + (i + 1) + ": nhận được [" + a.get(i) + "]";
    }

    /** Chi tiet cho nguoi cham: them dap an vao dung cho lech. */
    @Override
    public String explainDetailed(String expected, String actual) {
        List<String> e = tokens(expected);
        List<String> a = tokens(actual);
        if (e.size() != a.size()) {
            return "Sai số lượng giá trị: kỳ vọng " + e.size() + ", nhận được " + a.size();
        }
        int i = firstMismatch(e, a);
        if (i < 0) return "Khớp";
        return mismatchLabel() + " tại giá trị thứ " + (i + 1) + ": kỳ vọng [" + e.get(i)
                + "], nhận được [" + a.get(i) + "]";
    }
}
