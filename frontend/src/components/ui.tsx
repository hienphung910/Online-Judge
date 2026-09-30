import type { CSSProperties, ReactNode } from "react";
import type { VerdictCode } from "../types";

export const MONO: CSSProperties = { fontFamily: "var(--font-mono)" };

export const VERDICT_META: Record<VerdictCode, { label: string; color: string; bg: string; border: string }> = {
  AC: { label: "Accepted", color: "var(--color-ac-text)", bg: "var(--color-ac-bg)", border: "var(--color-green-border)" },
  WA: { label: "Wrong Answer", color: "var(--color-wa-text)", bg: "var(--color-wa-bg)", border: "#FFCDD2" },
  TLE: { label: "Time Limit Exceeded", color: "var(--color-orange)", bg: "var(--color-orange-bg)", border: "#FFE0B2" },
  MLE: { label: "Memory Limit Exceeded", color: "var(--color-purple)", bg: "rgba(106,27,154,0.08)", border: "rgba(106,27,154,0.2)" },
  RE: { label: "Runtime Error", color: "#AD1457", bg: "rgba(173,20,87,0.08)", border: "rgba(173,20,87,0.2)" },
  CE: { label: "Compile Error", color: "#757575", bg: "#F5F5F5", border: "#E0E0E0" },
  IE: { label: "Internal Error", color: "var(--color-orange)", bg: "var(--color-orange-bg)", border: "#FFE0B2" },
  PE: { label: "Presentation Error", color: "var(--color-orange)", bg: "var(--color-orange-bg)", border: "#FFE0B2" },
  PENDING: { label: "Đang chờ chấm", color: "#9E9E9E", bg: "#F5F5F5", border: "#E0E0E0" },
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
        borderRadius: 4, padding: "2px 8px", whiteSpace: "nowrap",
      }}
    >
      {live && <span style={{ width: 5, height: 5, borderRadius: "50%", background: m.color, animation: "livePulse 1.4s ease-in-out infinite" }} />}
      {verdict === "PENDING" ? "..." : verdict}
    </span>
  );
}

export function StatCard({ label, value, sub, color }: { label: string; value: string | number; sub?: string; color?: string }) {
  return (
    <div style={{
      background: "#fff", border: "1px solid #E0E0E0", borderRadius: 8,
      padding: "12px 16px", minWidth: 100,
    }}>
      <div style={{ fontSize: 10, color: "#9E9E9E", textTransform: "uppercase", letterSpacing: "0.08em", marginBottom: 4, fontFamily: "var(--font-mono)" }}>{label}</div>
      <div style={{ fontSize: 20, fontWeight: 800, color: color ?? "var(--color-red)", lineHeight: 1.1 }}>{value}</div>
      {sub && <div style={{ fontSize: 10, color: "#9E9E9E", marginTop: 2, fontFamily: "var(--font-mono)" }}>{sub}</div>}
    </div>
  );
}

export function ExecBar({ ms, limitMs = 2000 }: { ms: number | null; limitMs?: number }) {
  if (ms === null || ms === undefined) return <span style={{ color: "#9E9E9E", fontFamily: "var(--font-mono)", fontSize: 12 }}>—</span>;
  const ratio = Math.min(1, ms / limitMs);
  const color = ratio < 0.4 ? "var(--color-green)" : ratio < 0.8 ? "var(--color-orange)" : "var(--color-red)";
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
      <div style={{ width: 40, height: 3, background: "#EEEEEE", borderRadius: 2, flexShrink: 0 }}>
        <div style={{ height: "100%", width: `${ratio * 100}%`, background: color, borderRadius: 2 }} />
      </div>
      <span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "#757575" }}>{ms} ms</span>
    </div>
  );
}

export function ChevDown({ size = 11 }: { size?: number }) {
  return <svg width={size} height={size} viewBox="0 0 12 12" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round"><polyline points="2 4 6 8 10 4" /></svg>;
}

export function XIco({ size = 10 }: { size?: number }) {
  return <svg width={size} height={size} viewBox="0 0 10 10" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"><line x1="1" y1="1" x2="9" y2="9" /><line x1="9" y1="1" x2="1" y2="9" /></svg>;
}

export function SearchIco() {
  return <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><circle cx="6.5" cy="6.5" r="4.5" /><line x1="10" y1="10" x2="14" y2="14" /></svg>;
}

export function RefIco({ spinning }: { spinning: boolean }) {
  return <svg width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" style={{ animation: spinning ? "spin 0.7s linear infinite" : "none" }}><path d="M14 8a6 6 0 1 1-1.5-4" /><polyline points="14 2 14 6 10 6" /></svg>;
}

import { useEffect, useRef, useState } from "react";

