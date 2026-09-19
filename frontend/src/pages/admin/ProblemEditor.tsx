import { useState } from "react";
import { api } from "../../api";
import { Select } from "../../components/ui";
import type { NewTestInput } from "../../types";

const COMPARATORS = ["token", "exact", "float", "float:1e-6", "float:1e-9"];

let nextKey = 1;
interface TestRow extends NewTestInput {
  key: number;
}
function newTestRow(sample: boolean, name: string): TestRow {
  return { key: nextKey++, name, input: "", output: "", sample };
}

const LABEL: React.CSSProperties = {
  fontFamily: "var(--font-mono)", fontSize: 10, fontWeight: 600, color: "var(--color-text-muted)",
  textTransform: "uppercase", letterSpacing: "0.09em", marginBottom: 4, display: "block",
};
const INPUT: React.CSSProperties = {
  width: "100%", height: 34, padding: "0 10px", background: "var(--color-bg-base)",
  border: "1px solid var(--color-border)", borderRadius: 7, color: "var(--color-text-primary)",
  fontFamily: "var(--font-mono)", fontSize: 12.5, outline: "none", boxSizing: "border-box",
};
const AREA: React.CSSProperties = { ...INPUT, height: "auto", padding: "8px 10px", lineHeight: 1.6, resize: "vertical" };

/**
 * Modal "Them bai tap moi". Backend chi ho tro TAO bai (POST /api/admin/problems),
 * khong co API sua/xoa - nen day la form tao moi, khong phai form sua.
 */
