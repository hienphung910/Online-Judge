import { useEffect, useRef, useState } from "react";
import type { CSSProperties, ReactNode } from "react";
import type { VerdictCode } from "../types";

/**
 * Bo component dung chung, giu nguyen ngon ngu thiet ke cua ban Figma Make:
 * badge verdict, the thong ke, thanh do thoi gian, dropdown, bang du lieu.
 */

export const VERDICT_META: Record<VerdictCode, { label: string; color: string; bg: string; border: string }> = {
  AC: { label: "Accepted", color: "#4ade80", bg: "rgba(74,222,128,0.10)", border: "rgba(74,222,128,0.25)" },
  WA: { label: "Wrong Answer", color: "#f87171", bg: "rgba(248,113,113,0.10)", border: "rgba(248,113,113,0.25)" },
  TLE: { label: "Time Limit Exceeded", color: "#fb923c", bg: "rgba(251,146,60,0.10)", border: "rgba(251,146,60,0.25)" },
  MLE: { label: "Memory Limit Exceeded", color: "#c084fc", bg: "rgba(192,132,252,0.10)", border: "rgba(192,132,252,0.25)" },
  RE: { label: "Runtime Error", color: "#f472b6", bg: "rgba(244,114,182,0.10)", border: "rgba(244,114,182,0.25)" },
  CE: { label: "Compile Error", color: "#94a3b8", bg: "rgba(148,163,184,0.08)", border: "rgba(148,163,184,0.2)" },
  IE: { label: "Internal Error", color: "#fbbf24", bg: "rgba(251,191,36,0.10)", border: "rgba(251,191,36,0.25)" },
  PE: { label: "Presentation Error", color: "#fbbf24", bg: "rgba(251,191,36,0.10)", border: "rgba(251,191,36,0.25)" },
  PENDING: { label: "Đang chờ chấm", color: "#64748b", bg: "rgba(100,116,139,0.08)", border: "rgba(100,116,139,0.2)" },
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
      {live && (
        <span style={{ width: 5, height: 5, borderRadius: "50%", background: m.color, animation: "livePulse 1.4s ease-in-out infinite" }} />
      )}
      {verdict === "PENDING" ? "..." : verdict}
    </span>
  );
}

export function StatCard({ label, value, sub, color }: { label: string; value: string | number; sub?: string; color?: string }) {
  return (
    <div style={{ background: "var(--color-bg-panel)", border: "1px solid var(--color-border)", borderRadius: 8, padding: "12px 16px", minWidth: 108 }}>
      <div style={{ fontFamily: "var(--font-mono)", fontSize: 9, color: "var(--color-text-muted)", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: 4 }}>
        {label}
      </div>
      <div style={{ fontFamily: "var(--font-mono)", fontSize: 20, fontWeight: 700, color: color ?? "var(--color-text-primary)", lineHeight: 1.1 }}>
        {value}
      </div>
      {sub && <div style={{ fontFamily: "var(--font-mono)", fontSize: 10, color: "var(--color-text-muted)", marginTop: 2 }}>{sub}</div>}
    </div>
  );
}

/** Thanh truc quan hoa thoi gian chay so voi gioi han cua bai. */
export function ExecBar({ ms, limitMs = 2000 }: { ms: number | null; limitMs?: number }) {
  if (ms === null || ms === undefined) {
    return <span style={{ color: "var(--color-text-muted)", fontFamily: "var(--font-mono)", fontSize: 12 }}>—</span>;
  }
  const ratio = Math.min(1, ms / limitMs);
  const color = ratio < 0.4 ? "#4ade80" : ratio < 0.8 ? "#fbbf24" : "#f87171";
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
      <div style={{ width: 44, height: 2, background: "var(--color-bg-raised)", borderRadius: 1, flexShrink: 0 }}>
        <div style={{ height: "100%", width: `${ratio * 100}%`, background: color, borderRadius: 1 }} />
      </div>
      <span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-secondary)", minWidth: 38 }}>{ms}</span>
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

export function RefIco({ spinning }: { spinning: boolean }) {
  return (
    <svg
      width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor"
      strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"
      style={{ animation: spinning ? "spin 0.7s linear infinite" : "none" }}
    >
      <path d="M14 8a6 6 0 1 1-1.5-4" />
      <polyline points="14 2 14 6 10 6" />
    </svg>
  );
}

