import { useMemo, useState } from "react";
import { api } from "../../api";
import { DIFFICULTY_META, OTHER_TOPIC, orderByPath, topicKey } from "../../learningPath";
import { contestStatus, useLocalContests, type Contest } from "../../localContests";
import type { Problem, Topic } from "../../types";
import ProblemEditor from "./ProblemEditor";
import ProblemMetaEditor from "./ProblemMetaEditor";
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

export default function AdminPanel({ problems, topics, onProblemsChanged }: { problems: Problem[]; topics: Topic[]; onProblemsChanged: () => Promise<void> }) {
  const { contests, deleteContest } = useLocalContests();
  const [tab, setTab] = useState<AdminTab>("problems");
  const [showProblemEditor, setShowProblemEditor] = useState(false);
  const [editProblem, setEditProblem] = useState<Problem | null>(null);
  /** "" = moi chu de, ma chu de, hoac OTHER_TOPIC. */
  const [topicFilter, setTopicFilter] = useState("");
  const [movingId, setMovingId] = useState<string | null>(null);
  const [moveError, setMoveError] = useState("");
  const [editContest, setEditContest] = useState<Contest | "new" | null>(null);
  const [deleteTarget, setDeleteTarget] = useState<{ id: string; label: string } | null>(null);

  const known = useMemo(() => new Set(topics.map((t) => t.id)), [topics]);
  const ordered = useMemo(() => orderByPath(problems, topics), [problems, topics]);
  const visibleProblems = topicFilter ? ordered.filter((p) => topicKey(p, known) === topicFilter) : ordered;
  /** Vi tri cua bai trong nhom cung ma chu de - cung cach backend danh so lai. */
  const placeOf = useMemo(() => {
    const size = new Map<string, number>();
    const place = new Map<string, number>();
    for (const p of ordered) {
      const n = (size.get(p.topic) ?? 0) + 1;
      size.set(p.topic, n);
      place.set(p.id, n);
    }
    return (p: Problem) => ({ index: place.get(p.id) ?? 0, size: size.get(p.topic) ?? 0 });
  }, [ordered]);
  const topicLabel = (p: Problem) => {
    const t = topics.find((x) => x.id === p.topic);
    return t ? `${t.order}. ${t.name}` : p.topic ? `${p.topic} (không còn trong lộ trình)` : "Bài khác";
  };

  /** Nut len / xuong: doi cho voi bai ke ben trong cung chu de. */
  async function move(p: Problem, delta: number) {
    setMoveError("");
    setMovingId(p.id);
    try {
      await api.updateProblem(p.id, { topic: p.topic, difficulty: p.difficulty, position: placeOf(p).index + delta });
      await onProblemsChanged();
    } catch (e) {
      setMoveError(e instanceof Error ? e.message : String(e));
    } finally {
      setMovingId(null);
    }
  }

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
        <div style={{ flex: 1, display: "flex", flexDirection: "column", gap: 10, overflow: "hidden" }}>
          <div style={{ display: "flex", alignItems: "center", gap: 10, flexWrap: "wrap" }}>
            <label style={{ fontFamily: "var(--font-mono)", fontSize: 10, fontWeight: 600, color: "var(--color-text-muted)", textTransform: "uppercase", letterSpacing: "0.09em" }}>Chủ đề</label>
            <select value={topicFilter} onChange={(e) => setTopicFilter(e.target.value)} style={FILTER}>
              <option value="">Tất cả ({problems.length})</option>
              {topics.map((t) => <option key={t.id} value={t.id}>{t.order}. {t.name} ({t.problemCount})</option>)}
              {ordered.some((p) => topicKey(p, known) === OTHER_TOPIC) && <option value={OTHER_TOPIC}>Bài khác</option>}
            </select>
            {moveError && <span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-red)" }}>{moveError}</span>}
          </div>

          <div style={{ flex: 1, overflow: "auto", border: "1px solid var(--color-border)", borderRadius: 10, background: "var(--color-bg-panel)" }}>
            <table style={{ width: "100%", borderCollapse: "collapse" }}>
              <thead>
                <tr>
                  {["Mã", "Tên bài", "Chủ đề", "Vị trí", "Độ khó", "Giới hạn", "Điểm", ""].map((h, i) => (
                    <th key={i} style={{ padding: "9px 14px", textAlign: i === 7 ? "right" : "left", fontFamily: "var(--font-mono)", fontSize: 10, fontWeight: 600, color: "var(--color-text-muted)", textTransform: "uppercase", letterSpacing: "0.09em", borderBottom: "1px solid var(--color-border)", background: "var(--color-bg-raised)", whiteSpace: "nowrap", position: "sticky", top: 0 }}>{h}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {visibleProblems.length === 0
                  ? <tr><td colSpan={8} style={{ padding: 52, textAlign: "center", color: "var(--color-text-muted)", fontFamily: "var(--font-mono)", fontSize: 13 }}>{problems.length === 0 ? "Chưa có bài tập nào. Bấm \"Add Problem\"." : "Chủ đề này chưa có bài nào."}</td></tr>
                  : visibleProblems.map((p, idx) => {
                    const { index, size } = placeOf(p);
                    const diff = DIFFICULTY_META[p.difficulty];
                    // Bai gan ma chu de la: backend khong nhan ma do, phai sua qua nut "Sửa".
                    const movable = movingId === null && (p.topic === "" || known.has(p.topic));
                    return (
                      <tr key={p.id} style={{ borderBottom: idx < visibleProblems.length - 1 ? "1px solid var(--color-border-subtle)" : "none", opacity: movingId === p.id ? 0.5 : 1 }}>
                        <td style={{ padding: "8px 14px" }}><span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-maroon)", fontWeight: 700 }}>{p.id}</span></td>
                        <td style={{ padding: "8px 14px" }}><span style={{ fontSize: 13, fontWeight: 500, color: "var(--color-text-primary)" }}>{p.title}</span></td>
                        <td style={{ padding: "8px 14px", whiteSpace: "nowrap" }}><span style={{ fontSize: 12, color: "var(--color-text-secondary)" }}>{topicLabel(p)}</span></td>
                        <td style={{ padding: "8px 14px", whiteSpace: "nowrap" }}><span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-secondary)" }}>{index}/{size}</span></td>
                        <td style={{ padding: "8px 14px" }}>
                          {diff
                            ? <span style={{ fontSize: 11, fontWeight: 600, color: diff.color, background: diff.bg, borderRadius: 5, padding: "2px 8px", whiteSpace: "nowrap" }}>{diff.label}</span>
                            : <span style={{ fontSize: 12, color: "var(--color-text-muted)" }}>—</span>}
                        </td>
                        <td style={{ padding: "8px 14px", whiteSpace: "nowrap" }}><span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-secondary)" }}>{p.timeLimitMs} ms / {p.memoryLimitMb} MB</span></td>
                        <td style={{ padding: "8px 14px" }}><span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-secondary)" }}>{p.maxPoints.toFixed(0)}</span></td>
                        <td style={{ padding: "8px 14px" }}>
                          <div style={{ display: "flex", justifyContent: "flex-end", gap: 6 }}>
                            <button title="Lên trước một bậc" onClick={() => void move(p, -1)} disabled={!movable || index <= 1} style={arrowBtn(movable && index > 1)}>↑</button>
                            <button title="Xuống sau một bậc" onClick={() => void move(p, 1)} disabled={!movable || index >= size} style={arrowBtn(movable && index < size)}>↓</button>
                            <button onClick={() => setEditProblem(p)} style={ROW_BTN}>Sửa</button>
                          </div>
                        </td>
                      </tr>
                    );
                  })}
              </tbody>
            </table>
          </div>
          <div style={{ fontFamily: "var(--font-mono)", fontSize: 10.5, color: "var(--color-text-muted)" }}>
            Bảng xếp theo đúng thứ tự lộ trình học sinh thấy. ↑ ↓ đổi chỗ trong chủ đề; "Sửa" để đổi chủ đề, độ khó hoặc vị trí. Chưa có API sửa đề, test hay xoá bài.
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
        <ProblemEditor topics={topics} onClose={() => setShowProblemEditor(false)} onCreated={() => void onProblemsChanged()} />
      )}
      {editProblem && (
        <ProblemMetaEditor problem={editProblem} problems={problems} topics={topics} onClose={() => setEditProblem(null)} onSaved={onProblemsChanged} />
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

function arrowBtn(enabled: boolean): React.CSSProperties {
  return { ...ROW_BTN, padding: "0 8px", fontSize: 13, opacity: enabled ? 1 : 0.35, cursor: enabled ? "pointer" : "not-allowed" };
}

const FILTER: React.CSSProperties = {
  height: 32, padding: "0 10px", background: "var(--color-bg-panel)", border: "1px solid var(--color-border)",
  borderRadius: 7, color: "var(--color-text-primary)", fontFamily: "var(--font-sans)", fontSize: 12.5, outline: "none",
};
