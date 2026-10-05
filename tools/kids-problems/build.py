"""
Sinh bo bai tap thieu nhi (K001..K300) vao data/problems/.

    py tools/kids-problems/build.py check            kiem tra tat ca chu de
    py tools/kids-problems/build.py check t03 t07    chi kiem tra vai file chu de
    py tools/kids-problems/build.py write            kiem tra roi ghi ra data/problems/
    py tools/kids-problems/build.py export <thu-muc> xuat loi giai mau thanh file .py rieng
                                                     (de nop thu qua trinh cham that)

Moi file topics/tNN_*.py khai bao TOPIC = "<ma chu de trong data/topics.txt>" va
dung 30 bai. Ma bai co dinh theo vi tri: chu de thu i (tinh tu 1 theo
data/topics.txt), bai thu j trong file -> K{(i-1)*30 + j}.
"""

import ast
import importlib.util
import shutil
import sys
import textwrap
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
TOPICS_TXT = ROOT / "data" / "topics.txt"
PROBLEMS_DIR = ROOT / "data" / "problems"

sys.path.insert(0, str(HERE))
import kidslib  # noqa: E402

PER_TOPIC = 30
ID_PREFIX = "K"
MARKER = "# Sinh tu dong boi tools/kids-problems/build.py"
TIME_LIMIT_MS = 1000
MEMORY_LIMIT_MB = 128
MAX_IO_CHARS = 20000


# ---------------------------------------------------------------- doc du lieu

def read_topic_order():
    order = []
    for line in TOPICS_TXT.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            order.append(line.split("|")[0].strip())
    return order


def load_topic_file(path):
    """Import mot file chu de, tra ve (TOPIC, danh sach Spec cua rieng file do)."""
    start = len(kidslib.PROBLEMS)
    name = "kids_" + path.stem
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return getattr(module, "TOPIC", None), kidslib.PROBLEMS[start:], path


def topic_files(selected):
    files = sorted((HERE / "topics").glob("t[0-9][0-9]_*.py"))
    if selected:
        files = [f for f in files if any(f.name.startswith(s) for s in selected)]
    return files


# ------------------------------------------------- xuat loi giai thanh file rieng

def standalone_source(fn):
    """Ma nguon chay doc lap cua ham loi giai (bo decorator, them phan doc/ghi stdin)."""
    src_path = Path(fn.__code__.co_filename)
    source = src_path.read_text(encoding="utf-8")
    first = fn.__code__.co_firstlineno
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.FunctionDef) and node.name == fn.__name__:
            starts = [node.lineno] + [d.lineno for d in node.decorator_list]
            if first in starts:
                lines = source.splitlines()[node.lineno - 1:node.end_lineno]
                body = textwrap.dedent("\n".join(lines))
                return ("import sys\n\n\n" + body + "\n\n\n"
                        "sys.stdout.write(" + fn.__name__ + "(sys.stdin.read()))\n")
    raise RuntimeError("Không tìm thấy mã nguồn của " + fn.__name__)


def run_standalone(source, fn_name, inp):
    """Chay loi giai trong mot namespace sach -> bat loi dung bien toan cuc cua file chu de."""
    code = source.replace("sys.stdout.write(" + fn_name + "(sys.stdin.read()))\n", "")
    namespace = {"__name__": "__kids_check__"}
    exec(compile(code, "<standalone>", "exec"), namespace)
    return namespace[fn_name](inp)


# ---------------------------------------------------------------- kiem tra

