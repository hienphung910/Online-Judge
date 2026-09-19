package com.ptit.oj.util;

/**
 * Tien ich xu ly van ban dung chung.
 *
 * Vi sao can loc BOM: Notepad tren Windows luu file UTF-8 kem 3 byte BOM (EF BB BF).
 * Neu file test, file demo-plan hoac file input duoc tao bang Notepad thi ky tu BOM
 * se dinh vao dau chuoi, lam lech ket qua so sanh hoac lam lenh dau tien khong hop le.
 */
public final class TextUtils {

    /** Ky tu BOM sau khi da duoc giai ma sang UTF-16. */
    private static final char BOM = 0xFEFF;

    private TextUtils() { }

    /** Bo BOM o dau chuoi (neu co). Tra ve null neu dau vao la null. */
    public static String stripBom(String s) {
        if (s == null || s.isEmpty()) return s;
        return s.charAt(0) == BOM ? s.substring(1) : s;
    }
}
