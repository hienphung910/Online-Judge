import { useState } from "react";
import { useAuth } from "../auth";

type Mode = "login" | "register";

const FIELD_LABEL = {
  display: "block", fontFamily: "var(--font-mono)", fontSize: 10, fontWeight: 600,
  color: "var(--color-text-muted)", textTransform: "uppercase" as const, letterSpacing: "0.09em", marginBottom: 6,
};
const FIELD_INPUT = {
  width: "100%", height: 38, padding: "0 12px", background: "var(--color-bg-base)",
  border: "1px solid var(--color-border)", borderRadius: 7, color: "var(--color-text-primary)",
  fontSize: 14, fontFamily: "var(--font-sans)", outline: "none", boxSizing: "border-box" as const,
};

function Field({ label, ...props }: { label: string } & React.InputHTMLAttributes<HTMLInputElement>) {
  return (
    <div>
      <label style={FIELD_LABEL}>{label}</label>
      <input
        {...props}
        style={FIELD_INPUT}
        onFocus={(e) => { e.target.style.borderColor = "var(--color-maroon)"; }}
        onBlur={(e) => { e.target.style.borderColor = "var(--color-border)"; }}
      />
    </div>
  );
}

export default function LoginModal({ onClose }: { onClose: () => void }) {
  const { login, register } = useAuth();
  const [mode, setMode] = useState<Mode>("login");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("");
  const [fullName, setFullName] = useState("");
  const [studentCode, setStudentCode] = useState("");
  const [className, setClassName] = useState("");
  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");
  const [busy, setBusy] = useState(false);
  const [showPass, setShowPass] = useState(false);

  function switchMode(next: Mode) {
    setMode(next);
    setError("");
    setNotice("");
    setPassword("");
    setConfirm("");
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");
    setNotice("");
    if (mode === "login") {
      if (!username || !password) { setError("Hãy nhập tên đăng nhập và mật khẩu."); return; }
      setBusy(true);
      try {
        await login(username.trim(), password);
        onClose();
      } catch (e2) {
        setError(e2 instanceof Error ? e2.message : String(e2));
      } finally {
        setBusy(false);
      }
      return;
    }

    // register
    if (password.length < 8) { setError("Mật khẩu phải có ít nhất 8 ký tự."); return; }
    if (password !== confirm) { setError("Hai lần nhập mật khẩu không khớp."); return; }
    setBusy(true);
    try {
      await register({
        username: username.trim(),
        password,
        fullName: fullName.trim(),
        studentCode: studentCode.trim(),
        className: className.trim(),
      });
      switchMode("login");
      setNotice(`Đã tạo tài khoản @${username.trim()}. Mời bạn đăng nhập.`);
    } catch (e2) {
      setError(e2 instanceof Error ? e2.message : String(e2));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div
      style={{ position: "fixed", inset: 0, background: "rgba(28,20,16,0.45)", zIndex: 999, display: "flex", alignItems: "center", justifyContent: "center", padding: 16, overflowY: "auto" }}
      onClick={(e) => { if (e.target === e.currentTarget) onClose(); }}
    >
      <div style={{ background: "var(--color-bg-panel)", border: "1px solid var(--color-border)", borderRadius: 14, padding: "36px 40px", width: 400, boxShadow: "0 20px 60px rgba(28,20,16,0.18)", animation: "slideIn 0.2s ease", position: "relative", margin: "auto" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 24 }}>
          <div style={{ width: 34, height: 34, borderRadius: 8, background: "var(--color-maroon)", display: "flex", alignItems: "center", justifyContent: "center" }}>
            <svg width="18" height="18" viewBox="0 0 16 16" fill="none"><path d="M3 4h10M3 8h7M3 12h5" stroke="#FAF7F2" strokeWidth="1.8" strokeLinecap="round" /></svg>
          </div>
          <span style={{ fontFamily: "var(--font-serif)", fontSize: 20, fontWeight: 700, color: "var(--color-maroon)", letterSpacing: "-0.02em" }}>CodeForge</span>
        </div>

        <h2 style={{ fontFamily: "var(--font-serif)", fontSize: 22, fontWeight: 700, color: "var(--color-text-primary)", margin: "0 0 6px", letterSpacing: "-0.02em" }}>
          {mode === "login" ? "Đăng nhập" : "Đăng ký tài khoản học sinh"}
        </h2>
        <p style={{ fontFamily: "var(--font-sans)", fontSize: 13, color: "var(--color-text-muted)", margin: "0 0 20px" }}>
          {mode === "login"
            ? "Đăng nhập bằng tài khoản đã đăng ký trên PTIT Online Judge."
            : "Mọi tài khoản đăng ký ở đây đều là tài khoản học sinh."}
        </p>

        {notice && (
          <div style={{ marginBottom: 14, padding: "10px 12px", background: "var(--color-green-bg)", border: "1px solid var(--color-green-border)", borderRadius: 6, fontSize: 12.5, color: "var(--color-green)", fontFamily: "var(--font-mono)" }}>
            {notice}
          </div>
        )}

        <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          <Field label="Tên đăng nhập" value={username} onChange={(e) => setUsername(e.target.value)} autoFocus placeholder="hiennm" />

          {mode === "register" && (
            <>
              <Field label="Họ và tên" value={fullName} onChange={(e) => setFullName(e.target.value)} placeholder="Nguyễn Minh Hiển" />
              <Field label="Mã sinh viên" value={studentCode} onChange={(e) => setStudentCode(e.target.value)} placeholder="B24DCCN199" />
              <Field label="Lớp" value={className} onChange={(e) => setClassName(e.target.value)} placeholder="D24CQCN01" />
            </>
          )}

          <div>
            <label style={FIELD_LABEL}>Mật khẩu</label>
            <div style={{ position: "relative" }}>
              <input
                type={showPass ? "text" : "password"} value={password} onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••"
                style={{ ...FIELD_INPUT, padding: "0 40px 0 12px" }}
                onFocus={(e) => { e.target.style.borderColor = "var(--color-maroon)"; }}
                onBlur={(e) => { e.target.style.borderColor = "var(--color-border)"; }}
              />
              <button type="button" onClick={() => setShowPass((v) => !v)} style={{ position: "absolute", right: 10, top: "50%", transform: "translateY(-50%)", background: "none", border: "none", cursor: "pointer", color: "var(--color-text-muted)", display: "flex", alignItems: "center", padding: 2 }}>
                {showPass
                  ? <svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><path d="M1 8s3-5 7-5 7 5 7 5-3 5-7 5-7-5-7-5z" /><circle cx="8" cy="8" r="2" /><line x1="2" y1="2" x2="14" y2="14" /></svg>
                  : <svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><path d="M1 8s3-5 7-5 7 5 7 5-3 5-7 5-7-5-7-5z" /><circle cx="8" cy="8" r="2" /></svg>}
              </button>
            </div>
            {mode === "register" && <span style={{ fontFamily: "var(--font-mono)", fontSize: 10.5, color: "var(--color-text-muted)", marginTop: 5, display: "block" }}>Ít nhất 8 ký tự</span>}
          </div>

          {mode === "register" && (
            <Field label="Nhập lại mật khẩu" type="password" value={confirm} onChange={(e) => setConfirm(e.target.value)} />
          )}

          {error && (
            <div style={{ display: "flex", alignItems: "center", gap: 7, padding: "8px 12px", background: "var(--color-red-bg)", border: "1px solid var(--color-red-border)", borderRadius: 6 }}>
              <span style={{ fontFamily: "var(--font-sans)", fontSize: 12, color: "var(--color-red)" }}>{error}</span>
            </div>
          )}

          <button type="submit" disabled={busy} style={{ height: 40, background: "var(--color-maroon)", border: "none", borderRadius: 8, color: "#FAF7F2", fontSize: 14, fontWeight: 700, cursor: busy ? "not-allowed" : "pointer", fontFamily: "var(--font-sans)", marginTop: 4, opacity: busy ? 0.7 : 1, transition: "opacity 0.15s" }}>
            {busy ? "Đang xử lý..." : mode === "login" ? "Đăng nhập" : "Tạo tài khoản"}
          </button>

          <button type="button" onClick={() => switchMode(mode === "login" ? "register" : "login")} style={{ background: "none", border: "none", color: "var(--color-text-muted)", fontSize: 12.5, cursor: "pointer", fontFamily: "var(--font-sans)", textAlign: "center" }}>
            {mode === "login" ? "Chưa có tài khoản? Đăng ký" : "Đã có tài khoản? Đăng nhập"}
          </button>
        </form>

        <button onClick={onClose} style={{ position: "absolute", top: 16, right: 16, background: "none", border: "none", cursor: "pointer", color: "var(--color-text-muted)", padding: 6, borderRadius: 5, display: "flex" }}>
          <svg width="14" height="14" viewBox="0 0 10 10" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"><line x1="1" y1="1" x2="9" y2="9" /><line x1="9" y1="1" x2="1" y2="9" /></svg>
        </button>
      </div>
    </div>
  );
}
