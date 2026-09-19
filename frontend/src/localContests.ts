import { useCallback, useEffect, useState } from "react";

/**
 * Backend Java hien khong co model/API cho "cuoc thi" (contest) - chi co bai
 * tap (problem) va bai nop (submission). Trang Contests/ContestEditor la tinh
 * nang DEMO, chi luu trong localStorage cua trinh duyet, KHONG dong bo len may
 * chu va KHONG chia se giua nhieu nguoi dung. Neu can contest thuc su, phai
 * them model + API o backend truoc.
 */

export type ContestStatus = "Active" | "Upcoming" | "Completed";

export interface Contest {
  id: string;
  title: string;
  description: string;
  startTime: string; // ISO
  durationMins: number;
  problemIds: string[];
}

const STORAGE_KEY = "oj.demoContests";

function readAll(): Contest[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? (JSON.parse(raw) as Contest[]) : [];
  } catch {
    return [];
  }
}

function writeAll(list: Contest[]) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
  } catch {
    // localStorage khong dung duoc (che do rieng tu...) - danh mat thay doi trong phien nay
  }
}

export function contestStatus(c: Contest): ContestStatus {
  const start = new Date(c.startTime).getTime();
  const end = start + c.durationMins * 60000;
  const now = Date.now();
  if (now < start) return "Upcoming";
  if (now > end) return "Completed";
  return "Active";
}

export function useLocalContests() {
  const [contests, setContests] = useState<Contest[]>(() => readAll());

  useEffect(() => { writeAll(contests); }, [contests]);

  const addContest = useCallback((c: Omit<Contest, "id">) => {
    setContests((prev) => [...prev, { ...c, id: `LOCAL-${Date.now()}` }]);
  }, []);
  const updateContest = useCallback((id: string, patch: Partial<Contest>) => {
    setContests((prev) => prev.map((c) => (c.id === id ? { ...c, ...patch } : c)));
  }, []);
  const deleteContest = useCallback((id: string) => {
    setContests((prev) => prev.filter((c) => c.id !== id));
  }, []);

  return { contests, addContest, updateContest, deleteContest };
}
