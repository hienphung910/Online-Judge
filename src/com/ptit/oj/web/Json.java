package com.ptit.oj.web;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Bo sinh va doc JSON toi gian, viet tay de KHONG phai dung thu vien ngoai
 * (yeu cau cua bai tap lon: chi dung Java chuan).
 *
 * Pham vi ho tro:
 *  - Sinh: object / array long nhau, chuoi, so, boolean, null.
 *  - Doc : mot object phang (gia tri la chuoi / so / boolean / null) - du de
 *          nhan body cua request POST /api/submit.
 */
public final class Json {

    private Json() { }

    // ------------------------------------------------------------ phan sinh

    /** Bo dung mot JSON object theo kieu chuoi phuong thuc. */
    public static class Obj {
        private final StringBuilder sb = new StringBuilder("{");
        private boolean first = true;

        private Obj comma() {
            if (!first) sb.append(',');
            first = false;
            return this;
        }

        public Obj put(String key, String value) {
            comma().sb.append(quote(key)).append(':').append(value == null ? "null" : quote(value));
            return this;
        }

        public Obj put(String key, long value) {
            comma().sb.append(quote(key)).append(':').append(value);
            return this;
        }

        public Obj put(String key, double value) {
            comma().sb.append(quote(key)).append(':').append(number(value));
            return this;
        }

        public Obj put(String key, boolean value) {
            comma().sb.append(quote(key)).append(':').append(value);
            return this;
        }

        /** Gan mot doan JSON da dung san (object hoac array con). */
        public Obj putRaw(String key, String rawJson) {
            comma().sb.append(quote(key)).append(':').append(rawJson == null ? "null" : rawJson);
            return this;
        }

        public Obj putNull(String key) {
            comma().sb.append(quote(key)).append(":null");
            return this;
        }

        public String build() {
            return sb.toString() + "}";
        }
    }

    public static Obj obj() {
        return new Obj();
    }

