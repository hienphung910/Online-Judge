package com.ptit.oj.service;

import java.security.SecureRandom;
import java.time.Duration;
import java.time.Instant;
import java.util.Base64;
import java.util.Iterator;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;

/**
 * Quan ly phien dang nhap.
 *
 * Day la ung dung chay cuc bo nen phien duoc giu trong ConcurrentHashMap
 * (tat may chu la moi nguoi phai dang nhap lai - chap nhan duoc). Nhung token
 * thi van phai lam nghiem tuc:
 *   - sinh bang SecureRandom 32 byte (khong dung Math.random / UUID),
 *   - co han su dung, het han la khong dung duoc nua,
 *   - luu userId chu khong luu username, de doi ten khong lam hong phien.
 */
public class SessionService {

    private static final int TOKEN_BYTES = 32;
    private static final Duration DEFAULT_TTL = Duration.ofHours(8);

    private final Map<String, Session> sessions = new ConcurrentHashMap<>();
    private final SecureRandom random = new SecureRandom();
    private final Duration ttl;

    public SessionService() {
        this(DEFAULT_TTL);
    }

    public SessionService(Duration ttl) {
        this.ttl = ttl;
    }

    /** Mot phien dang nhap dang song. */
    public static final class Session {
        private final String userId;
        private final Instant expiresAt;

        private Session(String userId, Instant expiresAt) {
            this.userId = userId;
            this.expiresAt = expiresAt;
        }

        public String getUserId() { return userId; }
        public Instant getExpiresAt() { return expiresAt; }
        public boolean isExpired() { return Instant.now().isAfter(expiresAt); }
    }

    /** Tao token moi cho mot tai khoan. */
    public String createToken(String userId) {
        purgeExpired();
        byte[] bytes = new byte[TOKEN_BYTES];
        random.nextBytes(bytes);
        String token = Base64.getUrlEncoder().withoutPadding().encodeToString(bytes);
        sessions.put(token, new Session(userId, Instant.now().plus(ttl)));
        return token;
    }

    /** Tra ve userId neu token con hieu luc. */
    public Optional<String> resolve(String token) {
        if (token == null || token.isEmpty()) return Optional.empty();
        Session session = sessions.get(token);
        if (session == null) return Optional.empty();
        if (session.isExpired()) {
            sessions.remove(token);
            return Optional.empty();
        }
        return Optional.of(session.getUserId());
    }

    public Optional<Instant> expiresAt(String token) {
        Session session = token == null ? null : sessions.get(token);
        return session == null || session.isExpired() ? Optional.empty() : Optional.of(session.getExpiresAt());
    }

    /** Dang xuat. Tra ve true neu token dang ton tai. */
    public boolean invalidate(String token) {
        return token != null && sessions.remove(token) != null;
    }

    /** Huy moi phien cua mot tai khoan (dung khi doi mat khau / khoa tai khoan). */
    public void invalidateAllFor(String userId) {
        sessions.entrySet().removeIf(e -> e.getValue().getUserId().equals(userId));
    }

    public int activeSessionCount() {
        purgeExpired();
        return sessions.size();
    }

    /** Doc header "Authorization: Bearer xxx" -> "xxx". */
    public static String extractBearerToken(String authorizationHeader) {
        if (authorizationHeader == null) return null;
        String value = authorizationHeader.trim();
        if (value.regionMatches(true, 0, "Bearer ", 0, 7)) {
            String token = value.substring(7).trim();
            return token.isEmpty() ? null : token;
        }
        return null;
    }

    private void purgeExpired() {
        for (Iterator<Map.Entry<String, Session>> it = sessions.entrySet().iterator(); it.hasNext(); ) {
            if (it.next().getValue().isExpired()) it.remove();
        }
    }
}
