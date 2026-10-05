import { useCallback, useEffect, useState } from "react";
import { AuthProvider, useAuth } from "./auth";
import { api } from "./api";
import type { LanguageInfo, Problem, Topic } from "./types";
import Problems from "./pages/Problems";
import Submissions from "./pages/Submissions";
import Contests from "./pages/Contests";
import Leaderboard from "./pages/Leaderboard";
import AdminPanel from "./pages/admin/AdminPanel";
import StreakBadge, { StreakToast } from "./components/StreakBadge";
import { useStreak } from "./streak";


type Page = "Problems" | "Submissions" | "Contests" | "Leaderboard" | "Admin";

const NAV_ITEMS: { key: Page; label: string; icon: JSX.Element }[] = [
  {
    key: "Problems", label: "Lớp học",
    icon: <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.4"><rect x="2" y="2" width="12" height="12" rx="2" /><path d="M2 6h12M6 6v8" /></svg>,
  },
  {
    key: "Submissions", label: "Trạng thái",
    icon: <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.4"><rect x="2" y="2" width="12" height="12" rx="2" /><path d="M5 5h6M5 8h6M5 11h4" /></svg>,
  },
  {
    key: "Contests", label: "Bài nộp",
    icon: <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.4"><path d="M4 2v12M12 2v12M2 4h12M2 12h12" /></svg>,
  },
  {
    key: "Leaderboard", label: "Xếp hạng",
    icon: <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.4"><circle cx="8" cy="5" r="3" /><path d="M4 14l4-4 4 4" /></svg>,
  },
];

