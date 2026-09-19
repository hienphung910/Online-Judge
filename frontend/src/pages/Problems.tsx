import { useEffect, useMemo, useState } from "react";
import { api } from "../api";
import { useAuth } from "../auth";
import type { LanguageInfo, Problem, Submission } from "../types";
import ProblemDetail from "./ProblemDetail";
import { SearchIco, XIco } from "../components/ui";

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

  // Trang thai "da giai / da thu / chua lam" cua CHINH minh, suy tu lich su nop bai.
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
  const pct = problems.length > 0 ? Math.round((solvedCount / problems.length) * 100) : 0;

  if (selected) {
    return (
      <ProblemDetail
        problem={selected}
        languages={languages}
        onBack={() => setSelected(null)}
        onSubmitted={onSubmitted}
      />
    );
  }

  return (
    <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden", padding: "0 32px 24px" }}>
      <div style={{ paddingTop: 28, paddingBottom: 20, borderBottom: "1px solid var(--color-border)", marginBottom: 24 }}>
        <h1 style={{ fontFamily: "var(--font-serif)", fontSize: 30, fontWeight: 700, color: "var(--color-maroon)", margin: "0 0 4px", letterSpacing: "-0.02em" }}>Problem Set</h1>
        <p style={{ fontFamily: "var(--font-sans)", fontSize: 14, color: "var(--color-text-muted)", margin: 0 }}>Luyện tập các bài toán thuật toán và theo dõi tiến độ của bạn.</p>
      </div>

      <div style={{ display: "flex", gap: 14, marginBottom: 24, flexWrap: "wrap" }}>
        <div style={{ background: "var(--color-bg-panel)", border: "1px solid var(--color-border)", borderRadius: 10, padding: "16px 20px", display: "flex", alignItems: "center", gap: 20 }}>
          <div style={{ position: "relative", width: 58, height: 58, flexShrink: 0 }}>
            <svg width="58" height="58" viewBox="0 0 58 58">
              <circle cx="29" cy="29" r="24" fill="none" stroke="var(--color-bg-raised)" strokeWidth="5" />
              <circle cx="29" cy="29" r="24" fill="none" stroke="var(--color-maroon)" strokeWidth="5" strokeLinecap="round"
                strokeDasharray={`${2 * Math.PI * 24}`} strokeDashoffset={`${2 * Math.PI * 24 * (1 - pct / 100)}`} transform="rotate(-90 29 29)" />
            </svg>
            <div style={{ position: "absolute", inset: 0, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center" }}>
              <span style={{ fontFamily: "var(--font-mono)", fontSize: 13, fontWeight: 700, color: "var(--color-maroon)", lineHeight: 1 }}>{pct}%</span>
            </div>
          </div>
          <div>
            <div style={{ fontFamily: "var(--font-serif)", fontSize: 22, fontWeight: 700, color: "var(--color-maroon)", lineHeight: 1 }}>
              {solvedCount}<span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-muted)", fontWeight: 400 }}> / {problems.length}</span>
            </div>
            <div style={{ fontFamily: "var(--font-sans)", fontSize: 12, color: "var(--color-text-muted)", marginTop: 3 }}>bài đã giải</div>
          </div>
        </div>
      </div>

      <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 12, flexWrap: "wrap" }}>
        <div style={{ position: "relative", flex: 1, minWidth: 220, maxWidth: 380 }}>
          <span style={{ position: "absolute", left: 11, top: "50%", transform: "translateY(-50%)", color: "var(--color-text-muted)", pointerEvents: "none", display: "flex" }}><SearchIco /></span>
          <input
            type="text" placeholder="Tìm theo tên hoặc mã bài…" value={search} onChange={(e) => setSearch(e.target.value)}
            style={{ width: "100%", height: 34, paddingLeft: 34, paddingRight: search ? 30 : 12, background: "var(--color-bg-panel)", border: "1px solid var(--color-border)", borderRadius: 7, color: "var(--color-text-primary)", fontSize: 13, fontFamily: "var(--font-sans)", outline: "none", boxSizing: "border-box" }}
          />
          {search && <button onClick={() => setSearch("")} style={{ position: "absolute", right: 9, top: "50%", transform: "translateY(-50%)", background: "none", border: "none", color: "var(--color-text-muted)", cursor: "pointer", padding: 2, display: "flex", borderRadius: 3 }}><XIco size={10} /></button>}
        </div>
        <div style={{ flex: 1 }} />
        <span style={{ fontFamily: "var(--font-mono)", fontSize: 11, color: "var(--color-text-muted)" }}>{filtered.length} / {problems.length}</span>
      </div>

      <div style={{ flex: 1, overflow: "auto", border: "1px solid var(--color-border)", borderRadius: 10, background: "var(--color-bg-panel)" }}>
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr>
              <th style={{ ...TH_STYLE, width: 72, textAlign: "center" }}>Trạng thái</th>
              <th style={{ ...TH_STYLE, width: 100 }}>Mã bài</th>
              <th style={TH_STYLE}>Tên bài</th>
              <th style={{ ...TH_STYLE, width: 160 }}>Giới hạn</th>
              <th style={{ ...TH_STYLE, width: 100, textAlign: "right" }}>Điểm</th>
            </tr>
          </thead>
          <tbody>
            {filtered.length === 0 ? (
              <tr><td colSpan={5} style={{ padding: "52px 16px", textAlign: "center", color: "var(--color-text-muted)", fontFamily: "var(--font-mono)", fontSize: 13 }}>
                {problems.length === 0 ? "Chưa nạp được bài tập nào từ máy chủ." : "Không có bài nào khớp tìm kiếm."}
              </td></tr>
            ) : filtered.map((p) => {
              const isHov = hov === p.id;
              const status = statusByProblem.get(p.id) ?? "unsolved";
              return (
                <tr key={p.id} onMouseEnter={() => setHov(p.id)} onMouseLeave={() => setHov(null)} onClick={() => setSelected(p)}
                  style={{ borderBottom: "1px solid var(--color-border-subtle)", background: isHov ? "var(--color-bg-raised)" : "transparent", cursor: "pointer", transition: "background 0.12s" }}>
                  <td style={{ padding: "12px 16px", textAlign: "center" }}>
                    {status === "solved" && <CheckCircle />}
                    {status === "attempted" && <DashCircle />}
                  </td>
                  <td style={{ padding: "12px 16px" }}><span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-muted)" }}>{p.id}</span></td>
                  <td style={{ padding: "12px 16px" }}>
                    <span style={{ fontFamily: "var(--font-sans)", fontSize: 14, fontWeight: 500, color: isHov ? "var(--color-maroon)" : "var(--color-text-primary)" }}>{p.title}</span>
                  </td>
                  <td style={{ padding: "12px 16px" }}>
                    <span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-secondary)" }}>{p.timeLimitMs} ms / {p.memoryLimitMb} MB</span>
                  </td>
                  <td style={{ padding: "12px 16px", textAlign: "right" }}>
                    <span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-secondary)" }}>{p.maxPoints.toFixed(0)}</span>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}

const TH_STYLE: React.CSSProperties = {
  padding: "10px 16px", textAlign: "left", fontFamily: "var(--font-mono)", fontSize: 10, fontWeight: 600,
  color: "var(--color-text-muted)", textTransform: "uppercase", letterSpacing: "0.09em",
  borderBottom: "1px solid var(--color-border)", background: "var(--color-bg-raised)", whiteSpace: "nowrap",
};

function CheckCircle() {
  return (
    <svg width="15" height="15" viewBox="0 0 16 16" fill="none">
      <circle cx="8" cy="8" r="7" fill="var(--color-green-bg)" stroke="var(--color-green-border)" strokeWidth="1.2" />
      <polyline points="4.5 8.5 7 11 11.5 5.5" stroke="var(--color-green)" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}

function DashCircle() {
  return (
    <svg width="15" height="15" viewBox="0 0 16 16" fill="none">
      <circle cx="8" cy="8" r="7" fill="var(--color-amber-bg)" stroke="var(--color-amber-border)" strokeWidth="1.2" strokeDasharray="3 2" />
    </svg>
  );
}
