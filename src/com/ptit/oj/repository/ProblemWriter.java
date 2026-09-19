package com.ptit.oj.repository;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.AtomicMoveNotSupportedException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.Comparator;
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
