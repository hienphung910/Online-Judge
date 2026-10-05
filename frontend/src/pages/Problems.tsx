import { useEffect, useMemo, useState } from "react";
import { api } from "../api";
import { useAuth } from "../auth";
import { DIFFICULTY_META, OTHER_TOPIC, orderByPath, topicKey } from "../learningPath";
import type { LanguageInfo, Problem, Submission, Topic } from "../types";
import ProblemDetail from "./ProblemDetail";

type Status = "solved" | "attempted" | "unsolved";
interface Progress { total: number; solved: number }

export default function Problems({
  problems,
  topics,
  languages,
  onSubmitted,
  reloadKey,
}: {
  problems: Problem[];
  topics: Topic[];
  languages: LanguageInfo[];
  onSubmitted: () => void;
  reloadKey: number;
}) {
  const { user } = useAuth();
  const [search, setSearch] = useState("");
  /** "" = tat ca, ma chu de, hoac OTHER_TOPIC. */
  const [topicFilter, setTopicFilter] = useState("");
  /** 0 = moi do kho. */
  const [diffFilter, setDiffFilter] = useState(0);
  const [hov, setHov] = useState<string | null>(null);
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [mySubs, setMySubs] = useState<Submission[]>([]);

  useEffect(() => {
    let alive = true;
    if (!user) return;
    api.submissions()
      .then((subs) => { if (alive) setMySubs(subs.filter((s) => s.author === user.username)); })
      .catch(() => undefined);
    return () => { alive = false; };
  }, [user, reloadKey]);

  const statusByProblem = useMemo(() => {
    const map = new Map<string, Status>();
    for (const s of mySubs) {
      const cur = map.get(s.problem.id);
      if (s.verdict === "AC") map.set(s.problem.id, "solved");
      else if (cur !== "solved") map.set(s.problem.id, "attempted");
    }
    return map;
  }, [mySubs]);

  const known = useMemo(() => new Set(topics.map((t) => t.id)), [topics]);
  const topicName = useMemo(() => new Map(topics.map((t) => [t.id, t.name])), [topics]);
  const ordered = useMemo(() => orderByPath(problems, topics), [problems, topics]);

  const progress = useMemo(() => {
    const map = new Map<string, Progress>();
    for (const p of ordered) {
      const key = topicKey(p, known);
      const cur = map.get(key) ?? { total: 0, solved: 0 };
      cur.total++;
      if (statusByProblem.get(p.id) === "solved") cur.solved++;
      map.set(key, cur);
    }
    return map;
  }, [ordered, known, statusByProblem]);

  const filtered = useMemo(() => {
    const q = search.trim().toLowerCase();
    return ordered.filter((p) =>
      (!topicFilter || topicKey(p, known) === topicFilter)
      && (!diffFilter || p.difficulty === diffFilter)
      && (!q || p.title.toLowerCase().includes(q) || p.id.toLowerCase().includes(q)),
    );
  }, [ordered, known, topicFilter, diffFilter, search]);

  const solvedAll = ordered.filter((p) => statusByProblem.get(p.id) === "solved").length;
  const solvedInView = filtered.filter((p) => statusByProblem.get(p.id) === "solved").length;
  // Bai dau tien chua giai theo dung thu tu lo trinh -> goi y "hoc tiep".
  const nextToLearn = ordered.find((p) => statusByProblem.get(p.id) !== "solved") ?? null;
  const hasOther = progress.has(OTHER_TOPIC);
  const currentTopic = topics.find((t) => t.id === topicFilter);
  const nameOf = (p: Problem) => topicName.get(p.topic) ?? "Bài khác";

  const selected = selectedId ? problems.find((p) => p.id === selectedId) ?? null : null;
  if (selected) {
    // "Bai tiep theo": trong danh sach dang loc neu bai nam trong do, khong thi theo lo trinh chung.
    const list = filtered.some((p) => p.id === selected.id) ? filtered : ordered;
    const next = list[list.findIndex((p) => p.id === selected.id) + 1] ?? null;
    return (
      <ProblemDetail
        key={selected.id}
        problem={selected}
        languages={languages}
        topicName={nameOf(selected)}
        nextProblem={next}
        onNext={() => next && setSelectedId(next.id)}
        onBack={() => setSelectedId(null)}
        onSubmitted={onSubmitted}
      />
    );
  }

  return (
    <div style={{ flex: 1, display: "flex", overflow: "hidden" }}>
      {/* ═══ LO TRINH HOC ═══ */}
      <aside style={{
        width: 280, flexShrink: 0, background: "#fff", borderRight: "1px solid #E0E0E0",
        display: "flex", flexDirection: "column", overflow: "hidden",
      }}>
        <div style={{ padding: "16px 16px 12px", borderBottom: "1px solid #F0F0F0" }}>
          <div style={{ fontSize: 14, fontWeight: 700, color: "#212121" }}>Lộ trình học</div>
          <div style={{ fontSize: 12, color: "#757575", marginTop: 2 }}>
            Đã giải <b style={{ color: "var(--color-green)" }}>{solvedAll}</b>/{ordered.length} bài
          </div>
          <Bar value={solvedAll} total={ordered.length} />

          {nextToLearn && (
            <button
              onClick={() => setSelectedId(nextToLearn.id)}
              style={{
                width: "100%", marginTop: 12, padding: "10px 12px", textAlign: "left", cursor: "pointer",
                background: "#FDECEA", border: "1px solid #F5C6C2", borderRadius: 8,
              }}
            >
              <div style={{ fontSize: 10, fontWeight: 700, letterSpacing: "0.08em", color: "var(--color-red)" }}>
                {solvedAll === 0 ? "BẮT ĐẦU HỌC" : "HỌC TIẾP"} →
              </div>
              <div style={{ fontSize: 13, fontWeight: 600, color: "#212121", marginTop: 3, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                <span style={{ fontFamily: "var(--font-mono)", color: "var(--color-red)" }}>{nextToLearn.id}</span> {nextToLearn.title}
              </div>
              <div style={{ fontSize: 11, color: "#9E9E9E", marginTop: 2 }}>{nameOf(nextToLearn)}</div>
            </button>
          )}
        </div>

        <nav style={{ flex: 1, overflowY: "auto", padding: "8px 0" }}>
          <StepRow
            label="Tất cả bài tập"
            progress={{ total: ordered.length, solved: solvedAll }}
            active={topicFilter === ""}
            onClick={() => setTopicFilter("")}
          />
          {topics.map((t, i) => (
            <StepRow
              key={t.id}
              step={t.order}
              label={t.name}
              progress={progress.get(t.id) ?? { total: 0, solved: 0 }}
              active={topicFilter === t.id}
              first={i === 0}
              last={i === topics.length - 1}
              onClick={() => setTopicFilter(t.id)}
            />
          ))}
          {hasOther && (
            <StepRow
              label="Bài khác"
              progress={progress.get(OTHER_TOPIC)!}
              active={topicFilter === OTHER_TOPIC}
              onClick={() => setTopicFilter(OTHER_TOPIC)}
            />
          )}
        </nav>
      </aside>

      {/* ═══ DANH SACH BAI ═══ */}
      <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden" }}>
        <div style={{ padding: "12px 24px 8px", display: "flex", alignItems: "center", justifyContent: "space-between", gap: 16, flexShrink: 0 }}>
          <div style={{ minWidth: 0 }}>
            <div style={{ fontSize: 14, fontWeight: 600, color: "#212121" }}>
              {currentTopic ? `Chặng ${currentTopic.order}: ${currentTopic.name}` : topicFilter === OTHER_TOPIC ? "Bài khác" : "Lớp học của tôi"}
            </div>
            {currentTopic?.description && (
              <div style={{ fontSize: 12, color: "#757575", marginTop: 2 }}>{currentTopic.description}</div>
            )}
          </div>
          <div style={{ fontSize: 12, color: "#757575", background: "#fff", border: "1px solid #E0E0E0", borderRadius: 6, padding: "6px 14px", flexShrink: 0 }}>
            CodeForge — Luyện tập lập trình
          </div>
        </div>

        {/* ═══ SEARCH + DO KHO ═══ */}
        <div style={{ padding: "8px 24px", flexShrink: 0, display: "flex", alignItems: "center", gap: 12, flexWrap: "wrap" }}>
          <div style={{ position: "relative", width: 280 }}>
            <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#BDBDBD" strokeWidth="1.5" style={{ position: "absolute", left: 10, top: "50%", transform: "translateY(-50%)" }}>
              <circle cx="6.5" cy="6.5" r="4.5" /><line x1="10" y1="10" x2="14" y2="14" />
            </svg>
            <input
              type="text" placeholder="Tìm mã / tên bài" value={search} onChange={(e) => setSearch(e.target.value)}
              style={{
                width: "100%", height: 34, paddingLeft: 32, paddingRight: 10,
                background: "#fff", border: "1px solid #E0E0E0", borderRadius: 6,
                fontSize: 13, color: "#212121", outline: "none", boxSizing: "border-box",
              }}
              onFocus={(e) => { e.target.style.borderColor = "#C62828"; }}
              onBlur={(e) => { e.target.style.borderColor = "#E0E0E0"; }}
            />
          </div>
          <div style={{ display: "flex", gap: 6 }}>
            {[0, 1, 2, 3].map((d) => {
              const on = diffFilter === d;
              const meta = DIFFICULTY_META[d];
              return (
                <button key={d} onClick={() => setDiffFilter(d)} style={{
                  height: 30, padding: "0 12px", borderRadius: 15, cursor: "pointer", fontSize: 12, fontWeight: on ? 700 : 500,
                  border: `1px solid ${on ? (meta?.color ?? "var(--color-red)") : "#E0E0E0"}`,
                  background: on ? (meta?.bg ?? "#FDECEA") : "#fff",
                  color: on ? (meta?.color ?? "var(--color-red)") : "#616161",
                }}>
                  {meta?.label ?? "Mọi mức"}
                </button>
              );
            })}
          </div>
        </div>

        {/* ═══ PROBLEMS TABLE ═══ */}
        <div style={{ flex: 1, overflow: "auto", margin: "0 24px 12px", background: "#fff", border: "1px solid #E0E0E0", borderRadius: 8 }}>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ background: "var(--color-table-header-bg)" }}>
                <th style={TH_S}>TT</th>
                <th style={{ ...TH_S, textAlign: "left" }}>Mã</th>
                <th style={{ ...TH_S, textAlign: "left", width: "auto" }}>Tên đề</th>
                <th style={{ ...TH_S, textAlign: "left" }}>Chủ đề</th>
                <th style={TH_S}>Độ khó</th>
              </tr>
            </thead>
            <tbody>
              {filtered.length === 0 ? (
                <tr><td colSpan={5} style={{ padding: 40, textAlign: "center", color: "#9E9E9E", fontSize: 13 }}>
                  {problems.length === 0 ? "Chưa có bài tập nào." : "Không tìm thấy bài phù hợp."}
                </td></tr>
              ) : filtered.map((p, idx) => {
                const isHov = hov === p.id;
                const status = statusByProblem.get(p.id) ?? "unsolved";
                const rowBg = isHov ? "var(--color-table-hover)" : idx % 2 === 1 ? "var(--color-table-row-alt)" : "#fff";
                const diff = DIFFICULTY_META[p.difficulty];
                return (
                  <tr
                    key={p.id}
                    onMouseEnter={() => setHov(p.id)} onMouseLeave={() => setHov(null)}
                    onClick={() => setSelectedId(p.id)}
                    style={{ background: rowBg, cursor: "pointer", borderBottom: "1px solid #F5F5F5", transition: "background 0.1s" }}
                  >
                    <td style={{ ...TD_S, textAlign: "center", width: 44, color: "#9E9E9E" }}>{idx + 1}</td>
                    <td style={{ ...TD_S, width: 90 }}>
                      <span style={{
                        fontFamily: "var(--font-mono)", fontSize: 12, fontWeight: 600,
                        color: status === "solved" ? "var(--color-green)" : "var(--color-red)",
                      }}>
                        {p.id}
                      </span>
                    </td>
                    <td style={TD_S}>
                      <span style={{
                        fontSize: 13, fontWeight: 500,
                        color: status === "solved" ? "var(--color-green)" : isHov ? "var(--color-red)" : "#212121",
                      }}>
                        {status === "solved" && <span style={{ marginRight: 4 }}>✓</span>}
                        {p.title}
                      </span>
                      {status === "attempted" && <span style={{ marginLeft: 8, fontSize: 11, color: "#E65100" }}>đang làm</span>}
                    </td>
                    <td style={{ ...TD_S, color: "#616161", fontSize: 12.5, whiteSpace: "nowrap" }}>{nameOf(p)}</td>
                    <td style={{ ...TD_S, textAlign: "center", width: 80 }}>
                      {diff ? (
                        <span style={{ fontSize: 11.5, fontWeight: 700, padding: "2px 10px", borderRadius: 10, color: diff.color, background: diff.bg }}>
                          {diff.label}
                        </span>
                      ) : <span style={{ color: "#BDBDBD" }}>—</span>}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>

        {/* ═══ PROGRESS BAR ═══ */}
        <div style={{ padding: "0 24px 12px", flexShrink: 0, display: "flex", alignItems: "center", gap: 12 }}>
          <div style={{ flex: 1 }}><Bar value={solvedInView} total={filtered.length} height={6} /></div>
          <span style={{ fontSize: 12, color: "#757575", fontFamily: "var(--font-mono)", whiteSpace: "nowrap" }}>
            {solvedInView}/{filtered.length} bài đã giải
          </span>
        </div>
      </div>
    </div>
  );
}

function Bar({ value, total, height = 4 }: { value: number; total: number; height?: number }) {
  return (
    <div style={{ height, background: "#EEEEEE", borderRadius: height / 2, overflow: "hidden", marginTop: height === 4 ? 8 : 0 }}>
      <div style={{
        height: "100%", borderRadius: height / 2,
        width: total > 0 ? `${(value / total) * 100}%` : "0%",
        background: "linear-gradient(90deg, #66BB6A, #43A047)",
        transition: "width 0.5s ease",
      }} />
    </div>
  );
}

/** Mot chang tren lo trinh: vong tron so thu tu noi voi nhau bang mot duong doc. */
function StepRow({
  step, label, progress, active, first, last, onClick,
}: {
  step?: number; label: string; progress: Progress; active: boolean;
  first?: boolean; last?: boolean; onClick: () => void;
}) {
  const done = progress.total > 0 && progress.solved === progress.total;
  const started = progress.solved > 0;
  const ringColor = done ? "var(--color-green)" : started ? "var(--color-red)" : "#E0E0E0";
  return (
    <button
      onClick={onClick}
      style={{
        position: "relative", width: "100%", display: "flex", alignItems: "center", gap: 10,
        padding: "8px 16px 8px 13px", border: "none", cursor: "pointer", textAlign: "left",
        background: active ? "#FDECEA" : "transparent",
        borderLeft: `3px solid ${active ? "var(--color-red)" : "transparent"}`,
      }}
    >
      {step !== undefined && (
        <span style={{
          position: "absolute", left: 26, width: 2, background: "#EEEEEE",
          top: first ? "50%" : 0, bottom: last ? "50%" : 0,
        }} />
      )}
      <span style={{
        position: "relative", zIndex: 1, width: 28, height: 28, borderRadius: "50%", flexShrink: 0,
        display: "flex", alignItems: "center", justifyContent: "center",
        fontSize: 12, fontWeight: 700, boxSizing: "border-box",
        background: done ? "var(--color-green)" : "#fff",
        border: `2px solid ${ringColor}`,
        color: done ? "#fff" : started ? "var(--color-red)" : "#9E9E9E",
      }}>
        {step === undefined ? "≡" : done ? "✓" : step}
      </span>
      <span style={{ flex: 1, minWidth: 0 }}>
        <span style={{
          display: "block", fontSize: 13, fontWeight: active ? 700 : 500, color: "#212121",
          overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap",
        }}>{label}</span>
        <span style={{ display: "flex", alignItems: "center", gap: 6, marginTop: 3 }}>
          <span style={{ flex: 1, height: 3, background: "#EEEEEE", borderRadius: 2, overflow: "hidden" }}>
            <span style={{
              display: "block", height: "100%", background: done ? "var(--color-green)" : "#EF9A9A",
              width: progress.total > 0 ? `${(progress.solved / progress.total) * 100}%` : "0%",
            }} />
          </span>
          <span style={{ fontSize: 10.5, color: "#9E9E9E", fontFamily: "var(--font-mono)" }}>{progress.solved}/{progress.total}</span>
        </span>
      </span>
    </button>
  );
}

const TH_S: React.CSSProperties = {
  padding: "10px 14px", fontSize: 12, fontWeight: 700, color: "#757575",
  textAlign: "center", whiteSpace: "nowrap", textTransform: "uppercase",
  borderBottom: "1px solid var(--color-table-border)",
  position: "sticky", top: 0, zIndex: 2, background: "var(--color-table-header-bg)",
};

const TD_S: React.CSSProperties = {
  padding: "10px 14px", fontSize: 13, verticalAlign: "middle",
};
