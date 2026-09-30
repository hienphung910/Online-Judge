import { useState } from "react";
import { useAuth } from "../auth";

type Mode = "login" | "register";

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

  function switchMode(next: Mode) { setMode(next); setError(""); setNotice(""); setPassword(""); setConfirm(""); }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault(); setError(""); setNotice("");
    if (mode === "login") {
      if (!username || !password) { setError("Hãy nhập tên đăng nhập và mật khẩu."); return; }
      setBusy(true);
      try { await login(username.trim(), password); onClose(); }
      catch (e2) { setError(e2 instanceof Error ? e2.message : String(e2)); }
      finally { setBusy(false); }
      return;
    }
    if (password.length < 8) { setError("Mật khẩu phải có ít nhất 8 ký tự."); return; }
    if (password !== confirm) { setError("Hai lần nhập mật khẩu không khớp."); return; }
    setBusy(true);
    try {
      await register({ username: username.trim(), password, fullName: fullName.trim(), studentCode: studentCode.trim(), className: className.trim() });
      switchMode("login"); setNotice(`Đã tạo tài khoản @${username.trim()}. Mời bạn đăng nhập.`);
    } catch (e2) { setError(e2 instanceof Error ? e2.message : String(e2)); }
    finally { setBusy(false); }
  }

  const inputStyle: React.CSSProperties = {
    width: "100%", height: 44, padding: "0 14px", background: "#fff",
    border: "1px solid #E0E0E0", borderRadius: 8, color: "#212121",
    fontSize: 14, outline: "none", boxSizing: "border-box",
  };

  return (
    <div
      style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.4)", zIndex: 999, display: "flex", alignItems: "center", justifyContent: "center", padding: 16 }}
      onClick={(e) => { if (e.target === e.currentTarget) onClose(); }}
    >
      <div style={{
        background: "#fff", borderRadius: 12, padding: "36px 40px", width: 400,
        boxShadow: "0 16px 48px rgba(0,0,0,0.15)", animation: "slideIn 0.2s ease", position: "relative",
      }}>
        <h2 style={{ fontSize: 22, fontWeight: 700, color: "#212121", margin: "0 0 6px" }}>
          {mode === "login" ? "Đăng nhập" : "Đăng ký tài khoản"}
        </h2>
        <p style={{ fontSize: 13, color: "#9E9E9E", margin: "0 0 24px" }}>
          {mode === "login" ? "Truy cập hệ thống chấm bài" : "Tạo tài khoản học sinh mới"}
        </p>

        {notice && (
          <div style={{ marginBottom: 16, padding: "10px 14px", background: "#E8F5E9", border: "1px solid #C8E6C9", borderRadius: 6, fontSize: 12.5, color: "#2E7D32" }}>{notice}</div>
        )}

        <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          <div>
            <div style={{ display: "flex", alignItems: "center", gap: 8, ...inputStyle, padding: 0, paddingLeft: 12 }}>
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="#BDBDBD" strokeWidth="1.4"><circle cx="8" cy="5" r="3" /><path d="M2 14c0-3.3 2.7-6 6-6s6 2.7 6 6" /></svg>
              <input
                type="text" placeholder="Tên đăng nhập" value={username} onChange={(e) => setUsername(e.target.value)} autoFocus
                style={{ flex: 1, border: "none", outline: "none", fontSize: 14, height: "100%", background: "transparent" }}
              />
            </div>
          </div>

          {mode === "register" && (
            <>
              <input type="text" placeholder="Họ và tên" value={fullName} onChange={(e) => setFullName(e.target.value)} style={inputStyle} />
              <input type="text" placeholder="Mã sinh viên" value={studentCode} onChange={(e) => setStudentCode(e.target.value)} style={inputStyle} />
              <input type="text" placeholder="Lớp" value={className} onChange={(e) => setClassName(e.target.value)} style={inputStyle} />
            </>
          )}

          <div>
            <div style={{ display: "flex", alignItems: "center", gap: 8, ...inputStyle, padding: 0, paddingLeft: 12, paddingRight: 8 }}>
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="#BDBDBD" strokeWidth="1.4"><rect x="3" y="7" width="10" height="7" rx="1.5" /><path d="M5 7V5a3 3 0 0 1 6 0v2" /></svg>
              <input
                type={showPass ? "text" : "password"} placeholder="Mật khẩu" value={password} onChange={(e) => setPassword(e.target.value)}
                style={{ flex: 1, border: "none", outline: "none", fontSize: 14, height: "100%", background: "transparent" }}
              />
              <button type="button" onClick={() => setShowPass((v) => !v)} style={{ background: "none", border: "none", cursor: "pointer", color: "#BDBDBD", display: "flex", padding: 4 }}>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.4"><path d="M1 8s3-5 7-5 7 5 7 5-3 5-7 5-7-5-7-5z" /><circle cx="8" cy="8" r="2" />{showPass && <line x1="2" y1="2" x2="14" y2="14" />}</svg>
              </button>
            </div>
            {mode === "login" && <div style={{ textAlign: "right", marginTop: 6 }}><span style={{ fontSize: 12, color: "var(--color-red)", cursor: "pointer" }}>Quên mật khẩu?</span></div>}
          </div>

          {mode === "register" && (
            <input type="password" placeholder="Nhập lại mật khẩu" value={confirm} onChange={(e) => setConfirm(e.target.value)} style={inputStyle} />
          )}

          {error && (
            <div style={{ padding: "10px 14px", background: "#FFEBEE", border: "1px solid #FFCDD2", borderRadius: 6, fontSize: 12.5, color: "#C62828" }}>{error}</div>
          )}

          <button type="submit" disabled={busy} style={{
            height: 44, background: "var(--color-red)", border: "none", borderRadius: 8,
            color: "#fff", fontSize: 15, fontWeight: 600, cursor: busy ? "not-allowed" : "pointer",
            marginTop: 4, opacity: busy ? 0.6 : 1,
          }}>
            {busy ? "Đang xử lý..." : mode === "login" ? "Đăng nhập" : "Tạo tài khoản"}
          </button>



          <button type="button" onClick={() => switchMode(mode === "login" ? "register" : "login")} style={{
            background: "none", border: "none", color: "#9E9E9E", fontSize: 13, cursor: "pointer", textAlign: "center",
          }}>
            {mode === "login" ? "Chưa có tài khoản? Đăng ký" : "Đã có tài khoản? Đăng nhập"}
          </button>
        </form>

        <button onClick={onClose} style={{
          position: "absolute", top: 14, right: 14, background: "none", border: "none",
          cursor: "pointer", color: "#BDBDBD", fontSize: 18, lineHeight: 1,
        }}>×</button>
      </div>
    </div>
  );
}
