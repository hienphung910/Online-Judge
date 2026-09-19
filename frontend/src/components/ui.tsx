import { useEffect, useRef, useState } from "react";
import type { CSSProperties, ReactNode } from "react";
import type { VerdictCode } from "../types";

/**
 * Bo component dung chung cho toan bo giao dien (theme "CodeForge" - nen sang,
 * mau chu dao maroon). Moi trang deu dung lai tu day de giao dien nhat quan.
 */

export const MONO: CSSProperties = { fontFamily: "var(--font-mono)" };

export const VERDICT_META: Record<VerdictCode, { label: string; color: string; bg: string; border: string }> = {
  AC: { label: "Accepted", color: "var(--color-green)", bg: "var(--color-green-bg)", border: "var(--color-green-border)" },
  WA: { label: "Wrong Answer", color: "var(--color-red)", bg: "var(--color-red-bg)", border: "var(--color-red-border)" },
  TLE: { label: "Time Limit Exceeded", color: "var(--color-amber)", bg: "var(--color-amber-bg)", border: "var(--color-amber-border)" },
  MLE: { label: "Memory Limit Exceeded", color: "var(--color-purple)", bg: "var(--color-purple-bg)", border: "var(--color-purple-border)" },
  RE: { label: "Runtime Error", color: "#be185d", bg: "rgba(190,24,93,0.08)", border: "rgba(190,24,93,0.2)" },
  CE: { label: "Compile Error", color: "var(--color-text-muted)", bg: "var(--color-bg-raised)", border: "var(--color-border)" },
  IE: { label: "Internal Error", color: "var(--color-amber)", bg: "var(--color-amber-bg)", border: "var(--color-amber-border)" },
  PE: { label: "Presentation Error", color: "var(--color-amber)", bg: "var(--color-amber-bg)", border: "var(--color-amber-border)" },
  PENDING: { label: "Đang chờ chấm", color: "var(--color-text-muted)", bg: "var(--color-bg-raised)", border: "var(--color-border)" },
};

export function VerdictBadge({ verdict, size = 11 }: { verdict: VerdictCode; size?: number }) {
  const m = VERDICT_META[verdict] ?? VERDICT_META.IE;
  const live = verdict === "PENDING";
  return (
    <span
      title={m.label}
      style={{
        display: "inline-flex", alignItems: "center", gap: 5,
        fontFamily: "var(--font-mono)", fontSize: size, fontWeight: 700,
        color: m.color, background: m.bg, border: `1px solid ${m.border}`,
        borderRadius: 5, padding: "2px 8px", letterSpacing: "0.04em", whiteSpace: "nowrap",
      }}
    >
      {live && <span style={{ width: 5, height: 5, borderRadius: "50%", background: m.color, animation: "livePulse 1.4s ease-in-out infinite" }} />}
      {verdict === "PENDING" ? "..." : verdict}
    </span>
  );
}

export function StatCard({ label, value, sub, color }: { label: string; value: string | number; sub?: string; color?: string }) {
  return (
    <div style={{ background: "var(--color-bg-panel)", border: "1px solid var(--color-border)", borderRadius: 9, padding: "12px 18px", minWidth: 110 }}>
      <div style={{ ...MONO, fontSize: 9, color: "var(--color-text-muted)", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: 5 }}>{label}</div>
      <div style={{ fontFamily: "var(--font-serif)", fontSize: 22, fontWeight: 700, color: color ?? "var(--color-maroon)", lineHeight: 1.1 }}>{value}</div>
      {sub && <div style={{ ...MONO, fontSize: 10, color: "var(--color-text-muted)", marginTop: 3 }}>{sub}</div>}
    </div>
  );
}

/** Thanh truc quan hoa thoi gian chay so voi gioi han cua bai. */
export function ExecBar({ ms, limitMs = 2000 }: { ms: number | null; limitMs?: number }) {
  if (ms === null || ms === undefined) {
    return <span style={{ color: "var(--color-text-muted)", ...MONO, fontSize: 12 }}>—</span>;
  }
  const ratio = Math.min(1, ms / limitMs);
  const color = ratio < 0.4 ? "var(--color-green)" : ratio < 0.8 ? "var(--color-amber)" : "var(--color-red)";
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
      <div style={{ width: 44, height: 3, background: "var(--color-bg-raised)", borderRadius: 2, flexShrink: 0 }}>
        <div style={{ height: "100%", width: `${ratio * 100}%`, background: color, borderRadius: 2 }} />
      </div>
      <span style={{ ...MONO, fontSize: 12, color: "var(--color-text-secondary)", minWidth: 38 }}>{ms} ms</span>
    </div>
  );
}

