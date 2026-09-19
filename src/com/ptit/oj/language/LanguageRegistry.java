package com.ptit.oj.language;

import java.nio.file.Path;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

/**
 * FACTORY / REGISTRY: noi duy nhat biet danh sach ngon ngu duoc ho tro.
 * Them ngon ngu moi = 1 lop con Language + 1 dong register() (Open/Closed Principle).
 */
public class LanguageRegistry {

    private final Map<String, Language> byExtension = new LinkedHashMap<>();

    public LanguageRegistry() {
        register(new JavaLanguage());        // ngon ngu chinh cua bai tap lon
        register(new CppLanguage());
        register(new PythonLanguage());
        register(new GoLanguage());
        register(new JavaScriptLanguage());
        register(new RustLanguage());
    }

    public void register(Language language) {
        byExtension.put(language.getFileExtension().toLowerCase(), language);
    }

    /** Nhan dien ngon ngu tu duoi file ma nguon. */
    public Optional<Language> detect(Path sourceFile) {
        String name = sourceFile.getFileName().toString().toLowerCase();
        int dot = name.lastIndexOf('.');
        if (dot < 0) return Optional.empty();
        return Optional.ofNullable(byExtension.get(name.substring(dot)));
    }

    public Optional<Language> byName(String name) {
        for (Language l : byExtension.values()) {
            if (l.getName().equalsIgnoreCase(name)) return Optional.of(l);
        }
        return Optional.empty();
    }

    public List<Language> all() {
        return new ArrayList<>(byExtension.values());
    }
}
