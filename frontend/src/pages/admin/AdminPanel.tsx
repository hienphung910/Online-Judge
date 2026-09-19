import { useState } from "react";
import { contestStatus, useLocalContests, type Contest } from "../../localContests";
import type { Problem } from "../../types";
import ProblemEditor from "./ProblemEditor";
import ContestEditor from "./ContestEditor";

type AdminTab = "problems" | "contests";

function ConfirmDelete({ label, onConfirm, onCancel }: { label: string; onConfirm: () => void; onCancel: () => void }) {
  return (
    <div style={{ position: "fixed", inset: 0, background: "rgba(28,20,16,0.45)", zIndex: 1000, display: "flex", alignItems: "center", justifyContent: "center" }}>
      <div style={{ background: "var(--color-bg-panel)", border: "1px solid var(--color-border)", borderRadius: 12, padding: "28px 32px", maxWidth: 380, width: "100%", boxShadow: "0 16px 48px rgba(28,20,16,0.18)" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 16 }}>
          <span style={{ width: 36, height: 36, borderRadius: 8, background: "var(--color-red-bg)", border: "1px solid var(--color-red-border)", display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0 }}>
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="var(--color-red)" strokeWidth="1.6" strokeLinecap="round"><path d="M3 6h10l-1 8H4L3 6z" /><path d="M1 4h14" /><path d="M6 4V2h4v2" /></svg>
          </span>
          <div>
            <div style={{ fontFamily: "var(--font-serif)", fontSize: 16, fontWeight: 700, color: "var(--color-text-primary)" }}>Delete {label}?</div>
            <div style={{ fontFamily: "var(--font-sans)", fontSize: 12, color: "var(--color-text-muted)", marginTop: 2 }}>This action cannot be undone.</div>
          </div>
        </div>
        <div style={{ display: "flex", gap: 10, justifyContent: "flex-end" }}>
          <button onClick={onCancel} style={{ height: 34, padding: "0 18px", background: "none", border: "1px solid var(--color-border)", borderRadius: 7, color: "var(--color-text-muted)", fontSize: 13, cursor: "pointer", fontFamily: "var(--font-sans)" }}>Cancel</button>
          <button onClick={onConfirm} style={{ height: 34, padding: "0 18px", background: "var(--color-red)", border: "none", borderRadius: 7, color: "white", fontSize: 13, fontWeight: 600, cursor: "pointer", fontFamily: "var(--font-sans)" }}>Delete</button>
        </div>
      </div>
    </div>
  );
}

