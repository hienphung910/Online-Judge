import { useEffect, useRef, useState } from "react";
import { MILESTONES, nextMilestone, shiftDay, type StreakInfo } from "../streak";

/* Bang mau rieng cho streak: cam lua, de noi tren header do ma khong lan vao mau verdict. */
const FLAME = "#FB8C00";
const FLAME_DARK = "#E65100";
const HEAT = ["#F0F0F0", "#FFE0B2", "#FFB74D", "#FB8C00", "#E65100"];
const WEEKDAY = ["CN", "T2", "T3", "T4", "T5", "T6", "T7"];
/** So tuan hien tren lich nhiet. */
const WEEKS = 16;

export function FlameIcon({ size = 16, lit = true }: { size?: number; lit?: boolean }) {
  return (
    <svg width={size} height={size} viewBox="0 0 16 16" aria-hidden="true">
      <path
        d="M8 1c.6 2.2-.6 3.6-1.7 4.8C5.1 7.1 4 8.4 4 10.3 4 12.9 5.8 15 8 15s4-2.1 4-4.7c0-1.7-.7-3-1.6-4-.1 1.1-.6 1.9-1.3 2.3C9.4 5.9 9.1 3.2 8 1z"
        fill={lit ? FLAME : "none"}
        stroke={lit ? FLAME_DARK : "currentColor"}
        strokeWidth="1.1"
        strokeLinejoin="round"
      />
      {lit && (
        <path
          d="M8 15c-1.1 0-2-1-2-2.2 0-1.1.7-1.8 1.3-2.5.2.7.6 1.1 1.1 1.3 0-.8.2-1.5.6-2 .6.8 1 1.8 1 3 0 1.3-.9 2.4-2 2.4z"
          fill="#FFE082"
        />
      )}
    </svg>
  );
}

function weekdayOf(key: string): number {
  const [y, m, d] = key.split("-").map(Number);
  return new Date(Date.UTC(y, m - 1, d)).getUTCDay();
}

function shortDate(key: string): string {
  return `${key.slice(8, 10)}/${key.slice(5, 7)}`;
}

function heatColor(count: number): string {
  if (count <= 0) return HEAT[0];
  if (count === 1) return HEAT[1];
  if (count <= 3) return HEAT[2];
  if (count <= 6) return HEAT[3];
  return HEAT[4];
}

/** Loi nhan thay doi theo tinh trang chuoi - phan "kich thich" chinh nam o day. */
function statusMessage(info: StreakInfo): { text: string; color: string; bg: string } {
  if (info.activeToday) {
    return { text: "Hôm nay bạn đã luyện tập. Mai quay lại để chuỗi dài thêm nhé!", color: "#2E7D32", bg: "#E8F5E9" };
  }
  if (info.current > 0) {
    return {
      text: `Nộp ít nhất 1 bài trước 24:00 hôm nay để giữ chuỗi ${info.current} ngày!`,
      color: FLAME_DARK,
      bg: "#FFF3E0",
    };
  }
  if (info.activeDays > 0) {
    return { text: "Chuỗi đã bị ngắt. Nộp một bài hôm nay để bắt đầu lại!", color: "#C62828", bg: "#FFEBEE" };
  }
  return { text: "Nộp bài đầu tiên để bắt đầu chuỗi luyện tập của bạn!", color: "#616161", bg: "#F5F5F5" };
}

export default function StreakBadge({ info }: { info: StreakInfo | null }) {
  const [open, setOpen] = useState(false);
  const boxRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!open) return;
    const onDown = (e: MouseEvent) => {
      if (boxRef.current && !boxRef.current.contains(e.target as Node)) setOpen(false);
    };
    const onKey = (e: KeyboardEvent) => { if (e.key === "Escape") setOpen(false); };
    document.addEventListener("mousedown", onDown);
    document.addEventListener("keydown", onKey);
    return () => {
      document.removeEventListener("mousedown", onDown);
      document.removeEventListener("keydown", onKey);
    };
  }, [open]);

  if (!info) return null;

  const lit = info.activeToday;
  const title = lit
    ? `Chuỗi ${info.current} ngày — hôm nay đã luyện tập`
    : info.current > 0
      ? `Chuỗi ${info.current} ngày — hôm nay chưa nộp bài`
      : "Chưa có chuỗi luyện tập";

  return (
    <div ref={boxRef} style={{ position: "relative" }}>
      <button
        onClick={() => setOpen((v) => !v)}
        title={title}
        aria-label={title}
        style={{
          display: "flex", alignItems: "center", gap: 5, height: 28, padding: "0 10px 0 8px",
          borderRadius: 14, border: "none", cursor: "pointer",
          background: open ? "rgba(255,255,255,0.28)" : "rgba(255,255,255,0.15)",
          color: lit ? "#fff" : "rgba(255,255,255,0.75)",
          fontSize: 13, fontWeight: 700, fontFamily: "var(--font-mono)",
          transition: "background 0.15s",
        }}
      >
        <FlameIcon size={16} lit={lit} />
        {info.current}
        {!lit && info.current > 0 && (
          // Cham vang nho: chuoi dang con nhung hom nay chua nop - de mat nhac.
          <span style={{ width: 6, height: 6, borderRadius: "50%", background: "#FFD54F", animation: "livePulse 1.6s infinite" }} />
        )}
      </button>

      {open && <StreakPanel info={info} />}
    </div>
  );
}

