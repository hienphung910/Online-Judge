package com.ptit.oj.exception;

/**
 * Bao loi khi lam viec voi CSDL. Boc SQLException lai thanh unchecked de tang
 * tren (service / web) khong phai khai bao throws o khap noi, nhung van giu
 * nguyen nguyen nhan goc de debug.
 */
public class DataAccessException extends RuntimeException {

    public DataAccessException(String message) {
        super(message);
    }

    public DataAccessException(String message, Throwable cause) {
        super(message, cause);
    }
}
