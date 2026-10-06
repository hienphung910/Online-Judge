package com.ptit.oj.service;

import com.ptit.oj.compare.ComparatorFactory;
import com.ptit.oj.model.Problem;
import com.ptit.oj.model.User;
import com.ptit.oj.repository.ProblemDraft;
import com.ptit.oj.repository.ProblemLoader;
import com.ptit.oj.repository.ProblemWriter;
import com.ptit.oj.repository.Repository;

import java.io.IOException;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Set;
import java.util.function.Predicate;
import java.util.regex.Pattern;

/**
 * Nghiep vu quan tri de bai: kiem tra hop le -> ghi ra o dia -> nap vao bo nho.
 *
 * Tang web chi viec doc JSON roi goi createProblem(); moi luat kiem tra nam o day
 * nen console hay bat ky giao dien nao khac cung duoc bao ve giong het.
 */
public class ProblemAdminService {

    /** Ma bai: chi chu IN HOA, so, gach duoi va gach ngang -> khong the thanh duong dan. */
    private static final Pattern ID_PATTERN = Pattern.compile("[A-Z0-9_-]{1,32}");
    /** Ten test: chu thuong/hoa, so, gach duoi, gach ngang. Khong co dau cham hay dau gach cheo. */
    private static final Pattern TEST_NAME_PATTERN = Pattern.compile("[A-Za-z0-9_-]{1,64}");

    private static final long MIN_TIME_LIMIT_MS = 100;
    private static final long MAX_TIME_LIMIT_MS = 60_000;
    private static final int MIN_MEMORY_MB = 8;
    private static final int MAX_MEMORY_MB = 2048;
    private static final double MAX_TOTAL_POINTS = 100_000;
    private static final int MAX_TESTS = 200;
    private static final int MAX_TITLE = 200;
    private static final int MAX_STATEMENT = 200_000;
    private static final int MAX_TEST_CHARS = 1_000_000;

    private final Repository<Problem> problems;
    private final ProblemWriter writer;
    private final ProblemLoader loader;
    /** Hoi JudgeService xem ma chu de co trong lo trinh khong (lo trinh nap sau constructor). */
    private final Predicate<String> topicExists;

    public ProblemAdminService(Repository<Problem> problems, Path problemsDir, Predicate<String> topicExists) {
        this.problems = problems;
        this.writer = new ProblemWriter(problemsDir);
        this.loader = new ProblemLoader(problemsDir);
        this.topicExists = topicExists;
    }

    /** Loi nghiep vu kem ma HTTP goi y (400 sai du lieu, 403 thieu quyen, 409 trung ma bai). */
    public static class ProblemAdminException extends RuntimeException {
        private final int httpStatus;

        public ProblemAdminException(int httpStatus, String message) {
            super(message);
            this.httpStatus = httpStatus;
        }

        public int getHttpStatus() { return httpStatus; }
    }

    /**
     * Tao bai tap moi. Chi tai khoan co canCreateProblem() == true moi duoc goi
     * (tang web da chan truoc, day la lop chan thu hai - khong tin giao dien).
     */
    public synchronized Problem createProblem(User actor, ProblemDraft draft) {
        if (actor == null || !actor.canCreateProblem()) {
            throw new ProblemAdminException(403, "Chỉ tài khoản quản trị mới được tạo bài tập");
        }
        validate(draft);

        Path dir;
        try {
            dir = writer.write(draft);
        } catch (IOException e) {
            throw new ProblemAdminException(500, "Không ghi được bài tập ra ổ đĩa: " + e.getMessage());
        }

        // Nap lai tu chinh file vua ghi: bao dam thu muc tren o dia va du lieu
        // trong bo nho luon khop nhau, va bat som neu ghi ra thu bi loi.
        Problem problem = loader.load(dir);
        problems.save(problem);
        return problem;
    }