/** Dropdown tu ve, cho phep xoa lua chon (giong ban thiet ke goc). */
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
          display: "flex", alignItems: "center", gap: 6, height: 30, padding: "0 10px",
          background: value ? "rgba(80,227,194,0.06)" : "var(--color-bg-panel)",
          border: `1px solid ${value ? "rgba(80,227,194,0.25)" : "var(--color-border)"}`,
          borderRadius: 6, color: value ? "#50E3C2" : "var(--color-text-muted)",
          fontSize: 12, cursor: "pointer", fontFamily: "var(--font-mono)", whiteSpace: "nowrap",
        }}
      >
        {value || placeholder}
        {value ? (
          <span
            onClick={(e) => { e.stopPropagation(); onChange(""); }}
            style={{ display: "flex", color: "var(--color-text-muted)", marginLeft: 2 }}
          >
            <XIco size={9} />
          </span>
        ) : (
          <ChevDown size={10} />
        )}
      </button>
      {open && (
        <div
          style={{
            position: "absolute", top: "calc(100% + 4px)", left: 0, zIndex: 200,
            background: "var(--color-bg-panel)", border: "1px solid var(--color-border)",
            borderRadius: 8, boxShadow: "0 12px 32px rgba(0,0,0,0.6)",
            minWidth: 180, maxHeight: 260, overflowY: "auto", padding: 4,
          }}
        >
          {options.map((opt) => {
            const disabled = disabledOptions.includes(opt);
            const selected = opt === value;
            return (
              <button
                key={opt}
                disabled={disabled}
                onClick={() => { onChange(selected ? "" : opt); setOpen(false); }}
                style={{
                  width: "100%", display: "block", textAlign: "left", padding: "7px 10px",
                  background: selected ? "rgba(80,227,194,0.08)" : "none", border: "none",
                  color: disabled ? "var(--color-text-muted)" : selected ? "#50E3C2" : "var(--color-text-secondary)",
                  fontSize: 12, cursor: disabled ? "not-allowed" : "pointer",
                  fontFamily: "var(--font-mono)", borderRadius: 5,
                  textDecoration: disabled ? "line-through" : "none",
                }}
              >
                {selected ? `✓ ${opt}` : opt}
              </button>
            );
          })}
        </div>
      )}
    </div>
  );
}

export function Panel({ title, right, children, style }: { title?: string; right?: ReactNode; children: ReactNode; style?: CSSProperties }) {
  return (
    <div
      style={{
        background: "var(--color-bg-panel)", border: "1px solid var(--color-border)",
        borderRadius: 8, overflow: "hidden", display: "flex", flexDirection: "column", ...style,
      }}
    >
      {(title || right) && (
        <div
          style={{
            display: "flex", alignItems: "center", justifyContent: "space-between",
            padding: "9px 14px", borderBottom: "1px solid var(--color-border)",
            background: "var(--color-bg-raised)", flexShrink: 0,
          }}
        >
          <span style={{ fontFamily: "var(--font-mono)", fontSize: 10, letterSpacing: "0.12em", textTransform: "uppercase", color: "var(--color-text-muted)" }}>
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
  textAlign: "left", padding: "8px 12px", fontFamily: "var(--font-mono)", fontSize: 10,
  letterSpacing: "0.1em", textTransform: "uppercase", color: "var(--color-text-muted)",
  borderBottom: "1px solid var(--color-border)", whiteSpace: "nowrap", background: "var(--color-bg-panel)",
};

export const TD: CSSProperties = {
  padding: "8px 12px", fontSize: 12.5, borderBottom: "1px solid var(--color-border-subtle)",
  color: "var(--color-text-secondary)", verticalAlign: "middle",
};

export const MONO: CSSProperties = { fontFamily: "var(--font-mono)" };

export function Button({
  children, onClick, variant = "ghost", disabled, style,
}: {
  children: ReactNode;
  onClick?: () => void;
  variant?: "primary" | "ghost";
  disabled?: boolean;
  style?: CSSProperties;
}) {
  const primary = variant === "primary";
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      style={{
        display: "inline-flex", alignItems: "center", gap: 6, height: 30, padding: "0 14px",
        borderRadius: 6, fontSize: 12, fontFamily: "var(--font-mono)",
        cursor: disabled ? "not-allowed" : "pointer", opacity: disabled ? 0.5 : 1,
        background: primary ? "rgba(80,227,194,0.12)" : "var(--color-bg-panel)",
        border: `1px solid ${primary ? "rgba(80,227,194,0.35)" : "var(--color-border)"}`,
        color: primary ? "#50E3C2" : "var(--color-text-secondary)",
        ...style,
      }}
    >
      {children}
    </button>
  );
}

export function ErrorBox({ message }: { message: string }) {
  return (
    <div
      style={{
        margin: 12, padding: "10px 14px", borderRadius: 6, fontSize: 12.5,
        background: "rgba(248,113,113,0.08)", border: "1px solid rgba(248,113,113,0.25)",
        color: "#f87171", fontFamily: "var(--font-mono)", whiteSpace: "pre-wrap",
      }}
    >
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
      <pre
        style={{
          margin: 0, padding: "8px 10px", background: "var(--color-bg-base)",
          border: "1px solid var(--color-border)", borderRadius: 6,
          fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-primary)",
          whiteSpace: "pre-wrap", overflowX: "auto",
        }}
      >
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
