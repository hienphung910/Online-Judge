import { useState } from "react";
import { api } from "../api";
import { Button, ErrorBox, MONO, Panel, Select } from "../components/ui";
import type { NewTestInput } from "../types";

const COMPARATORS = ["token", "exact", "float", "float:1e-6", "float:1e-9"];

let nextKey = 1;
interface TestRow extends NewTestInput {
  key: number;
}

function newTestRow(sample: boolean, name: string): TestRow {
  return { key: nextKey++, name, input: "", output: "", sample };
}

const LABEL = {
  ...MONO,
  fontSize: 9.5,
  letterSpacing: "0.1em",
  textTransform: "uppercase" as const,
  color: "var(--color-text-muted)",
  marginBottom: 4,
  display: "block",
};

const INPUT = {
  width: "100%",
  height: 32,
  padding: "0 10px",
  background: "var(--color-bg-base)",
  border: "1px solid var(--color-border)",
  borderRadius: 6,
  color: "var(--color-text-primary)",
  fontFamily: "var(--font-mono)",
  fontSize: 12.5,
  outline: "none",
};

const AREA = { ...INPUT, height: "auto", padding: "8px 10px", lineHeight: 1.6, resize: "vertical" as const };

/**
 * Trang "Thêm bài tập" - CHI hien khi tai khoan dang dang nhap co vai tro ADMIN.
 *
 * Luu y: an trang nay khong phai la bao mat. Backend van kiem tra vai tro o
 * POST /api/admin/problems, nen goi thang API bang curl cung khong qua duoc.
 */
