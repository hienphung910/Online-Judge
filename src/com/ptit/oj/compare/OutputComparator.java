package com.ptit.oj.compare;

/**
 * STRATEGY PATTERN: mot cach so sanh output cua thi sinh voi dap an.
 * Judge chi lam viec voi interface nay, khong biet thuat toan cu the ben trong.
 *
 * Hai muc giai thich khi sai:
 *
 *   explain()         - ban CONG KHAI: gui ve trinh duyet, luu vao CSDL.
 *                       TUYET DOI KHONG chua dap an. Test an ma lo dap an thi thi sinh
 *                       nop bua vai lan, doc "ky vong" cua tung test roi hardcode lai la
 *                       qua het - bo cham thanh vo nghia. Chi noi lech o dau va thi sinh
 *                       da in ra gi (cai do ho biet san roi).
 *
 *   explainDetailed() - ban CHI TIET kem dap an: chi in ra terminal cua nguoi cham
 *                       (ConsoleJudgeListener), khong bao gio roi khoi may chu.
 *
 * An toan theo cau truc chu khong phai loc o bien: TestCaseResult.message luon la ban
 * cong khai, nen ApiServer / SseJudgeListener / kho CSDL khong can biet gi ve chuyen nay.
 */
public interface OutputComparator {

    /** Ten thuat toan, dung de in ra bao cao. */
    String getName();

    /** true neu output cua thi sinh duoc coi la dung. */
    boolean matches(String expected, String actual);

    /** Giai thich CONG KHAI vi sao sai - khong kem dap an. */
    default String explain(String expected, String actual) {
        return "Nhận được: [" + preview(actual) + "]";
    }

    /** Giai thich CHI TIET kem dap an - chi danh cho nguoi cham. */
    default String explainDetailed(String expected, String actual) {
        return "Kỳ vọng: [" + preview(expected) + "] | Nhận được: [" + preview(actual) + "]";
    }

    static String preview(String s) {
        String flat = s == null ? "" : s.replace("\r", "").replace("\n", " / ").trim();
        return flat.length() <= 60 ? flat : flat.substring(0, 57) + "...";
    }
}
