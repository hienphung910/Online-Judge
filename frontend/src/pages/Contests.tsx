import { useEffect, useMemo, useState } from "react";
import { api } from "../api";
import { useAuth } from "../auth";
import type { Submission } from "../types";
import CodeEditor from "../components/CodeEditor";
import TestSummary from "../components/TestSummary";

/** "Bài nộp" page — shows the current user's submission history (DLab "Bài nộp" style) */
export default function Contests({ problems }: { problems: import("../types").Problem[] }) {
  const { user } = useAuth();
  const [subs, setSubs] = useState<Submission[]>([]);
  const [loading, setLoading] = useState(false);
  const [detail, setDetail] = useState<Submission | null>(null);

  useEffect(() => {
    if (!user) return;
    setLoading(true);
    api.submissions()
      .then((all) => setSubs(all.filter((s) => s.author === user.username)))
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [user]);

  function fmtTime(iso: string) {
    const d = new Date(iso);
    if (isNaN(d.getTime())) return iso;
    return d.toLocaleString("vi-VN", { hour12: false, hour: "2-digit", minute: "2-digit", second: "2-digit", day: "2-digit", month: "2-digit", year: "2-digit" });
  }

  async function openDetail(id: string) {
    try { setDetail(await api.submission(id)); } catch {}
  }

  const accepted = subs.filter((s) => s.verdict === "AC").length;

  return (
    <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden" }}>
      {/* Header */}
      <div style={{
        display: "flex", alignItems: "center", justifyContent: "space-between",
        padding: "16px 24px", background: "#fff", borderBottom: "1px solid #E0E0E0", flexShrink: 0,
      }}>
        <div style={{ fontSize: 16, fontWeight: 700, color: "#212121" }}>Bài nộp của tôi</div>
        <div style={{ display: "flex", gap: 16, fontSize: 13, color: "#757575" }}>
          <span>Tổng: <b style={{ color: "#212121" }}>{subs.length}</b></span>
          <span>AC: <b style={{ color: "var(--color-green)" }}>{accepted}</b></span>
        </div>
      </div>

      {/* Table */}
      <div style={{ flex: 1, overflow: "auto", margin: "0 24px 16px" }}>
        <table style={{ width: "100%", borderCollapse: "collapse", minWidth: 700 }}>
          <thead>
            <tr style={{ background: "var(--color-table-header-bg)" }}>
              <th style={TH}>Thời gian</th>
              <th style={{ ...TH, textAlign: "left" }}>Bài tập</th>
              <th style={TH}>Ngôn ngữ</th>
              <th style={TH}>Kết quả</th>
              <th style={TH}>Điểm</th>
              <th style={TH}>Thời gian</th>
            </tr>
          </thead>
          <tbody>
            {subs.length === 0 ? (
              <tr><td colSpan={6} style={{ padding: 40, textAlign: "center", color: "#9E9E9E", fontSize: 13 }}>
                {loading ? "Đang tải..." : "Bạn chưa nộp bài nào."}
              </td></tr>
            ) : subs.map((s, idx) => (
              <tr
                key={s.id}
                onClick={() => void openDetail(s.id)}
                style={{
                  cursor: "pointer",
                  background: detail?.id === s.id ? "#FFF3E0" : idx % 2 === 1 ? "var(--color-table-row-alt)" : "#fff",
                  borderBottom: "1px solid #F5F5F5", transition: "background 0.1s",
                }}
                onMouseEnter={(e) => { if (detail?.id !== s.id) e.currentTarget.style.background = "var(--color-table-hover)"; }}
                onMouseLeave={(e) => { if (detail?.id !== s.id) e.currentTarget.style.background = idx % 2 === 1 ? "var(--color-table-row-alt)" : "#fff"; }}
              >
                <td style={{ ...TD, fontFamily: "var(--font-mono)", fontSize: 12, color: "#757575", whiteSpace: "nowrap" }}>{fmtTime(s.submittedAt)}</td>
                <td style={{ ...TD, textAlign: "left" }}>
                  <span style={{ fontFamily: "var(--font-mono)", fontSize: 12, fontWeight: 600, color: "var(--color-red)" }}>{s.problem.id}</span>
                  {" · "}
                  <span style={{ color: s.verdict === "AC" ? "var(--color-green)" : "#212121", fontWeight: 500 }}>{s.problem.title}</span>
                </td>
                <td style={{ ...TD, textAlign: "center", fontSize: 13 }}>{s.language}</td>
                <td style={{ ...TD, textAlign: "center" }}>
                  <span style={{
                    fontFamily: "var(--font-mono)", fontSize: 12, fontWeight: 700, padding: "2px 10px", borderRadius: 4,
                    background: s.verdict === "AC" ? "var(--color-ac-bg)" : s.verdict === "PENDING" ? "#F5F5F5" : "var(--color-wa-bg)",
                    color: s.verdict === "AC" ? "var(--color-ac-text)" : s.verdict === "PENDING" ? "#9E9E9E" : "var(--color-wa-text)",
                  }}>{s.verdict === "PENDING" ? "..." : s.verdict}</span>
                </td>
                <td style={{ ...TD, textAlign: "center", fontFamily: "var(--font-mono)", fontSize: 13, fontWeight: 600, color: s.verdict === "AC" ? "var(--color-green)" : "#616161" }}>
                  {(s.score ?? 0).toFixed(0)}/{s.maxPoints.toFixed(0)}
                </td>
                <td style={{ ...TD, fontFamily: "var(--font-mono)", fontSize: 12, color: "#757575", textAlign: "center" }}>
                  {s.execTimeMs !== null ? `${(s.execTimeMs / 1000).toFixed(2)}s` : "—"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Detail modal */}
      {detail && (
        <div style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.4)", zIndex: 100, display: "flex", alignItems: "center", justifyContent: "center", padding: 24 }}
          onClick={(e) => { if (e.target === e.currentTarget) setDetail(null); }}>
          <div style={{ background: "#fff", borderRadius: 10, width: "100%", maxWidth: 700, maxHeight: "80vh", overflow: "auto", boxShadow: "0 16px 48px rgba(0,0,0,0.15)", animation: "slideIn 0.15s ease" }}>
            <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", padding: "14px 20px", borderBottom: "1px solid #E0E0E0", background: "var(--color-table-header-bg)" }}>
              <div style={{ fontSize: 14, fontWeight: 700, color: "#212121" }}>{detail.problem.id} — {detail.problem.title}</div>
              <button onClick={() => setDetail(null)} style={{ background: "none", border: "none", fontSize: 18, color: "#9E9E9E", cursor: "pointer" }}>×</button>
            </div>
            <div style={{ padding: 20, display: "flex", flexDirection: "column", gap: 12 }}>
              <div style={{ display: "flex", gap: 12, alignItems: "center", flexWrap: "wrap" }}>
                <span style={{
                  fontFamily: "var(--font-mono)", fontSize: 12, fontWeight: 700, padding: "2px 10px", borderRadius: 4,
                  background: detail.verdict === "AC" ? "var(--color-ac-bg)" : "var(--color-wa-bg)",
                  color: detail.verdict === "AC" ? "var(--color-ac-text)" : "var(--color-wa-text)",
                }}>{detail.verdict}</span>
                <span style={{ fontFamily: "var(--font-mono)", fontSize: 12.5 }}>Đúng {detail.passed}/{detail.total} test · {(detail.score ?? 0).toFixed(1)}/{detail.maxPoints.toFixed(0)} điểm</span>
                <span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "#9E9E9E" }}>{detail.language}</span>
              </div>
              {detail.message && (
                <pre style={{ margin: 0, padding: "10px 14px", background: "#FAFAFA", border: "1px solid #E0E0E0", borderRadius: 6, fontFamily: "var(--font-mono)", fontSize: 11.5, color: "#616161", whiteSpace: "pre-wrap", maxHeight: 160, overflow: "auto" }}>{detail.message}</pre>
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
