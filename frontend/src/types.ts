/** Cac kieu du lieu khop 1-1 voi JSON do ApiServer.java tra ve. */

export type VerdictCode =
  | "AC"
  | "WA"
  | "TLE"
  | "MLE"
  | "RE"
  | "CE"
  | "IE"
  | "PE"
  | "PENDING";

/** Ma vai tro luu trong CSDL (cot users.role). */
export type RoleCode = "STUDENT" | "TEACHER" | "ADMIN";

/** Tai khoan dang dang nhap - KHONG bao gio chua hash hay salt mat khau. */
export interface AuthUser {
  id: string;
  username: string;
  fullName: string;
  role: RoleCode;
  roleName: string;
  canCreateProblem: boolean;
  solvedCount: number;
}

export interface LoginResponse {
  token: string;
  user: AuthUser;
}

export interface RegisterRequest {
  username: string;
  password: string;
  fullName: string;
  studentCode: string;
  className: string;
}

export interface LanguageInfo {
  name: string;
  extension: string;
  available: boolean;
  memoryLimitNote: string;
}

export interface Sample {
  input: string;
  output: string;
}

export interface Problem {
  id: string;
  title: string;
  statement: string;
  timeLimitMs: number;
  memoryLimitMb: number;
  comparator: string;
  maxPoints: number;
  /** Chi gom test vi du - test an khong bao gio duoc gui xuong trinh duyet. */
  samples: Sample[];
}

export interface TestResult {
  id: string;
  sample: boolean;
  verdict: VerdictCode;
  runtimeMs: number;
  points: number;
  message: string;
}

export interface Submission {
  id: string;
  submittedAt: string;
  author: string;
  authorName: string;
  problem: { id: string; title: string };
  language: string;
  fileName: string;
  maxPoints: number;
  verdict: VerdictCode;
  verdictName: string;
  execTimeMs: number | null;
  judgeTimeMs?: number;
  score: number | null;
  passed: number;
  total: number;
  message?: string;
  tests?: TestResult[];
  sourceCode?: string;
}

export interface ScoreRow {
  rank: number;
  username: string;
  fullName: string;
  role: RoleCode;
  roleName: string;
  total: number;
  /** So bai dat diem toi da. */
  solved: number;
  /** So bai khac nhau tung co lan nop AC (dinh nghia "so bai da giai"). */
  solvedCount: number;
  attempts: number;
  perProblem: { problemId: string; score: number }[];
}

export interface Stats {
  totalSubmissions: number;
  byVerdict: Partial<Record<VerdictCode, number>>;
}

/** Nguoi nop duoc backend lay tu token, client khong gui username nua. */
export interface SubmitRequest {
  problemId: string;
  language: string;
  code: string;
}

/* ------------------------------------------------------------------------- *
 * Su kien do POST /api/submit/stream day ve theo chuan Server-Sent Events.
 * Khop 1-1 voi SseJudgeListener.java ben backend.
 * ------------------------------------------------------------------------- */

export interface JudgeStartedEvent {
  submissionId: string;
  problemId: string;
  language: string;
  /** Tong so test, biet ngay tu dau de ve duoc thanh tien trinh. */
  total: number;
}

export interface CompiledEvent {
  success: boolean;
  /** Nguyen van thong bao cua trinh bien dich khi that bai. */
  message: string;
}

/** Mot test vua cham xong - den ngay khi no chay xong, khong cho ca loat. */
export interface LiveTestEvent {
  index: number;
  total: number;
  id: string;
  sample: boolean;
  verdict: VerdictCode;
  runtimeMs: number;
  points: number;
  message: string;
}

export interface JudgeFinishedEvent {
  verdict: VerdictCode;
  passed: number;
  total: number;
  score: number;
}

/**
 * Union co the phan biet duoc: TypeScript se bat loi neu quen xu ly mot nhanh,
 * nen them su kien moi o backend la trinh bien dich nhac ngay o frontend.
 */
export type JudgeEvent =
  | { type: "started"; data: JudgeStartedEvent }
  | { type: "compiled"; data: CompiledEvent }
  | { type: "test"; data: LiveTestEvent }
  | { type: "finished"; data: JudgeFinishedEvent }
  | { type: "done"; data: Submission }
  | { type: "error"; data: { error: string } };

export interface NewTestInput {
  name: string;
  input: string;
  output: string;
  sample: boolean;
}

export interface NewProblemRequest {
  id: string;
  title: string;
  statement: string;
  timeLimitMs: number;
  memoryLimitMb: number;
  comparator: string;
  totalPoints: number;
  tests: NewTestInput[];
}

export interface NewProblemResponse {
  message: string;
  problem: {
    id: string;
    title: string;
    timeLimitMs: number;
    memoryLimitMb: number;
    comparator: string;
    maxPoints: number;
  };
}