    /**
     * Doi chu de, do kho va vi tri trong lo trinh cua mot bai DA CO.
     *
     * position tinh tu 1 trong chu de dich, khong tinh chinh bai nay (lon hon so bai
     * thi xep cuoi). position = 0: giu cho cu neu van o chu de cu, xep cuoi neu doi chu de.
     *
     * Khi xep vi tri, ca chu de dich duoc danh so lai 1..n: neu chi ghi order cho
     * mot bai thi "vi tri 3" se nhay len dau, vi bai da xep luon dung truoc bai
     * chua xep (xem Problem.ORDER_IN_TOPIC). Chi ghi lai bai nao co so thu tu doi.
     */
    public synchronized Problem updateProblemMeta(User actor, String rawId, String rawTopic,
                                                  int difficulty, int position) {
        if (actor == null || !actor.canCreateProblem()) {
            throw new ProblemAdminException(403, "Chỉ tài khoản quản trị mới được sửa bài tập");
        }
        String id = normalizeId(rawId);
        Problem target = problems.findById(id)
                .orElseThrow(() -> new ProblemAdminException(404, "Không có bài " + id));
        String topic = validateTopic(rawTopic);
        validateDifficulty(difficulty);
        if (position < 0 || position > ProblemLoader.MAX_ORDER) {
            throw new ProblemAdminException(400,
                    "Vị trí phải từ 1 đến " + ProblemLoader.MAX_ORDER + " (0 = giữ nguyên)");
        }

        try {
            if (position == 0 && topic.equals(target.getTopic())) {
                // Khong doi cho: chi sua do kho (chu de giu nguyen), khong dung toi bai khac.
                return rewrite(id, metaChanges(topic, difficulty, target.getOrder()));
            }

            // Cac bai khac trong chu de dich, theo dung thu tu hoc hien tai.
            List<Problem> ordered = new ArrayList<>();
            for (Problem p : problems.findAll()) {
                if (!p.getId().equals(id) && p.getTopic().equals(topic)) ordered.add(p);
            }
            ordered.sort(Problem.ORDER_IN_TOPIC);
            int index = position == 0 ? ordered.size() : Math.min(position, ordered.size() + 1) - 1;
            ordered.add(index, target);

            // Ghi cac bai khac truoc, bai dang sua sau cung. Neu hong giua chung thi bai
            // dang sua van nhu cu, va thu tu van hop le vi luat "order roi ma bai" luon xep duoc.
            for (int i = 0; i < ordered.size(); i++) {
                Problem p = ordered.get(i);
                if (p != target && p.getOrder() != i + 1) {
                    rewrite(p.getId(), Collections.singletonMap("order", String.valueOf(i + 1)));
                }
            }
            return rewrite(id, metaChanges(topic, difficulty, index + 1));
        } catch (IOException e) {
            throw new ProblemAdminException(500, "Không ghi được bài tập ra ổ đĩa: " + e.getMessage());
        }
    }

    /** Ba khoa lo trinh cua problem.properties; null = xoa dong, giong khi tao bai. */
    private Map<String, String> metaChanges(String topic, int difficulty, int order) {
        Map<String, String> changes = new LinkedHashMap<>();
        changes.put("topic", topic.isEmpty() ? null : topic);
        changes.put("difficulty", difficulty > 0 ? String.valueOf(difficulty) : null);
        changes.put("order", order > 0 ? String.valueOf(order) : null);
        return changes;
    }

    /** Ghi ra o dia roi nap lai tu chinh file vua ghi, nhu createProblem(). */
    private Problem rewrite(String id, Map<String, String> changes) throws IOException {
        Problem problem = loader.load(writer.updateProperties(id, changes));
        problems.save(problem);
        return problem;
    }

    // ------------------------------------------------------------ kiem tra

    private void validate(ProblemDraft d) {
        String id = normalizeId(d.getId());
        d.setId(id);

        if (problems.findById(id).isPresent() || writer.exists(id)) {
            throw new ProblemAdminException(409, "Mã bài " + id + " đã tồn tại");
        }

        d.setTitle(requireText(d.getTitle(), "Tên bài", MAX_TITLE));
        d.setStatement(requireText(d.getStatement(), "Nội dung đề", MAX_STATEMENT));

        if (d.getTimeLimitMs() < MIN_TIME_LIMIT_MS || d.getTimeLimitMs() > MAX_TIME_LIMIT_MS) {
            throw new ProblemAdminException(400,
                    "Giới hạn thời gian phải từ " + MIN_TIME_LIMIT_MS + " đến " + MAX_TIME_LIMIT_MS + " ms");
        }
        if (d.getMemoryLimitMb() < MIN_MEMORY_MB || d.getMemoryLimitMb() > MAX_MEMORY_MB) {
            throw new ProblemAdminException(400,
                    "Giới hạn bộ nhớ phải từ " + MIN_MEMORY_MB + " đến " + MAX_MEMORY_MB + " MB");
        }
        if (!(d.getTotalPoints() > 0) || d.getTotalPoints() > MAX_TOTAL_POINTS) {
            throw new ProblemAdminException(400, "Tổng điểm phải lớn hơn 0 và tối đa " + (long) MAX_TOTAL_POINTS);
        }

        String comparator = d.getComparator() == null ? "token" : d.getComparator().trim();
        try {
            ComparatorFactory.create(comparator);       // nem neu kieu so sanh khong ho tro
        } catch (IllegalArgumentException e) {
            throw new ProblemAdminException(400, e.getMessage());
        }
        d.setComparator(comparator);

        d.setTopic(validateTopic(d.getTopic()));
        validateDifficulty(d.getDifficulty());

        if (d.getTests().isEmpty()) {
            throw new ProblemAdminException(400, "Bài tập phải có ít nhất một test");
        }
        if (d.getTests().size() > MAX_TESTS) {
            throw new ProblemAdminException(400, "Tối đa " + MAX_TESTS + " test cho một bài");
        }

        Set<String> seen = new LinkedHashSet<>();
        for (ProblemDraft.TestDraft t : d.getTests()) {
            validateTest(t, seen);
        }
    }

