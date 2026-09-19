import { useState } from "react";
import { useLocalContests, type Contest } from "../../localContests";
import type { Problem } from "../../types";

const INPUT_STYLE: React.CSSProperties = {
  height: 36, padding: "0 12px", background: "var(--color-bg-base)", border: "1px solid var(--color-border)",
  borderRadius: 7, color: "var(--color-text-primary)", fontSize: 13, fontFamily: "var(--font-sans)", outline: "none", width: "100%", boxSizing: "border-box",
};
const TEXTAREA_STYLE: React.CSSProperties = {
  ...INPUT_STYLE, height: "auto", padding: "10px 12px", resize: "vertical", lineHeight: 1.6,
};

function Field({ label, hint, children }: { label: string; hint?: string; children: React.ReactNode }) {
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
      <label style={{ fontFamily: "var(--font-mono)", fontSize: 10, fontWeight: 600, color: "var(--color-text-muted)", textTransform: "uppercase", letterSpacing: "0.09em" }}>{label}</label>
      {children}
      {hint && <span style={{ fontFamily: "var(--font-sans)", fontSize: 11, color: "var(--color-text-muted)" }}>{hint}</span>}
    </div>
  );
}

function toLocalDatetimeValue(iso: string): string {
  const d = new Date(iso);
  const pad = (n: number) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}T${pad(d.getHours())}:${pad(d.getMinutes())}`;
}

export default function ContestEditor({ contest, problems, onClose }: { contest?: Contest; problems: Problem[]; onClose: () => void }) {
  const { addContest, updateContest } = useLocalContests();
  const isEdit = !!contest;

  const [title, setTitle] = useState(contest?.title ?? "");
  const [description, setDescription] = useState(contest?.description ?? "");
  const [startTime, setStartTime] = useState(contest ? toLocalDatetimeValue(contest.startTime) : "");
  const [durationMins, setDurationMins] = useState(String(contest?.durationMins ?? 120));
  const [problemIds, setProblemIds] = useState<string[]>(contest?.problemIds ?? []);
  const [error, setError] = useState("");
  const [saved, setSaved] = useState(false);

  function toggleProblem(id: string) {
    setProblemIds((prev) => (prev.includes(id) ? prev.filter((x) => x !== id) : [...prev, id]));
  }

  function handleSubmit() {
    if (!title.trim()) return setError("Tên cuộc thi không được để trống.");
    if (!startTime) return setError("Chưa chọn thời gian bắt đầu.");
    const dur = Number(durationMins);
    if (!(dur > 0)) return setError("Thời lượng phải lớn hơn 0.");
    setError("");

    const payload = {
      title: title.trim(),
      description: description.trim(),
      startTime: new Date(startTime).toISOString(),
      durationMins: dur,
      problemIds,
    };
    if (isEdit) updateContest(contest!.id, payload);
    else addContest(payload);
    setSaved(true);
    setTimeout(onClose, 700);
  }

  return (
    <div style={{ position: "fixed", inset: 0, background: "rgba(28,20,16,0.5)", zIndex: 999, display: "flex", alignItems: "flex-start", justifyContent: "center", overflowY: "auto", padding: "32px 16px" }}>
      <div style={{ background: "var(--color-bg-panel)", border: "1px solid var(--color-border)", borderRadius: 14, width: "100%", maxWidth: 640, boxShadow: "0 24px 64px rgba(28,20,16,0.18)", marginBottom: 32 }}>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", padding: "20px 28px", borderBottom: "1px solid var(--color-border)" }}>
          <h2 style={{ fontFamily: "var(--font-serif)", fontSize: 20, fontWeight: 700, color: "var(--color-maroon)", margin: 0, letterSpacing: "-0.02em" }}>{isEdit ? "Edit Contest" : "New Contest"}</h2>
          <button onClick={onClose} style={{ background: "none", border: "none", cursor: "pointer", color: "var(--color-text-muted)", padding: 6, borderRadius: 5, display: "flex" }}>
            <svg width="15" height="15" viewBox="0 0 10 10" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"><line x1="1" y1="1" x2="9" y2="9" /><line x1="9" y1="1" x2="1" y2="9" /></svg>
          </button>
        </div>

        <div style={{ padding: "24px 28px", display: "flex", flexDirection: "column", gap: 18 }}>
          <div style={{ padding: "9px 12px", background: "var(--color-amber-bg)", border: "1px solid var(--color-amber-border)", borderRadius: 7, fontFamily: "var(--font-mono)", fontSize: 11, color: "var(--color-amber)", lineHeight: 1.6 }}>
            Demo: lưu trong trình duyệt, chưa đồng bộ lên máy chủ.
          </div>

          <Field label="Tên cuộc thi">
            <input style={INPUT_STYLE} value={title} onChange={(e) => setTitle(e.target.value)} placeholder="ICPC Practice Round" onFocus={(e) => (e.target.style.borderColor = "var(--color-maroon)")} onBlur={(e) => (e.target.style.borderColor = "var(--color-border)")} />
          </Field>

          <Field label="Mô tả">
            <textarea rows={3} style={TEXTAREA_STYLE} value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Mô tả ngắn về cuộc thi…" />
          </Field>

          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 14 }}>
            <Field label="Thời gian bắt đầu">
              <input type="datetime-local" style={{ ...INPUT_STYLE, fontFamily: "var(--font-mono)" }} value={startTime} onChange={(e) => setStartTime(e.target.value)} />
            </Field>
            <Field label="Thời lượng (phút)">
              <input inputMode="numeric" style={{ ...INPUT_STYLE, fontFamily: "var(--font-mono)" }} value={durationMins} onChange={(e) => setDurationMins(e.target.value)} />
            </Field>
          </div>

          <Field label={`Bài trong cuộc thi (${problemIds.length})`}>
            <div style={{ display: "flex", flexDirection: "column", gap: 4, maxHeight: 220, overflowY: "auto", border: "1px solid var(--color-border)", borderRadius: 7, padding: 6 }}>
              {problems.length === 0 && <span style={{ fontFamily: "var(--font-mono)", fontSize: 12, color: "var(--color-text-muted)", padding: 8 }}>Chưa có bài tập nào.</span>}
              {problems.map((p) => {
                const checked = problemIds.includes(p.id);
                return (
                  <label key={p.id} style={{ display: "flex", alignItems: "center", gap: 8, padding: "6px 8px", borderRadius: 6, cursor: "pointer", background: checked ? "var(--color-maroon-pale)" : "transparent" }}>
                    <input type="checkbox" checked={checked} onChange={() => toggleProblem(p.id)} />
                    <span style={{ fontFamily: "var(--font-mono)", fontSize: 11.5, color: "var(--color-text-muted)" }}>{p.id}</span>
                    <span style={{ fontFamily: "var(--font-sans)", fontSize: 13, color: "var(--color-text-primary)" }}>{p.title}</span>
                  </label>
                );
              })}
            </div>
          </Field>

          {error && <div style={{ fontFamily: "var(--font-sans)", fontSize: 12.5, color: "var(--color-red)" }}>{error}</div>}
        </div>

        <div style={{ display: "flex", alignItems: "center", justifyContent: "flex-end", gap: 10, padding: "16px 28px", borderTop: "1px solid var(--color-border)" }}>
          <button onClick={onClose} style={{ height: 36, padding: "0 20px", background: "none", border: "1px solid var(--color-border)", borderRadius: 7, color: "var(--color-text-muted)", fontSize: 13, cursor: "pointer", fontFamily: "var(--font-sans)" }}>Cancel</button>
          <button onClick={handleSubmit} style={{ height: 36, padding: "0 24px", background: saved ? "var(--color-green)" : "var(--color-maroon)", border: "none", borderRadius: 7, color: "#FAF7F2", fontSize: 13, fontWeight: 700, cursor: "pointer", fontFamily: "var(--font-sans)" }}>
            {saved ? "Saved!" : isEdit ? "Save changes" : "Create contest"}
          </button>
        </div>
      </div>
    </div>
  );
}
