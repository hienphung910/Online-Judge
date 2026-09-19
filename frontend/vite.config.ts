import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

// Cau hinh Vite cho giao dien PTIT Online Judge (theme "CodeForge").
// - npm run dev   : chay dev server, moi request /api duoc chuyen sang may chu
//                   Java o cong 8080 (nho vay khong can bat CORS).
// - npm run build : xuat file tinh vao frontend/dist, chinh la thu muc ma
//                   ApiServer.java phuc vu khi chay che do --serve.
export default defineConfig({
  plugins: [react(), tailwindcss()],
  build: {
    outDir: "dist",
    emptyOutDir: true,
    rollupOptions: {
      output: {
        // Tach phan LOI cua CodeMirror ra mot file rieng, cac bo phan tich cu
        // phap theo ngon ngu van tach theo import() dong trong CodeEditor.tsx.
        manualChunks: (id) => {
          const path = id.replace(/\\/g, "/");
          if (path.includes("node_modules/@codemirror/lang-")) return undefined;
          if (/node_modules\/@lezer\/(java|cpp|python|go|javascript|rust)\//.test(path)) {
            return undefined;
          }
          if (
            path.includes("node_modules/@codemirror/") ||
            path.includes("node_modules/@lezer/") ||
            path.includes("node_modules/codemirror/")
          ) {
            return "codemirror";
          }
          return undefined;
        },
      },
    },
  },
  server: {
    port: 5173,
    strictPort: false,
    proxy: {
      "/api": {
        target: "http://localhost:8080",
        changeOrigin: false,
      },
    },
  },
});
