package com.ptit.oj.web;

import com.ptit.oj.core.JudgeListener;
import com.ptit.oj.model.JudgeResult;
import com.ptit.oj.model.Submission;
import com.ptit.oj.model.TestCaseResult;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;

/**
 * OBSERVER PATTERN - ban danh cho web.
 *
 * ConsoleJudgeListener in tien trinh cham ra terminal; lop nay lam dung viec do
 * nhung day ve TRINH DUYET, ngay khi tung test vua chay xong, thay vi bat nguoi
 * dung ngoi cho den luc cham het roi moi thay ket qua mot cuc.
 *
 * Diem dang chu y: Judge KHONG he biet co lop nay ton tai. Them mot kieu theo doi
 * moi khong phai sua mot dong nao trong lop Judge - dung tinh than Open/Closed.
 *
 * Dinh dang la Server-Sent Events (SSE) cua chuan HTML:
 *
 *     event: test
 *     data: {"index":2,"total":4,...}
 *     (mot dong trong ket thuc su kien)
 *
 * Vi sao SSE chu khong phai WebSocket: du lieu chi chay MOT chieu (may chu -> trinh
 * duyet), va SSE di tren HTTP thuong nen HttpServer co san cua JDK phuc vu duoc,
 * khong phai them thu vien nao - dung rang buoc "chi mot thu vien ngoai" cua bai tap lon.
 *
 * Vong doi: moi request nop bai tao mot doi tuong rieng, gan vao Judge truoc khi
 * cham va go ra trong finally (xem ApiServer.handleSubmitStream).
 */
public class SseJudgeListener implements JudgeListener {

    private final OutputStream out;

    /**
     * Nguoi dung dong tab giua chung thi ghi tiep se nem IOException. Khi do chi
     * danh dau hong va im lang bo qua: viec cham VAN phai chay cho xong de con luu
     * vao CSDL, khong duoc de mot ket noi dut lam hong ca bai nop.
     */
    private boolean broken = false;

    public SseJudgeListener(OutputStream out) {
        this.out = out;
    }

    // ------------------------------------------------- cac moc trong qua trinh cham

    @Override
    public void onJudgeStarted(Submission submission) {
        send("started", Json.obj()
                .put("submissionId", submission.getId())
                .put("problemId", submission.getProblem().getId())
                .put("language", submission.getLanguage().getName())
                .put("total", submission.getProblem().getTestCases().size())
                .build());
    }

    @Override
    public void onCompiled(Submission submission, boolean success, String message) {
        send("compiled", Json.obj()
                .put("success", success)
                .put("message", message == null ? "" : message)
                .build());
    }

    @Override
    public void onTestCaseFinished(Submission submission, int index, int total, TestCaseResult result) {
        send("test", Json.obj()
                .put("index", index)
                .put("total", total)
                .put("id", result.getTestCase().getId())
                .put("sample", result.getTestCase().isSample())
                .put("verdict", result.getVerdict().getCode())
                .put("runtimeMs", result.getRuntimeMs())
                .put("points", result.getEarnedPoints())
                .put("message", result.getMessage() == null ? "" : result.getMessage())
                .build());
    }

    @Override
    public void onJudgeFinished(Submission submission, JudgeResult result) {
        send("finished", Json.obj()
                .put("verdict", result.getOverallVerdict().getCode())
                .put("passed", result.getPassedCount())
                .put("total", result.getTotalTests())
                .put("score", result.getScore())
                .build());
    }

    // ----------------------------------------------- su kien do ApiServer tu gui

    /**
     * Su kien cuoi cung: nguyen ban ghi bai nop giong het POST /api/submit tra ve,
     * de frontend co du du lieu ma khong phai goi them mot request nua.
     */
    public void sendDone(String submissionJson) {
        send("done", submissionJson);
    }

    /** Loi xay ra SAU khi da gui header nen khong dat duoc ma HTTP nua - bao qua su kien. */
    public void sendError(String message) {
        send("error", Json.obj().put("error", message).build());
    }

    // ------------------------------------------------------------------ ky thuat

    /**
     * Mot khung SSE = "event: <ten>", "data: <json>", roi mot dong trong.
     * Bat buoc flush() ngay: khong flush thi du lieu nam trong bo dem va nguoi dung
     * van thay dung mot cuc luc cuoi - mat sach y nghia cua viec stream.
     */
    private void send(String event, String jsonData) {
        if (broken) return;
        try {
            String frame = "event: " + event + "\ndata: " + jsonData + "\n\n";
            out.write(frame.getBytes(StandardCharsets.UTF_8));
            out.flush();
        } catch (IOException e) {
            broken = true;   // nguoi dung dong tab - khong phai loi, cu cham tiep cho xong
        }
    }
}