function AppShell() {
  const { user, checking, logout, login, register } = useAuth();
  const [page, setPage] = useState<Page>("Problems");

  const [avatarOpen, setAvatarOpen] = useState(false);

  const [problems, setProblems] = useState<Problem[]>([]);
  const [topics, setTopics] = useState<Topic[]>([]);
  const [languages, setLanguages] = useState<LanguageInfo[]>([]);
  const [online, setOnline] = useState<boolean | null>(null);
  const [reloadKey, setReloadKey] = useState(0);

  const [loginMode, setLoginMode] = useState<"login" | "register">("login");
  const [loginUser, setLoginUser] = useState("");
  const [loginPass, setLoginPass] = useState("");
  const [loginConfirm, setLoginConfirm] = useState("");
  const [loginFullName, setLoginFullName] = useState("");
  const [loginStudentCode, setLoginStudentCode] = useState("");
  const [loginClassName, setLoginClassName] = useState("");
  const [loginError, setLoginError] = useState("");
  const [loginNotice, setLoginNotice] = useState("");
  const [loginBusy, setLoginBusy] = useState(false);
  const [showPass, setShowPass] = useState(false);

  const isAdmin = user?.role === "ADMIN";
  const streak = useStreak(user?.username ?? null, reloadKey);

  const loadProblems = useCallback(async () => {
    // Lo trinh la tuy chon: loi khi tai chu de khong duoc lam hong ca trang bai tap.
    const [p, l, t] = await Promise.all([api.problems(), api.languages(), api.topics().catch(() => [])]);
    setProblems(p);
    setLanguages(l);
    setTopics(t);
  }, []);

  useEffect(() => {
    if (!user) { setProblems([]); setOnline(null); return; }
    let alive = true;
    loadProblems()
      .then(() => alive && setOnline(true))
      .catch(() => alive && setOnline(false));
    return () => { alive = false; };
  }, [user, loadProblems]);

  const onSubmitted = useCallback(() => { setReloadKey((k) => k + 1); }, []);
  const onProblemCreated = useCallback(() => { loadProblems().catch(() => undefined); setReloadKey((k) => k + 1); }, [loadProblems]);

  function handleLogout() { logout(); setPage("Problems"); setAvatarOpen(false); }

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault(); setLoginError(""); setLoginNotice("");
    if (loginMode === "login") {
      if (!loginUser || !loginPass) { setLoginError("Hãy nhập tên đăng nhập và mật khẩu."); return; }
      setLoginBusy(true);
      try { await login(loginUser.trim(), loginPass); }
      catch (e2) { setLoginError(e2 instanceof Error ? e2.message : String(e2)); }
      finally { setLoginBusy(false); }
      return;
    }
    if (loginPass.length < 8) { setLoginError("Mật khẩu phải có ít nhất 8 ký tự."); return; }
    if (loginPass !== loginConfirm) { setLoginError("Hai lần nhập mật khẩu không khớp."); return; }
    setLoginBusy(true);
    try {
      await register({ username: loginUser.trim(), password: loginPass, fullName: loginFullName.trim(), studentCode: loginStudentCode.trim(), className: loginClassName.trim() });
      setLoginMode("login"); setLoginNotice(`Đã tạo tài khoản @${loginUser.trim()}. Mời bạn đăng nhập.`); setLoginPass(""); setLoginConfirm("");
    } catch (e2) { setLoginError(e2 instanceof Error ? e2.message : String(e2)); }
    finally { setLoginBusy(false); }
  }

  const inputBox: React.CSSProperties = {
    width: "100%", height: 44, padding: "0 14px", background: "#fff",
    border: "1px solid #E0E0E0", borderRadius: 8, color: "#212121",
    fontSize: 14, outline: "none", boxSizing: "border-box",
  };

  if (checking) {
    return (
      <div style={{ height: "100%", display: "flex", alignItems: "center", justifyContent: "center", background: "var(--color-page-bg)" }}>
        <span style={{ fontSize: 13, color: "var(--color-text-muted)" }}>đang kiểm tra phiên đăng nhập...</span>
      </div>
    );
  }

  if (!user) {
    return (
      <div style={{ height: "100%", display: "flex", background: "var(--color-page-bg)" }}>
        {/* Left panel */}
        <div style={{ flex: "0 0 42%", background: "linear-gradient(160deg, #E3F2FD 0%, #EEF1F5 100%)", display: "flex", flexDirection: "column", justifyContent: "center", padding: "0 60px" }}>
          <div style={{ width: 60, height: 60, borderRadius: 12, background: "var(--color-red)", display: "flex", alignItems: "center", justifyContent: "center", marginBottom: 28 }}>
            <svg width="28" height="28" viewBox="0 0 16 16" fill="none"><path d="M3 4h10M3 8h7M3 12h5" stroke="#fff" strokeWidth="2" strokeLinecap="round" /></svg>
          </div>
          <h1 style={{ fontSize: 32, fontWeight: 800, color: "#212121", margin: "0 0 12px", lineHeight: 1.25 }}>CodeForge</h1>
          <p style={{ fontSize: 15, color: "#757575", margin: 0, lineHeight: 1.6 }}>
            Luyện tập và thi lập trình trực tuyến — chấm bài tự động, nhanh và chính xác.
          </p>
          <p style={{ fontSize: 13, color: "#BDBDBD", marginTop: 24, fontFamily: "var(--font-mono)" }}>{">_"} ready to judge</p>
        </div>
        {/* Right panel - inline form */}
        <div style={{ flex: 1, display: "flex", alignItems: "center", justifyContent: "center", padding: 40 }}>
          <form onSubmit={handleLogin} style={{ width: 400, display: "flex", flexDirection: "column", gap: 16 }}>
            <h2 style={{ fontSize: 24, fontWeight: 700, color: "#212121", margin: 0 }}>
              {loginMode === "login" ? "Đăng nhập" : "Đăng ký tài khoản"}
            </h2>
            <p style={{ fontSize: 14, color: "#9E9E9E", margin: 0 }}>
              {loginMode === "login" ? "Truy cập hệ thống chấm bài" : "Tạo tài khoản học sinh mới"}
            </p>

            {loginNotice && (
              <div style={{ padding: "10px 14px", background: "#E8F5E9", border: "1px solid #C8E6C9", borderRadius: 6, fontSize: 12.5, color: "#2E7D32" }}>{loginNotice}</div>
            )}

            {/* Username */}
            <div style={{ display: "flex", alignItems: "center", gap: 8, ...inputBox, padding: 0, paddingLeft: 12 }}>
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="#BDBDBD" strokeWidth="1.4"><circle cx="8" cy="5" r="3" /><path d="M2 14c0-3.3 2.7-6 6-6s6 2.7 6 6" /></svg>
              <input type="text" placeholder="Tên đăng nhập" value={loginUser} onChange={(e) => setLoginUser(e.target.value)} autoFocus
                style={{ flex: 1, border: "none", outline: "none", fontSize: 14, height: "100%", background: "transparent" }} />
            </div>

            {loginMode === "register" && (
              <>
                <input type="text" placeholder="Họ và tên" value={loginFullName} onChange={(e) => setLoginFullName(e.target.value)} style={inputBox} />
                <input type="text" placeholder="Mã sinh viên" value={loginStudentCode} onChange={(e) => setLoginStudentCode(e.target.value)} style={inputBox} />
                <input type="text" placeholder="Lớp" value={loginClassName} onChange={(e) => setLoginClassName(e.target.value)} style={inputBox} />
              </>
            )}

            {/* Password */}
            <div>
              <div style={{ display: "flex", alignItems: "center", gap: 8, ...inputBox, padding: 0, paddingLeft: 12, paddingRight: 8 }}>
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="#BDBDBD" strokeWidth="1.4"><rect x="3" y="7" width="10" height="7" rx="1.5" /><path d="M5 7V5a3 3 0 0 1 6 0v2" /></svg>
                <input type={showPass ? "text" : "password"} placeholder="Mật khẩu" value={loginPass} onChange={(e) => setLoginPass(e.target.value)}
                  style={{ flex: 1, border: "none", outline: "none", fontSize: 14, height: "100%", background: "transparent" }} />
                <button type="button" onClick={() => setShowPass((v) => !v)} style={{ background: "none", border: "none", cursor: "pointer", color: "#BDBDBD", display: "flex", padding: 4 }}>
                  <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.4"><path d="M1 8s3-5 7-5 7 5 7 5-3 5-7 5-7-5-7-5z" /><circle cx="8" cy="8" r="2" />{showPass && <line x1="2" y1="2" x2="14" y2="14" />}</svg>
                </button>
              </div>
              {loginMode === "login" && <div style={{ textAlign: "right", marginTop: 6 }}><span style={{ fontSize: 12, color: "var(--color-red)", cursor: "pointer" }}>Quên mật khẩu?</span></div>}
            </div>

            {loginMode === "register" && (
              <input type="password" placeholder="Nhập lại mật khẩu" value={loginConfirm} onChange={(e) => setLoginConfirm(e.target.value)} style={inputBox} />
            )}

            {loginError && (
              <div style={{ padding: "10px 14px", background: "#FFEBEE", border: "1px solid #FFCDD2", borderRadius: 6, fontSize: 12.5, color: "#C62828" }}>{loginError}</div>
            )}

            <button type="submit" disabled={loginBusy} style={{
              height: 44, background: "var(--color-red)", border: "none", borderRadius: 8,
              color: "#fff", fontSize: 15, fontWeight: 600, cursor: loginBusy ? "not-allowed" : "pointer",
              opacity: loginBusy ? 0.6 : 1,
            }}>
              {loginBusy ? "Đang xử lý..." : loginMode === "login" ? "Đăng nhập" : "Tạo tài khoản"}
            </button>

            <button type="button" onClick={() => { setLoginMode(loginMode === "login" ? "register" : "login"); setLoginError(""); setLoginNotice(""); setLoginPass(""); setLoginConfirm(""); }} style={{
              background: "none", border: "none", color: "#9E9E9E", fontSize: 13, cursor: "pointer", textAlign: "center",
            }}>
              {loginMode === "login" ? "Chưa có tài khoản? Đăng ký" : "Đã có tài khoản? Đăng nhập"}
            </button>
          </form>
        </div>
      </div>
    );
  }


  const navItems = isAdmin ? [...NAV_ITEMS, {
    key: "Admin" as Page, label: "Quản trị",
    icon: <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.4"><circle cx="8" cy="8" r="3" /><path d="M8 1v2M8 13v2M1 8h2M13 8h2" /></svg>,
  }] : NAV_ITEMS;

  return (
    <div style={{ height: "100%", display: "flex", flexDirection: "column", background: "var(--color-page-bg)" }}>
      {/* ═══ RED HEADER ═══ */}
      <header style={{
        display: "flex", alignItems: "center", height: 48, padding: "0 20px",
        background: "var(--color-header)", flexShrink: 0, zIndex: 50,
      }}>
        {/* Logo */}
        <div
          onClick={() => window.location.reload()}
          style={{ display: "flex", alignItems: "center", gap: 8, marginRight: 28, cursor: "pointer", userSelect: "none" }}
        >
          <div style={{ width: 30, height: 30, borderRadius: "50%", background: "rgba(255,255,255,0.15)", display: "flex", alignItems: "center", justifyContent: "center" }}>
            <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M3 4h10M3 8h7M3 12h5" stroke="#fff" strokeWidth="1.8" strokeLinecap="round" /></svg>
          </div>
          <span style={{ fontSize: 18, fontWeight: 800, color: "#fff", letterSpacing: "-0.01em" }}>CodeForge</span>
        </div>

        {/* Nav tabs */}
        <nav style={{ display: "flex", height: "100%", gap: 0 }}>
          {navItems.map((item) => {
            const active = page === item.key;
            return (
              <button
                key={item.key}
                onClick={() => setPage(item.key)}
                style={{
                  height: "100%", padding: "0 16px", border: "none", cursor: "pointer",
                  display: "flex", alignItems: "center", gap: 6,
                  background: active ? "rgba(255,255,255,0.18)" : "transparent",
                  color: active ? "#fff" : "rgba(255,255,255,0.8)",
                  fontSize: 13.5, fontWeight: active ? 700 : 500,
                  borderRadius: active ? "6px 6px 0 0" : 0,
                  transition: "background 0.15s",
                }}
                onMouseEnter={(e) => { if (!active) e.currentTarget.style.background = "rgba(255,255,255,0.08)"; }}
                onMouseLeave={(e) => { if (!active) e.currentTarget.style.background = "transparent"; }}
              >
                {item.icon}
                {item.label}
              </button>
            );
          })}
        </nav>

        <div style={{ flex: 1 }} />

        {/* Right side */}
        <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
          {/* Status dot */}
          <span style={{ display: "flex", alignItems: "center", gap: 4, fontSize: 11, color: "rgba(255,255,255,0.6)", fontFamily: "var(--font-mono)" }}>
            <span style={{
              width: 6, height: 6, borderRadius: "50%",
              background: online === false ? "#ff5252" : online ? "#69f0ae" : "rgba(255,255,255,0.4)",
              animation: online === null ? "livePulse 1.4s infinite" : "none",
            }} />
          </span>

          {/* Chuoi ngay luyen tap */}
          <StreakBadge info={streak.info} />

          {/* Notification bell */}
          <button style={{ background: "none", border: "none", color: "rgba(255,255,255,0.8)", cursor: "pointer", padding: 4, display: "flex" }}>
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.4"><path d="M4 6a4 4 0 0 1 8 0c0 4 2 5 2 5H2s2-1 2-5" /><path d="M6.5 13a1.5 1.5 0 0 0 3 0" /></svg>
          </button>

          {/* User avatar */}
          <div style={{ position: "relative" }}>
            <button
              onClick={() => setAvatarOpen((v) => !v)}
              style={{
                display: "flex", alignItems: "center", gap: 8, background: "none",
                border: "none", cursor: "pointer", padding: "4px 6px", borderRadius: 20,
              }}
            >
              <div style={{
                width: 28, height: 28, borderRadius: "50%", background: "#E57373",
                display: "flex", alignItems: "center", justifyContent: "center",
                fontSize: 11, fontWeight: 700, color: "#fff",
              }}>
                {user.username.slice(0, 2).toUpperCase()}
              </div>
              <span style={{ fontSize: 13, fontWeight: 600, color: "#fff" }}>{user.fullName || user.username}</span>
              <svg width="10" height="10" viewBox="0 0 12 12" fill="none" stroke="rgba(255,255,255,0.7)" strokeWidth="2" strokeLinecap="round" style={{ transform: avatarOpen ? "rotate(180deg)" : "none", transition: "transform 0.15s" }}><polyline points="2 4 6 8 10 4" /></svg>
            </button>

            {avatarOpen && (
              <div
                style={{
                  position: "absolute", top: "calc(100% + 6px)", right: 0,
                  background: "#fff", border: "1px solid #E0E0E0",
                  borderRadius: 10, boxShadow: "0 8px 30px rgba(0,0,0,0.12)", minWidth: 200, padding: 6, zIndex: 200,
                  animation: "slideIn 0.12s ease",
                }}
                onMouseLeave={() => setAvatarOpen(false)}
              >
                <div style={{ padding: "10px 14px 8px", borderBottom: "1px solid #F0F0F0", marginBottom: 4 }}>
                  <div style={{ fontSize: 14, fontWeight: 600, color: "#212121" }}>{user.fullName || user.username}</div>
                  <div style={{ fontSize: 11, color: "#9E9E9E", fontFamily: "var(--font-mono)" }}>@{user.username} · {user.roleName}</div>
                </div>
                {isAdmin && (
                  <button onClick={() => { setPage("Admin"); setAvatarOpen(false); }}
                    style={{ width: "100%", display: "flex", alignItems: "center", gap: 8, padding: "8px 14px", background: "none", border: "none", color: "var(--color-red)", fontSize: 13, cursor: "pointer", borderRadius: 6, textAlign: "left" }}
                    onMouseEnter={(e) => { e.currentTarget.style.background = "#FFF5F5"; }}
                    onMouseLeave={(e) => { e.currentTarget.style.background = "none"; }}
                  >
                    Quản trị
                  </button>
                )}
                <button onClick={handleLogout}
                  style={{ width: "100%", display: "flex", alignItems: "center", gap: 8, padding: "8px 14px", background: "none", border: "none", color: "#F44336", fontSize: 13, cursor: "pointer", borderRadius: 6, textAlign: "left" }}
                  onMouseEnter={(e) => { e.currentTarget.style.background = "#FFF5F5"; }}
                  onMouseLeave={(e) => { e.currentTarget.style.background = "none"; }}
                >
                  <svg width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><path d="M6 3H3a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h3" /><polyline points="10 10 14 8 10 6" /><line x1="14" y1="8" x2="6" y2="8" /></svg>
                  Đăng xuất
                </button>
              </div>
            )}
          </div>
        </div>
      </header>

      <StreakToast value={streak.increasedTo} onClose={streak.dismissIncrease} />

      {/* ═══ CONTENT ═══ */}
      <main style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden" }}>
        {online === false ? (
          <div style={{ flex: 1, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 12 }}>
            <div style={{ fontSize: 14, color: "#F44336", fontWeight: 600 }}>Không kết nối được máy chủ</div>
            <div style={{ fontSize: 13, color: "#9E9E9E", textAlign: "center", lineHeight: 1.7 }}>
              Chạy <code style={{ color: "var(--color-red)", background: "#FDECEA", padding: "2px 6px", borderRadius: 4 }}>.\run-web.ps1</code> rồi tải lại trang.
            </div>
          </div>
        ) : (
          <>
            {page === "Problems" && <Problems problems={problems} topics={topics} languages={languages} onSubmitted={onSubmitted} reloadKey={reloadKey} />}
            {page === "Submissions" && <Submissions reloadKey={reloadKey} />}
            {page === "Contests" && <Contests problems={problems} />}
            {page === "Leaderboard" && <Leaderboard reloadKey={reloadKey} problems={problems} />}
            {page === "Admin" && isAdmin && <AdminPanel onProblemCreated={onProblemCreated} problems={problems} topics={topics} />}
          </>
        )}
      </main>
    </div>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <AppShell />
    </AuthProvider>
  );
}