def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def build_problem(spec, errors):
    """Tinh output cho moi test va kiem tra; tra ve list (ten, input, output, sample)."""
    tag = f"[{spec.title}]"

    def err(msg):
        errors.append(f"{tag} {msg}")

    if not (3 <= len(spec.title) <= 60):
        err("tiêu đề phải dài 3-60 ký tự")
    if spec.difficulty not in kidslib.DIFFICULTY_NAMES:
        err("difficulty phải là 1, 2 hoặc 3")
    if spec.comparator not in kidslib.COMPARATORS:
        err(f"comparator phải là một trong {kidslib.COMPARATORS}")
    if "Đầu vào" not in spec.statement or "Đầu ra" not in spec.statement:
        err('đề phải có mục "Đầu vào:" và "Đầu ra:"')
    if len(spec.statement) > 3000:
        err("đề quá dài (> 3000 ký tự)")
    if spec.samples not in (1, 2):
        err("samples phải là 1 hoặc 2")

    try:
        inputs = spec.inputs()
    except Exception as e:  # noqa: BLE001
        err(f"sinh test lỗi: {e!r}")
        return []
    if len(inputs) < spec.samples + 4:
        err(f"cần ít nhất {spec.samples + 4} test (đang có {len(inputs)})")
    if len(inputs) > 15:
        err("tối đa 15 test")
    if len(set(inputs)) != len(inputs):
        err("có test bị trùng input")

    try:
        standalone = standalone_source(spec.solve)
    except Exception as e:  # noqa: BLE001
        err(str(e))
        return []

    tests, outputs = [], []
    for i, inp in enumerate(inputs):
        name = f"sample{i + 1:02d}" if i < spec.samples else f"{i - spec.samples + 1:02d}"
        if not inp.strip():
            err(f"test {name}: input rỗng")
        if not is_ascii(inp):
            err(f"test {name}: input có ký tự ngoài ASCII (không dùng chữ có dấu trong dữ liệu)")
        if len(inp) > MAX_IO_CHARS:
            err(f"test {name}: input quá dài")
        try:
            t0 = time.perf_counter()
            out = spec.solve(inp)
            elapsed = time.perf_counter() - t0
            again = spec.solve(inp)
            alone = run_standalone(standalone, spec.solve.__name__, inp)
        except Exception as e:  # noqa: BLE001
            err(f"test {name}: lời giải ném lỗi {e!r}")
            continue
        if not isinstance(out, str):
            err(f"test {name}: lời giải phải trả về str")
            continue
        if elapsed > 1.0:
            err(f"test {name}: lời giải chạy quá 1 giây")
        if again != out:
            err(f"test {name}: lời giải không ổn định (2 lần chạy ra 2 kết quả)")
        if alone != out:
            err(f"test {name}: lời giải không tự đủ (dùng biến ngoài hàm?)")
        if not out.endswith("\n"):
            out += "\n"
        if not out.strip():
            err(f"test {name}: output rỗng")
        if not is_ascii(out):
            err(f"test {name}: output có ký tự ngoài ASCII (in không dấu, ví dụ CHAN/LE, YES/NO)")
        if len(out) > MAX_IO_CHARS:
            err(f"test {name}: output quá dài")
        tests.append((name, inp, out, i < spec.samples))
        outputs.append(out)

    hidden = outputs[spec.samples:]
    if len(hidden) >= 2 and len(set(hidden)) == 1:
        err("mọi test ẩn có cùng một output - test chưa đủ đa dạng")
    return tests


def check(selected):
    order = read_topic_order()
    errors, warnings, topics = [], [], []
    titles = {}
    for path in topic_files(selected):
        topic, specs, _ = load_topic_file(path)
        where = path.name
        if topic not in order:
            errors.append(f"{where}: TOPIC = {topic!r} không có trong data/topics.txt")
            continue
        if len(specs) != PER_TOPIC:
            errors.append(f"{where}: cần đúng {PER_TOPIC} bài, đang có {len(specs)}")
        built = []
        last_diff = 0
        for spec in specs:
            if spec.title in titles:
                errors.append(f"{where}: tiêu đề \"{spec.title}\" trùng với bài trong {titles[spec.title]}")
            titles[spec.title] = where
            if spec.difficulty < last_diff:
                warnings.append(f"{where}: \"{spec.title}\" dễ hơn bài đứng trước (nên xếp từ dễ đến khó)")
            last_diff = max(last_diff, spec.difficulty)
            built.append((spec, build_problem(spec, errors)))
        topics.append((order.index(topic), topic, built))
        counts = {d: sum(1 for s in specs if s.difficulty == d) for d in (1, 2, 3)}
        print(f"{where:28s} {topic:12s} {len(specs):3d} bài  (dễ {counts[1]}, vừa {counts[2]}, khó {counts[3]})")
    return sorted(topics), errors, warnings


