package com.ptit.oj.model;

import com.ptit.oj.language.Language;

import java.nio.file.Path;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.UUID;

/** Mot lan nop bai cua nguoi dung. */
public class Submission extends Entity {

    private static final DateTimeFormatter FMT = DateTimeFormatter.ofPattern("HH:mm:ss dd/MM/yyyy");

    private final Problem problem;
    private final User author;
    private final Language language;
    private final Path sourcePath;
    private final LocalDateTime submittedAt;
    private JudgeResult result;   // duoc gan sau khi cham
    private String sourceCode;    // ma nguon that, duoc luu lai trong CSDL

    /** Tao bai nop moi (sinh ma va moc thoi gian ngay tai day). */
    public Submission(Problem problem, User author, Language language, Path sourcePath) {
        this(newId(), problem, author, language, sourcePath, LocalDateTime.now());
    }

    /**
     * Dung lai mot bai nop da luu trong CSDL (repository goi ham nay).
     * Ma va thoi diem nop lay tu CSDL nen khong duoc sinh moi.
     */
    public Submission(String id, Problem problem, User author, Language language,
                      Path sourcePath, LocalDateTime submittedAt) {
        super(id);
        this.problem = problem;
        this.author = author;
        this.language = language;
        this.sourcePath = sourcePath;
        this.submittedAt = submittedAt;
    }

    /**
     * Ma bai nop duy nhat qua moi lan khoi dong lai chuong trinh.
     * Truoc day dung AtomicInteger nen mo lai la quay ve SUB1001 va de trung
     * voi ban ghi cu trong CSDL; UUID khong co van de do.
     */
    public static String newId() {
        return "SUB-" + UUID.randomUUID().toString().replace("-", "").toUpperCase(Locale.ROOT);
    }

    public Problem getProblem() { return problem; }
    public User getAuthor() { return author; }
    public Language getLanguage() { return language; }
    public Path getSourcePath() { return sourcePath; }
    public LocalDateTime getSubmittedAt() { return submittedAt; }

    public JudgeResult getResult() { return result; }
    public void setResult(JudgeResult result) { this.result = result; }

    public String getSourceCode() { return sourceCode; }
    public void setSourceCode(String sourceCode) { this.sourceCode = sourceCode; }

    public boolean isJudged() { return result != null; }

    public Verdict getVerdict() {
        return result == null ? null : result.getOverallVerdict();
    }

    @Override
    public String describe() {
        String verdict = result == null ? "Chờ chấm" : result.getOverallVerdict().getCode();
        return String.format("%s | %s | %-5s | %-6s | %-4s | %s",
                getId(), submittedAt.format(FMT), problem.getId(),
                language.getName(), verdict, author.getUsername());
    }
}
