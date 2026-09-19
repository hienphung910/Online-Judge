package com.ptit.oj.model;

/**
 * Thong tin xac thuc cua mot tai khoan: KHONG chua mat khau goc, chi chua
 * chuoi bam PBKDF2 cung muoi va so vong lap da dung de bam.
 *
 * Day la doi tuong gia tri (immutable) nen truyen qua lai giua service va
 * repository ma khong so bi sua trom.
 */
public final class Credentials {

    private final String hashBase64;
    private final String saltBase64;
    private final int iterations;

    public Credentials(String hashBase64, String saltBase64, int iterations) {
        if (hashBase64 == null || hashBase64.isEmpty()) {
            throw new IllegalArgumentException("Thiếu chuỗi băm mật khẩu");
        }
        if (saltBase64 == null || saltBase64.isEmpty()) {
            throw new IllegalArgumentException("Thiếu muối băm mật khẩu");
        }
        if (iterations <= 0) {
            throw new IllegalArgumentException("Số vòng lặp phải dương");
        }
        this.hashBase64 = hashBase64;
        this.saltBase64 = saltBase64;
        this.iterations = iterations;
    }

    public String getHashBase64() { return hashBase64; }
    public String getSaltBase64() { return saltBase64; }
    public int getIterations() { return iterations; }

    /** Khong bao gio in hash/salt ra log. */
    @Override
    public String toString() {
        return "Credentials{pbkdf2, iterations=" + iterations + "}";
    }
}