def report(errors, warnings):
    for w in warnings:
        print("CẢNH BÁO:", w)
    for e in errors:
        print("LỖI:", e)
    print(f"=> {len(errors)} lỗi, {len(warnings)} cảnh báo")
    return not errors


# ---------------------------------------------------------------- ghi ra dia

def escape_property(value):
    out = []
    for c in value:
        if c in "=:#!\\":
            out.append("\\" + c)
        elif c == "\n":
            out.append("\\n")
        elif c != "\r":
            out.append(c)
    return "".join(out)


def write_text(path, text):
    path.write_text(text, encoding="utf-8", newline="\n")


def problem_id(topic_index, j):
    return f"{ID_PREFIX}{topic_index * PER_TOPIC + j + 1:03d}"


def write(topics):
    # Chi xoa nhung thu muc do chinh cong cu nay sinh ra (co dong MARKER).
    removed = 0
    for d in PROBLEMS_DIR.glob(ID_PREFIX + "[0-9][0-9][0-9]"):
        props = d / "problem.properties"
        if props.is_file() and props.read_text(encoding="utf-8").startswith(MARKER):
            shutil.rmtree(d)
            removed += 1
    written = 0
    for topic_index, topic, built in topics:
        for j, (spec, tests) in enumerate(built):
            pid = problem_id(topic_index, j)
            d = PROBLEMS_DIR / pid
            if d.exists():
                raise SystemExit(f"{d} đã tồn tại và không do công cụ này sinh ra - dừng để tránh ghi đè")
            (d / "tests").mkdir(parents=True)
            write_text(d / "problem.properties", "\n".join([
                MARKER + " - sua file chu de roi chay lai, dung sua tay",
                f"id={pid}",
                f"title={escape_property(spec.title)}",
                f"topic={topic}",
                f"difficulty={spec.difficulty}",
                f"timeLimitMs={TIME_LIMIT_MS}",
                f"memoryLimitMb={MEMORY_LIMIT_MB}",
                f"comparator={spec.comparator}",
                "totalPoints=100",
                "",
            ]))
            write_text(d / "statement.txt", spec.statement)
            for name, inp, out, _ in tests:
                write_text(d / "tests" / f"{name}.in", inp)
                write_text(d / "tests" / f"{name}.out", out)
            written += 1
    print(f"Đã xoá {removed} bài cũ, ghi {written} bài vào {PROBLEMS_DIR}")


def export(topics, target):
    target.mkdir(parents=True, exist_ok=True)
    lines = []
    for topic_index, topic, built in topics:
        for j, (spec, _) in enumerate(built):
            pid = problem_id(topic_index, j)
            write_text(target / f"{pid}.py", standalone_source(spec.solve))
            lines.append(f"{pid}\t{topic}\t{spec.title}")
    write_text(target / "manifest.tsv", "\n".join(lines) + "\n")
    print(f"Đã xuất {len(lines)} lời giải mẫu vào {target}")


def main(argv):
    # Terminal Windows mac dinh cp1252 -> in tieng Viet se vo; ep ve UTF-8.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    if not argv or argv[0] not in ("check", "write", "export"):
        print(__doc__)
        return 2
    cmd = argv[0]
    selected = argv[1:] if cmd == "check" else []
    topics, errors, warnings = check(selected)
    if not report(errors, warnings):
        return 1
    if cmd == "write":
        if len(topics) != len(read_topic_order()):
            print("Chưa đủ file chủ đề cho mọi dòng trong data/topics.txt - không ghi.")
            return 1
        write(topics)
    elif cmd == "export":
        if len(argv) < 2:
            print("Thiếu thư mục đích: build.py export <thu-muc>")
            return 2
        export(topics, Path(argv[1]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