export function ChevDown({ size = 11 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 12 12" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <polyline points="2 4 6 8 10 4" />
    </svg>
  );
}

export function XIco({ size = 10 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 10 10" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
      <line x1="1" y1="1" x2="9" y2="9" />
      <line x1="9" y1="1" x2="1" y2="9" />
    </svg>
  );
}

export function SearchIco() {
  return (
    <svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round">
      <circle cx="6.5" cy="6.5" r="4.5" /><line x1="10" y1="10" x2="14" y2="14" />
    </svg>
  );
}

export function RefIco({ spinning }: { spinning: boolean }) {
  return (
    <svg width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"
      style={{ animation: spinning ? "spin 0.7s linear infinite" : "none" }}>
      <path d="M14 8a6 6 0 1 1-1.5-4" />
      <polyline points="14 2 14 6 10 6" />
    </svg>
  );
}

/** Dropdown tu ve, cho phep xoa lua chon. */
export function Select({
  value, options, onChange, placeholder, disabledOptions = [],
}: {
  value: string;
  options: string[];
  onChange: (v: string) => void;
  placeholder: string;
  disabledOptions?: string[];
}) {
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function onClickOutside(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false);
    }
    document.addEventListener("mousedown", onClickOutside);
    return () => document.removeEventListener("mousedown", onClickOutside);
  }, []);

  return (
    <div ref={ref} style={{ position: "relative" }}>
      <button
        onClick={() => setOpen((v) => !v)}
        style={{
          display: "flex", alignItems: "center", gap: 6, height: 34, padding: "0 12px",
          background: value ? "var(--color-maroon-pale)" : "var(--color-bg-panel)",
          border: `1px solid ${value ? "var(--color-maroon)" : "var(--color-border)"}`,
          borderRadius: 7, color: value ? "var(--color-maroon)" : "var(--color-text-muted)",
          fontSize: 13, cursor: "pointer", fontFamily: "var(--font-sans)", whiteSpace: "nowrap",
          fontWeight: value ? 600 : 400,
        }}
      >
        {value || placeholder}
        {value ? (
          <span onClick={(e) => { e.stopPropagation(); onChange(""); }} style={{ display: "flex", color: "var(--color-maroon)", marginLeft: 2 }}>
            <XIco size={9} />
          </span>
        ) : (
          <ChevDown size={10} />
        )}
      </button>
      {open && (
        <div style={{
          position: "absolute", top: "calc(100% + 5px)", left: 0, zIndex: 200,
          background: "var(--color-bg-panel)", border: "1px solid var(--color-border)",
          borderRadius: 9, boxShadow: "0 8px 28px rgba(28,20,16,0.14)",
          minWidth: 180, maxHeight: 260, overflowY: "auto", padding: 5,
        }}>
          {options.map((opt) => {
            const disabled = disabledOptions.includes(opt);
            const selected = opt === value;
            return (
              <button
                key={opt}
                disabled={disabled}
                onClick={() => { onChange(selected ? "" : opt); setOpen(false); }}
                style={{
                  width: "100%", display: "block", textAlign: "left", padding: "8px 12px",
                  background: selected ? "var(--color-maroon-pale)" : "none", border: "none",
                  color: disabled ? "var(--color-text-muted)" : selected ? "var(--color-maroon)" : "var(--color-text-secondary)",
                  fontSize: 13, cursor: disabled ? "not-allowed" : "pointer",
                  fontFamily: "var(--font-sans)", borderRadius: 6, fontWeight: selected ? 600 : 400,
                  textDecoration: disabled ? "line-through" : "none",
                }}
                onMouseEnter={(e) => { if (!disabled && !selected) (e.currentTarget as HTMLElement).style.background = "var(--color-bg-raised)"; }}
                onMouseLeave={(e) => { if (!disabled && !selected) (e.currentTarget as HTMLElement).style.background = "none"; }}
              >
                {selected ? `✓  ${opt}` : opt}
              </button>
            );
          })}
        </div>
      )}
    </div>
  );
}

