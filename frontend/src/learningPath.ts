import type { Problem, Topic } from "./types";

/**
 * Tien ich cho lo trinh hoc. Thu tu hoc lay tu backend (data/topics.txt):
 * chu de dung truoc hoc truoc. Trong mot chu de: bai admin da xep (order > 0)
 * theo order, bai chua xep dung sau va theo ma bai - bo de K001..K300 duoc danh
 * ma dung theo thu tu tu de den kho. Luat nay trung voi Problem.ORDER_IN_TOPIC ben Java.
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

/** So sanh hai bai cung chu de: order truoc (0 = chua xep, dung sau), roi den ma bai. */
export function compareInTopic(a: Problem, b: Problem): number {
  const oa = a.order > 0 ? a.order : Number.MAX_SAFE_INTEGER;
  const ob = b.order > 0 ? b.order : Number.MAX_SAFE_INTEGER;
  // So sanh ma bai theo ma ky tu (khong dung localeCompare) de khop String.compareTo cua Java.
  return oa - ob || (a.id < b.id ? -1 : a.id > b.id ? 1 : 0);
}

/** Sap bai theo lo trinh: chu de theo thu tu hoc, trong chu de theo compareInTopic, bai khac xep cuoi. */
export function orderByPath(problems: Problem[], topics: Topic[]): Problem[] {
  const rank = new Map(topics.map((t) => [t.id, t.order]));
  const last = topics.length + 1;
  return [...problems].sort(
    (a, b) => (rank.get(a.topic) ?? last) - (rank.get(b.topic) ?? last) || compareInTopic(a, b),
  );
}