function StreakPanel({ info }: { info: StreakInfo }) {
  const msg = statusMessage(info);
  const next = nextMilestone(info.current);
  const prevMilestone = [...MILESTONES].reverse().find((m) => m <= info.current) ?? 0;
  const toNext = next === null ? 1 : (info.current - prevMilestone) / (next - prevMilestone);

  // 7 ngay gan nhat, ket thuc o hom nay.
  const week = Array.from({ length: 7 }, (_, i) => shiftDay(info.today, i - 6));

  // Lich nhiet: cot = tuan (bat dau thu Hai), hang = thu. Ngay sau hom nay de trong.
  const mondayOffset = (weekdayOf(info.today) + 6) % 7;
  const start = shiftDay(info.today, -mondayOffset - (WEEKS - 1) * 7);
  const columns = Array.from({ length: WEEKS }, (_, w) =>
    Array.from({ length: 7 }, (_, d) => shiftDay(start, w * 7 + d)),
  );

  return (
    <div
      style={{
        position: "absolute", top: "calc(100% + 8px)", right: 0, width: 300,
        background: "#fff", border: "1px solid #E0E0E0", borderRadius: 10,
        boxShadow: "0 8px 30px rgba(0,0,0,0.12)", padding: 16, zIndex: 200,
        animation: "slideIn 0.12s ease", color: "#212121",
      }}
    >
      {/* Tong quan */}
      <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
        <div style={{
          width: 48, height: 48, borderRadius: 12, flexShrink: 0,
          background: info.activeToday ? "#FFF3E0" : "#F5F5F5",
          display: "flex", alignItems: "center", justifyContent: "center", color: "#BDBDBD",
        }}>
          <FlameIcon size={28} lit={info.activeToday} />
        </div>
        <div>
          <div style={{ fontSize: 22, fontWeight: 800, lineHeight: 1.1 }}>
            {info.current} <span style={{ fontSize: 14, fontWeight: 600, color: "#616161" }}>ngày liên tiếp</span>
          </div>
          <div style={{ fontSize: 12, color: "#9E9E9E", marginTop: 2 }}>Chuỗi luyện tập hiện tại</div>
        </div>
      </div>

      <div style={{ marginTop: 12, padding: "8px 10px", borderRadius: 6, fontSize: 12.5, lineHeight: 1.5, color: msg.color, background: msg.bg }}>
        {msg.text}
      </div>

      {/* 7 ngay gan nhat */}
      <div style={{ display: "flex", justifyContent: "space-between", marginTop: 14 }}>
        {week.map((key) => {
          const active = info.perDay.has(key);
          const isToday = key === info.today;
          return (
            <div key={key} title={`${shortDate(key)}: ${info.perDay.get(key) ?? 0} bài nộp`}
              style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 4 }}>
              <span style={{ fontSize: 10.5, fontWeight: isToday ? 700 : 500, color: isToday ? FLAME_DARK : "#9E9E9E" }}>
                {isToday ? "Nay" : WEEKDAY[weekdayOf(key)]}
              </span>
              <div style={{
                width: 28, height: 28, borderRadius: "50%",
                display: "flex", alignItems: "center", justifyContent: "center",
                background: active ? "#FFF3E0" : "#FAFAFA",
                border: isToday ? `2px solid ${active ? FLAME : "#FFCC80"}` : "1px solid #EEEEEE",
                boxSizing: "border-box", color: "#E0E0E0",
              }}>
                {active ? <FlameIcon size={15} /> : <span style={{ width: 4, height: 4, borderRadius: "50%", background: "#E0E0E0" }} />}
              </div>
            </div>
          );
        })}
      </div>

      {/* Moc tiep theo */}
      <div style={{ marginTop: 14 }}>
        <div style={{ display: "flex", justifyContent: "space-between", fontSize: 12, marginBottom: 6 }}>
          <span style={{ color: "#616161" }}>
            {next === null ? "Bạn đã vượt mọi mốc!" : <>Mốc tiếp theo: <b style={{ color: "#212121" }}>{next} ngày</b></>}
          </span>
          {next !== null && <span style={{ color: FLAME_DARK, fontWeight: 600 }}>còn {next - info.current} ngày</span>}
        </div>
        <div style={{ height: 6, background: "#EEEEEE", borderRadius: 3, overflow: "hidden" }}>
          <div style={{
            height: "100%", width: `${Math.round(toNext * 100)}%`, borderRadius: 3,
            background: `linear-gradient(90deg, #FFB74D, ${FLAME_DARK})`, transition: "width 0.4s ease",
          }} />
        </div>
      </div>

      {/* So lieu */}
      <div style={{ display: "flex", gap: 8, marginTop: 14 }}>
        <MiniStat label="Dài nhất" value={`${info.longest} ngày`} />
        <MiniStat label="Tổng ngày học" value={`${info.activeDays} ngày`} />
      </div>

      {/* Lich nhiet */}
      <div style={{ marginTop: 14 }}>
        <div style={{ fontSize: 11, color: "#9E9E9E", marginBottom: 6 }}>{WEEKS} tuần gần đây</div>
        <div style={{ display: "flex", gap: 3 }}>
          {columns.map((days, w) => (
            <div key={w} style={{ display: "flex", flexDirection: "column", gap: 3 }}>
              {days.map((key) => {
                const future = key > info.today;
                const count = info.perDay.get(key) ?? 0;
                return (
                  <div key={key}
                    title={future ? undefined : `${shortDate(key)}: ${count} bài nộp`}
                    style={{
                      width: 13, height: 13, borderRadius: 3,
                      background: future ? "transparent" : heatColor(count),
                      outline: key === info.today ? `1.5px solid ${FLAME_DARK}` : "none",
                      outlineOffset: 1,
                    }} />
                );
              })}
            </div>
          ))}
        </div>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "flex-end", gap: 3, marginTop: 6, fontSize: 10.5, color: "#9E9E9E" }}>
          Ít
          {HEAT.map((c) => <span key={c} style={{ width: 10, height: 10, borderRadius: 2, background: c }} />)}
          Nhiều
        </div>
      </div>
    </div>
  );
}

