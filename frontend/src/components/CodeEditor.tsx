import { useEffect, useRef } from "react";
import { Compartment, EditorState, type Extension } from "@codemirror/state";
import { EditorView, keymap, placeholder as cmPlaceholder } from "@codemirror/view";
import { indentWithTab } from "@codemirror/commands";
import { HighlightStyle, syntaxHighlighting } from "@codemirror/language";
import { basicSetup } from "codemirror";
import { tags as t } from "@lezer/highlight";

/**
 * O soan ma nguon.
 *
 * Truoc day cho la mot <textarea> tran: khong so dong, khong to mau cu phap, go
 * Tab thi nhay ra khoi o. Doi sang CodeMirror 6 vi day la khung chiem nua man hinh
 * luc demo va la thu lech xa nhat so voi mot trinh cham that.
 *
 * Bang mau khong lay theme co san nao ma dat lai theo dung bien CSS cua du an
 * (xem index.css) de o code khong bi lac long giua cac panel xung quanh.
 */

/**
 * Moi ngon ngu mot bo phan tich cu phap, nap theo kieu import() dong.
 *
 * Vi sao khong import thang o dau file: 6 bo phan tich cong lai nang gan 800 kB,
 * gop het vao bundle thi ngay ca man hinh dang nhap cung phai tai. Nap dong thi
 * Vite tach moi ngon ngu thanh mot file rieng va trinh duyet chi lay dung cai
 * dang duoc chon.
 *
 * Ten khoa khop voi ten trong LanguageRegistry ben Java.
 */
const LANGUAGE_MODES: Record<string, () => Promise<Extension>> = {
  Java: () => import("@codemirror/lang-java").then((m) => m.java()),
  "C++": () => import("@codemirror/lang-cpp").then((m) => m.cpp()),
  Python: () => import("@codemirror/lang-python").then((m) => m.python()),
  Go: () => import("@codemirror/lang-go").then((m) => m.go()),
  JavaScript: () => import("@codemirror/lang-javascript").then((m) => m.javascript()),
  Rust: () => import("@codemirror/lang-rust").then((m) => m.rust()),
};

/** Mau nen / con tro / vung chon - deu tro ve bien CSS chung de doi mau mot cho la xong. */
const editorTheme = EditorView.theme(
  {
    "&": {
      backgroundColor: "var(--color-bg-base)",
      color: "var(--color-text-primary)",
      fontSize: "12.5px",
      border: "1px solid var(--color-border)",
      borderRadius: "6px",
      overflow: "hidden",
    },
    "&.cm-focused": {
      outline: "none",
      borderColor: "var(--color-border-active)",
    },
    ".cm-content": {
      fontFamily: "var(--font-mono)",
      padding: "10px 0",
      caretColor: "var(--color-accent-cyan)",
    },
    ".cm-scroller": {
      fontFamily: "var(--font-mono)",
      lineHeight: "1.65",
      overflow: "auto",
    },
    ".cm-gutters": {
      backgroundColor: "transparent",
      color: "var(--color-text-muted)",
      border: "none",
      borderRight: "1px solid var(--color-border-subtle)",
      paddingRight: "4px",
    },
    ".cm-activeLineGutter": {
      backgroundColor: "transparent",
      color: "var(--color-text-secondary)",
    },
    ".cm-activeLine": { backgroundColor: "rgba(148, 163, 184, 0.05)" },
    ".cm-cursor, .cm-dropCursor": { borderLeftColor: "var(--color-accent-cyan)" },
    "&.cm-focused .cm-selectionBackground, .cm-selectionBackground, .cm-content ::selection": {
      backgroundColor: "rgba(80, 227, 194, 0.2)",
    },
    ".cm-matchingBracket, &.cm-focused .cm-matchingBracket": {
      backgroundColor: "rgba(80, 227, 194, 0.18)",
      outline: "none",
    },
    ".cm-placeholder": { color: "var(--color-text-muted)" },
    ".cm-tooltip": {
      backgroundColor: "var(--color-bg-raised)",
      border: "1px solid var(--color-border)",
      color: "var(--color-text-primary)",
    },
  },
  { dark: true },
);

/** Mau to cu phap - lay tu dung bo mau accent cua giao dien, khong che them mau la. */
const highlightStyle = HighlightStyle.define([
  { tag: [t.keyword, t.moduleKeyword, t.controlKeyword], color: "#22d3ee" },
  { tag: [t.string, t.special(t.string)], color: "#4ade80" },
  { tag: [t.number, t.bool, t.null], color: "#fbbf24" },
  { tag: [t.comment, t.lineComment, t.blockComment], color: "#4b6280", fontStyle: "italic" },
  { tag: [t.function(t.variableName), t.function(t.propertyName)], color: "#50e3c2" },
  { tag: [t.typeName, t.className, t.namespace], color: "#7dd3fc" },
  { tag: [t.definition(t.variableName), t.propertyName], color: "#e2e8f0" },
  { tag: [t.operator, t.punctuation, t.separator, t.bracket], color: "#94a3b8" },
  { tag: [t.meta, t.annotation], color: "#c4b5fd" },
  { tag: t.invalid, color: "#f87171" },
]);

