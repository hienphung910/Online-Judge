import { useState } from "react";
import { api, setToken } from "../api";
import { Button, ErrorBox, MONO, Panel } from "../components/ui";
import type { AuthUser } from "../types";

type Mode = "login" | "register";

/** O nhap dung chung cho ca hai form, giu dung phong cach cua ban thiet ke. */
function Field({
  label,
  value,
  onChange,
  type = "text",
  placeholder,
  hint,
  autoFocus,
}: {
  label: string;
  value: string;
  onChange: (v: string) => void;
  type?: string;
  placeholder?: string;
  hint?: string;
  autoFocus?: boolean;
}) {
  return (
    <label style={{ display: "flex", flexDirection: "column", gap: 5 }}>
      <span
        style={{
          ...MONO, fontSize: 9.5, letterSpacing: "0.1em",
          textTransform: "uppercase", color: "var(--color-text-muted)",
        }}
      >
        {label}
      </span>
      <input
        value={value}
        type={type}
        autoFocus={autoFocus}
        placeholder={placeholder}
        onChange={(e) => onChange(e.target.value)}
        style={{
          height: 32, padding: "0 10px", background: "var(--color-bg-base)",
          border: "1px solid var(--color-border)", borderRadius: 6,
          color: "var(--color-text-primary)", fontFamily: "var(--font-mono)",
          fontSize: 12.5, outline: "none",
        }}
      />
      {hint && (
        <span style={{ ...MONO, fontSize: 10.5, color: "var(--color-text-muted)" }}>{hint}</span>
      )}
    </label>
  );
}

/**
 * Man hinh dang nhap / dang ky.
 *
 * Thay cho dropdown chon nguoi dung truoc day: bay gio muon nop bai duoi ten ai
 * thi phai co mat khau cua nguoi do.
 */
export default function Login({ onLoggedIn }: { onLoggedIn: (user: AuthUser) => void }) {
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

  function switchMode(next: Mode) {
    setMode(next);
    setError("");
    setNotice("");
    setPassword("");
    setConfirm("");
  }

  async function doLogin() {
    setError("");
    setNotice("");
    if (!username.trim() || !password) {
      setError("Hãy nhập tên đăng nhập và mật khẩu.");
      return;
    }
    setBusy(true);
    try {
      const res = await api.login(username.trim(), password);
      setToken(res.token);
      onLoggedIn(res.user);
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setBusy(false);
    }
  }

  async function doRegister() {
    setError("");
    setNotice("");
    if (password.length < 8) {
      setError("Mật khẩu phải có ít nhất 8 ký tự.");
      return;
    }
    if (password !== confirm) {
      setError("Hai lần nhập mật khẩu không khớp.");
      return;
    }
    setBusy(true);
    try {
      await api.register({
        username: username.trim(),
        password,
        fullName: fullName.trim(),
        studentCode: studentCode.trim(),
        className: className.trim(),
      });
      setMode("login");
      setPassword("");
      setConfirm("");
      setNotice(`Đã tạo tài khoản @${username.trim()}. Mời bạn đăng nhập.`);
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setBusy(false);
    }
  }

  const submit = mode === "login" ? doLogin : doRegister;

  return (
    <div
      style={{
        flex: 1, display: "flex", alignItems: "center", justifyContent: "center",
        padding: 16, overflow: "auto",
      }}
    >
      <div style={{ width: "100%", maxWidth: 400, display: "flex", flexDirection: "column", gap: 14 }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10, justifyContent: "center" }}>
          <div
            style={{
              width: 30, height: 30, borderRadius: 7,
              background: "linear-gradient(135deg,#50E3C2 0%,#0891b2 100%)",
              display: "flex", alignItems: "center", justifyContent: "center",
              fontSize: 12, fontWeight: 700, color: "#0b0f1a", fontFamily: "var(--font-mono)",
            }}
          >
            CP
          </div>
          <span style={{ fontWeight: 600, fontSize: 16, letterSpacing: "-0.01em" }}>
            PTIT Online Judge
          </span>
        </div>

        <Panel title={mode === "login" ? "Đăng nhập" : "Đăng ký tài khoản học sinh"}>
          {error && <ErrorBox message={error} />}
          {notice && (
            <div
              style={{
                margin: 12, padding: "10px 14px", borderRadius: 6, fontSize: 12.5,
                background: "rgba(74,222,128,0.08)", border: "1px solid rgba(74,222,128,0.25)",
                color: "#4ade80", fontFamily: "var(--font-mono)",
              }}
            >
              {notice}
            </div>
          )}

          <form
            onSubmit={(e) => {
              e.preventDefault();
              if (!busy) void submit();
            }}
            style={{ padding: 14, display: "flex", flexDirection: "column", gap: 12 }}
          >
            <Field
              label="Tên đăng nhập"
              value={username}
              onChange={setUsername}
              autoFocus
              placeholder="hiennm"
              hint={mode === "register" ? "3-32 ký tự, chỉ chữ, số, dấu chấm hoặc gạch dưới" : undefined}
            />

            {mode === "register" && (
              <>
                <Field label="Họ và tên" value={fullName} onChange={setFullName} placeholder="Nguyễn Minh Hiển" />
                <Field label="Mã sinh viên" value={studentCode} onChange={setStudentCode} placeholder="B24DCCN199" />
                <Field label="Lớp" value={className} onChange={setClassName} placeholder="D24CQCN01" />
              </>
            )}

            <Field
              label="Mật khẩu"
              value={password}
              onChange={setPassword}
              type="password"
              hint={mode === "register" ? "Ít nhất 8 ký tự" : undefined}
            />

            {mode === "register" && (
              <Field label="Nhập lại mật khẩu" value={confirm} onChange={setConfirm} type="password" />
            )}

            <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
              <Button variant="primary" onClick={() => void submit()} disabled={busy}>
                {busy ? "Đang xử lý..." : mode === "login" ? "Đăng nhập" : "Tạo tài khoản"}
              </Button>
              <div style={{ flex: 1 }} />
              <Button onClick={() => switchMode(mode === "login" ? "register" : "login")} disabled={busy}>
                {mode === "login" ? "Chưa có tài khoản?" : "Đã có tài khoản?"}
              </Button>
            </div>
            {/* Nut submit an: cho phep bam Enter trong o nhap de gui form */}
            <button type="submit" style={{ display: "none" }} aria-hidden />
          </form>
        </Panel>

        <div
          style={{
            ...MONO, fontSize: 11, color: "var(--color-text-muted)",
            textAlign: "center", lineHeight: 1.8,
          }}
        >
          Tài khoản quản trị được tạo lần đầu ở terminal khi chạy máy chủ.
          <br />
          Học sinh tự đăng ký ở đây - mọi tài khoản đăng ký đều là học sinh.
        </div>
      </div>
    </div>
  );
}