export function Select({
  value, options, onChange, placeholder, disabledOptions = [],
}: {
  value: string; options: string[]; onChange: (v: string) => void; placeholder: string; disabledOptions?: string[];
}) {
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);
  useEffect(() => {
    function h(e: MouseEvent) { if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false); }
    document.addEventListener("mousedown", h);
    return () => document.removeEventListener("mousedown", h);
  }, []);

  return (
    <div ref={ref} style={{ position: "relative" }}>
      <button onClick={() => setOpen((v) => !v)} style={{
        display: "flex", alignItems: "center", gap: 6, height: 34, padding: "0 12px",
        background: value ? "#FDECEA" : "#fff", border: `1px solid ${value ? "var(--color-red)" : "#E0E0E0"}`,
        borderRadius: 6, color: value ? "var(--color-red)" : "#9E9E9E",
        fontSize: 13, cursor: "pointer", fontWeight: value ? 600 : 400, whiteSpace: "nowrap",
      }}>
        {value || placeholder}
        {value ? <span onClick={(e) => { e.stopPropagation(); onChange(""); }} style={{ display: "flex", color: "var(--color-red)", marginLeft: 2 }}><XIco size={9} /></span> : <ChevDown size={10} />}
      </button>
      {open && (
        <div style={{
          position: "absolute", top: "calc(100% + 4px)", left: 0, zIndex: 200,
          background: "#fff", border: "1px solid #E0E0E0", borderRadius: 8,
          boxShadow: "0 8px 24px rgba(0,0,0,0.1)", minWidth: 160, maxHeight: 240,
          overflowY: "auto", padding: 4, animation: "slideIn 0.1s ease",
        }}>
          {options.map((opt) => {
            const disabled = disabledOptions.includes(opt);
            const selected = opt === value;
            return (
              <button key={opt} disabled={disabled} onClick={() => { onChange(selected ? "" : opt); setOpen(false); }}
                style={{
                  width: "100%", display: "block", textAlign: "left", padding: "7px 12px",
                  background: selected ? "#FDECEA" : "none", border: "none",
                  color: disabled ? "#BDBDBD" : selected ? "var(--color-red)" : "#616161",
                  fontSize: 13, cursor: disabled ? "not-allowed" : "pointer", borderRadius: 4,
                  fontWeight: selected ? 600 : 400, textDecoration: disabled ? "line-through" : "none",
                }}
                onMouseEnter={(e) => { if (!disabled && !selected) e.currentTarget.style.background = "#F5F5F5"; }}
                onMouseLeave={(e) => { if (!disabled && !selected) e.currentTarget.style.background = "none"; }}
              >{selected ? `✓ ${opt}` : opt}</button>
            );
          })}
        </div>
      )}
    </div>
  );
}

export function Panel({ title, right, children, style }: { title?: ReactNode; right?: ReactNode; children: ReactNode; style?: CSSProperties }) {
  return (
    <div style={{ background: "#fff", border: "1px solid #E0E0E0", borderRadius: 8, overflow: "hidden", display: "flex", flexDirection: "column", ...style }}>
      {(title || right) && (
        <div style={{
          display: "flex", alignItems: "center", justifyContent: "space-between",
          padding: "10px 16px", borderBottom: "1px solid #E0E0E0", background: "var(--color-table-header-bg)",
          flexShrink: 0, gap: 10, flexWrap: "wrap",
        }}>
          <span style={{ fontSize: 13, fontWeight: 700, color: "#212121" }}>{title}</span>
          {right}
        </div>
      )}
      {children}
    </div>
  );
}

export const TH: CSSProperties = {
  textAlign: "left", padding: "10px 14px", fontFamily: "var(--font-mono)", fontSize: 11,
  textTransform: "uppercase", color: "#757575", fontWeight: 700,
  borderBottom: "1px solid var(--color-table-border)", whiteSpace: "nowrap",
  background: "var(--color-table-header-bg)", position: "sticky", top: 0,
};

export const TD: CSSProperties = {
  padding: "10px 14px", fontSize: 13, borderBottom: "1px solid #F5F5F5", color: "#616161", verticalAlign: "middle",
};

export function Button({
  children, onClick, variant = "ghost", disabled, style, type,
}: {
  children: ReactNode; onClick?: () => void; variant?: "primary" | "ghost" | "danger"; disabled?: boolean; style?: CSSProperties; type?: "button" | "submit";
}) {
  const primary = variant === "primary";
  const danger = variant === "danger";
  return (
    <button type={type ?? "button"} onClick={onClick} disabled={disabled} style={{
      display: "inline-flex", alignItems: "center", gap: 6, height: 32, padding: "0 14px",
      borderRadius: 6, fontSize: 12.5, fontWeight: primary ? 700 : 500,
      cursor: disabled ? "not-allowed" : "pointer", opacity: disabled ? 0.5 : 1,
      background: primary ? "var(--color-red)" : "none",
      border: `1px solid ${primary ? "var(--color-red)" : danger ? "#F44336" : "#E0E0E0"}`,
      color: primary ? "#fff" : danger ? "#F44336" : "#616161",
      transition: "background 0.15s", ...style,
    }}>{children}</button>
  );
}

export function ErrorBox({ message }: { message: string }) {
  return (
    <div style={{ margin: 12, padding: "10px 14px", borderRadius: 6, fontSize: 12.5, background: "#FFEBEE", border: "1px solid #FFCDD2", color: "#C62828", fontFamily: "var(--font-mono)", whiteSpace: "pre-wrap" }}>{message}</div>
  );
}

export function Notice({ message }: { message: string }) {
  return (
    <div style={{ margin: 12, padding: "10px 14px", borderRadius: 6, fontSize: 12.5, background: "var(--color-ac-bg)", border: "1px solid var(--color-green-border)", color: "var(--color-green)", fontFamily: "var(--font-mono)" }}>{message}</div>
  );
}

export function SampleBox({ label, text }: { label: string; text: string }) {
  return (
    <div style={{ minWidth: 0 }}>
      <div style={{ fontSize: 10, textTransform: "uppercase", letterSpacing: "0.08em", color: "#9E9E9E", marginBottom: 4, fontFamily: "var(--font-mono)", fontWeight: 600 }}>{label}</div>
      <pre style={{ margin: 0, padding: "8px 12px", background: "#FAFAFA", border: "1px solid #E0E0E0", borderRadius: 6, fontFamily: "var(--font-mono)", fontSize: 12, color: "#212121", whiteSpace: "pre-wrap", overflowX: "auto" }}>{text.trimEnd()}</pre>
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
