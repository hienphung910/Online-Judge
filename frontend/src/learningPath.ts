import type { Problem, Topic } from "./types";

/**
 * Tien ich cho lo trinh hoc. Thu tu hoc lay tu backend (data/topics.txt):
 * chu de dung truoc hoc truoc, trong mot chu de thi theo ma bai - bo de K001..K300
 * duoc danh ma dung theo thu tu tu de den kho.
 */

export const DIFFICULTY_META: Record<number, { label: string; color: string; bg: string }> = {
  1: { label: "Dễ", color: "#2E7D32", bg: "#E8F5E9" },
  2: { label: "Vừa", color: "#E65100", bg: "#FFF3E0" },
  3: { label: "Khó", color: "#C62828", bg: "#FFEBEE" },
};

/** Nhom cho bai chua gan chu de, hoac gan chu de khong con trong lo trinh. */
export const OTHER_TOPIC = "__other__";

export function topicKey(p: Problem, known: Set<string>): string {
  return known.has(p.topic) ? p.topic : OTHER_TOPIC;
}

/** Sap bai theo lo trinh: chu de theo thu tu hoc, trong chu de theo ma bai, bai khac xep cuoi. */
export function orderByPath(problems: Problem[], topics: Topic[]): Problem[] {
  const rank = new Map(topics.map((t) => [t.id, t.order]));
  const last = topics.length + 1;
  return [...problems].sort(
    (a, b) => (rank.get(a.topic) ?? last) - (rank.get(b.topic) ?? last) || a.id.localeCompare(b.id),
  );
}
