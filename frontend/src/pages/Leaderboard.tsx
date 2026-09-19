import { useCallback, useEffect, useState } from "react";
import { api } from "../api";
import { Button, MONO, Panel, RefIco, StatCard, TD, TH, VERDICT_META, ErrorBox } from "../components/ui";
import type { Problem, ScoreRow, Stats, VerdictCode } from "../types";

export default function Leaderboard({ reloadKey, problems }: { reloadKey: number; problems: Problem[] }) {
  const [rows, setRows] = useState<ScoreRow[]>([]);
  const [stats, setStats] = useState<Stats | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const load = useCallback(async () => {
    setLoading(true);
    try {
      const [r, s] = await Promise.all([api.scoreboard(), api.stats()]);
      setRows(r);
      setStats(s);
      setError("");
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => { void load(); }, [load, reloadKey]);

  const verdictEntries = stats
    ? (Object.entries(stats.byVerdict) as [VerdictCode, number][]).sort((a, b) => b[1] - a[1])
    : [];

  return (
    <div style={{ flex: 1, display: "flex", flexDirection: "column", padding: "24px 32px", gap: 16, overflow: "auto" }}>
      <h1 style={{ fontFamily: "var(--font-serif)", fontSize: 26, fontWeight: 700, color: "var(--color-maroon)", margin: 0, letterSpacing: "-0.02em" }}>Bảng xếp hạng</h1>

      <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
        <StatCard label="Thí sinh" value={rows.length} />
        <StatCard label="Bài nộp" value={stats?.totalSubmissions ?? 0} />
        <StatCard label="Điểm cao nhất" value={rows.length > 0 ? rows[0].total.toFixed(1) : "—"} sub={rows.length > 0 ? `@${rows[0].username}` : undefined} color="var(--color-green)" />
        {verdictEntries.slice(0, 3).map(([code, count]) => (
          <StatCard key={code} label={code} value={count} color={VERDICT_META[code]?.color} />
        ))}
      </div>

      <Panel title="Bảng xếp hạng (lấy điểm cao nhất của mỗi bài)" right={<Button onClick={() => void load()}><RefIco spinning={loading} /></Button>}>
        {error && <ErrorBox message={error} />}
        <div style={{ overflowX: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse", minWidth: 720 }}>
            <thead>
              <tr>
                <th style={TH}>Hạng</th>
                <th style={TH}>Thí sinh</th>
                <th style={TH}>Họ tên</th>
                {problems.map((p) => <th key={p.id} style={{ ...TH, textAlign: "center" }}>{p.id}</th>)}
                <th style={{ ...TH, textAlign: "right" }}>Tổng điểm</th>
                <th style={{ ...TH, textAlign: "center" }}>AC</th>
                <th style={{ ...TH, textAlign: "center" }}>Số lần</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((r) => (
                <tr key={r.username}>
                  <td style={{ ...TD, ...MONO, color: r.rank === 1 ? "var(--color-amber)" : "var(--color-text-secondary)", fontWeight: r.rank === 1 ? 700 : 400 }}>#{r.rank}</td>
                  <td style={{ ...TD, ...MONO, color: "var(--color-maroon)" }}>@{r.username}</td>
                  <td style={{ ...TD, color: "var(--color-text-primary)" }}>{r.fullName}</td>
                  {problems.map((p) => {
                    const cell = r.perProblem.find((x) => x.problemId === p.id);
                    const full = cell !== undefined && cell.score >= p.maxPoints - 1e-9;
                    return (
                      <td key={p.id} style={{ ...TD, ...MONO, textAlign: "center", color: cell === undefined ? "var(--color-text-muted)" : full ? "var(--color-green)" : "var(--color-amber)" }}>
                        {cell === undefined ? "—" : cell.score.toFixed(0)}
                      </td>
                    );
                  })}
                  <td style={{ ...TD, ...MONO, textAlign: "right", color: "var(--color-text-primary)", fontWeight: 600 }}>{r.total.toFixed(1)}</td>
                  <td style={{ ...TD, ...MONO, textAlign: "center", color: "var(--color-green)" }}>{r.solved}</td>
                  <td style={{ ...TD, ...MONO, textAlign: "center" }}>{r.attempts}</td>
                </tr>
              ))}
              {rows.length === 0 && (
                <tr><td style={{ ...TD, ...MONO, color: "var(--color-text-muted)" }} colSpan={6 + problems.length}>Chưa có dữ liệu. Hãy nộp một bài.</td></tr>
              )}
            </tbody>
          </table>
        </div>
      </Panel>

      {verdictEntries.length > 0 && (
        <Panel title="Thống kê verdict của cả phiên chấm" right={<span style={{ ...MONO, fontSize: 11, color: "var(--color-text-muted)" }}>{stats?.totalSubmissions ?? 0} bài nộp</span>}>
          <div style={{ padding: 14, display: "flex", flexDirection: "column", gap: 9 }}>
            {verdictEntries.map(([code, count]) => {
              const meta = VERDICT_META[code] ?? VERDICT_META.IE;
              const total = stats?.totalSubmissions || 1;
              const percent = (count / total) * 100;
              return (
                <div key={code} title={`${code} — ${meta.label}: ${count}/${total} bài nộp (${percent.toFixed(1)}%)`} style={{ display: "flex", alignItems: "center", gap: 10 }}>
                  <span style={{ ...MONO, fontSize: 11.5, fontWeight: 700, color: meta.color, width: 42 }}>{code}</span>
                  <span style={{ ...MONO, fontSize: 11, color: "var(--color-text-muted)", width: 160 }}>{meta.label}</span>
                  <div style={{ flex: 1, height: 8, background: "var(--color-bg-raised)", borderRadius: 4 }}>
                    <div style={{ width: `${Math.max(percent, count > 0 ? 1.5 : 0)}%`, height: "100%", background: meta.color, borderRadius: "0 4px 4px 0", transition: "width 0.3s ease-out" }} />
                  </div>
                  <span style={{ ...MONO, fontSize: 11.5, color: "var(--color-text-primary)", width: 34, textAlign: "right" }}>{count}</span>
                  <span style={{ ...MONO, fontSize: 11, color: "var(--color-text-muted)", width: 48, textAlign: "right" }}>{percent.toFixed(0)}%</span>
                </div>
              );
            })}
          </div>
        </Panel>
      )}
    </div>
  );
}
