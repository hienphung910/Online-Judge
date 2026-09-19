import { useCallback, useEffect, useState } from "react";
import { AuthProvider, useAuth } from "./auth";
import { api } from "./api";
import type { LanguageInfo, Problem } from "./types";
import Problems from "./pages/Problems";
import Submissions from "./pages/Submissions";
import Contests from "./pages/Contests";
import Leaderboard from "./pages/Leaderboard";
import AdminPanel from "./pages/admin/AdminPanel";
import LoginModal from "./components/LoginModal";

type Page = "Problems" | "Submissions" | "Contests" | "Leaderboard" | "Admin";

function Logo({ onClick }: { onClick?: () => void }) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 10, marginRight: 32, cursor: onClick ? "pointer" : "default" }} onClick={onClick}>
      <div style={{ width: 30, height: 30, borderRadius: 7, background: "var(--color-maroon)", display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0 }}>
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path d="M3 4h10M3 8h7M3 12h5" stroke="#FAF7F2" strokeWidth="1.8" strokeLinecap="round" />
        </svg>
      </div>
      <span style={{ fontFamily: "var(--font-serif)", fontSize: 17, fontWeight: 700, color: "var(--color-maroon)", letterSpacing: "-0.02em" }}>CodeForge</span>
    </div>
  );
}

