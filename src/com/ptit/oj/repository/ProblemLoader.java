package com.ptit.oj.repository;

import com.ptit.oj.exception.ProblemLoadException;
import com.ptit.oj.model.Problem;
import com.ptit.oj.model.TestCase;
import com.ptit.oj.util.TextUtils;

import java.io.IOException;
import java.io.Reader;
import java.io.StringReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Properties;

/**
 * Doc de bai va bo test tu o dia. Cau truc mot bai:
 *
 *   data/problems/P001/
 *       problem.properties   (id, title, timeLimitMs, memoryLimitMb, comparator, totalPoints)
 *       statement.txt        (de bai, tuy chon)
 *       tests/01.in  01.out  02.in  02.out ...
 *
 * Test co ten bat dau bang "sample" duoc coi la test vi du (hien thi cho thi sinh).
 */
public class ProblemLoader {

    private final Path problemsDir;

    public ProblemLoader(Path problemsDir) {
        this.problemsDir = problemsDir;
    }

    /** Doc toan bo cac bai trong thu muc, sap xep theo ma bai. */
    public List<Problem> loadAll() {
        if (!Files.isDirectory(problemsDir)) {
            throw new ProblemLoadException("Không thấy thư mục đề bài: " + problemsDir.toAbsolutePath());
        }
        List<Problem> problems = new ArrayList<>();
        try (DirectoryStream<Path> dirs = Files.newDirectoryStream(problemsDir, Files::isDirectory)) {
            for (Path dir : dirs) {
                // Bo qua thu muc tam do ProblemWriter dang dung de ghi bai moi,
                // va cac thu muc an cua he thong / IDE.
                String name = dir.getFileName().toString();
                if (name.startsWith(ProblemWriter.TEMP_PREFIX) || name.startsWith(".")) continue;
                problems.add(load(dir));
            }
        } catch (IOException e) {
            throw new ProblemLoadException("Lỗi đọc thư mục đề bài", e);
        }
        problems.sort((a, b) -> a.getId().compareTo(b.getId()));
        return problems;
    }

    /** Doc mot bai tu thu muc cua no. */
    public Problem load(Path dir) {
        Path configFile = dir.resolve("problem.properties");
        if (!Files.isRegularFile(configFile)) {
            throw new ProblemLoadException("Thiếu problem.properties trong " + dir);
        }
        Properties config = new Properties();
        // Doc bang UTF-8 (khong dung Properties.load(InputStream) vi ban do mac dinh ISO-8859-1
        // se lam sai tieng Viet co dau trong title), dong thoi loc BOM neu co.
        try (Reader reader = new StringReader(readText(configFile))) {
            config.load(reader);
        } catch (IOException e) {
            throw new ProblemLoadException("Không đọc được " + configFile, e);
        }

        String id = config.getProperty("id", dir.getFileName().toString()).trim();
        String title = config.getProperty("title", id).trim();
        long timeLimit = parseLong(config.getProperty("timeLimitMs"), 2000);
        int memoryLimit = (int) parseLong(config.getProperty("memoryLimitMb"), 256);
        String comparator = config.getProperty("comparator", "token").trim();
        double totalPoints = parseDouble(config.getProperty("totalPoints"), 100);
        String statement = readTextIfExists(dir.resolve("statement.txt"));

        Problem problem = new Problem(id, title, statement, timeLimit, memoryLimit, comparator);

        List<Path> inputs = listInputs(dir.resolve("tests"));
        if (inputs.isEmpty()) {
            throw new ProblemLoadException("Bài " + id + " không có test nào trong tests/");
        }
        double pointsPerTest = totalPoints / inputs.size();

        for (Path in : inputs) {
            String base = in.getFileName().toString().replaceAll("\\.in$", "");
            Path out = in.getParent().resolve(base + ".out");
            if (!Files.isRegularFile(out)) {
                throw new ProblemLoadException("Thiếu file đáp án cho test " + in.getFileName());
            }
            boolean sample = base.toLowerCase().startsWith("sample");
            problem.addTestCase(new TestCase(base, readText(in), readText(out), pointsPerTest, sample));
        }
        return problem;
    }

    private List<Path> listInputs(Path testsDir) {
        if (!Files.isDirectory(testsDir)) return Collections.emptyList();
        List<Path> inputs = new ArrayList<>();
        try (DirectoryStream<Path> files = Files.newDirectoryStream(testsDir, "*.in")) {
            for (Path f : files) inputs.add(f);
        } catch (IOException e) {
            throw new ProblemLoadException("Lỗi đọc thư mục test " + testsDir, e);
        }
        // Test vi du (sample*) chay truoc, sau do den cac test an, moi nhom sap theo ten.
        inputs.sort((a, b) -> {
            String na = a.getFileName().toString().toLowerCase();
            String nb = b.getFileName().toString().toLowerCase();
            int ra = na.startsWith("sample") ? 0 : 1;
            int rb = nb.startsWith("sample") ? 0 : 1;
            return ra != rb ? Integer.compare(ra, rb) : na.compareTo(nb);
        });
        return inputs;
    }

    private String readText(Path file) {
        try {
            // stripBom: file test tao bang Notepad co BOM se lam sai ket qua so sanh
            return TextUtils.stripBom(new String(Files.readAllBytes(file), StandardCharsets.UTF_8));
        } catch (IOException e) {
            throw new ProblemLoadException("Không đọc được file " + file, e);
        }
    }

    private String readTextIfExists(Path file) {
        return Files.isRegularFile(file) ? readText(file) : "";
    }

    private long parseLong(String value, long fallback) {
        try {
            return value == null ? fallback : Long.parseLong(value.trim());
        } catch (NumberFormatException e) {
            return fallback;
        }
    }

    private double parseDouble(String value, double fallback) {
        try {
            return value == null ? fallback : Double.parseDouble(value.trim());
        } catch (NumberFormatException e) {
            return fallback;
        }
    }
}
