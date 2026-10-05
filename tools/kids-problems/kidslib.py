"""
Thu vien nho de soan bo bai tap thieu nhi.

Moi bai duoc khai bao bang decorator @problem dat ngay tren ham loi giai mau:

    @problem(
        title="Chao ban moi",
        difficulty=1,
        statement=\"\"\"
            Cau chuyen ngan...

            Đầu vào:
            - ...

            Đầu ra:
            - ...
        \"\"\",
        tests=["An\\n", "Binh\\n", ...],      # hoac: tests=lambda r: [...]
    )
    def solve(inp):
        name = inp.split()[0]
        return f"Xin chao, {name}!\\n"

Dap an cua MOI test duoc tinh bang chinh ham loi giai, nen khong bao gio go tay
output. Ham loi giai phai TU DU (chi import thu vien chuan ben trong than ham)
vi build.py con xuat no ra thanh bai nop Python de chay qua trinh cham that.
"""

import random
import textwrap
import zlib

#: Moi bai da khai bao, theo dung thu tu xuat hien trong file chu de.
PROBLEMS = []

COMPARATORS = ("token", "lines")
DIFFICULTY_NAMES = {1: "Dễ", 2: "Vừa", 3: "Khó"}


class Spec:
    """Mot bai tap: thong tin de + loi giai mau + cach sinh test."""

    def __init__(self, title, difficulty, statement, tests, comparator, samples, solve):
        self.title = title
        self.difficulty = difficulty
        self.statement = reflow(textwrap.dedent(statement).strip()) + "\n"
        self.tests_source = tests
        self.comparator = comparator
        self.samples = samples
        self.solve = solve
        self.module = solve.__module__

    def seed(self):
        # crc32 thay vi hash(): hash() cua Python doi gia tri moi lan chay.
        return zlib.crc32(self.title.encode("utf-8"))

    def inputs(self):
        """Danh sach input (chuoi), test dau tien la test vi du."""
        src = self.tests_source
        raw = src(random.Random(self.seed())) if callable(src) else list(src)
        fixed = []
        for t in raw:
            t = str(t).replace("\r\n", "\n")
            fixed.append(t if t.endswith("\n") else t + "\n")
        return fixed


def reflow(text):
    """
    Noi cac dong bi ngat giua cau (do viet trong ma nguon cho gon) thanh mot dong:
    trang de hien statement voi white-space: pre-wrap nen moi dau xuong dong deu
    duoc giu. Chi noi khi dong truoc la cau van dai (>= 40 ky tu, khong ket thuc
    bang ':') va dong sau bat dau bang chu cai - dong trong, gach dau dong, tieu de
    muc va hinh ve ngan (dong ngan, bat dau bang dau cach / * / #) giu nguyen.
    """
    out = []
    for line in text.split("\n"):
        prev = out[-1] if out else ""
        body = line.lstrip()
        indent = len(line) - len(body)
        continues = (
            len(prev.strip()) >= 40
            and not prev.rstrip().endswith(":")
            and (body[:1].isalpha() or body[:1] == "(")
            and (indent == 0 or (prev.lstrip().startswith("- ") and indent <= 4))
        )
        if continues:
            out[-1] = prev.rstrip() + " " + body
        else:
            out.append(line.rstrip())
    return "\n".join(out)


def problem(title, difficulty, statement, tests, comparator="token", samples=1):
    """Dang ky mot bai tap. Xem docstring cua module de biet cach dung."""

    def deco(fn):
        PROBLEMS.append(Spec(title, difficulty, statement, tests, comparator, samples, fn))
        return fn

    return deco