export function Panel({ title, right, children, style }: { title?: ReactNode; right?: ReactNode; children: ReactNode; style?: CSSProperties }) {
  return (
    <div style={{
      background: "var(--color-bg-panel)", border: "1px solid var(--color-border)",
      borderRadius: 10, overflow: "hidden", display: "flex", flexDirection: "column", ...style,
    }}>
      {(title || right) && (
        <div style={{
          display: "flex", alignItems: "center", justifyContent: "space-between",
          padding: "10px 16px", borderBottom: "1px solid var(--color-border)",
          background: "var(--color-bg-raised)", flexShrink: 0, gap: 10, flexWrap: "wrap",
        }}>
          <span style={{ ...MONO, fontSize: 11, letterSpacing: "0.08em", textTransform: "uppercase", color: "var(--color-text-secondary)", fontWeight: 600 }}>
            {title}
          </span>
          {right}
        </div>
      )}
      {children}
    </div>
  );
}

export const TH: CSSProperties = {
  textAlign: "left", padding: "10px 14px", fontFamily: "var(--font-mono)", fontSize: 10,
  letterSpacing: "0.09em", textTransform: "uppercase", color: "var(--color-text-muted)",
  fontWeight: 600, borderBottom: "1px solid var(--color-border)", whiteSpace: "nowrap",
  background: "var(--color-bg-raised)",
};

export const TD: CSSProperties = {
  padding: "10px 14px", fontSize: 13, borderBottom: "1px solid var(--color-border-subtle)",
  color: "var(--color-text-secondary)", verticalAlign: "middle",
};

export function Button({
  children, onClick, variant = "ghost", disabled, style, type,
}: {
  children: ReactNode;
  onClick?: () => void;
  variant?: "primary" | "ghost" | "danger";
  disabled?: boolean;
  style?: CSSProperties;
  type?: "button" | "submit";
}) {
  const primary = variant === "primary";
  const danger = variant === "danger";
  return (
    <button
      type={type ?? "button"}
      onClick={onClick}
      disabled={disabled}
      style={{
        display: "inline-flex", alignItems: "center", gap: 6, height: 32, padding: "0 14px",
        borderRadius: 7, fontSize: 12.5, fontFamily: "var(--font-sans)", fontWeight: primary ? 600 : 400,
        cursor: disabled ? "not-allowed" : "pointer", opacity: disabled ? 0.55 : 1,
        background: primary ? "var(--color-maroon)" : danger ? "none" : "var(--color-bg-panel)",
        border: `1px solid ${primary ? "var(--color-maroon)" : danger ? "var(--color-red)" : "var(--color-border)"}`,
        color: primary ? "#FAF7F2" : danger ? "var(--color-red)" : "var(--color-text-secondary)",
        transition: "opacity 0.15s",
        ...style,
      }}
    >
      {children}
    </button>
  );
}

export function ErrorBox({ message }: { message: string }) {
  return (
    <div style={{
      margin: 12, padding: "10px 14px", borderRadius: 7, fontSize: 12.5,
      background: "var(--color-red-bg)", border: "1px solid var(--color-red-border)",
      color: "var(--color-red)", fontFamily: "var(--font-mono)", whiteSpace: "pre-wrap",
    }}>
      {message}
    </div>
  );
}

export function Notice({ message }: { message: string }) {
  return (
    <div style={{
      margin: 12, padding: "10px 14px", borderRadius: 7, fontSize: 12.5,
      background: "var(--color-green-bg)", border: "1px solid var(--color-green-border)",
      color: "var(--color-green)", fontFamily: "var(--font-mono)",
    }}>
      {message}
    </div>
  );
}

/** Khoi hien thi input / output cua test vi du. */
export function SampleBox({ label, text }: { label: string; text: string }) {
  return (
    <div style={{ minWidth: 0 }}>
      <div style={{ ...MONO, fontSize: 9.5, letterSpacing: "0.1em", textTransform: "uppercase", color: "var(--color-text-muted)", marginBottom: 4 }}>
        {label}
      </div>
      <pre style={{
        margin: 0, padding: "8px 10px", background: "var(--color-bg-base)",
        border: "1px solid var(--color-border)", borderRadius: 6,
        fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-primary)",
        whiteSpace: "pre-wrap", overflowX: "auto",
      }}>
        {text.trimEnd()}
      </pre>
    </div>
  );
}

export function formatTime(iso: string): string {
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return iso;
  return d.toLocaleTimeString("vi-VN", { hour12: false, hour: "2-digit", minute: "2-digit", second: "2-digit" });
}

export function timeAgo(iso: string): string {
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return "";
  const s = Math.floor((Date.now() - d.getTime()) / 1000);
  if (s < 5) return "vừa xong";
  if (s < 60) return `${s} giây trước`;
  if (s < 3600) return `${Math.floor(s / 60)} phút trước`;
  return `${Math.floor(s / 3600)} giờ trước`;
}
