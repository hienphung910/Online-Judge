import { useMemo, useState } from "react";
import { api } from "../api";
import { useAuth } from "../auth";
import CodeEditor from "../components/CodeEditor";
import TestSummary from "../components/TestSummary";
import { Button, ErrorBox, MONO, Panel, SampleBox, Select, VerdictBadge } from "../components/ui";
import type { JudgeFinishedEvent, LanguageInfo, LiveTestEvent, Problem, Submission } from "../types";

/** Code mẫu giải bài A+B cho từng ngôn ngữ - tiện khi thử nhanh. */
const TEMPLATES: Record<string, string> = {
  Java: `import java.util.Scanner;\n\npublic class Solution {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        long a = sc.nextLong();\n        long b = sc.nextLong();\n        System.out.println(a + b);\n    }\n}\n`,
  "C++": `#include <iostream>\n\nint main() {\n    long long a, b;\n    std::cin >> a >> b;\n    std::cout << a + b << std::endl;\n    return 0;\n}\n`,
  Python: `import sys\n\ndata = sys.stdin.read().split()\nprint(int(data[0]) + int(data[1]))\n`,
  Go: `package main\n\nimport "fmt"\n\nfunc main() {\n\tvar a, b int64\n\tfmt.Scan(&a, &b)\n\tfmt.Println(a + b)\n}\n`,
  JavaScript: `const data = require("fs").readFileSync(0, "utf8").trim().split(/\\s+/);\nconsole.log((BigInt(data[0]) + BigInt(data[1])).toString());\n`,
  Rust: `use std::io::Read;\n\nfn main() {\n    let mut input = String::new();\n    std::io::stdin().read_to_string(&mut input).unwrap();\n    let nums: Vec<i64> = input.split_whitespace().map(|x| x.parse().unwrap()).collect();\n    println!("{}", nums[0] + nums[1]);\n}\n`,
};

interface LiveState {
  total: number;
  compiled: "waiting" | "ok" | "failed";
  compileMessage: string;
  tests: LiveTestEvent[];
  finished: JudgeFinishedEvent | null;
}
const EMPTY_LIVE: LiveState = { total: 0, compiled: "waiting", compileMessage: "", tests: [], finished: null };