function MiniStat({ label, value }: { label: string; value: string }) {
  return (
    <div style={{ flex: 1, background: "#FAFAFA", border: "1px solid #F0F0F0", borderRadius: 6, padding: "8px 10px" }}>
      <div style={{ fontSize: 10, color: "#9E9E9E", textTransform: "uppercase", letterSpacing: "0.06em", fontFamily: "var(--font-mono)" }}>{label}</div>
      <div style={{ fontSize: 15, fontWeight: 700, marginTop: 2 }}>{value}</div>
    </div>
  );
}

/** Thong bao nho bat len khi chuoi vua tang sau mot lan nop bai, tu tat sau vai giay. */
export function StreakToast({ value, onClose }: { value: number | null; onClose: () => void }) {
  useEffect(() => {
    if (value === null) return;
    const t = window.setTimeout(onClose, 5000);
    return () => window.clearTimeout(t);
  }, [value, onClose]);

  if (value === null) return null;
  const milestone = MILESTONES.includes(value);
  const next = nextMilestone(value);

  return (
    <div
      role="status"
      onClick={onClose}
      style={{
        position: "fixed", top: 60, right: 20, zIndex: 300, cursor: "pointer",
        display: "flex", alignItems: "center", gap: 12, padding: "12px 16px",
        background: "#fff", border: `1px solid #FFCC80`, borderRadius: 10,
        boxShadow: "0 8px 30px rgba(0,0,0,0.14)", animation: "slideIn 0.18s ease",
      }}
    >
      <FlameIcon size={30} />
      <div>
        <div style={{ fontSize: 14, fontWeight: 700, color: "#212121" }}>
          {milestone ? `Đạt mốc ${value} ngày liên tiếp!` : `Chuỗi luyện tập: ${value} ngày!`}
        </div>
        <div style={{ fontSize: 12, color: "#757575", marginTop: 2 }}>
          {value === 1
            ? "Khởi đầu tốt — quay lại vào ngày mai để giữ chuỗi."
            : next !== null
              ? `Cố lên, còn ${next - value} ngày nữa tới mốc ${next} ngày.`
              : "Phong độ tuyệt vời, giữ vững nhé!"}
        </div>
      </div>
    </div>
  );
}
