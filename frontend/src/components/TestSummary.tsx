import { MONO, VERDICT_META } from "./ui";
import type { VerdictCode } from "../types";

/**
 * Tom tat ket qua theo kieu Codeforces: KHONG liet ke tung test, chi noi truot o
 * test nao - vi du "WA on test 2, 4 · TLE on test 3".
 *
 * Vi sao bo bang tung test: nguoi hoc chi can biet minh truot o dau de quay lai
 * sua; bang day du (thoi gian, diem tung test) chi lam roi mat. Chi tiet van con
 * tren terminal nguoi cham va trong CSDL.
 *
 * Danh so theo VI TRI test (1-based) dung thu tu may chu cham, khong dung ten file
 * test (sample01, 02...) vi ten co the khong lien tuc. Test vi du ghi them "(ví dụ)"
 * de nguoi hoc biet minh truot ngay o test cong khai - cai ho co the tu chay lai.
 *
 * Dung duoc cho ca ket qua cuoi (TestResult[]) va ket qua dang chay ve tung phan
 * qua SSE (LiveTestEvent[]) - chi can moi phan tu co verdict va sample.
 */
export interface SummarizableTest {
  verdict: VerdictCode;
  sample: boolean;
}

export default function TestSummary({
  tests,
  size = 12.5,
}: {
  tests: SummarizableTest[];
  size?: number;
}) {
  // Gom cac test truot theo verdict; Map giu dung thu tu xuat hien dau tien.
  const groups = new Map<VerdictCode, string[]>();
  tests.forEach((t, i) => {
    if (t.verdict === "AC") return;
    const label = t.sample ? `${i + 1} (ví dụ)` : String(i + 1);
    const list = groups.get(t.verdict);
    if (list) list.push(label);
    else groups.set(t.verdict, [label]);
  });
  if (groups.size === 0) return null;

  return (
    <div style={{ display: "flex", gap: 14, flexWrap: "wrap", alignItems: "center", ...MONO, fontSize: size }}>
      {Array.from(groups.entries()).map(([verdict, positions]) => {
        const meta = VERDICT_META[verdict] ?? VERDICT_META.IE;
        return (
          <span key={verdict} style={{ color: "var(--color-text-secondary)" }}>
            <b style={{ color: meta.color }}>{verdict}</b> on test {positions.join(", ")}
          </span>
        );
      })}
    </div>
  );
}