export default function ProblemDetail({
  problem,
  languages,
  onBack,
  onSubmitted,
}: {
  problem: Problem;
  languages: LanguageInfo[];
  onBack: () => void;
  onSubmitted: () => void;
}) {
  const { user, refresh } = useAuth();
  const [language, setLanguage] = useState(languages[0]?.name ?? "Java");
  const [code, setCode] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState<Submission | null>(null);
  const [live, setLive] = useState<LiveState>(EMPTY_LIVE);

  const langNames = useMemo(() => languages.map((l) => l.name), [languages]);
  const unavailable = useMemo(() => languages.filter((l) => !l.available).map((l) => l.name), [languages]);
  const currentLang = languages.find((l) => l.name === language);

  async function doSubmit() {
    setError("");
    setResult(null);
    setLive(EMPTY_LIVE);
    if (!language) return setError("Chưa chọn ngôn ngữ.");
    if (!code.trim()) return setError("Mã nguồn đang rỗng.");

    setBusy(true);
    try {
      await api.submitStream({ problemId: problem.id, language, code }, (event) => {
        switch (event.type) {
          case "started":
            setLive((s) => ({ ...s, total: event.data.total }));
            break;
          case "compiled":
            setLive((s) => ({ ...s, compiled: event.data.success ? "ok" : "failed", compileMessage: event.data.message }));
            break;
          case "test":
            setLive((s) => ({ ...s, total: event.data.total, tests: [...s.tests, event.data] }));
            break;
          case "finished":
            setLive((s) => ({ ...s, finished: event.data }));
            break;
          case "done":
            setResult(event.data);
            onSubmitted();
            void refresh();
            break;
          case "error":
            setError(event.data.error);
            break;
        }
      });
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setBusy(false);
    }
  }

  const shownTests = result?.tests ?? live.tests;
  const totalTests = result?.total ?? live.total;
  const passedTests = result?.passed ?? shownTests.filter((t) => t.verdict === "AC").length;
  const progress = totalTests > 0 ? Math.round((shownTests.length / totalTests) * 100) : 0;

  return (
    <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden", padding: "0 32px 24px" }}>
      <div style={{ paddingTop: 20, paddingBottom: 16, display: "flex", alignItems: "center", gap: 10, flexShrink: 0 }}>
        <button onClick={onBack} style={{ display: "flex", alignItems: "center", gap: 6, background: "none", border: "1px solid var(--color-border)", borderRadius: 7, height: 32, padding: "0 12px", color: "var(--color-text-secondary)", fontSize: 12.5, cursor: "pointer", fontFamily: "var(--font-sans)" }}>
          <svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><polyline points="7 2 3 6 7 10" /></svg>
          Danh sách bài
        </button>
        <h1 style={{ fontFamily: "var(--font-serif)", fontSize: 22, fontWeight: 700, color: "var(--color-maroon)", margin: 0, letterSpacing: "-0.02em" }}>
          {problem.id} — {problem.title}
        </h1>
      </div>

      <div style={{ flex: 1, overflow: "hidden", display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16 }}>
        {/* Cột trái: đề bài */}
        <Panel title="Đề bài" style={{ overflow: "hidden" }}>
          <div style={{ padding: 16, display: "flex", flexDirection: "column", gap: 14, overflowY: "auto" }}>
            <pre style={{ margin: 0, whiteSpace: "pre-wrap", fontFamily: "var(--font-sans)", fontSize: 13.5, lineHeight: 1.75, color: "var(--color-text-secondary)" }}>
              {problem.statement || "(Đề bài chưa có statement.txt)"}
            </pre>

            <div style={{ display: "flex", gap: 16, flexWrap: "wrap", ...MONO, fontSize: 11.5, color: "var(--color-text-muted)" }}>
              <span>Thời gian: <b style={{ color: "var(--color-text-secondary)" }}>{problem.timeLimitMs} ms</b></span>
              <span>Bộ nhớ: <b style={{ color: "var(--color-text-secondary)" }}>{problem.memoryLimitMb} MB</b></span>
              <span>Tổng điểm: <b style={{ color: "var(--color-text-secondary)" }}>{problem.maxPoints.toFixed(0)}</b></span>
            </div>

            {problem.samples.map((s, i) => (
              <div key={i} style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
                <SampleBox label={`Input ví dụ ${i + 1}`} text={s.input} />
                <SampleBox label={`Output ví dụ ${i + 1}`} text={s.output} />
              </div>
            ))}
          </div>
        </Panel>

        {/* Cột phải: nộp bài + kết quả */}
        <div style={{ display: "flex", flexDirection: "column", gap: 14, minWidth: 0, overflowY: "auto" }}>
          <Panel title="Nộp bài" right={<span style={{ ...MONO, fontSize: 11, color: "var(--color-text-muted)" }}>@{user?.username}</span>}>
            <div style={{ padding: 14, display: "flex", flexDirection: "column", gap: 12 }}>
              <div style={{ display: "flex", gap: 10, flexWrap: "wrap", alignItems: "center" }}>
                <Select value={language} options={langNames} onChange={setLanguage} placeholder="Chọn ngôn ngữ" disabledOptions={unavailable} />
                <Button onClick={() => setCode(TEMPLATES[language] ?? "")} disabled={!TEMPLATES[language]}>Chèn code mẫu A+B</Button>
                <div style={{ flex: 1 }} />
                <Button variant="primary" onClick={() => void doSubmit()} disabled={busy}>{busy ? "Đang chấm..." : "Nộp và chấm"}</Button>
              </div>

              {currentLang && !currentLang.available && (
                <div style={{ ...MONO, fontSize: 11.5, color: "var(--color-amber)" }}>
                  Máy này chưa cài toolchain cho {currentLang.name} — chọn ngôn ngữ khác hoặc cài thêm.
                </div>
              )}

              <CodeEditor value={code} language={language} onChange={setCode} />

              <div style={{ ...MONO, fontSize: 11, color: "var(--color-text-muted)" }}>
                {currentLang?.memoryLimitNote ? `Giới hạn bộ nhớ: ${currentLang.memoryLimitNote}` : ""}
              </div>
            </div>
          </Panel>

          <Panel
            title="Kết quả chấm"
            right={
              result ? <span style={{ ...MONO, fontSize: 11, color: "var(--color-text-muted)" }}>{result.id}</span>
              : busy ? <span style={{ ...MONO, fontSize: 11, color: "var(--color-maroon)", animation: "livePulse 1.2s infinite" }}>● đang chấm trực tiếp</span>
              : null
            }
          >
            {error && <ErrorBox message={error} />}

            {!error && !busy && !result && (
              <div style={{ padding: 18, ...MONO, fontSize: 12, color: "var(--color-text-muted)", lineHeight: 1.8 }}>
                Dán code rồi bấm "Nộp và chấm". Kết quả cập nhật ngay khi máy chủ chấm xong từng test.
              </div>
            )}

            {(busy || result) && !error && (
              <div style={{ padding: 14, display: "flex", flexDirection: "column", gap: 12 }}>
                <ProgressStrip busy={busy} compiled={live.compiled} done={shownTests.length} total={totalTests} percent={progress} />

                <div style={{ display: "flex", alignItems: "center", gap: 12, flexWrap: "wrap" }}>
                  <VerdictBadge verdict={result?.verdict ?? "PENDING"} size={13} />
                  {live.compiled === "ok" && (
                    <span style={{ ...MONO, fontSize: 13, color: "var(--color-text-primary)" }}>Đúng {passedTests}/{totalTests || "?"} test</span>
                  )}
                  {result && (
                    <span style={{ ...MONO, fontSize: 13, color: "var(--color-green)" }}>{(result.score ?? 0).toFixed(1)}/{result.maxPoints.toFixed(0)} điểm</span>
                  )}
                  {result && live.compiled === "ok" && result.execTimeMs !== null && (
                    <span style={{ ...MONO, fontSize: 12, color: "var(--color-text-muted)" }}>test lâu nhất {result.execTimeMs} ms</span>
                  )}
                </div>

                <TestSummary tests={shownTests} size={13} />

                {result && (
                  <div style={{ ...MONO, fontSize: 11, color: "var(--color-text-muted)" }}>File biên dịch: {result.fileName} · ngôn ngữ {result.language}</div>
                )}

                {(live.compiled === "failed" || result?.message) && (
                  <pre style={{ margin: 0, padding: "10px 12px", background: "var(--color-bg-base)", border: "1px solid var(--color-red-border)", borderRadius: 6, fontFamily: "var(--font-mono)", fontSize: 11.5, color: "var(--color-text-secondary)", whiteSpace: "pre-wrap", maxHeight: 200, overflow: "auto" }}>
                    {result?.message || live.compileMessage}
                  </pre>
                )}
              </div>
            )}
          </Panel>
        </div>
      </div>
    </div>
  );
}

