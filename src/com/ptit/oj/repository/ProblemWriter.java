package com.ptit.oj.repository;

import com.ptit.oj.util.TextUtils;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.AtomicMoveNotSupportedException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.UUID;
import java.util.stream.Stream;

/**
 * Ghi mot bai tap moi ra o dia theo dung cau truc ma ProblemLoader doc duoc:
 *
 *   data/problems/P004/problem.properties
 *   data/problems/P004/statement.txt
 *   data/problems/P004/tests/sample01.in / .out / 01.in / 01.out ...
 *
 * Ghi theo kieu "tat ca hoac khong":
 *   1. tao thu muc tam _tmp_xxx NGAY BEN TRONG data/problems (cung o dia nen
 *      doi ten la thao tac nguyen tu, khong phai copy qua phan vung khac),
 *   2. ghi day du moi file,
 *   3. doi ten thu muc tam thanh ma bai that.
 * Neu buoc nao hong thi thu muc tam bi xoa, khong de lai bai tap do dang.
 */
public class ProblemWriter {

    /** ProblemLoader bo qua cac thu muc bat dau bang tien to nay. */
    public static final String TEMP_PREFIX = "_tmp_";

    private final Path problemsDir;

    public ProblemWriter(Path problemsDir) {
        this.problemsDir = problemsDir;
    }

    public Path getProblemsDir() { return problemsDir; }

    public boolean exists(String problemId) {
        return Files.isDirectory(problemsDir.resolve(problemId));
    }

    /**
     * Ghi ban thao ra o dia va tra ve thu muc chinh thuc cua bai.
     * Nguoi goi phai kiem tra hop le TRUOC (xem ProblemAdminService).
     */
    public Path write(ProblemDraft draft) throws IOException {
        Files.createDirectories(problemsDir);
        Path target = problemsDir.resolve(draft.getId());
        if (Files.exists(target)) {
            throw new IOException("Thư mục bài " + draft.getId() + " đã tồn tại");
        }

        Path temp = problemsDir.resolve(TEMP_PREFIX + UUID.randomUUID().toString().substring(0, 8));
        try {
            Files.createDirectory(temp);
            writeText(temp.resolve("problem.properties"), buildProperties(draft));
            writeText(temp.resolve("statement.txt"), draft.getStatement());

            Path testsDir = temp.resolve("tests");
            Files.createDirectory(testsDir);
            for (ProblemDraft.TestDraft t : draft.getTests()) {
                writeText(testsDir.resolve(t.getName() + ".in"), t.getInput());
                writeText(testsDir.resolve(t.getName() + ".out"), t.getOutput());
            }

            moveDirectory(temp, target);
            return target;
        } catch (IOException | RuntimeException e) {
            deleteRecursively(temp);
            throw e;
        }
    }

    /**
     * Sua vai khoa trong problem.properties cua mot bai DA CO, vi du topic / difficulty / order.
     * Gia tri null nghia la xoa dong do (giong write() bo qua topic rong hay difficulty = 0).
     *
     * Sua theo tung dong chu khong dung Properties.store(): moi dong khac giu nguyen,
     * ke ca dong ghi chu dau file ma tools/kids-problems/build.py dung de nhan ra bai
     * do no sinh - mat dong do thi lan chay build.py sau se dung lai vi tuong bai viet tay.
     *
     * Ghi ra file tam canh ben roi doi ten de len file cu, nen problem.properties
     * hoac con nguyen ban cu hoac da la ban moi, khong bao gio bi ghi do dang.
     */
    public Path updateProperties(String problemId, Map<String, String> changes) throws IOException {
        Path dir = problemsDir.resolve(problemId);
        Path file = dir.resolve("problem.properties");
        if (!Files.isRegularFile(file)) {
            throw new IOException("Không thấy " + file);
        }
        String text = TextUtils.stripBom(new String(Files.readAllBytes(file), StandardCharsets.UTF_8));
        String newline = text.contains("\r\n") ? "\r\n" : "\n";
        String[] lines = text.split("\r?\n", -1);

        List<String> out = new ArrayList<>();
        Set<String> done = new HashSet<>();
        for (int i = 0; i < lines.length; i++) {
            String key = propertyKey(lines[i]);
            if (key != null && changes.containsKey(key)) {
                // Bo dong cu cung cac dong noi tiep cua no (dong ket thuc bang dau \ le).
                while (continuesOnNextLine(lines[i]) && i + 1 < lines.length) i++;
                String value = changes.get(key);
                if (done.add(key) && value != null) out.add(key + "=" + escapeProperty(value));
                continue;
            }
            out.add(lines[i]);
            // Dong noi tiep cua mot khoa khac: chep nguyen, khong doc nham thanh khoa moi.
            while (key != null && continuesOnNextLine(lines[i]) && i + 1 < lines.length) {
                out.add(lines[++i]);
            }
        }

        // Khoa chua co trong file thi them vao cuoi, truoc dong trong ket thuc file.
        int insertAt = !out.isEmpty() && out.get(out.size() - 1).isEmpty() ? out.size() - 1 : out.size();
        for (Map.Entry<String, String> e : changes.entrySet()) {
            if (e.getValue() != null && !done.contains(e.getKey())) {
                out.add(insertAt++, e.getKey() + "=" + escapeProperty(e.getValue()));
            }
        }
        if (out.isEmpty() || !out.get(out.size() - 1).isEmpty()) out.add("");

        Path temp = dir.resolve(TEMP_PREFIX + UUID.randomUUID().toString().substring(0, 8) + ".properties");
        try {
            writeText(temp, String.join(newline, out));
            replaceFile(temp, file);
        } catch (IOException | RuntimeException e) {
            Files.deleteIfExists(temp);
            throw e;
        }
        return dir;
    }

