import { useEffect, useMemo, useState } from "react";
import { api } from "../api";
import CodeEditor from "../components/CodeEditor";
import TestSummary from "../components/TestSummary";
import {
  Button, ErrorBox, MONO, Panel, SampleBox, Select, VerdictBadge,
} from "../components/ui";
import type {
  JudgeFinishedEvent, LanguageInfo, LiveTestEvent, Problem, Submission,
} from "../types";

/** Code mau giai bai P001 (a + b) cho tung ngon ngu - tien khi demo. */
const TEMPLATES: Record<string, string> = {
  Java: `import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        System.out.println(a + b);
    }
}
`,
  "C++": `#include <iostream>

int main() {
    long long a, b;
    std::cin >> a >> b;
    std::cout << a + b << std::endl;
    return 0;
}
`,
  Python: `import sys

data = sys.stdin.read().split()
print(int(data[0]) + int(data[1]))
`,
  Go: `package main

import "fmt"

func main() {
\tvar a, b int64
\tfmt.Scan(&a, &b)
\tfmt.Println(a + b)
}
`,
  JavaScript: `const data = require("fs").readFileSync(0, "utf8").trim().split(/\\s+/);
console.log((BigInt(data[0]) + BigInt(data[1])).toString());
`,
  Rust: `use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let nums: Vec<i64> = input.split_whitespace().map(|x| x.parse().unwrap()).collect();
    println!("{}", nums[0] + nums[1]);
}
`,
};

/** Trang thai cham dang dien ra, dung dan tu cac su kien SSE gui ve. */
interface LiveState {
  total: number;
  compiled: "waiting" | "ok" | "failed";
  compileMessage: string;
  tests: LiveTestEvent[];
  finished: JudgeFinishedEvent | null;
}

const EMPTY_LIVE: LiveState = {
  total: 0,
  compiled: "waiting",
  compileMessage: "",
  tests: [],
  finished: null,
};

