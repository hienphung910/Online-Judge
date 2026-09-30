import { useEffect, useMemo, useState } from "react";
import { api } from "../api";
import { useAuth } from "../auth";
import type { LanguageInfo, Problem, Submission } from "../types";
import ProblemDetail from "./ProblemDetail";

type Status = "solved" | "attempted" | "unsolved";

export default function Problems({
  problems,
  languages,
  onSubmitted,
  reloadKey,
}: {
  problems: Problem[];
  languages: LanguageInfo[];
  onSubmitted: () => void;
  reloadKey: number;
}) {
  const { user } = useAuth();
  const [search, setSearch] = useState("");
  const [hov, setHov] = useState<string | null>(null);
  const [selected, setSelected] = useState<Problem | null>(null);
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

  const filtered = useMemo(() => {
    if (!search.trim()) return problems;
    const q = search.toLowerCase();
    return problems.filter((p) => p.title.toLowerCase().includes(q) || p.id.toLowerCase().includes(q));
  }, [problems, search]);

  const solvedCount = problems.filter((p) => statusByProblem.get(p.id) === "solved").length;

  if (selected) {
    return <ProblemDetail problem={selected} languages={languages} onBack={() => setSelected(null)} onSubmitted={onSubmitted} />;
  }

  return (
    <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden" }}>


      {/* ═══ CLASS SECTION ═══ */}
      <div style={{ padding: "12px 24px 8px", display: "flex", alignItems: "center", justifyContent: "space-between", flexShrink: 0 }}>
        <div style={{ fontSize: 14, fontWeight: 600, color: "#212121" }}>Lớp học của tôi</div>
        <div style={{ fontSize: 12, color: "#757575", background: "#fff", border: "1px solid #E0E0E0", borderRadius: 6, padding: "6px 14px" }}>
          CodeForge — Luyện tập lập trình
        </div>
      </div>

      {/* ═══ SEARCH BAR ═══ */}
      <div style={{ padding: "8px 24px", flexShrink: 0 }}>
        <div style={{ position: "relative", maxWidth: 280 }}>
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
      </div>

      {/* ═══ PROBLEMS TABLE ═══ */}
      <div style={{ flex: 1, overflow: "auto", margin: "0 24px 16px", background: "#fff", border: "1px solid #E0E0E0", borderRadius: 8 }}>
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr style={{ background: "var(--color-table-header-bg)" }}>
              <th style={TH_S}>TT</th>
              <th style={{ ...TH_S, textAlign: "left" }}>Mã</th>
              <th style={{ ...TH_S, textAlign: "left", width: "auto" }}>Tên đề</th>
              <th style={TH_S}>
                <span style={{ display: "flex", alignItems: "center", gap: 4 }}>
                  Chủ đề
                  <svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="#9E9E9E" strokeWidth="1.5"><path d="M2 4l3 3 3-3" /></svg>
                </span>
              </th>
              <th style={TH_S}>
                <span style={{ display: "flex", alignItems: "center", gap: 4 }}>
                  Chủ đề con
                  <svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="#9E9E9E" strokeWidth="1.5"><path d="M2 4l3 3 3-3" /></svg>
                </span>
              </th>
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
              return (
                <tr
                  key={p.id}
                  onMouseEnter={() => setHov(p.id)} onMouseLeave={() => setHov(null)}
                  onClick={() => setSelected(p)}
                  style={{ background: rowBg, cursor: "pointer", borderBottom: "1px solid #F5F5F5", transition: "background 0.1s" }}
                >
                  <td style={{ ...TD_S, textAlign: "center", width: 44, color: "#9E9E9E" }}>{idx + 1}</td>
                  <td style={{ ...TD_S, width: 100 }}>
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
                  </td>
                  <td style={{ ...TD_S, color: "#616161", fontSize: 12.5 }}>NGÔN NGỮ JAVA</td>
                  <td style={{ ...TD_S, color: "#616161", fontSize: 12.5 }}>LẬP TRÌNH JAVA CƠ BẢN</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      {/* ═══ PROGRESS BAR ═══ */}
      <div style={{ padding: "0 24px 12px", flexShrink: 0 }}>
        <div style={{ height: 6, background: "#E0E0E0", borderRadius: 3, overflow: "hidden" }}>
          <div style={{
            height: "100%", borderRadius: 3,
            width: problems.length > 0 ? `${(solvedCount / problems.length) * 100}%` : "0%",
            background: "linear-gradient(90deg, #66BB6A, #43A047)",
            transition: "width 0.5s ease",
          }} />
        </div>
      </div>
    </div>
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
