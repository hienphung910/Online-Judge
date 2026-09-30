import { useCallback, useEffect, useMemo, useState } from "react";
import { api } from "../api";
import CodeEditor from "../components/CodeEditor";
import TestSummary from "../components/TestSummary";
import type { Submission, VerdictCode } from "../types";

const REFRESH_MS = 3000;

function VBadge({ verdict }: { verdict: VerdictCode }) {
  const isAC = verdict === "AC";
  const isPending = verdict === "PENDING";
  return (
    <span style={{
      fontFamily: "var(--font-mono)", fontSize: 12, fontWeight: 700, padding: "2px 10px", borderRadius: 4,
      background: isAC ? "var(--color-ac-bg)" : isPending ? "#F5F5F5" : "var(--color-wa-bg)",
      color: isAC ? "var(--color-ac-text)" : isPending ? "#9E9E9E" : "var(--color-wa-text)",
    }}>
      {isPending ? "..." : verdict}
    </span>
  );
}

export default function Submissions({ reloadKey }: { reloadKey: number }) {
  const [subs, setSubs] = useState<Submission[]>([]);
  const [detail, setDetail] = useState<Submission | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [auto, setAuto] = useState(true);

  const load = useCallback(async () => {
    setLoading(true);
    try { setSubs(await api.submissions()); setError(""); }
    catch (e) { setError(e instanceof Error ? e.message : String(e)); }
    finally { setLoading(false); }
  }, []);

  useEffect(() => { void load(); }, [load, reloadKey]);
  useEffect(() => { if (!auto) return; const id = setInterval(() => void load(), REFRESH_MS); return () => clearInterval(id); }, [auto, load]);

  const languages = useMemo(() => Array.from(new Set(subs.map((s) => s.language))), [subs]);

  async function openDetail(id: string) {
    try { setDetail(await api.submission(id)); } catch (e) { setError(e instanceof Error ? e.message : String(e)); }
  }

  function fmtTime(iso: string) {
    const d = new Date(iso);
    if (isNaN(d.getTime())) return iso;
    return d.toLocaleString("vi-VN", { hour12: false, hour: "2-digit", minute: "2-digit", second: "2-digit", day: "2-digit", month: "2-digit", year: "2-digit" });
  }

  return (
    <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden" }}>
      {/* Header bar */}
      <div style={{
        display: "flex", alignItems: "center", justifyContent: "space-between",
        padding: "16px 24px", background: "#fff", borderBottom: "1px solid #E0E0E0", flexShrink: 0,
      }}>
        <div style={{ fontSize: 16, fontWeight: 700, color: "#212121" }}>Trạng thái nộp bài</div>
        <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
          <span style={{ fontSize: 13, color: "#757575" }}>Tự làm mới</span>
          {/* DLab-style toggle */}
          <button
            onClick={() => setAuto((v) => !v)}
            style={{
              width: 44, height: 24, borderRadius: 12, border: "none", cursor: "pointer",
              background: auto ? "var(--color-red)" : "#E0E0E0",
              position: "relative", transition: "background 0.2s",
            }}
          >
            <span style={{
              position: "absolute", top: 2, left: auto ? 22 : 2,
              width: 20, height: 20, borderRadius: "50%", background: "#fff",
              boxShadow: "0 1px 3px rgba(0,0,0,0.2)", transition: "left 0.2s",
            }} />
            <span style={{
              position: "absolute", top: 5, fontSize: 9, fontWeight: 700, color: "#fff",
              left: auto ? 5 : undefined, right: auto ? undefined : 5,
            }}>
              {auto ? "Live" : ""}
            </span>
          </button>
        </div>
      </div>

      {error && (
        <div style={{ margin: "12px 24px", padding: "10px 14px", background: "#FFEBEE", border: "1px solid #FFCDD2", borderRadius: 6, fontSize: 13, color: "#C62828" }}>
          {error}
        </div>
      )}

      {/* Table */}
      <div style={{ flex: 1, overflow: "auto", margin: "0 24px 16px" }}>
        <table style={{ width: "100%", borderCollapse: "collapse", minWidth: 800 }}>
          <thead>
            <tr style={{ background: "var(--color-table-header-bg)" }}>
              <th style={TH}>Thời gian</th>
              <th style={TH}>Người nộp</th>
              <th style={{ ...TH, textAlign: "left" }}>Bài tập</th>
              <th style={TH}>Ngôn ngữ</th>
              <th style={TH}>Kết quả</th>
              <th style={TH}>Thời gian</th>
            </tr>
          </thead>
          <tbody>
            {subs.length === 0 ? (
              <tr><td colSpan={6} style={{ padding: 40, textAlign: "center", color: "#9E9E9E", fontSize: 13 }}>Chưa có bài nộp nào.</td></tr>
            ) : subs.map((s, idx) => (
              <tr
                key={s.id}
                onClick={() => void openDetail(s.id)}
                style={{
                  cursor: "pointer",
                  background: detail?.id === s.id ? "#FFF3E0" : idx % 2 === 1 ? "var(--color-table-row-alt)" : "#fff",
                  borderBottom: "1px solid #F5F5F5",
                  transition: "background 0.1s",
                }}
                onMouseEnter={(e) => { if (detail?.id !== s.id) e.currentTarget.style.background = "var(--color-table-hover)"; }}
                onMouseLeave={(e) => { if (detail?.id !== s.id) e.currentTarget.style.background = idx % 2 === 1 ? "var(--color-table-row-alt)" : "#fff"; }}
              >
                <td style={{ ...TD, fontFamily: "var(--font-mono)", fontSize: 12, color: "#757575", whiteSpace: "nowrap" }}>
                  {fmtTime(s.submittedAt)}
                </td>
                <td style={{ ...TD, fontSize: 13 }}>
                  {s.authorName || s.author} · <span style={{ color: "#9E9E9E", fontFamily: "var(--font-mono)", fontSize: 11 }}>{s.author}</span>
                </td>
                <td style={{ ...TD, textAlign: "left" }}>
                  <span style={{ fontFamily: "var(--font-mono)", fontSize: 12, fontWeight: 600, color: "var(--color-red)" }}>{s.problem.id}</span>
                  {" · "}
                  <span style={{ color: s.verdict === "AC" ? "var(--color-green)" : "var(--color-red)", fontWeight: 500 }}>{s.problem.title}</span>
                </td>
                <td style={{ ...TD, fontSize: 13, textAlign: "center" }}>{s.language}</td>
                <td style={{ ...TD, textAlign: "center" }}><VBadge verdict={s.verdict} /></td>
                <td style={{ ...TD, fontFamily: "var(--font-mono)", fontSize: 12, color: "#757575", textAlign: "center" }}>
                  {s.execTimeMs !== null ? `${(s.execTimeMs / 1000).toFixed(2)}s` : "—"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Detail panel */}
      {detail && (
        <div style={{
          position: "fixed", inset: 0, background: "rgba(0,0,0,0.4)", zIndex: 100,
          display: "flex", alignItems: "center", justifyContent: "center", padding: 24,
        }} onClick={(e) => { if (e.target === e.currentTarget) setDetail(null); }}>
          <div style={{
            background: "#fff", borderRadius: 10, width: "100%", maxWidth: 700, maxHeight: "80vh",
            overflow: "auto", boxShadow: "0 16px 48px rgba(0,0,0,0.15)", animation: "slideIn 0.15s ease",
          }}>
            <div style={{
              display: "flex", alignItems: "center", justifyContent: "space-between",
              padding: "14px 20px", borderBottom: "1px solid #E0E0E0", background: "var(--color-table-header-bg)",
            }}>
              <div style={{ fontSize: 14, fontWeight: 700, color: "#212121" }}>
                {detail.problem.id} — {detail.problem.title}
              </div>
              <button onClick={() => setDetail(null)} style={{ background: "none", border: "none", fontSize: 18, color: "#9E9E9E", cursor: "pointer" }}>×</button>
            </div>
            <div style={{ padding: 20, display: "flex", flexDirection: "column", gap: 12 }}>
              <div style={{ display: "flex", gap: 12, alignItems: "center", flexWrap: "wrap" }}>
                <VBadge verdict={detail.verdict} />
                <span style={{ fontFamily: "var(--font-mono)", fontSize: 12.5 }}>
                  Đúng {detail.passed}/{detail.total} test · {(detail.score ?? 0).toFixed(1)}/{detail.maxPoints.toFixed(0)} điểm
                </span>
                <span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "#9E9E9E" }}>
                  {detail.language} · @{detail.author}
                </span>
              </div>
              {detail.message && (
                <pre style={{
                  margin: 0, padding: "10px 14px", background: "#FAFAFA", border: "1px solid #E0E0E0",
                  borderRadius: 6, fontFamily: "var(--font-mono)", fontSize: 11.5, color: "#616161",
                  whiteSpace: "pre-wrap", maxHeight: 160, overflow: "auto",
                }}>{detail.message}</pre>
              )}
              {detail.tests && detail.tests.length > 0 && <TestSummary tests={detail.tests} />}
              {detail.sourceCode && (
                <div>
                  <div style={{ fontFamily: "var(--font-mono)", fontSize: 10, color: "#9E9E9E", textTransform: "uppercase", letterSpacing: "0.08em", marginBottom: 4 }}>Mã nguồn</div>
                  <CodeEditor value={detail.sourceCode} language={detail.language} readOnly minHeight={0} maxHeight={300} />
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

const TH: React.CSSProperties = {
  padding: "10px 14px", fontSize: 12, fontWeight: 700, color: "#757575",
  textAlign: "center", whiteSpace: "nowrap", borderBottom: "1px solid var(--color-table-border)",
  position: "sticky", top: 0, zIndex: 2, background: "var(--color-table-header-bg)",
};

const TD: React.CSSProperties = {
  padding: "10px 14px", fontSize: 13, verticalAlign: "middle",
};