export default function AdminPanel({ problems, onProblemCreated }: { problems: Problem[]; onProblemCreated: () => void }) {
  const { contests, deleteContest } = useLocalContests();
  const [tab, setTab] = useState<AdminTab>("problems");
  const [showProblemEditor, setShowProblemEditor] = useState(false);
  const [editContest, setEditContest] = useState<Contest | "new" | null>(null);
  const [deleteTarget, setDeleteTarget] = useState<{ id: string; label: string } | null>(null);

  function fmtDur(m: number) { const h = Math.floor(m / 60), r = m % 60; return h > 0 ? `${h}h${r > 0 ? " " + r + "m" : ""}` : r + "m"; }
  const STATUS_COLOR: Record<string, string> = { Active: "var(--color-green)", Upcoming: "var(--color-blue)", Completed: "var(--color-text-muted)" };

  return (
    <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden", padding: "0 32px 24px" }}>
      <div style={{ paddingTop: 28, paddingBottom: 20, borderBottom: "1px solid var(--color-border)", marginBottom: 24, display: "flex", alignItems: "flex-end", justifyContent: "space-between", flexWrap: "wrap", gap: 12 }}>
        <div>
          <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 4 }}>
            <div style={{ width: 30, height: 30, borderRadius: 7, background: "var(--color-maroon)", display: "flex", alignItems: "center", justifyContent: "center" }}>
              <svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="#FAF7F2" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><rect x="2" y="3" width="12" height="10" rx="1.5" /><path d="M5 7h6M5 10h4" /></svg>
            </div>
            <h1 style={{ fontFamily: "var(--font-serif)", fontSize: 26, fontWeight: 700, color: "var(--color-maroon)", margin: 0, letterSpacing: "-0.02em" }}>Admin Panel</h1>
          </div>
          <p style={{ fontFamily: "var(--font-sans)", fontSize: 13, color: "var(--color-text-muted)", margin: 0 }}>Quản lý bài tập và cuộc thi (demo).</p>
        </div>

        <button
          onClick={() => (tab === "problems" ? setShowProblemEditor(true) : setEditContest("new"))}
          style={{ display: "flex", alignItems: "center", gap: 7, height: 38, padding: "0 20px", background: "var(--color-maroon)", border: "none", borderRadius: 8, color: "#FAF7F2", fontSize: 13, fontWeight: 700, cursor: "pointer", fontFamily: "var(--font-sans)" }}
        >
          <svg width="13" height="13" viewBox="0 0 12 12" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"><line x1="6" y1="1" x2="6" y2="11" /><line x1="1" y1="6" x2="11" y2="6" /></svg>
          {tab === "problems" ? "Add Problem" : "New Contest"}
        </button>
      </div>

      <div style={{ display: "flex", gap: 12, marginBottom: 24, flexWrap: "wrap" }}>
        {[
          { label: "Total Problems", value: problems.length, color: "var(--color-maroon)" },
          { label: "Active Contests", value: contests.filter((c) => contestStatus(c) === "Active").length, color: "var(--color-green)" },
          { label: "Upcoming Contests", value: contests.filter((c) => contestStatus(c) === "Upcoming").length, color: "var(--color-blue)" },
          { label: "Total Contests", value: contests.length, color: "var(--color-text-secondary)" },
        ].map(({ label, value, color }) => (
          <div key={label} style={{ background: "var(--color-bg-panel)", border: "1px solid var(--color-border)", borderRadius: 9, padding: "12px 18px", display: "flex", flexDirection: "column", gap: 3, minWidth: 130 }}>
            <span style={{ fontFamily: "var(--font-mono)", fontSize: 9, color: "var(--color-text-muted)", textTransform: "uppercase", letterSpacing: "0.1em" }}>{label}</span>
            <span style={{ fontFamily: "var(--font-serif)", fontSize: 24, fontWeight: 700, color, lineHeight: 1 }}>{value}</span>
          </div>
        ))}
      </div>

      <div style={{ display: "flex", gap: 0, borderBottom: "1px solid var(--color-border)", marginBottom: 16 }}>
        {(["problems", "contests"] as AdminTab[]).map((t) => (
          <button key={t} onClick={() => setTab(t)} style={{ height: 38, padding: "0 20px", background: "none", border: "none", borderBottom: `2px solid ${tab === t ? "var(--color-maroon)" : "transparent"}`, color: tab === t ? "var(--color-maroon)" : "var(--color-text-muted)", fontSize: 13, fontWeight: tab === t ? 600 : 400, cursor: "pointer", fontFamily: "var(--font-sans)", textTransform: "capitalize" }}>
            {t} ({t === "problems" ? problems.length : contests.length})
          </button>
        ))}
      </div>

      {tab === "problems" && (
        <div style={{ flex: 1, overflow: "auto", border: "1px solid var(--color-border)", borderRadius: 10, background: "var(--color-bg-panel)" }}>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr>
                {["Mã", "Tên bài", "Giới hạn", "Điểm"].map((h) => (
                  <th key={h} style={{ padding: "9px 14px", textAlign: "left", fontFamily: "var(--font-mono)", fontSize: 10, fontWeight: 600, color: "var(--color-text-muted)", textTransform: "uppercase", letterSpacing: "0.09em", borderBottom: "1px solid var(--color-border)", background: "var(--color-bg-raised)" }}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {problems.length === 0
                ? <tr><td colSpan={4} style={{ padding: 52, textAlign: "center", color: "var(--color-text-muted)", fontFamily: "var(--font-mono)", fontSize: 13 }}>Chưa có bài tập nào. Bấm "Add Problem".</td></tr>
                : problems.map((p, idx) => (
                  <tr key={p.id} style={{ borderBottom: idx < problems.length - 1 ? "1px solid var(--color-border-subtle)" : "none" }}>
                    <td style={{ padding: "10px 14px" }}><span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-maroon)", fontWeight: 700 }}>{p.id}</span></td>
                    <td style={{ padding: "10px 14px" }}><span style={{ fontSize: 13, fontWeight: 500, color: "var(--color-text-primary)" }}>{p.title}</span></td>
                    <td style={{ padding: "10px 14px" }}><span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-secondary)" }}>{p.timeLimitMs} ms / {p.memoryLimitMb} MB</span></td>
                    <td style={{ padding: "10px 14px" }}><span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-secondary)" }}>{p.maxPoints.toFixed(0)}</span></td>
                  </tr>
                ))}
            </tbody>
          </table>
          <div style={{ padding: "8px 14px", fontFamily: "var(--font-mono)", fontSize: 10.5, color: "var(--color-text-muted)", borderTop: "1px solid var(--color-border-subtle)" }}>
            Backend hiện chỉ hỗ trợ tạo bài mới, chưa có API sửa/xoá bài đã tạo.
          </div>
        </div>
      )}

      {tab === "contests" && (
        <div style={{ flex: 1, overflow: "auto", border: "1px solid var(--color-border)", borderRadius: 10, background: "var(--color-bg-panel)" }}>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr>
                {["ID", "Title", "Start Time", "Duration", "Problems", "Status", "Actions"].map((h, i) => (
                  <th key={h} style={{ padding: "9px 14px", textAlign: i === 6 ? "right" : "left", fontFamily: "var(--font-mono)", fontSize: 10, fontWeight: 600, color: "var(--color-text-muted)", textTransform: "uppercase", letterSpacing: "0.09em", borderBottom: "1px solid var(--color-border)", background: "var(--color-bg-raised)", whiteSpace: "nowrap" }}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {contests.length === 0
                ? <tr><td colSpan={7} style={{ padding: 52, textAlign: "center", color: "var(--color-text-muted)", fontFamily: "var(--font-mono)", fontSize: 13 }}>Chưa có cuộc thi nào. Bấm "New Contest".</td></tr>
                : contests.map((c, idx) => {
                  const status = contestStatus(c);
                  const sc = STATUS_COLOR[status];
                  return (
                    <tr key={c.id} style={{ borderBottom: idx < contests.length - 1 ? "1px solid var(--color-border-subtle)" : "none" }}>
                      <td style={{ padding: "10px 14px" }}><span style={{ fontFamily: "var(--font-mono)", fontSize: 11.5, color: "var(--color-maroon)", fontWeight: 700 }}>{c.id.slice(0, 12)}</span></td>
                      <td style={{ padding: "10px 14px" }}><span style={{ fontSize: 13, fontWeight: 500, color: "var(--color-text-primary)" }}>{c.title}</span></td>
                      <td style={{ padding: "10px 14px" }}><span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-secondary)" }}>{new Date(c.startTime).toLocaleString("vi-VN")}</span></td>
                      <td style={{ padding: "10px 14px" }}><span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-secondary)" }}>{fmtDur(c.durationMins)}</span></td>
                      <td style={{ padding: "10px 14px" }}><span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-maroon)", fontWeight: 700 }}>{c.problemIds.length}</span></td>
                      <td style={{ padding: "10px 14px" }}><span style={{ fontFamily: "var(--font-mono)", fontSize: 11, fontWeight: 600, color: sc, background: `${sc}15`, border: `1px solid ${sc}40`, borderRadius: 5, padding: "2px 9px" }}>{status}</span></td>
                      <td style={{ padding: "10px 14px", textAlign: "right" }}>
                        <div style={{ display: "flex", justifyContent: "flex-end", gap: 6 }}>
                          <button onClick={() => setEditContest(c)} style={ROW_BTN}>Edit</button>
                          <button onClick={() => setDeleteTarget({ id: c.id, label: c.title })} style={{ ...ROW_BTN, color: "var(--color-red)" }}>Delete</button>
                        </div>
                      </td>
                    </tr>
                  );
                })}
            </tbody>
          </table>
        </div>
      )}

      {showProblemEditor && (
        <ProblemEditor onClose={() => setShowProblemEditor(false)} onCreated={onProblemCreated} />
      )}
      {editContest !== null && (
        <ContestEditor problems={problems} contest={editContest === "new" ? undefined : editContest} onClose={() => setEditContest(null)} />
      )}
      {deleteTarget && (
        <ConfirmDelete label={deleteTarget.label} onConfirm={() => { deleteContest(deleteTarget.id); setDeleteTarget(null); }} onCancel={() => setDeleteTarget(null)} />
      )}
    </div>
  );
}

const ROW_BTN: React.CSSProperties = {
  display: "flex", alignItems: "center", gap: 5, height: 28, padding: "0 11px", background: "none",
  border: "1px solid var(--color-border)", borderRadius: 6, color: "var(--color-text-muted)", fontSize: 11,
  cursor: "pointer", fontFamily: "var(--font-sans)",
};