    /** Ten khoa cua mot dong .properties, hoac null neu la dong trong / ghi chu. */
    private static String propertyKey(String line) {
        int i = 0;
        while (i < line.length() && isPropertySpace(line.charAt(i))) i++;
        if (i == line.length() || line.charAt(i) == '#' || line.charAt(i) == '!') return null;
        StringBuilder key = new StringBuilder();
        for (; i < line.length(); i++) {
            char c = line.charAt(i);
            if (c == '\\' && i + 1 < line.length()) {
                key.append(line.charAt(++i));
            } else if (c == '=' || c == ':' || isPropertySpace(c)) {
                break;
            } else {
                key.append(c);
            }
        }
        return key.toString();
    }

    private static boolean isPropertySpace(char c) {
        return c == ' ' || c == '\t' || c == '\f';
    }

    /** Dong ket thuc bang so le dau \ thi gia tri con tiep o dong sau. */
    private static boolean continuesOnNextLine(String line) {
        int slashes = 0;
        for (int i = line.length() - 1; i >= 0 && line.charAt(i) == '\\'; i--) slashes++;
        return slashes % 2 == 1;
    }

    /**
     * Noi dung problem.properties. Escape ky tu dac biet cua dinh dang .properties
     * de tieu de co dau ':' hay '=' khong lam hong file.
     */
    private String buildProperties(ProblemDraft d) {
        StringBuilder sb = new StringBuilder();
        sb.append("# Sinh tu giao dien quan tri (POST /api/admin/problems)\n");
        sb.append("id=").append(escapeProperty(d.getId())).append('\n');
        sb.append("title=").append(escapeProperty(d.getTitle())).append('\n');
        sb.append("timeLimitMs=").append(d.getTimeLimitMs()).append('\n');
        sb.append("memoryLimitMb=").append(d.getMemoryLimitMb()).append('\n');
        sb.append("comparator=").append(escapeProperty(d.getComparator())).append('\n');
        sb.append("totalPoints=").append(formatPoints(d.getTotalPoints())).append('\n');
        if (d.getTopic() != null && !d.getTopic().isEmpty()) {
            sb.append("topic=").append(escapeProperty(d.getTopic())).append('\n');
        }
        if (d.getDifficulty() > 0) {
            sb.append("difficulty=").append(d.getDifficulty()).append('\n');
        }
        return sb.toString();
    }

    private String formatPoints(double points) {
        if (points == Math.rint(points) && Math.abs(points) < 1e15) return String.valueOf((long) points);
        return String.valueOf(points);
    }

    /** Trong file .properties cac ky tu = : # ! va dau xuong dong phai duoc escape. */
    private String escapeProperty(String value) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < value.length(); i++) {
            char c = value.charAt(i);
            switch (c) {
                case '=':  sb.append("\\="); break;
                case ':':  sb.append("\\:"); break;
                case '#':  sb.append("\\#"); break;
                case '!':  sb.append("\\!"); break;
                case '\\': sb.append("\\\\"); break;
                case '\n': sb.append("\\n"); break;
                case '\r': break;
                default:   sb.append(c);
            }
        }
        return sb.toString();
    }

    /** Moi file deu ghi UTF-8 - ProblemLoader cung doc UTF-8. */
    private void writeText(Path file, String content) throws IOException {
        Files.write(file, (content == null ? "" : content).getBytes(StandardCharsets.UTF_8));
    }

    private void moveDirectory(Path from, Path to) throws IOException {
        try {
            Files.move(from, to, StandardCopyOption.ATOMIC_MOVE);
        } catch (AtomicMoveNotSupportedException e) {
            Files.move(from, to);       // vai he thong file khong ho tro doi ten nguyen tu
        }
    }

    private void replaceFile(Path from, Path to) throws IOException {
        try {
            Files.move(from, to, StandardCopyOption.REPLACE_EXISTING, StandardCopyOption.ATOMIC_MOVE);
        } catch (AtomicMoveNotSupportedException e) {
            Files.move(from, to, StandardCopyOption.REPLACE_EXISTING);
        }
    }

    private void deleteRecursively(Path dir) {
        if (dir == null || !Files.exists(dir)) return;
        try (Stream<Path> walk = Files.walk(dir)) {
            walk.sorted(Comparator.reverseOrder()).forEach(p -> {
                try {
                    Files.deleteIfExists(p);
                } catch (IOException ignored) {
                    // don dep het suc; file con lai se mang tien to _tmp_ nen bi bo qua khi nap
                }
            });
        } catch (IOException ignored) {
            // bo qua
        }
    }
}