    /** Ghep cac doan JSON thanh mot array. */
    public static String array(List<String> items) {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < items.size(); i++) {
            if (i > 0) sb.append(',');
            sb.append(items.get(i));
        }
        return sb.append(']').toString();
    }

    /** Mang chuoi, vi du danh sach ten ngon ngu. */
    public static String stringArray(List<String> values) {
        List<String> quoted = new ArrayList<>(values.size());
        for (String v : values) quoted.add(quote(v));
        return array(quoted);
    }

    /** Bo qua NaN/Infinity vi JSON khong bieu dien duoc (tra ve 0). */
    private static String number(double value) {
        if (Double.isNaN(value) || Double.isInfinite(value)) return "0";
        if (value == Math.rint(value) && Math.abs(value) < 1e15) {
            return String.valueOf((long) value);
        }
        return String.valueOf(Math.round(value * 1000.0) / 1000.0);
    }

    /** Boc chuoi trong dau ngoac kep va escape dung chuan JSON. */
    public static String quote(String s) {
        if (s == null) return "null";
        StringBuilder sb = new StringBuilder(s.length() + 16).append('"');
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            switch (c) {
                case '"':  sb.append("\\\""); break;
                case '\\': sb.append("\\\\"); break;
                case '\n': sb.append("\\n");  break;
                case '\r': sb.append("\\r");  break;
                case '\t': sb.append("\\t");  break;
                case '\b': sb.append("\\b");  break;
                case '\f': sb.append("\\f");  break;
                default:
                    if (c < 0x20) {
                        sb.append(String.format("\\u%04x", (int) c));
                    } else {
                        sb.append(c);
                    }
            }
        }
        return sb.append('"').toString();
    }

    // -------------------------------------------------------------- phan doc

    /**
     * Mot gia tri JSON bat ky sau khi doc: object, array, chuoi, so, boolean, null.
     *
     * Truoc day chi co parseFlatObject() nen khong nhan duoc body long nhau cua
     * POST /api/admin/problems (co mang "tests" gom nhieu object). Lop nay la bo
     * doc de quy day du - van la Java thuan, khong them thu vien ngoai.
     */
    public static final class Value {

        private final Object raw;   // null | String | Double | Boolean | List<Value> | Map<String,Value>

        private Value(Object raw) {
            this.raw = raw;
        }

        public boolean isNull()   { return raw == null; }
        public boolean isObject() { return raw instanceof Map; }
        public boolean isArray()  { return raw instanceof List; }
        public boolean isString() { return raw instanceof String; }
        public boolean isNumber() { return raw instanceof Double; }
        public boolean isBoolean() { return raw instanceof Boolean; }

        @SuppressWarnings("unchecked")
        private Map<String, Value> asMap() {
            if (!isObject()) throw new IllegalArgumentException("Cần một JSON object");
            return (Map<String, Value>) raw;
        }

        @SuppressWarnings("unchecked")
        public List<Value> asArray() {
            if (!isArray()) throw new IllegalArgumentException("Cần một JSON array");
            return (List<Value>) raw;
        }

        /** Co thuoc tinh nay khong (ke ca khi gia tri la null). */
        public boolean has(String key) {
            return isObject() && asMap().containsKey(key);
        }

        /** Gia tri cua thuoc tinh, hoac Value rong (isNull) neu khong co. */
        public Value get(String key) {
            if (!isObject()) return new Value(null);
            Value v = asMap().get(key);
            return v == null ? new Value(null) : v;
        }

        /** Danh sach con cua thuoc tinh; rong neu thuoc tinh khong ton tai. */
        public List<Value> getArray(String key) {
            Value v = get(key);
            return v.isArray() ? v.asArray() : Collections.<Value>emptyList();
        }

        /** Chuoi, hoac null neu thuoc tinh khong co / la null. So va boolean cung doc duoc. */
        public String getString(String key) {
            Value v = get(key);
            if (v.isNull()) return null;
            if (v.isString()) return (String) v.raw;
            if (v.isNumber()) return number((Double) v.raw);
            if (v.isBoolean()) return String.valueOf(v.raw);
            throw new IllegalArgumentException("Thuộc tính \"" + key + "\" phải là chuỗi");
        }

        public String getString(String key, String fallback) {
            String v = getString(key);
            return v == null ? fallback : v;
        }

        public double getDouble(String key, double fallback) {
            Value v = get(key);
            if (v.isNumber()) return (Double) v.raw;
            if (v.isString()) {
                try {
                    return Double.parseDouble(((String) v.raw).trim());
                } catch (NumberFormatException e) {
                    throw new IllegalArgumentException("Thuộc tính \"" + key + "\" phải là số");
                }
            }
            if (v.isNull()) return fallback;
            throw new IllegalArgumentException("Thuộc tính \"" + key + "\" phải là số");
        }

        public long getLong(String key, long fallback) {
            double d = getDouble(key, fallback);
            if (d != Math.rint(d)) throw new IllegalArgumentException("Thuộc tính \"" + key + "\" phải là số nguyên");
            return (long) d;
        }

        public boolean getBoolean(String key, boolean fallback) {
            Value v = get(key);
            if (v.isBoolean()) return (Boolean) v.raw;
            if (v.isString()) return Boolean.parseBoolean(((String) v.raw).trim());
            if (v.isNumber()) return ((Double) v.raw) != 0;
            return fallback;
        }
    }

    /** So ky tu toi da cua mot chuoi JSON - chan tren de tranh body khong lo. */
    private static final int MAX_JSON_CHARS = 8 * 1024 * 1024;
    /** Do sau long nhau toi da - chan cac body co tinh lam tran ngan xep. */
    private static final int MAX_DEPTH = 32;

    /** Doc mot chuoi JSON bat ky. Nem IllegalArgumentException neu sai cu phap. */
    public static Value parse(String json) {
        if (json == null) throw new IllegalArgumentException("Body rỗng");
        if (json.length() > MAX_JSON_CHARS) throw new IllegalArgumentException("Dữ liệu JSON quá lớn");
        Parser parser = new Parser(json);
        Value value = parser.readValue(0);
        parser.skipWhitespace();
        if (!parser.atEnd()) {
            throw new IllegalArgumentException("Thừa ký tự sau JSON tại vị trí " + parser.position());
        }
        return value;
    }

    /** Doc va bat buoc ket qua phai la mot JSON object. */
    public static Value parseObject(String json) {
        Value v = parse(json);
        if (!v.isObject()) throw new IllegalArgumentException("Body phải là một JSON object");
        return v;
    }

    /** Bo doc de quy: object / array / string / number / true / false / null. */
    private static final class Parser {

        private final String s;
        private int i;

        private Parser(String s) {
            this.s = s;
        }

        private int position() { return i; }

        private boolean atEnd() { return i >= s.length(); }

        private void skipWhitespace() {
            while (i < s.length() && Character.isWhitespace(s.charAt(i))) i++;
        }

        private char peek() {
            if (i >= s.length()) throw new IllegalArgumentException("JSON kết thúc đột ngột");
            return s.charAt(i);
        }

        private Value readValue(int depth) {
            if (depth > MAX_DEPTH) throw new IllegalArgumentException("JSON lồng nhau quá sâu");
            skipWhitespace();
            char c = peek();
            switch (c) {
                case '{': return readObject(depth);
                case '[': return readArray(depth);
                case '"': return new Value(readQuotedString());
                case 't': return new Value(readLiteral("true", Boolean.TRUE));
                case 'f': return new Value(readLiteral("false", Boolean.FALSE));
                case 'n': return new Value(readLiteral("null", null));
                default:  return new Value(readNumber());
            }
        }

        private Value readObject(int depth) {
            Map<String, Value> map = new LinkedHashMap<>();
            i++;                                  // bo dau {
            skipWhitespace();
            if (peek() == '}') {
                i++;
                return new Value(map);
            }
            while (true) {
                skipWhitespace();
                if (peek() != '"') {
                    throw new IllegalArgumentException("Thiếu tên thuộc tính tại vị trí " + i);
                }
                String key = readQuotedString();
                skipWhitespace();
                if (peek() != ':') throw new IllegalArgumentException("Thiếu dấu : sau \"" + key + "\"");
                i++;
                map.put(key, readValue(depth + 1));
                skipWhitespace();
                char c = peek();
                if (c == ',') {
                    i++;
                    continue;
                }
                if (c == '}') {
                    i++;
                    return new Value(map);
                }
                throw new IllegalArgumentException("Ký tự không mong đợi trong object tại vị trí " + i + ": " + c);
            }
        }

        private Value readArray(int depth) {
            List<Value> items = new ArrayList<>();
            i++;                                  // bo dau [
            skipWhitespace();
            if (peek() == ']') {
                i++;
                return new Value(items);
            }
            while (true) {
                items.add(readValue(depth + 1));
                skipWhitespace();
                char c = peek();
                if (c == ',') {
                    i++;
                    continue;
                }
                if (c == ']') {
                    i++;
                    return new Value(items);
                }
                throw new IllegalArgumentException("Ký tự không mong đợi trong mảng tại vị trí " + i + ": " + c);
            }
        }

        private String readQuotedString() {
            StringBuilder out = new StringBuilder();
            i = Json.readString(s, i, out);
            return out.toString();
        }

        private Object readLiteral(String literal, Object value) {
            if (!s.startsWith(literal, i)) {
                throw new IllegalArgumentException("Giá trị không hợp lệ tại vị trí " + i);
            }
            i += literal.length();
            return value;
        }

        private Double readNumber() {
            int start = i;
            if (i < s.length() && (s.charAt(i) == '-' || s.charAt(i) == '+')) i++;
            while (i < s.length() && "0123456789.eE+-".indexOf(s.charAt(i)) >= 0) i++;
            String text = s.substring(start, i);
            try {
                return Double.valueOf(text);
            } catch (NumberFormatException e) {
                throw new IllegalArgumentException("Số không hợp lệ tại vị trí " + start + ": " + text);
            }
        }
    }

    /**
     * Doc mot JSON object phang thanh Map (gia tri luon tra ve duoi dang String).
     * Nem IllegalArgumentException neu chuoi khong hop le.
     */
    public static Map<String, String> parseFlatObject(String json) {
        Map<String, String> result = new LinkedHashMap<>();
        if (json == null) throw new IllegalArgumentException("Body rỗng");
        int i = skipSpace(json, 0);
        if (i >= json.length() || json.charAt(i) != '{') {
            throw new IllegalArgumentException("JSON phải bắt đầu bằng {");
        }
        i = skipSpace(json, i + 1);
        if (i < json.length() && json.charAt(i) == '}') return result;

        while (i < json.length()) {
            i = skipSpace(json, i);
            if (json.charAt(i) != '"') throw new IllegalArgumentException("Thiếu tên thuộc tính tại vị trí " + i);
            StringBuilder key = new StringBuilder();
            i = readString(json, i, key);

            i = skipSpace(json, i);
            if (i >= json.length() || json.charAt(i) != ':') {
                throw new IllegalArgumentException("Thiếu dấu : sau " + key);
            }
            i = skipSpace(json, i + 1);

            StringBuilder value = new StringBuilder();
            if (json.charAt(i) == '"') {
                i = readString(json, i, value);
            } else {
                while (i < json.length() && ",}".indexOf(json.charAt(i)) < 0) {
                    value.append(json.charAt(i++));
                }
            }
            result.put(key.toString(), value.toString().trim());

            i = skipSpace(json, i);
            if (i >= json.length()) break;
            char c = json.charAt(i);
            if (c == ',') {
                i++;
                continue;
            }
            if (c == '}') break;
            throw new IllegalArgumentException("Ký tự không mong đợi tại vị trí " + i + ": " + c);
        }
        return result;
    }

    private static int skipSpace(String s, int i) {
        while (i < s.length() && Character.isWhitespace(s.charAt(i))) i++;
        return i;
    }

    /** Doc chuoi bat dau tai dau ngoac kep, giai ma escape. Tra ve vi tri sau chuoi. */
    static int readString(String s, int i, StringBuilder out) {
        i++;   // bo dau ngoac kep mo
        while (i < s.length()) {
            char c = s.charAt(i);
            if (c == '"') return i + 1;
            if (c == '\\') {
                if (i + 1 >= s.length()) break;
                char e = s.charAt(++i);
                switch (e) {
                    case 'n':  out.append('\n'); break;
                    case 'r':  out.append('\r'); break;
                    case 't':  out.append('\t'); break;
                    case 'b':  out.append('\b'); break;
                    case 'f':  out.append('\f'); break;
                    case '"':  out.append('"');  break;
                    case '\\': out.append('\\'); break;
                    case '/':  out.append('/');  break;
                    case 'u':
                        if (i + 4 >= s.length()) throw new IllegalArgumentException("Escape \\u bị cắt");
                        out.append((char) Integer.parseInt(s.substring(i + 1, i + 5), 16));
                        i += 4;
                        break;
                    default:
                        throw new IllegalArgumentException("Escape không hợp lệ: \\" + e);
                }
                i++;
            } else {
                out.append(c);
                i++;
            }
        }
        throw new IllegalArgumentException("Chuỗi JSON chưa được đóng");
    }
}
