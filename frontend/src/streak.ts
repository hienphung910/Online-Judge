import { useCallback, useEffect, useRef, useState } from "react";
import { api } from "./api";
import type { Submission } from "./types";

/**
 * Chuoi ngay luyen tap (streak) - tinh hoan toan o frontend tu lich su nop bai.
 *
 * Mot ngay duoc tinh la "co luyen tap" khi nguoi dung nop it nhat 1 bai trong
 * ngay do, bat ke verdict: nop sai roi sua cung la dang hoc. Chuoi hien tai van
 * con neu hom qua co nop ma hom nay chua - chi dut khi bo trong tron mot ngay.
 *
 * Khoa ngay lay thang 10 ky tu dau cua submittedAt ("yyyy-MM-ddTHH:mm:ss" theo
 * gio may chu). May chu chi lang nghe 127.0.0.1 nen gio may chu = gio trinh duyet.
 */

/** Cac moc de khoe va de nhac "con bao nhieu ngay nua". */
export const MILESTONES = [3, 7, 14, 30, 50, 100, 200, 365];

export interface StreakInfo {
  /** So ngay lien tiep tinh den hom nay (hoac hom qua neu hom nay chua nop). */
  current: number;
  /** Chuoi dai nhat tung dat. */
  longest: number;
  /** Hom nay da nop bai chua. */
  activeToday: boolean;
  /** Tong so ngay co nop bai. */
  activeDays: number;
  /** So bai nop theo tung ngay, khoa "yyyy-MM-dd". */
  perDay: Map<string, number>;
  /** Ngay hom nay theo gio may, "yyyy-MM-dd". */
  today: string;
}

const DAY_MS = 24 * 60 * 60 * 1000;

/** Ngay theo gio dia phuong cua trinh duyet, dang "yyyy-MM-dd". */
export function localDayKey(d: Date): string {
  const m = String(d.getMonth() + 1).padStart(2, "0");
  const day = String(d.getDate()).padStart(2, "0");
  return `${d.getFullYear()}-${m}-${day}`;
}

/**
 * Cong/tru ngay tren khoa "yyyy-MM-dd". Tinh bang UTC de khong bao gio bi lech
 * mot ngay vi gio mua he.
 */
export function shiftDay(key: string, days: number): string {
  const [y, m, d] = key.split("-").map(Number);
  return new Date(Date.UTC(y, m - 1, d) + days * DAY_MS).toISOString().slice(0, 10);
}

export function computeStreak(subs: Submission[], now: Date = new Date()): StreakInfo {
  const perDay = new Map<string, number>();
  for (const s of subs) {
    const key = s.submittedAt.slice(0, 10);
    perDay.set(key, (perDay.get(key) ?? 0) + 1);
  }

  const today = localDayKey(now);
  const activeToday = perDay.has(today);

  // Chuoi hien tai: dem lui tu hom nay, hoac tu hom qua neu hom nay chua nop.
  let current = 0;
  let cursor = activeToday ? today : shiftDay(today, -1);
  while (perDay.has(cursor)) {
    current++;
    cursor = shiftDay(cursor, -1);
  }

  // Chuoi dai nhat: quet cac ngay da sap xep, noi doan khi hai ngay sat nhau.
  let longest = 0;
  let run = 0;
  let prev: string | null = null;
  for (const key of [...perDay.keys()].sort()) {
    run = prev !== null && shiftDay(prev, 1) === key ? run + 1 : 1;
    longest = Math.max(longest, run);
    prev = key;
  }

  return { current, longest, activeToday, activeDays: perDay.size, perDay, today };
}

/** Moc ke tiep lon hon chuoi hien tai, hoac null neu da vuot het. */
export function nextMilestone(current: number): number | null {
  return MILESTONES.find((m) => m > current) ?? null;
}

/**
 * Tai lich su nop bai cua chinh nguoi dung va tinh streak.
 * Goi lai moi khi reloadKey doi (tuc la vua nop bai xong).
 *
 * `increasedTo` co gia tri khi chuoi vua tang len trong phien nay - dung de hien
 * loi chuc mung, khong bat len o lan tai dau tien.
 */
export function useStreak(username: string | null, reloadKey: number) {
  const [info, setInfo] = useState<StreakInfo | null>(null);
  const [increasedTo, setIncreasedTo] = useState<number | null>(null);
  // Nho kem username de doi tai khoan khong bi tinh nham la "chuoi vua tang".
  const last = useRef<{ username: string; current: number } | null>(null);

  useEffect(() => {
    if (!username) {
      setInfo(null);
      setIncreasedTo(null);
      last.current = null;
      return;
    }
    let alive = true;
    api.submissions()
      .then((subs) => {
        if (!alive) return;
        // Admin nhan ve bai nop cua moi nguoi, nen luon loc lai theo chinh minh.
        const next = computeStreak(subs.filter((s) => s.author === username));
        const prev = last.current;
        if (prev && prev.username === username && next.current > prev.current) {
          setIncreasedTo(next.current);
        }
        last.current = { username, current: next.current };
        setInfo(next);
      })
      .catch(() => undefined);
    return () => { alive = false; };
  }, [username, reloadKey]);

  // Giu nguyen tham chieu de bo dem tu tat cua StreakToast khong bi dat lai moi lan render.
  const dismissIncrease = useCallback(() => setIncreasedTo(null), []);
  return { info, increasedTo, dismissIncrease };
}
