import { useCallback, useEffect, useMemo, useState } from "react";
import { api } from "../api";
import CodeEditor from "../components/CodeEditor";
import TestSummary from "../components/TestSummary";
import { Button, ErrorBox, ExecBar, MONO, Panel, RefIco, Select, StatCard, TD, TH, VerdictBadge, formatTime, timeAgo } from "../components/ui";
import type { Submission, VerdictCode } from "../types";

const VERDICT_FILTERS: VerdictCode[] = ["AC", "WA", "TLE", "MLE", "RE", "CE"];
const REFRESH_MS = 3000;

export default function Submissions({ reloadKey }: { reloadKey: number }) {
  const [subs, setSubs] = useState<Submission[]>([]);
  const [detail, setDetail] = useState<Submission | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [auto, setAuto] = useState(true);
  const [fVerdict, setFVerdict] = useState("");
  const [fLang, setFLang] = useState("");
  const [fAuthor, setFAuthor] = useState("");

  const load = useCallback(async () => {
    setLoading(true);
    try {
      setSubs(await api.submissions());
      setError("");
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { void load(); }, [load, reloadKey]);

  useEffect(() => {
    if (!auto) return;
    const id = setInterval(() => void load(), REFRESH_MS);
    return () => clearInterval(id);
  }, [auto, load]);

  const languages = useMemo(() => Array.from(new Set(subs.map((s) => s.language))), [subs]);
  const authors = useMemo(() => Array.from(new Set(subs.map((s) => s.author))), [subs]);

  const filtered = subs.filter(
    (s) => (!fVerdict || s.verdict === fVerdict) && (!fLang || s.language === fLang) && (!fAuthor || s.author === fAuthor),
  );

  const accepted = subs.filter((s) => s.verdict === "AC").length;
  const acRate = subs.length > 0 ? Math.round((accepted / subs.length) * 100) : 0;

  async function openDetail(id: string) {
    try {
      setDetail(await api.submission(id));
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    }
  }

  return (
    <div style={{ flex: 1, display: "flex", flexDirection: "column", padding: "24px 32px", gap: 16, overflow: "auto" }}>
      <h1 style={{ fontFamily: "var(--font-serif)", fontSize: 26, fontWeight: 700, color: "var(--color-maroon)", margin: 0, letterSpacing: "-0.02em" }}>Lịch sử nộp bài</h1>

      <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
        <StatCard label="Bài nộp" value={subs.length} />
        <StatCard label="Accepted" value={accepted} color="var(--color-green)" sub={`${acRate}% AC`} />
        <StatCard label="Ngôn ngữ" value={languages.length} />
        <StatCard label="Thí sinh" value={authors.length} />
      </div>

      <Panel
        title={`${filtered.length}/${subs.length} bài nộp`}
        right={
          <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
            <Select value={fVerdict} options={VERDICT_FILTERS} onChange={setFVerdict} placeholder="Verdict" />
            <Select value={fLang} options={languages} onChange={setFLang} placeholder="Ngôn ngữ" />
            <Select value={fAuthor} options={authors} onChange={setFAuthor} placeholder="Thí sinh" />
            <Button onClick={() => setAuto((v) => !v)} style={auto ? { color: "var(--color-green)", borderColor: "var(--color-green-border)" } : undefined}>
              {auto ? "Tự động làm mới: bật" : "Tự động làm mới: tắt"}
            </Button>
            <Button onClick={() => void load()}><RefIco spinning={loading} /></Button>
          </div>
        }
      >
        {error && <ErrorBox message={error} />}
        <div style={{ overflowX: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse", minWidth: 860 }}>
            <thead>
              <tr>
                <th style={TH}>Mã nộp</th>
                <th style={TH}>Thời điểm</th>
                <th style={TH}>Thí sinh</th>
                <th style={TH}>Bài</th>
                <th style={TH}>Ngôn ngữ</th>
                <th style={TH}>Kết quả</th>
                <th style={TH}>Test</th>
                <th style={TH}>Điểm</th>
                <th style={TH}>Thời gian</th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((s) => (
                <tr key={s.id} onClick={() => void openDetail(s.id)} style={{ cursor: "pointer", background: detail?.id === s.id ? "var(--color-bg-raised)" : "transparent" }}>
                  <td style={{ ...TD, ...MONO, color: "var(--color-maroon)" }}>{s.id}</td>
                  <td style={{ ...TD, ...MONO, whiteSpace: "nowrap" }}>
                    {formatTime(s.submittedAt)}
                    <span style={{ color: "var(--color-text-muted)", fontSize: 10.5 }}> · {timeAgo(s.submittedAt)}</span>
                  </td>
                  <td style={{ ...TD, ...MONO }}>{s.author}</td>
                  <td style={TD}>
                    <span style={{ ...MONO, color: "var(--color-text-muted)" }}>{s.problem.id}</span>{" "}
                    <span style={{ color: "var(--color-text-primary)" }}>{s.problem.title}</span>
                  </td>
                  <td style={{ ...TD, ...MONO }}>{s.language}</td>
                  <td style={TD}><VerdictBadge verdict={s.verdict} /></td>
                  <td style={{ ...TD, ...MONO }}>{s.passed}/{s.total}</td>
                  <td style={{ ...TD, ...MONO, color: s.verdict === "AC" ? "var(--color-green)" : "var(--color-text-secondary)" }}>{(s.score ?? 0).toFixed(1)}</td>
                  <td style={TD}><ExecBar ms={s.execTimeMs} /></td>
                </tr>
              ))}
              {filtered.length === 0 && (
                <tr><td style={{ ...TD, ...MONO, color: "var(--color-text-muted)" }} colSpan={9}>Chưa có bài nộp nào khớp bộ lọc.</td></tr>
              )}
            </tbody>
          </table>
        </div>
      </Panel>

      {detail && (
        <Panel title={`${detail.id} — ${detail.problem.id} ${detail.problem.title}`} right={<Button onClick={() => setDetail(null)}>Đóng</Button>}>
          <div style={{ padding: 14, display: "flex", flexDirection: "column", gap: 12 }}>
            <div style={{ display: "flex", gap: 12, alignItems: "center", flexWrap: "wrap" }}>
              <VerdictBadge verdict={detail.verdict} size={13} />
              <span style={{ ...MONO, fontSize: 12.5 }}>
                Đúng {detail.passed}/{detail.total} test · {(detail.score ?? 0).toFixed(1)}/{detail.maxPoints.toFixed(0)} điểm
              </span>
              <span style={{ ...MONO, fontSize: 12, color: "var(--color-text-muted)" }}>
                {detail.language} · {detail.fileName} · @{detail.author} ({detail.authorName})
              </span>
            </div>

            {detail.message && (
              <pre style={{ margin: 0, padding: "10px 12px", background: "var(--color-bg-base)", border: "1px solid var(--color-border)", borderRadius: 6, fontFamily: "var(--font-mono)", fontSize: 11.5, color: "var(--color-text-secondary)", whiteSpace: "pre-wrap", maxHeight: 180, overflow: "auto" }}>
                {detail.message}
              </pre>
            )}

            {detail.tests && detail.tests.length > 0 && <TestSummary tests={detail.tests} />}

            {detail.sourceCode && (
              <div>
                <div style={{ ...MONO, fontSize: 9.5, letterSpacing: "0.1em", textTransform: "uppercase", color: "var(--color-text-muted)", marginBottom: 4 }}>Mã nguồn đã nộp</div>
                <CodeEditor value={detail.sourceCode} language={detail.language} readOnly minHeight={0} maxHeight={320} />
              </div>
            )}
          </div>
        </Panel>
      )}
    </div>
  );
}
