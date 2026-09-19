import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from "react";
import { api, getToken, setToken, setUnauthorizedHandler } from "./api";
import type { AuthUser, RegisterRequest } from "./types";

interface AuthCtx {
  user: AuthUser | null;
  /** true trong luc dang hoi may chu xem token cu con hieu luc khong. */
  checking: boolean;
  login: (username: string, password: string) => Promise<void>;
  register: (body: RegisterRequest) => Promise<void>;
  logout: () => void;
  /** Goi lai sau khi nop bai de cap nhat solvedCount hien tren avatar. */
  refresh: () => Promise<void>;
}

const Ctx = createContext<AuthCtx>({
  user: null,
  checking: true,
  login: async () => {},
  register: async () => {},
  logout: () => {},
  refresh: async () => {},
});

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<AuthUser | null>(null);
  const [checking, setChecking] = useState(true);

  useEffect(() => {
    setUnauthorizedHandler(() => setUser(null));
    return () => setUnauthorizedHandler(null);
  }, []);

  useEffect(() => {
    let alive = true;
    if (!getToken()) {
      setChecking(false);
      return;
    }
    api.me()
      .then((u) => alive && setUser(u))
      .catch(() => alive && setToken(null))
      .finally(() => alive && setChecking(false));
    return () => { alive = false; };
  }, []);

  const login = useCallback(async (username: string, password: string) => {
    const res = await api.login(username, password);
    setToken(res.token);
    setUser(res.user);
  }, []);

  const register = useCallback(async (body: RegisterRequest) => {
    await api.register(body);
  }, []);

  const logout = useCallback(() => {
    api.logout().catch(() => undefined);
    setToken(null);
    setUser(null);
  }, []);

  const refresh = useCallback(async () => {
    try {
      setUser(await api.me());
    } catch {
      // token co the da het han - unauthorized handler se tu dang xuat
    }
  }, []);

  return <Ctx.Provider value={{ user, checking, login, register, logout, refresh }}>{children}</Ctx.Provider>;
}

export function useAuth() {
  return useContext(Ctx);
}