function AppShell() {
  const { user, checking, logout } = useAuth();
  const [page, setPage] = useState<Page>("Problems");
  const [showLogin, setShowLogin] = useState(false);
  const [avatarOpen, setAvatarOpen] = useState(false);

  const [problems, setProblems] = useState<Problem[]>([]);
  const [languages, setLanguages] = useState<LanguageInfo[]>([]);
  const [online, setOnline] = useState<boolean | null>(null);
  const [reloadKey, setReloadKey] = useState(0);

  const isAdmin = user?.role === "ADMIN";
  const NAV: Page[] = isAdmin
    ? ["Problems", "Submissions", "Contests", "Leaderboard", "Admin"]
    : ["Problems", "Submissions", "Contests", "Leaderboard"];

  const loadProblems = useCallback(async () => {
    const [p, l] = await Promise.all([api.problems(), api.languages()]);
    setProblems(p);
    setLanguages(l);
  }, []);

  useEffect(() => {
    if (!user) { setProblems([]); setOnline(null); return; }
    let alive = true;
    loadProblems()
      .then(() => alive && setOnline(true))
      .catch(() => alive && setOnline(false));
    return () => { alive = false; };
  }, [user, loadProblems]);

  const onSubmitted = useCallback(() => {
    setReloadKey((k) => k + 1);
  }, []);

  const onProblemCreated = useCallback(() => {
    loadProblems().catch(() => undefined);
    setReloadKey((k) => k + 1);
  }, [loadProblems]);

  function handleLogout() {
    logout();
    setPage("Problems");
    setAvatarOpen(false);
  }

  if (checking) {
    return (
      <div style={{ height: "100%", display: "flex", alignItems: "center", justifyContent: "center", background: "var(--color-bg-base)" }}>
        <span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-muted)" }}>đang kiểm tra phiên đăng nhập...</span>
      </div>
    );
  }

  if (!user) {
    return (
      <div style={{ height: "100%", display: "flex", flexDirection: "column", background: "var(--color-bg-base)", fontFamily: "var(--font-sans)" }}>
        <header style={{ display: "flex", alignItems: "center", height: 52, padding: "0 32px", borderBottom: "1px solid var(--color-border)", background: "var(--color-bg-panel)" }}>
          <Logo />
        </header>
        <div style={{ flex: 1, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 18, padding: 24, textAlign: "center" }}>
          <h1 style={{ fontFamily: "var(--font-serif)", fontSize: 28, fontWeight: 700, color: "var(--color-maroon)", margin: 0, letterSpacing: "-0.02em" }}>
            PTIT Online Judge
          </h1>
          <p style={{ fontFamily: "var(--font-sans)", fontSize: 14, color: "var(--color-text-muted)", margin: 0, maxWidth: 420 }}>
            Đăng nhập để xem đề bài, nộp bài và theo dõi bảng xếp hạng.
          </p>
          <button
            onClick={() => setShowLogin(true)}
            style={{ display: "flex", alignItems: "center", gap: 8, height: 42, padding: "0 24px", background: "var(--color-maroon)", border: "none", borderRadius: 8, color: "#FAF7F2", fontSize: 14, fontWeight: 700, cursor: "pointer", fontFamily: "var(--font-sans)" }}
          >
            Đăng nhập / Đăng ký
          </button>
        </div>
        {showLogin && <LoginModal onClose={() => setShowLogin(false)} />}
        <style>{`input::placeholder { color: var(--color-text-muted); }`}</style>
      </div>
    );
  }

  return (
    <div style={{ height: "100%", display: "flex", flexDirection: "column", background: "var(--color-bg-base)", fontFamily: "var(--font-sans)", color: "var(--color-text-primary)" }}>
      <header style={{ display: "flex", alignItems: "center", height: 52, padding: "0 32px", borderBottom: "1px solid var(--color-border)", background: "var(--color-bg-panel)", flexShrink: 0, position: "relative", zIndex: 50 }}>
        <Logo onClick={() => setPage("Problems")} />

        <nav style={{ display: "flex", height: "100%" }}>
          {NAV.map((item) => {
            const active = page === item;
            const isAdminTab = item === "Admin";
            return (
              <button
                key={item}
                onClick={() => setPage(item)}
                style={{
                  position: "relative", height: "100%", padding: "0 18px", background: "none", border: "none",
                  color: active ? "var(--color-maroon)" : isAdminTab ? "var(--color-maroon)" : "var(--color-text-muted)",
                  fontSize: 13, fontWeight: active ? 600 : isAdminTab ? 500 : 400,
                  cursor: "pointer", fontFamily: "var(--font-sans)", transition: "color 0.15s",
                  display: "flex", alignItems: "center", gap: 6,
                }}
              >
                {isAdminTab && (
                  <svg width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                    <rect x="2" y="3" width="12" height="10" rx="1.5" /><path d="M5 7h6M5 10h4" />
                  </svg>
                )}
                {item}
                {active && <span style={{ position: "absolute", bottom: 0, left: "50%", transform: "translateX(-50%)", width: "60%", height: 2, background: "var(--color-maroon)", borderRadius: "1px 1px 0 0" }} />}
              </button>
            );
          })}
        </nav>

        <div style={{ flex: 1 }} />

        <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
          <span style={{ fontFamily: "var(--font-mono)", fontSize: 11, color: online === false ? "var(--color-red)" : "var(--color-text-muted)" }}>
            {online === null ? "● đang kết nối..." : online ? "● máy chủ sẵn sàng" : "● không kết nối được máy chủ"}
          </span>
          <div style={{ width: 1, height: 20, background: "var(--color-border)" }} />

          <div style={{ position: "relative" }}>
            <button
              onClick={() => setAvatarOpen((v) => !v)}
              style={{ display: "flex", alignItems: "center", gap: 8, background: "none", border: "none", cursor: "pointer", padding: "4px 6px", borderRadius: 7 }}
            >
              <div style={{ width: 30, height: 30, borderRadius: "50%", background: "var(--color-maroon)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 11, fontWeight: 700, color: "#FAF7F2", letterSpacing: "0.03em" }}>
                {user.username.slice(0, 2).toUpperCase()}
              </div>
              <div style={{ textAlign: "left" }}>
                <div style={{ fontFamily: "var(--font-sans)", fontSize: 12, fontWeight: 600, color: "var(--color-text-primary)", lineHeight: 1.2 }}>{user.username}</div>
                {isAdmin
                  ? <div style={{ fontFamily: "var(--font-mono)", fontSize: 9, color: "var(--color-maroon)", fontWeight: 700, letterSpacing: "0.06em" }}>ADMIN</div>
                  : <div style={{ fontFamily: "var(--font-mono)", fontSize: 9, color: "var(--color-text-muted)" }}>đã giải {user.solvedCount}</div>}
              </div>
              <svg width="10" height="10" viewBox="0 0 12 12" fill="none" stroke="var(--color-text-muted)" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" style={{ transform: avatarOpen ? "rotate(180deg)" : "none", transition: "transform 0.2s" }}><polyline points="2 4 6 8 10 4" /></svg>
            </button>

            {avatarOpen && (
              <div
                style={{ position: "absolute", top: "calc(100% + 6px)", right: 0, background: "var(--color-bg-panel)", border: "1px solid var(--color-border)", borderRadius: 10, boxShadow: "0 8px 28px rgba(28,20,16,0.13)", minWidth: 200, padding: 6, zIndex: 200 }}
                onMouseLeave={() => setAvatarOpen(false)}
              >
                <div style={{ padding: "8px 12px 6px", borderBottom: "1px solid var(--color-border-subtle)", marginBottom: 4 }}>
                  <div style={{ fontFamily: "var(--font-sans)", fontSize: 13, fontWeight: 600, color: "var(--color-text-primary)" }}>{user.fullName || user.username}</div>
                  <div style={{ fontFamily: "var(--font-mono)", fontSize: 10, color: "var(--color-text-muted)" }}>{user.roleName} · đã giải {user.solvedCount} bài</div>
                </div>
                {isAdmin && (
                  <button onClick={() => { setPage("Admin"); setAvatarOpen(false); }} style={{ width: "100%", display: "flex", alignItems: "center", gap: 8, padding: "7px 12px", background: "none", border: "none", color: "var(--color-maroon)", fontSize: 13, cursor: "pointer", fontFamily: "var(--font-sans)", borderRadius: 6, textAlign: "left", fontWeight: 500 }}>
                    <svg width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><rect x="2" y="3" width="12" height="10" rx="1.5" /><path d="M5 7h6M5 10h4" /></svg>
                    Admin Panel
                  </button>
                )}
                <button onClick={handleLogout} style={{ width: "100%", display: "flex", alignItems: "center", gap: 8, padding: "7px 12px", background: "none", border: "none", color: "var(--color-red)", fontSize: 13, cursor: "pointer", fontFamily: "var(--font-sans)", borderRadius: 6, textAlign: "left" }}>
                  <svg width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M6 3H3a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h3" /><polyline points="10 10 14 8 10 6" /><line x1="14" y1="8" x2="6" y2="8" /></svg>
                  Sign out
                </button>
              </div>
            )}
          </div>
        </div>
      </header>

      <main style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden" }}>
        {online === false ? (
          <div style={{ flex: 1, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 10 }}>
            <div style={{ fontFamily: "var(--font-mono)", fontSize: 13, color: "var(--color-red)" }}>Không kết nối được máy chủ Java</div>
            <div style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-muted)", textAlign: "center", lineHeight: 1.7 }}>
              Hãy chạy ở thư mục gốc của project: <code style={{ color: "var(--color-maroon)" }}>.\run-web.ps1</code>
              <br />rồi tải lại trang này.
            </div>
          </div>
        ) : (
          <>
            {page === "Problems" && <Problems problems={problems} languages={languages} onSubmitted={onSubmitted} reloadKey={reloadKey} />}
            {page === "Submissions" && <Submissions reloadKey={reloadKey} />}
            {page === "Contests" && <Contests problems={problems} />}
            {page === "Leaderboard" && <Leaderboard reloadKey={reloadKey} problems={problems} />}
            {page === "Admin" && isAdmin && <AdminPanel onProblemCreated={onProblemCreated} problems={problems} />}
          </>
        )}
      </main>

      <style>{`
        input::placeholder, textarea::placeholder { color: var(--color-text-muted); }
      `}</style>
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
