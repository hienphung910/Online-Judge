import { useEffect, useState } from "react";
import { contestStatus, useLocalContests, type Contest, type ContestStatus } from "../localContests";
import type { Problem } from "../types";
import { MONO } from "../components/ui";

const STATUS_COLOR: Record<ContestStatus, string> = {
  Active: "var(--color-green)",
  Upcoming: "var(--color-blue)",
  Completed: "var(--color-text-muted)",
};

function fmtDur(m: number) {
  const h = Math.floor(m / 60), r = m % 60;
  return h > 0 ? `${h}h${r > 0 ? " " + r + "m" : ""}` : r + "m";
}

function Countdown({ target }: { target: number }) {
  const [now, setNow] = useState(Date.now());
  useEffect(() => {
    const id = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(id);
  }, []);
  const diff = Math.max(0, target - now);
  const h = Math.floor(diff / 3600000);
  const m = Math.floor((diff % 3600000) / 60000);
  const s = Math.floor((diff % 60000) / 1000);
  return <span>{String(h).padStart(2, "0")}:{String(m).padStart(2, "0")}:{String(s).padStart(2, "0")}</span>;
}

export default function Contests({ problems }: { problems: Problem[] }) {
  const { contests } = useLocalContests();
  const byId = new Map(problems.map((p) => [p.id, p]));

  const sorted = [...contests].sort((a, b) => new Date(a.startTime).getTime() - new Date(b.startTime).getTime());

  return (
    <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "auto", padding: "0 32px 24px" }}>
      <div style={{ paddingTop: 28, paddingBottom: 20, borderBottom: "1px solid var(--color-border)", marginBottom: 20 }}>
        <h1 style={{ fontFamily: "var(--font-serif)", fontSize: 30, fontWeight: 700, color: "var(--color-maroon)", margin: "0 0 4px", letterSpacing: "-0.02em" }}>Contests</h1>
        <p style={{ fontFamily: "var(--font-sans)", fontSize: 14, color: "var(--color-text-muted)", margin: 0 }}>Danh sách cuộc thi.</p>
      </div>

      <div style={{ marginBottom: 20, padding: "10px 14px", background: "var(--color-amber-bg)", border: "1px solid var(--color-amber-border)", borderRadius: 8, ...MONO, fontSize: 12, color: "var(--color-amber)", lineHeight: 1.6 }}>
        Tính năng demo: dữ liệu cuộc thi chỉ lưu trong trình duyệt của bạn (localStorage), backend hiện chưa hỗ trợ contest nên không đồng bộ giữa các máy/người dùng.
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
        {sorted.length === 0 && (
          <div style={{ padding: 52, textAlign: "center", color: "var(--color-text-muted)", ...MONO, fontSize: 13, border: "1px solid var(--color-border)", borderRadius: 10, background: "var(--color-bg-panel)" }}>
            Chưa có cuộc thi nào. Quản trị viên có thể tạo ở trang Admin.
          </div>
        )}
        {sorted.map((c) => {
          const status = contestStatus(c);
          const start = new Date(c.startTime).getTime();
          const end = start + c.durationMins * 60000;
          return (
            <div key={c.id} style={{ background: "var(--color-bg-panel)", border: "1px solid var(--color-border)", borderRadius: 10, padding: "18px 22px" }}>
              <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between", gap: 12, marginBottom: 8, flexWrap: "wrap" }}>
                <div>
                  <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                    <h3 style={{ fontFamily: "var(--font-serif)", fontSize: 18, fontWeight: 700, color: "var(--color-text-primary)", margin: 0 }}>{c.title}</h3>
                    <span style={{ ...MONO, fontSize: 10.5, fontWeight: 700, color: STATUS_COLOR[status], background: `${STATUS_COLOR[status]}15`, border: `1px solid ${STATUS_COLOR[status]}40`, borderRadius: 5, padding: "2px 9px" }}>{status}</span>
                  </div>
                  <p style={{ fontFamily: "var(--font-sans)", fontSize: 13, color: "var(--color-text-muted)", margin: "6px 0 0", maxWidth: 620 }}>{c.description}</p>
                </div>
                {status === "Upcoming" && (
                  <div style={{ textAlign: "right" }}>
                    <div style={{ ...MONO, fontSize: 10, color: "var(--color-text-muted)", textTransform: "uppercase", letterSpacing: "0.08em" }}>Bắt đầu sau</div>
                    <div style={{ ...MONO, fontSize: 18, fontWeight: 700, color: "var(--color-blue)" }}><Countdown target={start} /></div>
                  </div>
                )}
                {status === "Active" && (
                  <div style={{ textAlign: "right" }}>
                    <div style={{ ...MONO, fontSize: 10, color: "var(--color-text-muted)", textTransform: "uppercase", letterSpacing: "0.08em" }}>Kết thúc sau</div>
                    <div style={{ ...MONO, fontSize: 18, fontWeight: 700, color: "var(--color-green)" }}><Countdown target={end} /></div>
                  </div>
                )}
              </div>
              <div style={{ display: "flex", gap: 14, flexWrap: "wrap", ...MONO, fontSize: 11.5, color: "var(--color-text-muted)", marginBottom: 10 }}>
                <span>Bắt đầu: {new Date(c.startTime).toLocaleString("vi-VN")}</span>
                <span>Thời lượng: {fmtDur(c.durationMins)}</span>
                <span>{c.problemIds.length} bài</span>
              </div>
              {c.problemIds.length > 0 && (
                <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
                  {c.problemIds.map((pid) => {
                    const p = byId.get(pid);
                    return (
                      <span key={pid} style={{ ...MONO, fontSize: 11, color: p ? "var(--color-maroon)" : "var(--color-text-muted)", background: "var(--color-maroon-pale)", border: "1px solid rgba(124,29,43,0.2)", borderRadius: 5, padding: "3px 9px" }}>
                        {pid}{p ? ` · ${p.title}` : " (đã xoá)"}
                      </span>
                    );
                  })}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

export type { Contest };