export default function CodeEditor({
  value,
  language,
  onChange,
  placeholder = "Dán mã nguồn của bạn vào đây...",
  minHeight = 360,
  maxHeight,
  readOnly = false,
}: {
  value: string;
  language: string;
  /** Bo qua khi readOnly: noi dung khong doi duoc nen khong bao gio duoc goi. */
  onChange?: (value: string) => void;
  placeholder?: string;
  minHeight?: number;
  /** Co thi khung chi cao toi day, ben trong tu cuon - dung cho che do xem lai. */
  maxHeight?: number;
  /**
   * Che do CHI XEM: cung theme, cung to mau cu phap, cung nap dong bo ngon ngu,
   * nhung khong sua duoc. Trang Lich su nop dung de hien ma nguon da nop -
   * mot component cho ca hai viec, khong viet bo hien thi thu hai.
   */
  readOnly?: boolean;
}) {
  const host = useRef<HTMLDivElement | null>(null);
  const view = useRef<EditorView | null>(null);

  /** Chi cho phep thay MOT phan cau hinh (bo phan tich cu phap) mà khong dung lai editor. */
  const languageSlot = useRef(new Compartment());

  /**
   * Giu onChange trong ref: neu dua thang vao mang phu thuoc cua useEffect thi
   * moi lan component ve lai se dung ca editor len roi tao lai, mat vi tri con tro.
   */
  const onChangeRef = useRef(onChange);
  onChangeRef.current = onChange;

  // Tao editor DUNG MOT LAN. Doi ngon ngu khong dung lai editor nua (xem effect duoi).
  useEffect(() => {
    if (!host.current) return;

    const instance = new EditorView({
      state: EditorState.create({
        doc: value,
        extensions: [
          basicSetup,
          keymap.of([indentWithTab]), // Tab thut dong thay vi nhay ra khoi o
          editorTheme,
          syntaxHighlighting(highlightStyle),
          cmPlaceholder(placeholder),
          EditorView.lineWrapping,
          EditorView.theme({
            ".cm-scroller": {
              minHeight: `${minHeight}px`,
              ...(maxHeight !== undefined ? { maxHeight: `${maxHeight}px` } : {}),
            },
          }),
          // Che do xem: khoa noi dung va bo con tro / contenteditable; moi thu khac giu nguyen.
          ...(readOnly ? [EditorState.readOnly.of(true), EditorView.editable.of(false)] : []),
          languageSlot.current.of([]), // cho trong, nap sau khi biet ngon ngu
          EditorView.updateListener.of((update) => {
            if (update.docChanged) onChangeRef.current?.(update.state.doc.toString());
          }),
        ],
      }),
      parent: host.current,
    });
    view.current = instance;
    return () => {
      instance.destroy();
      view.current = null;
    };
    // Co y chi chay mot lan: value va language duoc dong bo o hai effect ben duoi.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Doi ngon ngu: nap bo phan tich cu phap roi thay dung phan do trong cau hinh.
  useEffect(() => {
    let cancelled = false;
    const load = LANGUAGE_MODES[language];
    if (!load) {
      view.current?.dispatch({ effects: languageSlot.current.reconfigure([]) });
      return;
    }
    load()
      .then((extension) => {
        // Nguoi dung co the doi ngon ngu lan nua (hoac roi trang) trong luc dang tai.
        if (cancelled || !view.current) return;
        view.current.dispatch({ effects: languageSlot.current.reconfigure(extension) });
      })
      .catch(() => {
        // Khong tai duoc thi cu de o code khong to mau - van go va nop binh thuong.
      });
    return () => {
      cancelled = true;
    };
  }, [language]);

  /**
   * Dong bo mot chieu tu ngoai vao (vi du bam "Chèn code mẫu").
   * Chi ghi de khi noi dung that su khac, neu khong moi lan go phim se tu dat lai
   * ca tai lieu va con tro nhay ve dau dong.
   */
  useEffect(() => {
    const instance = view.current;
    if (!instance) return;
    const current = instance.state.doc.toString();
    if (current === value) return;
    instance.dispatch({ changes: { from: 0, to: current.length, insert: value } });
  }, [value]);

  return <div ref={host} style={{ minWidth: 0 }} />;
}