export default function SubmitPage({
  problems,
  languages,
  username,
  preselectedProblem,
  onSubmitted,
}: {
  problems: Problem[];
  languages: LanguageInfo[];
  username: string;
  preselectedProblem: string;
  onSubmitted: () => void;
}) {
  const [problemId, setProblemId] = useState(preselectedProblem);
  const [language, setLanguage] = useState("Java");
  const [code, setCode] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState<Submission | null>(null);
  const [live, setLive] = useState<LiveState>(EMPTY_LIVE);

  useEffect(() => {
    if (preselectedProblem) setProblemId(preselectedProblem);
  }, [preselectedProblem]);

  // Neu vao truc tiep trang nay thi chon san bai dau tien khi danh sach nap xong.
  useEffect(() => {
    if (!problemId && problems.length > 0) setProblemId(problems[0].id);
  }, [problems, problemId]);

  const problem = problems.find((p) => p.id === problemId);
  const langNames = useMemo(() => languages.map((l) => l.name), [languages]);
  const unavailable = useMemo(() => languages.filter((l) => !l.available).map((l) => l.name), [languages]);
  const currentLang = languages.find((l) => l.name === language);

  async function doSubmit() {
    setError("");
    setResult(null);
    setLive(EMPTY_LIVE);
    if (!problemId) return setError("Chưa chọn bài.");
    if (!language) return setError("Chưa chọn ngôn ngữ.");
    if (!code.trim()) return setError("Mã nguồn đang rỗng.");

    setBusy(true);
    try {
      // Ban stream: tung test hien ra ngay khi may chu cham xong test do.
      // Khong gui username - may chu lay nguoi nop tu token dang nhap.
      await api.submitStream({ problemId, language, code }, (event) => {
        switch (event.type) {
          case "started":
            setLive((s) => ({ ...s, total: event.data.total }));
            break;
          case "compiled":
            setLive((s) => ({
              ...s,
              compiled: event.data.success ? "ok" : "failed",
              compileMessage: event.data.message,
            }));
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

  // Trong luc cham thi lay tu su kien; cham xong thi lay ban chinh thuc cua may chu.
  const shownTests = result?.tests ?? live.tests;
  const totalTests = result?.total ?? live.total;
  // Luc dang cham thi tu dem tu su kien; cham xong thi lay so chinh thuc cua may chu.
  const passedTests = result?.passed ?? shownTests.filter((t) => t.verdict === "AC").length;
  const progress = totalTests > 0 ? Math.round((shownTests.length / totalTests) * 100) : 0;

  return (
    <div className="submit-grid">
      {/* ── Cột trái: đề bài, luôn hiện để vừa code vừa đọc ── */}
      <Panel
        title={problem ? `${problem.id} — ${problem.title}` : "Đề bài"}
        style={{ position: "sticky", top: 0, maxHeight: "calc(100vh - 92px)" }}
      >
        {!problem ? (
          <div style={{ padding: 18, ...MONO, fontSize: 12, color: "var(--color-text-muted)", lineHeight: 1.8 }}>
            Chọn một bài ở tab <b style={{ color: "var(--color-text-secondary)" }}>Bài tập</b> hoặc ở ô chọn bài bên cạnh.
          </div>
        ) : (
          <div style={{ padding: 14, display: "flex", flexDirection: "column", gap: 12, overflowY: "auto" }}>
            <pre
              style={{
                margin: 0, whiteSpace: "pre-wrap", fontFamily: "var(--font-sans)",
                fontSize: 13, lineHeight: 1.75, color: "var(--color-text-secondary)",
              }}
            >
              {problem.statement || "(Đề bài chưa có statement.txt)"}
            </pre>

            <div style={{ display: "flex", gap: 16, flexWrap: "wrap", ...MONO, fontSize: 11.5, color: "var(--color-text-muted)" }}>
              <span>
                Thời gian: <b style={{ color: "var(--color-text-secondary)" }}>{problem.timeLimitMs} ms</b>
              </span>
              <span>
                Bộ nhớ: <b style={{ color: "var(--color-text-secondary)" }}>{problem.memoryLimitMb} MB</b>
              </span>
              <span>
                Tổng điểm: <b style={{ color: "var(--color-text-secondary)" }}>{problem.maxPoints.toFixed(0)}</b>
              </span>
            </div>

            {problem.samples.map((s, i) => (
              <div key={i} style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
                <SampleBox label={`Input ví dụ ${i + 1}`} text={s.input} />
                <SampleBox label={`Output ví dụ ${i + 1}`} text={s.output} />
              </div>
            ))}
          </div>
        )}
      </Panel>

      {/* ── Cột phải: khung code, rồi kết quả chấm ── */}
      <div style={{ display: "flex", flexDirection: "column", gap: 14, minWidth: 0 }}>
        <Panel
          title="Nộp bài"
          right={
            <span style={{ ...MONO, fontSize: 11, color: "var(--color-text-muted)" }}>
              đang nộp với tài khoản @{username}
            </span>
          }
        >
          <div style={{ padding: 14, display: "flex", flexDirection: "column", gap: 12 }}>
            <div style={{ display: "flex", gap: 10, flexWrap: "wrap", alignItems: "center" }}>
              <Select
                value={problemId}
                options={problems.map((p) => p.id)}
                onChange={(v) => setProblemId(v)}
                placeholder="Chọn bài"
              />
              <Select
                value={language}
                options={langNames}
                onChange={(v) => setLanguage(v)}
                placeholder="Chọn ngôn ngữ"
                disabledOptions={unavailable}
              />
              <Button onClick={() => setCode(TEMPLATES[language] ?? "")} disabled={!TEMPLATES[language]}>
                Chèn code mẫu A+B
              </Button>
              <div style={{ flex: 1 }} />
              <Button variant="primary" onClick={doSubmit} disabled={busy}>
                {busy ? "Đang chấm..." : "Nộp và chấm"}
              </Button>
            </div>

            {currentLang && !currentLang.available && (
              <div style={{ ...MONO, fontSize: 11.5, color: "#fbbf24" }}>
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
            result ? (
              <span style={{ ...MONO, fontSize: 11, color: "var(--color-text-muted)" }}>{result.id}</span>
            ) : busy ? (
              <span style={{ ...MONO, fontSize: 11, color: "var(--color-accent-cyan)", animation: "livePulse 1.2s infinite" }}>
                ● đang chấm trực tiếp
              </span>
            ) : null
          }
        >
          {error && <ErrorBox message={error} />}

          {!error && !busy && !result && (
            <div style={{ padding: 18, ...MONO, fontSize: 12, color: "var(--color-text-muted)", lineHeight: 1.8 }}>
              Dán code rồi bấm “Nộp và chấm”. Kết quả cập nhật ngay khi máy chủ chấm xong từng test.
            </div>
          )}

          {(busy || result) && !error && (
            <div style={{ padding: 14, display: "flex", flexDirection: "column", gap: 12 }}>
              {/* ── Thanh tiến trình + các bước ── */}
              <ProgressStrip
                busy={busy}
                compiled={live.compiled}
                done={shownTests.length}
                total={totalTests}
                percent={progress}
              />

              {/* ── Tóm tắt kiểu Codeforces: badge · Đúng k/N test · điểm. Cập nhật ngay trong lúc chấm. ── */}
              <div style={{ display: "flex", alignItems: "center", gap: 12, flexWrap: "wrap" }}>
                <VerdictBadge verdict={result?.verdict ?? "PENDING"} size={13} />
                {live.compiled === "ok" && (
                  // CE thì test chưa chạy, không có gì để "đúng k/N" - chỉ hiện badge và khối lỗi javac.
                  <span style={{ ...MONO, fontSize: 13, color: "var(--color-text-primary)" }}>
                    Đúng {passedTests}/{totalTests || "?"} test
                  </span>
                )}
                {result && (
                  <span style={{ ...MONO, fontSize: 13, color: "#50E3C2" }}>
                    {(result.score ?? 0).toFixed(1)}/{result.maxPoints.toFixed(0)} điểm
                  </span>
                )}
                {result && live.compiled === "ok" && result.execTimeMs !== null && (
                  <span style={{ ...MONO, fontSize: 12, color: "var(--color-text-muted)" }}>
                    test lâu nhất {result.execTimeMs} ms
                  </span>
                )}
              </div>

              {/* ── Trượt ở test nào: "WA on test 2, 4 · TLE on test 3" — hiện ngay khi test đó vừa trượt ── */}
              <TestSummary tests={shownTests} size={13} />

              {result && (
                <div style={{ ...MONO, fontSize: 11, color: "var(--color-text-muted)" }}>
                  File biên dịch: {result.fileName} · ngôn ngữ {result.language}
                </div>
              )}

              {/* ── Lỗi biên dịch: hiện ngay lúc nhận được, không đợi chấm xong ── */}
              {(live.compiled === "failed" || result?.message) && (
                <pre
                  style={{
                    margin: 0, padding: "10px 12px", background: "var(--color-bg-base)",
                    border: "1px solid rgba(248,113,113,0.35)", borderRadius: 6,
                    fontFamily: "var(--font-mono)", fontSize: 11.5, color: "#94a3b8",
                    whiteSpace: "pre-wrap", maxHeight: 200, overflow: "auto",
                  }}
                >
                  {result?.message || live.compileMessage}
                </pre>
              )}
            </div>
          )}
        </Panel>
      </div>
    </div>
  );
}

/**
 * Thanh tien trinh cham: bien dich -> tung test.
 * Chi la hien thi, moi so deu den tu su kien SSE nen khong doan hay noi suy gi ca.
 */
function ProgressStrip({
  busy,
  compiled,
  done,
  total,
  percent,
}: {
  busy: boolean;
  compiled: "waiting" | "ok" | "failed";
  done: number;
  total: number;
  percent: number;
}) {
  const compileLabel =
    compiled === "waiting" ? "đang biên dịch..." : compiled === "ok" ? "biên dịch OK" : "biên dịch THẤT BẠI";
  const compileColor =
    compiled === "waiting" ? "var(--color-text-muted)" : compiled === "ok" ? "#4ade80" : "#f87171";

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
      <div style={{ display: "flex", alignItems: "center", gap: 12, ...MONO, fontSize: 11.5 }}>
        <span style={{ color: compileColor }}>{compileLabel}</span>
        {compiled === "ok" && (
          <span style={{ color: "var(--color-text-secondary)" }}>
            test {done}/{total || "?"}
          </span>
        )}
        <div style={{ flex: 1 }} />
        {busy && (
          <span style={{ color: "var(--color-text-muted)", animation: "livePulse 1.2s infinite" }}>
            máy chủ đang chạy...
          </span>
        )}
      </div>

      <div
        style={{
          height: 4, borderRadius: 2, background: "var(--color-bg-base)",
          border: "1px solid var(--color-border-subtle)", overflow: "hidden",
        }}
      >
        <div
          style={{
            height: "100%",
            width: `${compiled === "failed" ? 100 : percent}%`,
            background: compiled === "failed" ? "#f87171" : "var(--color-accent-cyan)",
            transition: "width 0.25s ease-out",
          }}
        />
      </div>
    </div>
  );
}
