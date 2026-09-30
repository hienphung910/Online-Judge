import { useCallback, useEffect, useState } from "react";
import { api } from "../api";
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
      setRows(r); setStats(s); setError("");
    } catch (e) { setError(e instanceof Error ? e.message : String(e)); }
    finally { setLoading(false); }
  }, []);

  useEffect(() => { void load(); }, [load, reloadKey]);

  const top3 = rows.slice(0, 3);
  // Reorder for podium display: [#2, #1, #3]
  const podiumOrder = top3.length >= 3 ? [top3[1], top3[0], top3[2]] : top3;
  const PODIUM_COLORS = [
    { border: "#CE93D8", bg: "#F3E5F5", badge: "#9C27B0", medal: "🥈", height: 110 }, // #2
    { border: "#FFD54F", bg: "#FFFDE7", badge: "#F9A825", medal: "🥇", height: 140 }, // #1
    { border: "#FFAB91", bg: "#FBE9E7", badge: "#E65100", medal: "🥉", height: 95 },  // #3
  ];

  return (
    <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "auto" }}>
      {/* Header */}
      <div style={{
        display: "flex", alignItems: "center", justifyContent: "space-between",
        padding: "16px 24px", background: "#fff", borderBottom: "1px solid #E0E0E0", flexShrink: 0,
      }}>
        <div style={{ fontSize: 16, fontWeight: 700, color: "#212121" }}>Bảng xếp hạng lớp</div>
        <div style={{ fontSize: 12, color: "#757575", background: "#fff", border: "1px solid #E0E0E0", borderRadius: 6, padding: "6px 14px" }}>
          CodeForge — Luyện tập lập trình
        </div>
      </div>

      <div style={{ fontSize: 13, color: "#9E9E9E", padding: "12px 24px 0" }}>
        Tổng {problems.length} bài luyện tập
      </div>

      {error && (
        <div style={{ margin: "12px 24px", padding: "10px 14px", background: "#FFEBEE", border: "1px solid #FFCDD2", borderRadius: 6, fontSize: 13, color: "#C62828" }}>{error}</div>
      )}

      {/* ═══ PODIUM TOP 3 ═══ */}
      {top3.length >= 3 && (
        <div style={{ display: "flex", justifyContent: "center", alignItems: "flex-end", gap: 24, padding: "32px 24px 24px" }}>
          {podiumOrder.map((r, i) => {
            const cfg = PODIUM_COLORS[i];
            return (
              <div key={r.username} style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 8 }}>
                {/* Medal */}
                <div style={{ fontSize: 20 }}>{cfg.medal}</div>
                {/* Avatar circle */}
                <div style={{
                  width: i === 1 ? 72 : 60, height: i === 1 ? 72 : 60, borderRadius: "50%",
                  background: "#F5F5F5", border: `3px solid ${cfg.border}`,
                  display: "flex", alignItems: "center", justifyContent: "center",
                  color: "#9E9E9E", position: "relative",
                }}>
                  <svg width="28" height="28" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.2">
                    <circle cx="8" cy="5" r="3" /><path d="M2 14c0-3.3 2.7-6 6-6s6 2.7 6 6" />
                  </svg>
                  {/* Rank badge */}
                  <div style={{
                    position: "absolute", top: -4, right: -4,
                    width: 20, height: 20, borderRadius: "50%", background: cfg.badge,
                    display: "flex", alignItems: "center", justifyContent: "center",
                    fontSize: 10, fontWeight: 700, color: "#fff",
                  }}>{r.rank}</div>
                </div>
                {/* Name */}
                <div style={{ fontSize: 14, fontWeight: 700, color: "#212121", textAlign: "center" }}>{r.fullName || r.username}</div>
                <div style={{ fontSize: 11, color: "#9E9E9E", fontFamily: "var(--font-mono)" }}>{r.username}</div>
                {/* Score card */}
                <div style={{
                  width: i === 1 ? 140 : 120, height: cfg.height,
                  background: cfg.bg, border: `2px solid ${cfg.border}`, borderRadius: 10,
                  display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center",
                }}>
                  <div style={{ fontSize: i === 1 ? 36 : 30, fontWeight: 800, color: "#212121" }}>{r.solvedCount}</div>
                  <div style={{ fontSize: 12, color: "#757575" }}>bài</div>
                  <div style={{ fontSize: 13, fontWeight: 700, color: cfg.badge }}>#{r.rank}</div>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* ═══ RANKING TABLE ═══ */}
      <div style={{ margin: "0 24px 16px", background: "#fff", border: "1px solid #E0E0E0", borderRadius: 8 }}>
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr style={{ background: "var(--color-table-header-bg)" }}>
              <th style={TH}>Hạng</th>
              <th style={{ ...TH, textAlign: "left" }}>Sinh viên</th>
              <th style={TH}>Mã SV</th>
              <th style={TH}>Đã giải</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((r, idx) => (
              <tr key={r.username} style={{
                background: idx % 2 === 1 ? "var(--color-table-row-alt)" : "#fff",
                borderBottom: "1px solid #F5F5F5",
              }}>
                <td style={{ ...TD, textAlign: "center", fontWeight: 700, color: r.rank <= 3 ? "var(--color-red)" : "#757575" }}>{r.rank}</td>
                <td style={{ ...TD, textAlign: "left" }}>
                  <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                    <div style={{
                      width: 28, height: 28, borderRadius: "50%",
                      background: r.rank <= 3 ? "#FFCDD2" : "#F5F5F5",
                      display: "flex", alignItems: "center", justifyContent: "center",
                    }}>
                      <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke={r.rank <= 3 ? "#C62828" : "#9E9E9E"} strokeWidth="1.2">
                        <circle cx="8" cy="5" r="3" /><path d="M2 14c0-3.3 2.7-6 6-6s6 2.7 6 6" />
                      </svg>
                    </div>
                    <span style={{ fontSize: 13, fontWeight: 500, color: "#212121" }}>{r.fullName || r.username}</span>
                  </div>
                </td>
                <td style={{ ...TD, textAlign: "center", fontFamily: "var(--font-mono)", fontSize: 12, color: "#616161", fontWeight: 600 }}>{r.username}</td>
                <td style={{ ...TD, textAlign: "center" }}>
                  <span style={{ fontFamily: "var(--font-mono)", fontSize: 13, fontWeight: 700, color: "var(--color-red)" }}>{r.solvedCount}</span>
                </td>
              </tr>
            ))}
            {rows.length === 0 && (
              <tr><td colSpan={4} style={{ padding: 40, textAlign: "center", color: "#9E9E9E", fontSize: 13 }}>Chưa có dữ liệu.</td></tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

const TH: React.CSSProperties = {
  padding: "10px 14px", fontSize: 12, fontWeight: 700, color: "#757575",
  textAlign: "center", whiteSpace: "nowrap", borderBottom: "1px solid var(--color-table-border)",
  background: "var(--color-table-header-bg)",
};

const TD: React.CSSProperties = {
  padding: "10px 14px", fontSize: 13, verticalAlign: "middle",
};