export default function ProblemEditor({ onClose, onCreated }: { onClose: () => void; onCreated: () => void }) {
  const [id, setId] = useState("");
  const [title, setTitle] = useState("");
  const [statement, setStatement] = useState("");
  const [timeLimitMs, setTimeLimitMs] = useState("1000");
  const [memoryLimitMb, setMemoryLimitMb] = useState("64");
  const [comparator, setComparator] = useState("token");
  const [totalPoints, setTotalPoints] = useState("100");
  const [tests, setTests] = useState<TestRow[]>([newTestRow(true, "sample01"), newTestRow(false, "01")]);
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  const [saved, setSaved] = useState(false);

  function patchTest(key: number, patch: Partial<TestRow>) {
    setTests((rows) => rows.map((t) => (t.key === key ? { ...t, ...patch } : t)));
  }
  function removeTest(key: number) {
    setTests((rows) => rows.filter((t) => t.key !== key));
  }

  function validate(): string {
    const cleanId = id.trim().toUpperCase();
    if (!/^[A-Z0-9_-]{1,32}$/.test(cleanId)) return "Mã bài chỉ gồm chữ in hoa, số, gạch dưới hoặc gạch ngang (tối đa 32 ký tự).";
    if (!title.trim()) return "Tên bài không được để trống.";
    if (!statement.trim()) return "Nội dung đề không được để trống.";
    if (!(Number(timeLimitMs) >= 100 && Number(timeLimitMs) <= 60000)) return "Giới hạn thời gian phải từ 100 đến 60000 ms.";
    if (!(Number(memoryLimitMb) >= 8 && Number(memoryLimitMb) <= 2048)) return "Giới hạn bộ nhớ phải từ 8 đến 2048 MB.";
    if (!(Number(totalPoints) > 0)) return "Tổng điểm phải lớn hơn 0.";
    if (tests.length === 0) return "Bài tập phải có ít nhất một test.";

    const seen = new Set<string>();
    for (const t of tests) {
      const name = t.name.trim();
      if (!/^[A-Za-z0-9_-]{1,64}$/.test(name)) return `Tên test "${name}" chỉ được gồm chữ, số, gạch dưới hoặc gạch ngang.`;
      if (seen.has(name.toLowerCase())) return `Tên test "${name}" bị trùng.`;
      seen.add(name.toLowerCase());
      const looksSample = name.toLowerCase().startsWith("sample");
      if (t.sample && !looksSample) return `Test ví dụ "${name}" phải có tên bắt đầu bằng "sample".`;
      if (!t.sample && looksSample) return `Test ẩn "${name}" không được đặt tên bắt đầu bằng "sample".`;
      if (!t.input.trim()) return `Test "${name}" chưa có input.`;
      if (!t.output.trim()) return `Test "${name}" chưa có output.`;
    }
    return "";
  }

  async function doCreate() {
    setError("");
    const problem = validate();
    if (problem) { setError(problem); return; }
    setBusy(true);
    try {
      await api.createProblem({
        id: id.trim().toUpperCase(),
        title: title.trim(),
        statement,
        timeLimitMs: Number(timeLimitMs),
        memoryLimitMb: Number(memoryLimitMb),
        comparator,
        totalPoints: Number(totalPoints),
        tests: tests.map((t) => ({ name: t.name.trim(), input: t.input, output: t.output, sample: t.sample })),
      });
      setSaved(true);
      onCreated();
      setTimeout(onClose, 700);
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div style={{ position: "fixed", inset: 0, background: "rgba(28,20,16,0.5)", zIndex: 999, display: "flex", alignItems: "flex-start", justifyContent: "center", overflowY: "auto", padding: "32px 16px" }}>
      <div style={{ background: "var(--color-bg-panel)", border: "1px solid var(--color-border)", borderRadius: 14, width: "100%", maxWidth: 760, boxShadow: "0 24px 64px rgba(28,20,16,0.18)", marginBottom: 32 }}>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", padding: "20px 28px", borderBottom: "1px solid var(--color-border)" }}>
          <h2 style={{ fontFamily: "var(--font-serif)", fontSize: 20, fontWeight: 700, color: "var(--color-maroon)", margin: 0, letterSpacing: "-0.02em" }}>New Problem</h2>
          <button onClick={onClose} style={{ background: "none", border: "none", cursor: "pointer", color: "var(--color-text-muted)", padding: 6, borderRadius: 5, display: "flex" }}>
            <svg width="15" height="15" viewBox="0 0 10 10" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"><line x1="1" y1="1" x2="9" y2="9" /><line x1="9" y1="1" x2="1" y2="9" /></svg>
          </button>
        </div>

        <div style={{ padding: "24px 28px", display: "flex", flexDirection: "column", gap: 14 }}>
          {error && (
            <div style={{ padding: "10px 14px", borderRadius: 7, fontSize: 12.5, background: "var(--color-red-bg)", border: "1px solid var(--color-red-border)", color: "var(--color-red)", fontFamily: "var(--font-mono)", whiteSpace: "pre-wrap" }}>{error}</div>
          )}
          {saved && (
            <div style={{ padding: "10px 14px", borderRadius: 7, fontSize: 12.5, background: "var(--color-green-bg)", border: "1px solid var(--color-green-border)", color: "var(--color-green)", fontFamily: "var(--font-mono)" }}>Đã tạo bài tập.</div>
          )}

          <div style={{ display: "grid", gridTemplateColumns: "160px 1fr", gap: 10 }}>
            <div>
              <label style={LABEL}>Mã bài</label>
              <input value={id} onChange={(e) => setId(e.target.value.toUpperCase())} placeholder="P004" style={INPUT} />
            </div>
            <div>
              <label style={LABEL}>Tên bài</label>
              <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Tổng hai số nguyên" style={{ ...INPUT, fontFamily: "var(--font-sans)" }} />
            </div>
          </div>

          <div>
            <label style={LABEL}>Nội dung đề (statement.txt)</label>
            <textarea value={statement} onChange={(e) => setStatement(e.target.value)} spellCheck={false} rows={6}
              placeholder={"Cho hai số nguyên a và b.\n\nInput : một dòng chứa hai số a và b.\nOutput: một số duy nhất là a + b."}
              style={AREA} />
          </div>

          <div style={{ display: "flex", gap: 10, flexWrap: "wrap", alignItems: "flex-end" }}>
            <div style={{ width: 150 }}>
              <label style={LABEL}>Thời gian (ms)</label>
              <input value={timeLimitMs} onChange={(e) => setTimeLimitMs(e.target.value)} inputMode="numeric" style={INPUT} />
            </div>
            <div style={{ width: 150 }}>
              <label style={LABEL}>Bộ nhớ (MB)</label>
              <input value={memoryLimitMb} onChange={(e) => setMemoryLimitMb(e.target.value)} inputMode="numeric" style={INPUT} />
            </div>
            <div style={{ width: 150 }}>
              <label style={LABEL}>Tổng điểm</label>
              <input value={totalPoints} onChange={(e) => setTotalPoints(e.target.value)} inputMode="numeric" style={INPUT} />
            </div>
            <div>
              <label style={LABEL}>Kiểu so sánh</label>
              <Select value={comparator} options={COMPARATORS} onChange={(v) => setComparator(v || "token")} placeholder="Chọn kiểu so sánh" />
            </div>
          </div>

          <div style={{ borderTop: "1px solid var(--color-border)", paddingTop: 14, display: "flex", flexDirection: "column", gap: 12 }}>
            <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
              <span style={LABEL as React.CSSProperties}>Bộ test ({tests.length})</span>
              <div style={{ display: "flex", gap: 8 }}>
                <button onClick={() => setTests((r) => [...r, newTestRow(true, `sample${r.length + 1}`)])} style={ADD_BTN}>+ Test ví dụ</button>
                <button onClick={() => setTests((r) => [...r, newTestRow(false, String(r.length + 1).padStart(2, "0"))])} style={ADD_BTN}>+ Test ẩn</button>
              </div>
            </div>

            <div style={{ fontFamily: "var(--font-mono)", fontSize: 11, color: "var(--color-text-muted)", lineHeight: 1.7 }}>
              Test ví dụ hiển thị cho thí sinh (tên phải bắt đầu bằng <b>sample</b>). Test ẩn chỉ dùng để chấm.
            </div>

            {tests.map((t, index) => (
              <div key={t.key} style={{ border: "1px solid var(--color-border)", borderRadius: 8, background: "var(--color-bg-raised)", padding: 12, display: "flex", flexDirection: "column", gap: 10 }}>
                <div style={{ display: "flex", gap: 10, alignItems: "center", flexWrap: "wrap" }}>
                  <span style={{ fontFamily: "var(--font-mono)", fontSize: 11, color: "var(--color-text-muted)", minWidth: 30 }}>#{index + 1}</span>
                  <div style={{ width: 180 }}>
                    <input value={t.name} onChange={(e) => patchTest(t.key, { name: e.target.value })} placeholder="tên file test" style={INPUT} />
                  </div>
                  <label style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-secondary)", display: "flex", alignItems: "center", gap: 6, cursor: "pointer" }}>
                    <input type="checkbox" checked={t.sample} onChange={(e) => {
                      const sample = e.target.checked;
                      const name = t.name.trim();
                      const looksSample = name.toLowerCase().startsWith("sample");
                      const nextName = sample
                        ? (looksSample ? name : `sample_${name}`)
                        : (looksSample ? name.replace(/^sample_?/i, "") || `${index + 1}` : name);
                      patchTest(t.key, { sample, name: nextName });
                    }} />
                    Test ví dụ
                  </label>
                  <div style={{ flex: 1 }} />
                  <button onClick={() => removeTest(t.key)} disabled={tests.length <= 1} style={{ ...ADD_BTN, opacity: tests.length <= 1 ? 0.5 : 1, cursor: tests.length <= 1 ? "not-allowed" : "pointer" }}>Xoá</button>
                </div>
                <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
                  <div>
                    <label style={LABEL}>Input</label>
                    <textarea value={t.input} onChange={(e) => patchTest(t.key, { input: e.target.value })} spellCheck={false} rows={3} placeholder="1 2" style={AREA} />
                  </div>
                  <div>
                    <label style={LABEL}>Output mong đợi</label>
                    <textarea value={t.output} onChange={(e) => patchTest(t.key, { output: e.target.value })} spellCheck={false} rows={3} placeholder="3" style={AREA} />
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div style={{ display: "flex", alignItems: "center", justifyContent: "flex-end", gap: 10, padding: "16px 28px", borderTop: "1px solid var(--color-border)" }}>
          <button onClick={onClose} style={{ height: 36, padding: "0 20px", background: "none", border: "1px solid var(--color-border)", borderRadius: 7, color: "var(--color-text-muted)", fontSize: 13, cursor: "pointer", fontFamily: "var(--font-sans)" }}>Cancel</button>
          <button onClick={() => void doCreate()} disabled={busy} style={{ height: 36, padding: "0 24px", background: saved ? "var(--color-green)" : "var(--color-maroon)", border: "none", borderRadius: 7, color: "#FAF7F2", fontSize: 13, fontWeight: 700, cursor: busy ? "not-allowed" : "pointer", opacity: busy ? 0.7 : 1, fontFamily: "var(--font-sans)" }}>
            {busy ? "Đang tạo..." : saved ? "Saved!" : "Create problem"}
          </button>
        </div>
      </div>
    </div>
  );
}

const ADD_BTN: React.CSSProperties = {
  display: "flex", alignItems: "center", gap: 5, height: 28, padding: "0 11px", background: "none",
  border: "1px solid var(--color-border)", borderRadius: 6, color: "var(--color-text-muted)", fontSize: 11.5,
  cursor: "pointer", fontFamily: "var(--font-sans)",
};