export default function AdminProblems({ onCreated }: { onCreated: () => void }) {
  const [id, setId] = useState("");
  const [title, setTitle] = useState("");
  const [statement, setStatement] = useState("");
  const [timeLimitMs, setTimeLimitMs] = useState("1000");
  const [memoryLimitMb, setMemoryLimitMb] = useState("64");
  const [comparator, setComparator] = useState("token");
  const [totalPoints, setTotalPoints] = useState("100");
  const [tests, setTests] = useState<TestRow[]>([newTestRow(true, "sample01"), newTestRow(false, "01")]);

  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [busy, setBusy] = useState(false);

  function patchTest(key: number, patch: Partial<TestRow>) {
    setTests((rows) => rows.map((t) => (t.key === key ? { ...t, ...patch } : t)));
  }

  function removeTest(key: number) {
    setTests((rows) => rows.filter((t) => t.key !== key));
  }

  function resetForm() {
    setId("");
    setTitle("");
    setStatement("");
    setTimeLimitMs("1000");
    setMemoryLimitMb("64");
    setComparator("token");
    setTotalPoints("100");
    setTests([newTestRow(true, "sample01"), newTestRow(false, "01")]);
  }

  /** Kiem tra so bo ngay tren trinh duyet de bao loi nhanh; backend van kiem tra lai. */
  function validate(): string {
    const cleanId = id.trim().toUpperCase();
    if (!/^[A-Z0-9_-]{1,32}$/.test(cleanId)) {
      return "Mã bài chỉ gồm chữ in hoa, số, gạch dưới hoặc gạch ngang (tối đa 32 ký tự).";
    }
    if (!title.trim()) return "Tên bài không được để trống.";
    if (!statement.trim()) return "Nội dung đề không được để trống.";
    if (!(Number(timeLimitMs) >= 100 && Number(timeLimitMs) <= 60000)) {
      return "Giới hạn thời gian phải từ 100 đến 60000 ms.";
    }
    if (!(Number(memoryLimitMb) >= 8 && Number(memoryLimitMb) <= 2048)) {
      return "Giới hạn bộ nhớ phải từ 8 đến 2048 MB.";
    }
    if (!(Number(totalPoints) > 0)) return "Tổng điểm phải lớn hơn 0.";
    if (tests.length === 0) return "Bài tập phải có ít nhất một test.";

    const seen = new Set<string>();
    for (const t of tests) {
      const name = t.name.trim();
      if (!/^[A-Za-z0-9_-]{1,64}$/.test(name)) {
        return `Tên test "${name}" chỉ được gồm chữ, số, gạch dưới hoặc gạch ngang.`;
      }
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
    setSuccess("");
    const problem = validate();
    if (problem) {
      setError(problem);
      return;
    }
    setBusy(true);
    try {
      const res = await api.createProblem({
        id: id.trim().toUpperCase(),
        title: title.trim(),
        statement,
        timeLimitMs: Number(timeLimitMs),
        memoryLimitMb: Number(memoryLimitMb),
        comparator,
        totalPoints: Number(totalPoints),
        tests: tests.map((t) => ({
          name: t.name.trim(),
          input: t.input,
          output: t.output,
          sample: t.sample,
        })),
      });
      setSuccess(`${res.message} — ${res.problem.title} (${res.problem.maxPoints} điểm).`);
      resetForm();
      onCreated();          // bao App tai lai GET /api/problems de bai moi hien ngay
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div style={{ flex: 1, display: "flex", flexDirection: "column", padding: 16, gap: 14, overflow: "auto" }}>
      {/* flexShrink: 0 - neu khong, khung flex cha se ep panel cao lai va cat mat o nhap */}
      <Panel
        style={{ flexShrink: 0 }}
        title="Thêm bài tập mới"
        right={
          <span style={{ ...MONO, fontSize: 10.5, color: "var(--color-text-muted)" }}>
            chỉ tài khoản quản trị
          </span>
        }
      >
        {error && <ErrorBox message={error} />}
        {success && (
          <div
            style={{
              margin: 12, padding: "10px 14px", borderRadius: 6, fontSize: 12.5,
              background: "rgba(74,222,128,0.08)", border: "1px solid rgba(74,222,128,0.25)",
              color: "#4ade80", fontFamily: "var(--font-mono)",
            }}
          >
            {success}
          </div>
        )}

        <div style={{ padding: 14, display: "flex", flexDirection: "column", gap: 12 }}>
          <div style={{ display: "grid", gridTemplateColumns: "160px 1fr", gap: 10 }}>
            <div>
              <label style={LABEL}>Mã bài</label>
              <input
                value={id}
                onChange={(e) => setId(e.target.value.toUpperCase())}
                placeholder="P004"
                style={INPUT}
              />
            </div>
            <div>
              <label style={LABEL}>Tên bài</label>
              <input
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="Tổng hai số nguyên"
                style={INPUT}
              />
            </div>
          </div>

          <div>
            <label style={LABEL}>Nội dung đề (statement.txt)</label>
            <textarea
              value={statement}
              onChange={(e) => setStatement(e.target.value)}
              spellCheck={false}
              rows={7}
              placeholder={"Cho hai số nguyên a và b.\n\nInput : một dòng chứa hai số a và b.\nOutput: một số duy nhất là a + b."}
              style={AREA}
            />
          </div>

          <div style={{ display: "flex", gap: 10, flexWrap: "wrap", alignItems: "flex-end" }}>
            <div style={{ width: 150 }}>
              <label style={LABEL}>Thời gian (ms)</label>
              <input
                value={timeLimitMs}
                onChange={(e) => setTimeLimitMs(e.target.value)}
                inputMode="numeric"
                style={INPUT}
              />
            </div>
            <div style={{ width: 150 }}>
              <label style={LABEL}>Bộ nhớ (MB)</label>
              <input
                value={memoryLimitMb}
                onChange={(e) => setMemoryLimitMb(e.target.value)}
                inputMode="numeric"
                style={INPUT}
              />
            </div>
            <div style={{ width: 150 }}>
              <label style={LABEL}>Tổng điểm</label>
              <input
                value={totalPoints}
                onChange={(e) => setTotalPoints(e.target.value)}
                inputMode="numeric"
                style={INPUT}
              />
            </div>
            <div>
              <label style={LABEL}>Kiểu so sánh</label>
              <Select
                value={comparator}
                options={COMPARATORS}
                onChange={(v) => setComparator(v || "token")}
                placeholder="Chọn kiểu so sánh"
              />
            </div>
          </div>
        </div>
      </Panel>

      <Panel
        style={{ flexShrink: 0 }}
        title={`Bộ test (${tests.length})`}
        right={
          <div style={{ display: "flex", gap: 8 }}>
            <Button onClick={() => setTests((r) => [...r, newTestRow(true, `sample${r.length + 1}`)])}>
              + Test ví dụ
            </Button>
            <Button onClick={() => setTests((r) => [...r, newTestRow(false, String(r.length + 1).padStart(2, "0"))])}>
              + Test ẩn
            </Button>
          </div>
        }
      >
        <div style={{ padding: 14, display: "flex", flexDirection: "column", gap: 14 }}>
          <div style={{ ...MONO, fontSize: 11, color: "var(--color-text-muted)", lineHeight: 1.7 }}>
            Test ví dụ được hiển thị cho thí sinh (tên phải bắt đầu bằng <b>sample</b>). Test ẩn
            chỉ dùng để chấm và không bao giờ được gửi xuống trình duyệt của thí sinh.
          </div>

          {tests.map((t, index) => (
            <div
              key={t.key}
              style={{
                border: "1px solid var(--color-border)", borderRadius: 8,
                background: "var(--color-bg-raised)", padding: 12,
                display: "flex", flexDirection: "column", gap: 10,
              }}
            >
              <div style={{ display: "flex", gap: 10, alignItems: "center", flexWrap: "wrap" }}>
                <span style={{ ...MONO, fontSize: 11, color: "var(--color-text-muted)", minWidth: 46 }}>
                  #{index + 1}
                </span>
                <div style={{ width: 180 }}>
                  <input
                    value={t.name}
                    onChange={(e) => patchTest(t.key, { name: e.target.value })}
                    placeholder="tên file test"
                    style={INPUT}
                  />
                </div>
                <label
                  style={{
                    ...MONO, fontSize: 12, color: "var(--color-text-secondary)",
                    display: "flex", alignItems: "center", gap: 6, cursor: "pointer",
                  }}
                >
                  <input
                    type="checkbox"
                    checked={t.sample}
                    onChange={(e) => {
                      const sample = e.target.checked;
                      const name = t.name.trim();
                      const looksSample = name.toLowerCase().startsWith("sample");
                      // Doi ten cho khop quy uoc de nguoi dung khong phai sua tay.
                      const nextName = sample
                        ? (looksSample ? name : `sample_${name}`)
                        : (looksSample ? name.replace(/^sample_?/i, "") || `${index + 1}` : name);
                      patchTest(t.key, { sample, name: nextName });
                    }}
                  />
                  Test ví dụ
                </label>
                <div style={{ flex: 1 }} />
                <Button onClick={() => removeTest(t.key)} disabled={tests.length <= 1}>
                  Xoá
                </Button>
              </div>

              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
                <div>
                  <label style={LABEL}>Input</label>
                  <textarea
                    value={t.input}
                    onChange={(e) => patchTest(t.key, { input: e.target.value })}
                    spellCheck={false}
                    rows={4}
                    placeholder="1 2"
                    style={AREA}
                  />
                </div>
                <div>
                  <label style={LABEL}>Output mong đợi</label>
                  <textarea
                    value={t.output}
                    onChange={(e) => patchTest(t.key, { output: e.target.value })}
                    spellCheck={false}
                    rows={4}
                    placeholder="3"
                    style={AREA}
                  />
                </div>
              </div>
            </div>
          ))}

          <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
            <Button variant="primary" onClick={() => void doCreate()} disabled={busy}>
              {busy ? "Đang tạo..." : "Tạo bài tập"}
            </Button>
            <span style={{ ...MONO, fontSize: 11, color: "var(--color-text-muted)" }}>
              Điểm mỗi test = tổng điểm chia đều cho {tests.length} test.
            </span>
          </div>
        </div>
      </Panel>
    </div>
  );
}