    /** Tra ve ma chu de da cat khoang trang; "" = chua phan loai (nhom "Bai khac"). */
    private String validateTopic(String rawTopic) {
        String topic = rawTopic == null ? "" : rawTopic.trim();
        if (!topic.isEmpty() && !topicExists.test(topic)) {
            throw new ProblemAdminException(400, "Chủ đề \"" + topic + "\" không có trong lộ trình (data/topics.txt)");
        }
        return topic;
    }

    private void validateDifficulty(int difficulty) {
        if (difficulty < 0 || difficulty > 3) {
            throw new ProblemAdminException(400, "Độ khó phải là 1 (Dễ), 2 (Vừa), 3 (Khó) hoặc 0 (chưa đánh giá)");
        }
    }

    private void validateTest(ProblemDraft.TestDraft t, Set<String> seen) {
        String name = t.getName() == null ? "" : t.getName().trim();
        if (name.isEmpty()) {
            throw new ProblemAdminException(400, "Tên test không được để trống");
        }
        // Chan truoc cac dang duong dan de thong bao loi noi dung ro rang.
        if (name.contains("..") || name.contains("/") || name.contains("\\")) {
            throw new ProblemAdminException(400, "Tên test \"" + name + "\" chứa ký tự đường dẫn");
        }
        if (!TEST_NAME_PATTERN.matcher(name).matches()) {
            throw new ProblemAdminException(400,
                    "Tên test \"" + name + "\" chỉ được gồm chữ, số, gạch dưới hoặc gạch ngang");
        }
        // He thong file cua Windows khong phan biet hoa thuong -> "01" va "01" phai coi la trung.
        if (!seen.add(name.toLowerCase(Locale.ROOT))) {
            throw new ProblemAdminException(400, "Tên test \"" + name + "\" bị trùng");
        }

        boolean looksSample = name.toLowerCase(Locale.ROOT).startsWith("sample");
        if (!t.isSample() && looksSample) {
            throw new ProblemAdminException(400,
                    "Test ẩn không được đặt tên bắt đầu bằng \"sample\" (tên này dành cho test ví dụ)");
        }
        if (t.isSample() && !looksSample) {
            throw new ProblemAdminException(400,
                    "Test ví dụ phải có tên bắt đầu bằng \"sample\", ví dụ sample01");
        }

        requireText(t.getInput(), "Input của test " + name, MAX_TEST_CHARS);
        requireText(t.getOutput(), "Output của test " + name, MAX_TEST_CHARS);
    }

    private String normalizeId(String rawId) {
        String id = rawId == null ? "" : rawId.trim().toUpperCase(Locale.ROOT);
        if (id.isEmpty()) {
            throw new ProblemAdminException(400, "Thiếu mã bài");
        }
        if (id.contains("..") || id.contains("/") || id.contains("\\")) {
            throw new ProblemAdminException(400, "Mã bài chứa ký tự đường dẫn không hợp lệ");
        }
        if (!ID_PATTERN.matcher(id).matches()) {
            throw new ProblemAdminException(400,
                    "Mã bài chỉ được gồm chữ in hoa, số, gạch dưới hoặc gạch ngang (tối đa 32 ký tự)");
        }
        return id;
    }

    private String requireText(String value, String label, int max) {
        String v = value == null ? "" : value;
        if (v.trim().isEmpty()) {
            throw new ProblemAdminException(400, label + " không được để trống");
        }
        if (v.length() > max) {
            throw new ProblemAdminException(400, label + " quá dài (tối đa " + max + " ký tự)");
        }
        return v;
    }
}
