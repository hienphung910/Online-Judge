import { useCallback, useEffect, useState } from "react";
import Problems from "./pages/Problems";
import SubmitPage from "./pages/Submit";
import Submissions from "./pages/Submissions";
import Leaderboard from "./pages/Leaderboard";
import Login from "./pages/Login";
import AdminProblems from "./pages/AdminProblems";
import { api, getToken, setToken, setUnauthorizedHandler } from "./api";
import type { AuthUser, LanguageInfo, Problem } from "./types";

type Page = "Bài tập" | "Nộp bài" | "Lịch sử nộp" | "Bảng xếp hạng" | "Thêm bài tập";

const BASE_NAV: Page[] = ["Bài tập", "Nộp bài", "Lịch sử nộp", "Bảng xếp hạng"];

export default function App() {
  const [page, setPage] = useState<Page>("Bài tập");
  const [problems, setProblems] = useState<Problem[]>([]);
  const [languages, setLanguages] = useState<LanguageInfo[]>([]);
  const [auth, setAuth] = useState<AuthUser | null>(null);
  const [checkingSession, setCheckingSession] = useState(true);
  const [online, setOnline] = useState<boolean | null>(null);
  const [preselected, setPreselected] = useState<string>("");
  const [reloadKey, setReloadKey] = useState(0);

  const isAdmin = auth?.role === "ADMIN";
  const navItems: Page[] = isAdmin ? [...BASE_NAV, "Thêm bài tập"] : BASE_NAV;

  /** May chu bao 401 (token het han) -> quay ve man hinh dang nhap. */
  useEffect(() => {
    setUnauthorizedHandler(() => {
      setAuth(null);
      setProblems([]);
    });
    return () => setUnauthorizedHandler(null);
  }, []);

  /** Con token trong sessionStorage thi hoi lai may chu xem con hieu luc khong. */
  useEffect(() => {
    let alive = true;
    if (!getToken()) {
      setCheckingSession(false);
      return;
    }
    api
      .me()
      .then((user) => alive && setAuth(user))
      .catch(() => alive && setToken(null))
      .finally(() => alive && setCheckingSession(false));
    return () => {
      alive = false;
    };
  }, []);

  const loadProblems = useCallback(async () => {
    const [p, l] = await Promise.all([api.problems(), api.languages()]);
    setProblems(p);
    setLanguages(l);
  }, []);

  /** Sau khi dang nhap moi tai du lieu (cac endpoint nay deu can token). */
  useEffect(() => {
    if (!auth) return;
    let alive = true;
    loadProblems()
      .then(() => alive && setOnline(true))
      .catch(() => alive && setOnline(false));
    return () => {
      alive = false;
    };
  }, [auth, loadProblems]);

  /** Tu trang Bài tập bam "Nộp bài" -> nhay sang form voi bai da chon san. */
  const goSubmit = useCallback((problemId: string) => {
    setPreselected(problemId);
    setPage("Nộp bài");
  }, []);

  /** Sau khi nop xong: bao cac trang khac tai lai va cap nhat so bai da giai. */
  const onSubmitted = useCallback(() => {
    setReloadKey((k) => k + 1);
    api.me().then(setAuth).catch(() => undefined);
  }, []);

  /** Admin vua tao bai moi -> nap lai danh sach de bai moi hien ngay. */
  const onProblemCreated = useCallback(() => {
    loadProblems().catch(() => undefined);
    setReloadKey((k) => k + 1);
  }, [loadProblems]);

  const doLogout = useCallback(async () => {
    try {
      await api.logout();
    } catch {
      // token co the da het han - van dang xuat o phia trinh duyet
    }
    setToken(null);
    setAuth(null);
    setProblems([]);
    setPage("Bài tập");
  }, []);

  const shell = (children: React.ReactNode) => (
    <div
      style={{
        height: "100%", display: "flex", flexDirection: "column",
        background: "var(--color-bg-base)", fontFamily: "var(--font-sans)",
        color: "var(--color-text-primary)", overflow: "hidden",
      }}
    >
      {children}
    </div>
  );

  if (checkingSession) {
    return shell(
      <div style={{ flex: 1, display: "flex", alignItems: "center", justifyContent: "center" }}>
        <span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-muted)" }}>
          đang kiểm tra phiên đăng nhập...
        </span>
      </div>,
    );
  }

  if (!auth) {
    return shell(<Login onLoggedIn={setAuth} />);
  }

  return shell(
    <>
      <nav
        style={{
          display: "flex", alignItems: "center", height: 46, padding: "0 20px",
          borderBottom: "1px solid var(--color-border)", background: "var(--color-bg-panel)",
          flexShrink: 0, gap: 14,
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
          <div
            style={{
              width: 22, height: 22, borderRadius: 5,
              background: "linear-gradient(135deg,#50E3C2 0%,#0891b2 100%)",
              display: "flex", alignItems: "center", justifyContent: "center",
              fontSize: 10, fontWeight: 700, color: "#0b0f1a", fontFamily: "var(--font-mono)",
            }}
          >
            CP
          </div>
          <span style={{ fontWeight: 600, fontSize: 13, letterSpacing: "-0.01em" }}>PTIT Online Judge</span>
        </div>

        <div style={{ width: 1, height: 18, background: "var(--color-border)" }} />

        {navItems.map((item) => {
          const active = page === item;
          const admin = item === "Thêm bài tập";
          return (
            <button
              key={item}
              onClick={() => setPage(item)}
              style={{
                background: active ? "var(--color-bg-raised)" : "none",
                border: active ? "1px solid var(--color-border)" : "1px solid transparent",
                color: active
                  ? "var(--color-text-primary)"
                  : admin
                    ? "#50E3C2"
                    : "var(--color-text-muted)",
                borderRadius: 5, padding: "5px 11px", fontSize: 12.5, cursor: "pointer",
              }}
            >
              {item}
            </button>
          );
        })}

        <div style={{ flex: 1 }} />

        {/* Trang thai ket noi may chu Java */}
        <span
          style={{
            fontFamily: "var(--font-mono)", fontSize: 11,
            color: online === false ? "#f87171" : "var(--color-text-muted)",
          }}
        >
          {online === null ? "đang kết nối..." : online ? "● máy chủ Java: sẵn sàng" : "● không kết nối được máy chủ"}
        </span>

        {/* Nguoi dang dang nhap + so bai da giai */}
        <div
          style={{
            display: "flex", alignItems: "center", gap: 8, height: 28, padding: "0 10px",
            background: "var(--color-bg-raised)", border: "1px solid var(--color-border)",
            borderRadius: 6,
          }}
          title={`${auth.roleName} ${auth.fullName}`}
        >
          <span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-accent)" }}>
            @{auth.username}
          </span>
          {isAdmin && (
            <span
              style={{
                fontFamily: "var(--font-mono)", fontSize: 9.5, fontWeight: 700, letterSpacing: "0.06em",
                color: "#fbbf24", background: "rgba(251,191,36,0.10)",
                border: "1px solid rgba(251,191,36,0.25)", borderRadius: 4, padding: "1px 5px",
              }}
            >
              ADMIN
            </span>
          )}
          <span style={{ fontFamily: "var(--font-mono)", fontSize: 11, color: "var(--color-text-muted)" }}>
            đã giải {auth.solvedCount}
          </span>
        </div>

        <button
          onClick={() => void doLogout()}
          style={{
            height: 28, padding: "0 11px", background: "none",
            border: "1px solid var(--color-border)", borderRadius: 6,
            color: "var(--color-text-muted)", fontSize: 12,
            fontFamily: "var(--font-mono)", cursor: "pointer",
          }}
        >
          Đăng xuất
        </button>
      </nav>

      <div style={{ flex: 1, overflow: "hidden", display: "flex" }}>
        {online === false ? (
          <div
            style={{
              flex: 1, display: "flex", alignItems: "center", justifyContent: "center",
              flexDirection: "column", gap: 10,
            }}
          >
            <div style={{ fontFamily: "var(--font-mono)", fontSize: 13, color: "#f87171" }}>
              Không kết nối được máy chủ Java
            </div>
            <div
              style={{
                fontFamily: "var(--font-mono)", fontSize: 12,
                color: "var(--color-text-muted)", textAlign: "center", lineHeight: 1.7,
              }}
            >
              Hãy chạy ở thư mục gốc của project:
              <br />
              <code style={{ color: "var(--color-text-accent)" }}>run.ps1 --serve</code>
              <br />
              rồi tải lại trang này.
            </div>
          </div>
        ) : (
          <>
            {page === "Bài tập" && <Problems problems={problems} onSubmitClick={goSubmit} />}
            {page === "Nộp bài" && (
              <SubmitPage
                problems={problems}
                languages={languages}
                username={auth.username}
                preselectedProblem={preselected}
                onSubmitted={onSubmitted}
              />
            )}
            {page === "Lịch sử nộp" && <Submissions reloadKey={reloadKey} />}
            {page === "Bảng xếp hạng" && <Leaderboard reloadKey={reloadKey} problems={problems} />}
            {page === "Thêm bài tập" && isAdmin && <AdminProblems onCreated={onProblemCreated} />}
          </>
        )}
      </div>
    </>,
  );
}
