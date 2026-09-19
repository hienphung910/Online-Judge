import type {
  AuthUser,
  JudgeEvent,
  LanguageInfo,
  LoginResponse,
  NewProblemRequest,
  NewProblemResponse,
  Problem,
  RegisterRequest,
  ScoreRow,
  Stats,
  Submission,
  SubmitRequest,
} from "./types";

/**
 * Lop mong goi REST API cua may chu Java.
 * Khi chay "npm run dev", Vite chuyen tiep /api sang http://localhost:8080 (xem vite.config.ts).
 * Khi chay che do --serve, frontend duoc chinh may chu Java phuc vu nen cung duong dan.
 *
 * Token dang nhap duoc giu trong sessionStorage (dong tab la mat) va tu dong gan
 * vao header Authorization cua moi request.
 */

const TOKEN_KEY = "oj.token";

let token: string | null = readStoredToken();
let onUnauthorized: (() => void) | null = null;

function readStoredToken(): string | null {
  try {
    return sessionStorage.getItem(TOKEN_KEY);
  } catch {
    return null; // trinh duyet chan sessionStorage (che do rieng tu) -> chi giu trong bo nho
  }
}

export function setToken(value: string | null) {
  token = value;
  try {
    if (value) sessionStorage.setItem(TOKEN_KEY, value);
    else sessionStorage.removeItem(TOKEN_KEY);
  } catch {
    // khong luu duoc thi van dung duoc trong phien hien tai
  }
}

export function getToken(): string | null {
  return token;
}

/** App dang ky ham nay de tu dang xuat khi may chu tra ve 401. */
export function setUnauthorizedHandler(handler: (() => void) | null) {
  onUnauthorized = handler;
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const headers: Record<string, string> = { "Content-Type": "application/json" };
  if (token) headers.Authorization = `Bearer ${token}`;

  const res = await fetch(path, { ...init, headers: { ...headers, ...(init?.headers ?? {}) } });
  const text = await res.text();
  let data: unknown = null;
  if (text) {
    try {
      data = JSON.parse(text);
    } catch {
      throw new Error(`Máy chủ trả về dữ liệu không phải JSON: ${text.slice(0, 120)}`);
    }
  }
  if (!res.ok) {
    if (res.status === 401) {
      setToken(null);
      onUnauthorized?.();
    }
    const message =
      data && typeof data === "object" && data !== null && "error" in data
        ? String((data as { error: unknown }).error)
        : `Lỗi HTTP ${res.status}`;
    throw new Error(message);
  }
  return data as T;
}

function postJson<T>(path: string, body: unknown): Promise<T> {
  return request<T>(path, { method: "POST", body: JSON.stringify(body) });
}

/**
 * Nop bai va nhan ket qua TUNG TEST ngay khi may chu cham xong test do.
 *
 * Vi sao khong dung EventSource co san cua trinh duyet: EventSource chi goi duoc
 * GET, ma nop bai thi phai POST kem ma nguon. Nen o day doc thang than phan hoi
 * bang ReadableStream roi tu tach khung SSE - van dung chuan SSE, chi la tu doc.
 *
 * Loi truoc khi stream bat dau (sai bai, thieu quyen...) van la JSON kem ma HTTP
 * binh thuong, nen xu ly y het cac endpoint khac.
 */
async function submitStream(
  body: SubmitRequest,
  onEvent: (event: JudgeEvent) => void,
): Promise<void> {
  const headers: Record<string, string> = { "Content-Type": "application/json" };
  if (token) headers.Authorization = `Bearer ${token}`;

  const res = await fetch("/api/submit/stream", {
    method: "POST",
    headers,
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    const text = await res.text();
    if (res.status === 401) {
      setToken(null);
      onUnauthorized?.();
    }
    let message = `Lỗi HTTP ${res.status}`;
    try {
      const parsed: unknown = JSON.parse(text);
      if (parsed && typeof parsed === "object" && "error" in parsed) {
        message = String((parsed as { error: unknown }).error);
      }
    } catch {
      // khong phai JSON thi giu thong bao mac dinh
    }
    throw new Error(message);
  }
  if (!res.body) throw new Error("Trình duyệt này không đọc được luồng phản hồi.");

  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";

  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    buffer += decoder.decode(value, { stream: true });

    // Mot khung SSE ket thuc bang dong trong. Phan du giu lai cho lan doc sau,
    // vi mot goi TCP co the cat doi giua khung.
    for (;;) {
      const cut = buffer.indexOf("\n\n");
      if (cut === -1) break;
      const frame = buffer.slice(0, cut);
      buffer = buffer.slice(cut + 2);
      const parsed = parseFrame(frame);
      if (parsed) onEvent(parsed);
    }
  }
}

/** Tach mot khung "event: <ten>\ndata: <json>" thanh doi tuong JudgeEvent. */
function parseFrame(frame: string): JudgeEvent | null {
  let event = "";
  let data = "";
  for (const line of frame.split("\n")) {
    if (line.startsWith("event:")) event = line.slice(6).trim();
    else if (line.startsWith("data:")) data += line.slice(5).trim();
  }
  if (!event || !data) return null;
  try {
    return { type: event, data: JSON.parse(data) } as JudgeEvent;
  } catch {
    return null; // khung hong thi bo qua, khong lam sap ca trang
  }
}

export const api = {
  // --- xac thuc ---
  register: (body: RegisterRequest) => postJson<{ message: string }>("/api/auth/register", body),
  login: (username: string, password: string) =>
    postJson<LoginResponse>("/api/auth/login", { username, password }),
  me: () => request<AuthUser>("/api/auth/me"),
  logout: () => postJson<{ ok: boolean }>("/api/auth/logout", {}),

  // --- du lieu ---
  languages: () => request<LanguageInfo[]>("/api/languages"),
  problems: () => request<Problem[]>("/api/problems"),
  submissions: () => request<Submission[]>("/api/submissions"),
  submission: (id: string) => request<Submission>(`/api/submissions/${encodeURIComponent(id)}`),
  scoreboard: () => request<ScoreRow[]>("/api/scoreboard"),
  stats: () => request<Stats>("/api/stats"),
  submit: (body: SubmitRequest) => postJson<Submission>("/api/submit", body),
  /** Ban stream cua submit: goi onEvent moi khi mot test vua cham xong. */
  submitStream,

  // --- quan tri (backend van kiem tra lai vai tro) ---
  createProblem: (body: NewProblemRequest) =>
    postJson<NewProblemResponse>("/api/admin/problems", body),
};
