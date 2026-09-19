package com.ptit.oj.service;

import com.ptit.oj.model.Credentials;

import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.spec.InvalidKeySpecException;
import java.util.Arrays;
import java.util.Base64;

/**
 * Bam va kiem tra mat khau. Chi dung API chuan cua JDK, khong them thu vien ngoai.
 *
 *  - PBKDF2WithHmacSHA256: co suc can ep buoc nho so vong lap lon (khac han
 *    MD5/SHA-256 tran, vi hai cai do bam qua nhanh nen do rat de).
 *  - SecureRandom: sinh muoi ngau nhien RIENG cho tung tai khoan, nen hai nguoi
 *    dat cung mat khau van cho ra hai chuoi bam khac nhau (chong rainbow table).
 *  - MessageDigest.isEqual: so sanh theo thoi gian hang so, khong ro ri thong tin
 *    qua thoi gian phan hoi nhu equals() thong thuong.
 *
 * Lop nay KHONG BAO GIO luu, tra ve hay ghi log mat khau goc.
 */
public class PasswordService {

    public static final int MIN_PASSWORD_LENGTH = 8;
    /** Chan tren de mot request khong the bat may chu bam mot chuoi khong lo. */
    public static final int MAX_PASSWORD_LENGTH = 128;

    private static final String ALGORITHM = "PBKDF2WithHmacSHA256";
    private static final int DEFAULT_ITERATIONS = 120_000;
    private static final int SALT_BYTES = 16;
    private static final int KEY_BITS = 256;

    private final SecureRandom random = new SecureRandom();
    private final int iterations;

    public PasswordService() {
        this(DEFAULT_ITERATIONS);
    }

    public PasswordService(int iterations) {
        if (iterations <= 0) throw new IllegalArgumentException("Số vòng lặp phải dương");
        this.iterations = iterations;
    }

    /** Kiem tra do dai mat khau truoc khi bam. Nem IllegalArgumentException neu sai. */
    public void validate(String rawPassword) {
        if (rawPassword == null || rawPassword.isEmpty()) {
            throw new IllegalArgumentException("Mật khẩu không được rỗng");
        }
        if (rawPassword.length() < MIN_PASSWORD_LENGTH) {
            throw new IllegalArgumentException("Mật khẩu phải có ít nhất " + MIN_PASSWORD_LENGTH + " ký tự");
        }
        if (rawPassword.length() > MAX_PASSWORD_LENGTH) {
            throw new IllegalArgumentException("Mật khẩu tối đa " + MAX_PASSWORD_LENGTH + " ký tự");
        }
    }

    /** Sinh muoi moi va bam mat khau. */
    public Credentials hash(String rawPassword) {
        validate(rawPassword);
        byte[] salt = new byte[SALT_BYTES];
        random.nextBytes(salt);
        byte[] hash = pbkdf2(rawPassword.toCharArray(), salt, iterations);
        try {
            return new Credentials(
                    Base64.getEncoder().encodeToString(hash),
                    Base64.getEncoder().encodeToString(salt),
                    iterations);
        } finally {
            Arrays.fill(hash, (byte) 0);
        }
    }

    /** So sanh mat khau nguoi dung nhap voi ban ghi trong CSDL. */
    public boolean matches(String rawPassword, Credentials stored) {
        if (rawPassword == null || stored == null) return false;
        if (rawPassword.length() > MAX_PASSWORD_LENGTH) return false;
        byte[] expected;
        byte[] salt;
        try {
            expected = Base64.getDecoder().decode(stored.getHashBase64());
            salt = Base64.getDecoder().decode(stored.getSaltBase64());
        } catch (IllegalArgumentException e) {
            return false;   // ban ghi hong -> coi nhu sai mat khau, khong lam sap may chu
        }
        byte[] actual = pbkdf2(rawPassword.toCharArray(), salt, stored.getIterations());
        try {
            return MessageDigest.isEqual(expected, actual);
        } finally {
            Arrays.fill(actual, (byte) 0);
        }
    }

    /** Sinh mat khau ngau nhien manh - dung cho tai khoan admin khoi tao lan dau. */
    public String generateRandomPassword() {
        byte[] bytes = new byte[18];
        random.nextBytes(bytes);
        return Base64.getUrlEncoder().withoutPadding().encodeToString(bytes);
    }

    private byte[] pbkdf2(char[] password, byte[] salt, int rounds) {
        PBEKeySpec spec = new PBEKeySpec(password, salt, rounds, KEY_BITS);
        try {
            return SecretKeyFactory.getInstance(ALGORITHM).generateSecret(spec).getEncoded();
        } catch (NoSuchAlgorithmException | InvalidKeySpecException e) {
            throw new IllegalStateException("JVM không hỗ trợ " + ALGORITHM, e);
        } finally {
            spec.clearPassword();
            Arrays.fill(password, '\0');
        }
    }

    /** Chuan hoa username; nem IllegalArgumentException neu khong hop le. */
    public static String normalizeUsername(String username) {
        String u = username == null ? "" : username.trim();
        if (u.length() < 3 || u.length() > 32) {
            throw new IllegalArgumentException("Tên đăng nhập phải dài 3-32 ký tự");
        }
        if (!u.matches("[A-Za-z0-9_.]+")) {
            throw new IllegalArgumentException("Tên đăng nhập chỉ gồm chữ, số, dấu chấm hoặc gạch dưới");
        }
        return u;
    }
}
