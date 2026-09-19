package com.ptit.oj.web;

/**
 * Loi cua mot request kem ma HTTP nen tra ve.
 *
 * Nho co lop nay, cac handler chi can nem loi voi dung ngu nghia
 * (400 / 401 / 403 / 404 / 409) va mot cho duy nhat trong ApiServer lo viec
 * bien no thanh phan hoi JSON - khong lo stack trace ra ngoai.
 */
public class ApiException extends RuntimeException {

    private final int status;

    public ApiException(int status, String message) {
        super(message);
        this.status = status;
    }

    public int getStatus() { return status; }

    public static ApiException badRequest(String message)  { return new ApiException(400, message); }
    public static ApiException unauthorized(String message) { return new ApiException(401, message); }
    public static ApiException forbidden(String message)   { return new ApiException(403, message); }
    public static ApiException notFound(String message)    { return new ApiException(404, message); }
    public static ApiException conflict(String message)    { return new ApiException(409, message); }
}