function ProgressStrip({ busy, compiled, done, total, percent }: { busy: boolean; compiled: "waiting" | "ok" | "failed"; done: number; total: number; percent: number }) {
  const compileLabel = compiled === "waiting" ? "đang biên dịch..." : compiled === "ok" ? "biên dịch OK" : "biên dịch THẤT BẠI";
  const compileColor = compiled === "waiting" ? "var(--color-text-muted)" : compiled === "ok" ? "var(--color-green)" : "var(--color-red)";
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
      <div style={{ display: "flex", alignItems: "center", gap: 12, ...MONO, fontSize: 11.5 }}>
        <span style={{ color: compileColor }}>{compileLabel}</span>
        {compiled === "ok" && <span style={{ color: "var(--color-text-secondary)" }}>test {done}/{total || "?"}</span>}
        <div style={{ flex: 1 }} />
        {busy && <span style={{ color: "var(--color-text-muted)", animation: "livePulse 1.2s infinite" }}>máy chủ đang chạy...</span>}
      </div>
      <div style={{ height: 4, borderRadius: 2, background: "var(--color-bg-base)", border: "1px solid var(--color-border-subtle)", overflow: "hidden" }}>
        <div style={{ height: "100%", width: `${compiled === "failed" ? 100 : percent}%`, background: compiled === "failed" ? "var(--color-red)" : "var(--color-maroon)", transition: "width 0.25s ease-out" }} />
      </div>
    </div>
  );
}
