package com.ptit.oj.repository;

import com.ptit.oj.exception.ProblemLoadException;
import com.ptit.oj.model.Topic;
import com.ptit.oj.util.TextUtils;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.regex.Pattern;

/**
 * Doc lo trinh hoc tu data/topics.txt. Moi dong mot chu de, theo dung thu tu hoc:
 *
 *   # dong bat dau bang # la ghi chu
 *   vong-lap | Vong lap | Lap lai mot viec nhieu lan voi for va while.
 *
 * Khong co file thi tra ve danh sach rong: lo trinh la tuy chon, he thong
 * van chay nhu cu (moi bai nam o nhom "Bai khac").
 */
public class TopicLoader {

    /** Ma chu de: chu thuong khong dau, so va gach ngang -> an toan khi dat trong URL / properties. */
    public static final Pattern ID_PATTERN = Pattern.compile("[a-z0-9-]{1,40}");

    private final Path file;

    public TopicLoader(Path file) {
        this.file = file;
    }

    public List<Topic> loadAll() {
        List<Topic> topics = new ArrayList<>();
        if (!Files.isRegularFile(file)) return topics;

        String text;
        try {
            text = TextUtils.stripBom(new String(Files.readAllBytes(file), StandardCharsets.UTF_8));
        } catch (IOException e) {
            throw new ProblemLoadException("Không đọc được " + file, e);
        }

        Set<String> seen = new HashSet<>();
        int lineNo = 0;
        for (String raw : text.split("\r?\n")) {
            lineNo++;
            String line = raw.trim();
            if (line.isEmpty() || line.startsWith("#")) continue;

            String[] parts = line.split("\\|", 3);
            String id = parts[0].trim();
            String name = parts.length > 1 ? parts[1].trim() : "";
            String description = parts.length > 2 ? parts[2].trim() : "";
            String where = file.getFileName() + " dòng " + lineNo;

            if (!ID_PATTERN.matcher(id).matches()) {
                throw new ProblemLoadException(where + ": mã chủ đề \"" + id
                        + "\" chỉ được gồm chữ thường không dấu, số và gạch ngang");
            }
            if (name.isEmpty()) {
                throw new ProblemLoadException(where + ": thiếu tên chủ đề (cú pháp: ma | Tên | Mô tả)");
            }
            if (!seen.add(id)) {
                throw new ProblemLoadException(where + ": mã chủ đề \"" + id + "\" bị trùng");
            }
            topics.add(new Topic(id, name, description, topics.size() + 1));
        }
        return topics;
    }
}
