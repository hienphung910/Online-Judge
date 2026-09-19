import { useState } from "react";
import { MONO, Panel, StatCard, TD, TH } from "../components/ui";
import type { Problem } from "../types";

/**
 * Trang danh sach bai tap. Bam vao mot dong se chuyen sang trang "Nop bai"
 * cua bai do - noi de bai nam ngay canh khung code.
 */
export default function Problems({
  problems,
  onSubmitClick,
}: {
  problems: Problem[];
  onSubmitClick: (problemId: string) => void;
}) {
  const [hovered, setHovered] = useState<string>("");

  return (
    <div style={{ flex: 1, display: "flex", flexDirection: "column", padding: 16, gap: 14, overflow: "auto" }}>
      <div style={{ display: "flex", gap: 10, flexWrap: "wrap" }}>
        <StatCard label="Số bài" value={problems.length} />
      </div>

      <Panel
        title="Danh sách bài tập"
        right={
          <span style={{ ...MONO, fontSize: 10.5, color: "var(--color-text-muted)" }}>
            bấm vào một bài để xem đề và nộp
          </span>
        }
      >
        <div style={{ overflowX: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse", minWidth: 480 }}>
            <thead>
              <tr>
                <th style={TH}>Mã</th>
                <th style={TH}>Tên bài</th>
                <th style={TH}>Giới hạn</th>
                <th style={{ ...TH, textAlign: "right" }}>Điểm</th>
                <th style={TH} />
              </tr>
            </thead>
            <tbody>
              {problems.map((p) => (
                <tr
                  key={p.id}
                  onClick={() => onSubmitClick(p.id)}
                  onMouseEnter={() => setHovered(p.id)}
                  onMouseLeave={() => setHovered("")}
                  style={{
                    cursor: "pointer",
                    background: hovered === p.id ? "var(--color-bg-hover)" : "transparent",
                  }}
                >
                  <td style={{ ...TD, ...MONO, color: "var(--color-text-accent)" }}>{p.id}</td>
                  <td style={{ ...TD, color: "var(--color-text-primary)" }}>{p.title}</td>
                  <td style={{ ...TD, ...MONO, whiteSpace: "nowrap" }}>
                    {p.timeLimitMs} ms / {p.memoryLimitMb} MB
                  </td>
                  <td style={{ ...TD, ...MONO, textAlign: "right" }}>{p.maxPoints.toFixed(0)}</td>
                  <td style={{ ...TD, ...MONO, textAlign: "right", color: hovered === p.id ? "#50E3C2" : "var(--color-text-muted)", whiteSpace: "nowrap" }}>
                    Nộp bài →
                  </td>
                </tr>
              ))}
              {problems.length === 0 && (
                <tr>
                  <td style={{ ...TD, ...MONO, color: "var(--color-text-muted)" }} colSpan={5}>
                    Chưa nạp được bài tập nào từ máy chủ.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </Panel>
    </div>
  );
}
