"""Chu de 10: Thu thach tong hop (K271-K300).

Bang hai chieu, mo phong, quy hoach dong don gian va loang (BFS) cho bai kho.
Cac ham _xxx o dau file CHI dung de sinh test; ham loi giai luon tu du.
"""

from kidslib import problem

TOPIC = "thu-thach"


# ------------------------------------------------------------ sinh test

def _fmt(a):
    return "\n".join(" ".join(str(v) for v in row) for row in a)


def _rand(r, n, m, lo, hi):
    return [[r.randint(lo, hi) for _ in range(m)] for _ in range(n)]


def _mat(r, n, m, lo, hi):
    return f"{n} {m}\n{_fmt(_rand(r, n, m, lo, hi))}\n"


def _const(n, m, v):
    return f"{n} {m}\n{_fmt([[v] * m for _ in range(n)])}\n"


def _square(a):
    return f"{len(a)}\n{_fmt(a)}\n"


def _grid_rows(r, n, m, p, on="#", off="."):
    return ["".join(on if r.random() < p else off for _ in range(m)) for _ in range(n)]


def _grid(r, n, m, p, on="#", off="."):
    return f"{n} {m}\n" + "\n".join(_grid_rows(r, n, m, p, on, off)) + "\n"


def _chars(n, m, rows):
    return f"{n} {m}\n" + "\n".join(rows) + "\n"


# ================================================================ DỄ (10)

@problem(
    title="Khay kẹo nhiều ngăn của mẹ",
    difficulty=1,
    statement="""
        Mẹ có một khay đựng kẹo chia thành n hàng và m cột ô nhỏ, mỗi ô có một số viên kẹo.
        Em hãy đếm giúp mẹ xem cả khay có tất cả bao nhiêu viên kẹo nhé!

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m: số hàng và số cột của khay.
        - n dòng tiếp theo, mỗi dòng chứa m số nguyên cách nhau một dấu cách: số viên kẹo trong từng ô của hàng đó.

        Đầu ra:
        - Một số nguyên duy nhất: tổng số viên kẹo trong cả khay.

        Giới hạn:
        - 1 ≤ n, m ≤ 50.
        - Mỗi ô có từ 0 đến 1000 viên kẹo.

        Gợi ý:
        - Dùng hai vòng lặp lồng nhau: vòng ngoài đi qua từng hàng, vòng trong đi qua từng ô của hàng đó.
    """,
    tests=lambda r: [
        "2 3\n1 2 3\n4 5 6\n",
        "1 1\n0\n",
        "1 1\n1000\n",
        _const(3, 4, 0),
        _const(50, 50, 1000),
        _mat(r, 1, 10, 0, 1000),
        _mat(r, 10, 1, 0, 1000),
        _mat(r, 7, 9, 0, 100),
        _mat(r, 30, 40, 0, 1000),
    ],
)
def tong_keo_trong_khay(inp):
    data = inp.split()
    n, m = int(data[0]), int(data[1])
    total = 0
    for k in range(n * m):
        total += int(data[2 + k])
    return f"{total}\n"


@problem(
    title="Vườn táo nhiều hàng của ông nội",
    difficulty=1,
    statement="""
        Ông nội trồng táo thành n hàng, mỗi hàng có m cây. Ông đã đếm số quả trên từng cây
        và muốn biết mỗi hàng cây cho tất cả bao nhiêu quả. Em giúp ông tính nhé!

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m: số hàng cây và số cây trên mỗi hàng.
        - n dòng tiếp theo, dòng thứ i chứa m số nguyên cách nhau một dấu cách: số quả trên từng cây của hàng thứ i.

        Đầu ra:
        - In ra n dòng, dòng thứ i là tổng số quả của hàng cây thứ i.

        Giới hạn:
        - 1 ≤ n, m ≤ 50.
        - Mỗi cây có từ 0 đến 100 quả.
    """,
    tests=lambda r: [
        "3 4\n1 2 3 4\n10 0 5 5\n7 7 7 7\n",
        "1 1\n0\n",
        "1 5\n100 100 100 100 100\n",
        "5 1\n3\n0\n8\n100\n1\n",
        _const(4, 4, 0),
        _mat(r, 6, 8, 0, 100),
        _mat(r, 50, 50, 0, 100),
        _mat(r, 20, 3, 0, 20),
    ],
)
def tong_tung_hang_tao(inp):
    data = inp.split()
    n, m = int(data[0]), int(data[1])
    out = []
    pos = 2
    for _ in range(n):
        s = 0
        for _ in range(m):
            s += int(data[pos])
            pos += 1
        out.append(str(s))
    return "\n".join(out) + "\n"


@problem(
    title="Bông hoa điểm tốt theo từng ngày",
    difficulty=1,
    statement="""
        Lớp của cô Mai có n bạn. Trong m ngày, cô ghi lại số bông hoa điểm tốt mỗi bạn nhận được vào một bảng:
        hàng thứ i là của bạn thứ i, cột thứ j là của ngày thứ j.
        Em hãy tính xem cả lớp nhận được bao nhiêu bông hoa trong từng ngày.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m: số bạn trong lớp và số ngày.
        - n dòng tiếp theo, mỗi dòng chứa m số nguyên cách nhau một dấu cách.

        Đầu ra:
        - In ra trên một dòng m số nguyên cách nhau một dấu cách: số thứ j là tổng các số ở cột thứ j (tổng số hoa của cả lớp trong ngày thứ j).

        Giới hạn:
        - 1 ≤ n, m ≤ 50.
        - Mỗi số trong bảng từ 0 đến 10.
    """,
    tests=lambda r: [
        "3 4\n1 0 2 3\n2 2 0 1\n0 1 1 4\n",
        "1 1\n7\n",
        "1 6\n1 2 3 4 5 6\n",
        "6 1\n1\n2\n3\n4\n5\n6\n",
        _const(5, 5, 0),
        _const(50, 50, 10),
        _mat(r, 8, 7, 0, 10),
        _mat(r, 40, 30, 0, 10),
    ],
)
def tong_tung_cot_hoa(inp):
    data = inp.split()
    n, m = int(data[0]), int(data[1])
    col = [0] * m
    for i in range(n):
        for j in range(m):
            col[j] += int(data[2 + i * m + j])
    return " ".join(str(v) for v in col) + "\n"


@problem(
    title="Thỏ Bông đếm bụi cỏ non",
    difficulty=1,
    statement="""
        Khu vườn của Thỏ Bông hình chữ nhật, được chia thành n hàng và m cột ô vuông.
        Ô có bụi cỏ non được ký hiệu '#', ô đất trống được ký hiệu '.'.
        Thỏ Bông muốn biết trong vườn có bao nhiêu bụi cỏ để ăn dần mỗi ngày.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo, mỗi dòng gồm đúng m ký tự '#' hoặc '.' viết liền nhau (không có dấu cách).

        Đầu ra:
        - Một số nguyên: số ô có bụi cỏ (số ký tự '#').

        Giới hạn:
        - 1 ≤ n, m ≤ 50.
    """,
    tests=lambda r: [
        "3 4\n#..#\n.##.\n...#\n",
        "1 1\n.\n",
        "1 1\n#\n",
        _chars(4, 6, ["." * 6] * 4),
        _chars(50, 50, ["#" * 50] * 50),
        _grid(r, 1, 50, 0.5),
        _grid(r, 50, 1, 0.3),
        _grid(r, 20, 30, 0.3),
        _grid(r, 45, 50, 0.7),
    ],
)
def dem_bui_co(inp):
    data = inp.split()
    n = int(data[0])
    total = 0
    for row in data[2:2 + n]:
        total += row.count("#")
    return f"{total}\n"


def _tests_vo_so(r):
    def two(n, m, lo, hi):
        return f"{n} {m}\n{_fmt(_rand(r, n, m, lo, hi))}\n{_fmt(_rand(r, n, m, lo, hi))}\n"

    return [
        "2 3\n1 2 3\n0 5 1\n4 0 2\n3 3 3\n",
        "1 1\n0\n0\n",
        "1 1\n500\n500\n",
        "2 2\n0 0\n0 0\n1 2\n3 4\n",
        two(1, 8, 0, 500),
        two(8, 1, 0, 500),
        two(5, 6, 0, 20),
        two(30, 30, 0, 500),
    ]


@problem(
    title="Hai bạn nhặt vỏ sò trên bãi biển",
    difficulty=1,
    statement="""
        Bãi biển được chia thành n hàng và m cột ô. An và Bình mỗi bạn ghi lại số vỏ sò mình nhặt được ở từng ô
        vào một bảng riêng. Em hãy lập bảng tổng: mỗi ô của bảng tổng là số vỏ sò cả hai bạn nhặt được ở ô đó.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo là bảng của An, mỗi dòng m số nguyên cách nhau một dấu cách.
        - n dòng tiếp theo nữa là bảng của Bình, viết theo cùng cách.

        Đầu ra:
        - In ra n dòng, mỗi dòng m số nguyên cách nhau một dấu cách: số ở hàng i, cột j bằng số của An cộng số của Bình ở cùng hàng i, cột j.

        Giới hạn:
        - 1 ≤ n, m ≤ 30.
        - Mỗi số trong hai bảng từ 0 đến 500.
    """,
    tests=_tests_vo_so,
)
def cong_hai_bang(inp):
    data = inp.split()
    n, m = int(data[0]), int(data[1])
    a = data[2:2 + n * m]
    b = data[2 + n * m:2 + 2 * n * m]
    lines = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(str(int(a[i * m + j]) + int(b[i * m + j])))
        lines.append(" ".join(row))
    return "\n".join(lines) + "\n"


@problem(
    title="Mèo Mướp đi chéo bắt cá",
    difficulty=1,
    statement="""
        Sàn bếp hình vuông có n hàng và n cột ô, ô ở hàng i, cột j có một số con cá.
        Mèo Mướp đi từ góc trên bên trái xuống góc dưới bên phải theo đường chéo, tức là đi qua các ô
        (1, 1), (2, 2), ..., (n, n), và ăn hết cá ở những ô đó. Hỏi Mướp ăn được bao nhiêu con cá?

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n.
        - n dòng tiếp theo, mỗi dòng chứa n số nguyên cách nhau một dấu cách. Hàng được đánh số từ 1 đến n từ trên xuống dưới, cột từ 1 đến n từ trái sang phải.

        Đầu ra:
        - Một số nguyên: tổng số cá ở các ô (1, 1), (2, 2), ..., (n, n).

        Giới hạn:
        - 1 ≤ n ≤ 50.
        - Mỗi ô có từ 0 đến 100 con cá.
    """,
    tests=lambda r: [
        "3\n1 2 3\n4 5 6\n7 8 9\n",
        "1\n42\n",
        "2\n0 100\n100 0\n",
        _square([[100] * 50 for _ in range(50)]),
        _square(_rand(r, 4, 4, 0, 9)),
        _square(_rand(r, 10, 10, 0, 100)),
        _square(_rand(r, 25, 25, 0, 100)),
        _square(_rand(r, 50, 50, 0, 100)),
    ],
)
def duong_cheo_meo_muop(inp):
    data = inp.split()
    n = int(data[0])
    total = 0
    for i in range(n):
        total += int(data[1 + i * n + i])
    return f"{total}\n"


@problem(
    title="Tìm ô kẹo nhiều nhất trên bàn cờ",
    difficulty=1,
    statement="""
        Bạn Na rải kẹo lên một bàn cờ có n hàng và m cột, mỗi ô có một số viên kẹo.
        Na muốn biết ô nào có nhiều kẹo nhất và ô đó nằm ở đâu.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo, mỗi dòng chứa m số nguyên cách nhau một dấu cách.
        - Hàng được đánh số từ 1 đến n từ trên xuống dưới, cột được đánh số từ 1 đến m từ trái sang phải.

        Đầu ra:
        - In ra ba số nguyên trên một dòng, cách nhau một dấu cách: số kẹo nhiều nhất, số thứ tự hàng và số thứ tự cột của ô đó.
        - Nếu có nhiều ô cùng nhiều kẹo nhất, chọn ô có số hàng nhỏ nhất; nếu vẫn còn nhiều ô thì chọn ô có số cột nhỏ nhất.

        Giới hạn:
        - 1 ≤ n, m ≤ 50.
        - Mỗi ô có từ 0 đến 1000 viên kẹo.
    """,
    tests=lambda r: [
        "3 3\n1 5 2\n7 3 7\n0 6 4\n",
        "1 1\n0\n",
        _const(4, 5, 9),
        "2 3\n1 2 3\n4 5 6\n",
        "3 2\n5 1\n2 5\n5 0\n",
        _mat(r, 1, 30, 0, 1000),
        _mat(r, 12, 9, 0, 50),
        _mat(r, 50, 50, 0, 1000),
        _mat(r, 30, 20, 0, 10),
    ],
)
def o_keo_nhieu_nhat(inp):
    data = inp.split()
    n, m = int(data[0]), int(data[1])
    best, br, bc = -1, 0, 0
    for i in range(n):
        for j in range(m):
            v = int(data[2 + i * m + j])
            if v > best:
                best, br, bc = v, i + 1, j + 1
    return f"{best} {br} {bc}\n"


@problem(
    title="Lật bảng số của cô giáo Lan",
    difficulty=1,
    statement="""
        Cô Lan có một bảng số gồm n hàng và m cột. Cô muốn lật bảng: cột thứ nhất trở thành hàng thứ nhất,
        cột thứ hai trở thành hàng thứ hai, và cứ thế tiếp tục. Em hãy giúp cô viết bảng mới nhé!

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo, mỗi dòng chứa m số nguyên cách nhau một dấu cách.

        Đầu ra:
        - In ra bảng mới gồm m dòng, mỗi dòng n số nguyên cách nhau một dấu cách.
        - Dòng thứ j gồm các số ở cột thứ j của bảng cũ, lấy lần lượt từ hàng 1 xuống hàng n.

        Giới hạn:
        - 1 ≤ n, m ≤ 50.
        - Mỗi số từ 0 đến 999.
    """,
    tests=lambda r: [
        "2 3\n1 2 3\n4 5 6\n",
        "1 1\n5\n",
        "1 4\n7 8 9 10\n",
        "4 1\n7\n8\n9\n10\n",
        "3 3\n1 2 3\n4 5 6\n7 8 9\n",
        _mat(r, 5, 8, 0, 99),
        _mat(r, 50, 50, 0, 999),
        _mat(r, 20, 3, 0, 999),
    ],
)
def lat_bang_so(inp):
    data = inp.split()
    n, m = int(data[0]), int(data[1])
    a = [[int(data[2 + i * m + j]) for j in range(m)] for i in range(n)]
    lines = []
    for j in range(m):
        lines.append(" ".join(str(a[i][j]) for i in range(n)))
    return "\n".join(lines) + "\n"


@problem(
    title="Robot Bi đi dạo trên mặt phẳng",
    difficulty=1,
    statement="""
        Robot Bi đứng ở điểm (0, 0) trên một mặt phẳng rất rộng, không có tường hay mép nào cả.
        Bi nhận được một chuỗi lệnh và làm lần lượt từng lệnh. Mỗi lệnh là một chữ cái:
        - U: đi lên một bước, y tăng 1;
        - D: đi xuống một bước, y giảm 1;
        - R: sang phải một bước, x tăng 1;
        - L: sang trái một bước, x giảm 1.
        Hỏi sau khi làm hết các lệnh, Bi đang đứng ở điểm nào?

        Đầu vào:
        - Một dòng chứa chuỗi lệnh, chỉ gồm các chữ cái U, D, L, R viết liền nhau.

        Đầu ra:
        - In ra hai số nguyên x và y cách nhau một dấu cách: tọa độ cuối cùng của Bi (x, y có thể là số âm).

        Giới hạn:
        - Chuỗi lệnh dài từ 1 đến 100 ký tự.
    """,
    tests=lambda r: [
        "UURRRDL\n",
        "U\n",
        "LLLL\n",
        "UDLR\n",
        "D" * 100 + "\n",
        "".join(r.choice("UDLR") for _ in range(30)) + "\n",
        "".join(r.choice("UUDLRR") for _ in range(100)) + "\n",
        "".join(r.choice("UDDLLR") for _ in range(77)) + "\n",
    ],
)
def robot_bi_di_dao(inp):
    s = inp.split()[0]
    x, y = 0, 0
    for ch in s:
        if ch == "U":
            y += 1
        elif ch == "D":
            y -= 1
        elif ch == "R":
            x += 1
        elif ch == "L":
            x -= 1
    return f"{x} {y}\n"


def _tests_tham(r):
    def sym(n):
        a = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                a[i][j] = a[j][i] = r.randint(0, 9)
        return a

    def broken(n):
        a = sym(n)
        i, j = r.sample(range(n), 2)
        a[i][j] = (a[i][j] + 1 + r.randint(0, 8)) % 10
        return a

    return [
        _square([[1, 2, 3], [2, 5, 4], [3, 4, 9]]),
        _square([[7]]),
        _square([[1, 2], [2, 1]]),
        _square([[1, 2], [3, 1]]),
        _square([[1, 2, 3], [4, 5, 2], [7, 4, 1]]),
        _square(sym(10)),
        _square(broken(10)),
        _square(sym(30)),
        _square(broken(30)),
        _square(_rand(r, 6, 6, 0, 9)),
    ]


@problem(
    title="Tấm thảm đối xứng của bà ngoại",
    difficulty=1,
    statement="""
        Bà ngoại dệt một tấm thảm hình vuông n hàng, n cột ô; mỗi ô có một màu được ghi bằng một chữ số.
        Bà bảo tấm thảm là "đối xứng" nếu gấp nó theo đường chéo từ góc trên bên trái xuống góc dưới bên phải
        thì hai nửa trùng khít nhau. Nói cách khác: với mọi i và j, số ở hàng i, cột j bằng số ở hàng j, cột i.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n.
        - n dòng tiếp theo, mỗi dòng chứa n chữ số (từ 0 đến 9) cách nhau một dấu cách.

        Đầu ra:
        - In ra YES nếu tấm thảm đối xứng, ngược lại in ra NO.

        Giới hạn:
        - 1 ≤ n ≤ 30.
    """,
    tests=_tests_tham,
)
def tham_doi_xung(inp):
    data = inp.split()
    n = int(data[0])
    a = [[int(data[1 + i * n + j]) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                return "NO\n"
    return "YES\n"


# ================================================================ VỪA (12)

@problem(
    title="Chú ngựa gỗ nhảy hình chữ L",
    difficulty=2,
    statement="""
        Trên một bàn cờ có n hàng và m cột, chú ngựa gỗ đang đứng ở ô hàng r, cột c.
        Hàng được đánh số từ 1 đến n từ trên xuống dưới, cột từ 1 đến m từ trái sang phải.
        Mỗi lần nhảy, ngựa đi theo hình chữ L: 2 ô theo một hướng (lên, xuống, trái hoặc phải) rồi 1 ô theo hướng vuông góc với hướng đó.
        Như vậy có tất cả 8 kiểu nhảy. Hỏi từ chỗ đang đứng, ngựa có thể nhảy tới bao nhiêu ô mà không rơi ra ngoài bàn cờ?

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - Dòng thứ hai chứa hai số nguyên r và c: vị trí của ngựa.

        Đầu ra:
        - Một số nguyên: số ô ngựa có thể nhảy tới bằng một lần nhảy.

        Giới hạn:
        - 1 ≤ n, m ≤ 100; 1 ≤ r ≤ n; 1 ≤ c ≤ m.

        Gợi ý:
        - Từ ô (r, c), ngựa có thể tới các ô (r + a, c + b) với (a, b) là một trong 8 cặp: (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2).
    """,
    tests=[
        "8 8\n1 1\n",
        "8 8\n4 5\n",
        "1 1\n1 1\n",
        "3 3\n2 2\n",
        "2 3\n1 1\n",
        "8 8\n1 2\n",
        "100 100\n50 1\n",
        "8 8\n2 7\n",
        "3 100\n2 50\n",
    ],
)
def ngua_go_nhay(inp):
    n, m, r, c = (int(x) for x in inp.split()[:4])
    moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    count = 0
    for a, b in moves:
        if 1 <= r + a <= n and 1 <= c + b <= m:
            count += 1
    return f"{count}\n"


def _tests_robot_lau(r):
    tests = [
        "3 4\n2 2\nUUURRRRDL\n",
        "1 1\n1 1\nUDLRUDLR\n",
        "5 5\n3 3\nUUUUUUUU\n",
        "10 10\n10 10\nRRRRDDDD\n",
        "4 7\n1 1\nRRRRRRRRRRDDDDDDDLL\n",
    ]
    for n, m, k in ((20, 30, 120), (50, 50, 200), (2, 50, 150)):
        tests.append(f"{n} {m}\n{r.randint(1, n)} {r.randint(1, m)}\n"
                     + "".join(r.choice("UDLR") for _ in range(k)) + "\n")
    return tests


@problem(
    title="Robot lau sàn không ra khỏi phòng",
    difficulty=2,
    statement="""
        Robot lau sàn làm việc trong một căn phòng có n hàng và m cột ô vuông.
        Hàng được đánh số từ 1 đến n từ trên xuống dưới, cột từ 1 đến m từ trái sang phải.
        Lúc đầu robot ở ô hàng r, cột c. Robot làm lần lượt từng lệnh:
        - U: lên trên một ô (số hàng giảm 1);
        - D: xuống dưới một ô (số hàng tăng 1);
        - L: sang trái một ô (số cột giảm 1);
        - R: sang phải một ô (số cột tăng 1).
        Nếu một lệnh làm robot đi ra ngoài phòng thì robot đứng yên, bỏ qua lệnh đó rồi làm tiếp các lệnh sau.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - Dòng thứ hai chứa hai số nguyên r và c: vị trí ban đầu của robot.
        - Dòng thứ ba chứa chuỗi lệnh chỉ gồm các chữ U, D, L, R viết liền nhau.

        Đầu ra:
        - In ra hai số nguyên cách nhau một dấu cách: số hàng và số cột của ô robot đứng sau khi làm hết lệnh.

        Giới hạn:
        - 1 ≤ n, m ≤ 50; 1 ≤ r ≤ n; 1 ≤ c ≤ m.
        - Chuỗi lệnh dài từ 1 đến 200 ký tự.
    """,
    tests=_tests_robot_lau,
)
def robot_lau_san(inp):
    data = inp.split()
    n, m, r, c = int(data[0]), int(data[1]), int(data[2]), int(data[3])
    for ch in data[4]:
        nr, nc = r, c
        if ch == "U":
            nr -= 1
        elif ch == "D":
            nr += 1
        elif ch == "L":
            nc -= 1
        elif ch == "R":
            nc += 1
        if 1 <= nr <= n and 1 <= nc <= m:
            r, c = nr, nc
    return f"{r} {c}\n"


@problem(
    title="Điền số theo đường con rắn bò",
    difficulty=2,
    statement="""
        Bạn Tí muốn điền các số 1, 2, 3, ..., n·m vào một bảng có n hàng và m cột theo kiểu con rắn bò:
        hàng 1 điền từ trái sang phải, hàng 2 điền từ phải sang trái, hàng 3 lại từ trái sang phải, và cứ thế đổi chiều.
        Số tiếp theo luôn được điền ngay sau số trước, hết hàng này thì rắn bò xuống hàng dưới.

        Đầu vào:
        - Một dòng chứa hai số nguyên n và m.

        Đầu ra:
        - In ra n dòng, mỗi dòng m số nguyên cách nhau một dấu cách: bảng số sau khi điền.

        Giới hạn:
        - 1 ≤ n, m ≤ 20.
    """,
    tests=["3 4\n", "1 1\n", "1 6\n", "6 1\n", "2 2\n", "20 20\n", "7 3\n", "4 9\n"],
)
def dien_so_con_ran(inp):
    n, m = (int(x) for x in inp.split()[:2])
    lines = []
    k = 1
    for i in range(n):
        row = list(range(k, k + m))
        k += m
        if i % 2 == 1:
            row.reverse()
        lines.append(" ".join(str(v) for v in row))
    return "\n".join(lines) + "\n"


@problem(
    title="Xoay bức tranh ghép hình 90 độ",
    difficulty=2,
    statement="""
        Bức tranh ghép của bạn Minh có n hàng và m cột mảnh ghép, trên mỗi mảnh có ghi một số.
        Minh xoay cả bức tranh 90 độ theo chiều kim đồng hồ. Em hãy in ra bức tranh sau khi xoay.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo, mỗi dòng chứa m số nguyên cách nhau một dấu cách.

        Đầu ra:
        - Sau khi xoay, bức tranh có m hàng và n cột. In ra m dòng, mỗi dòng n số nguyên cách nhau một dấu cách.
        - Hàng thứ j của tranh mới là cột thứ j của tranh cũ, đọc từ dưới lên trên (từ hàng n lên hàng 1).

        Giới hạn:
        - 1 ≤ n, m ≤ 30.
        - Mỗi số từ 0 đến 99.
    """,
    tests=lambda r: [
        "2 3\n1 2 3\n4 5 6\n",
        "1 1\n8\n",
        "1 5\n1 2 3 4 5\n",
        "5 1\n1\n2\n3\n4\n5\n",
        "3 3\n1 2 3\n4 5 6\n7 8 9\n",
        _mat(r, 4, 7, 0, 99),
        _mat(r, 30, 30, 0, 99),
        _mat(r, 12, 5, 0, 99),
    ],
)
def xoay_tranh_90(inp):
    data = inp.split()
    n, m = int(data[0]), int(data[1])
    a = [[int(data[2 + i * m + j]) for j in range(m)] for i in range(n)]
    lines = []
    for j in range(m):
        lines.append(" ".join(str(a[i][j]) for i in range(n - 1, -1, -1)))
    return "\n".join(lines) + "\n"


def _tests_caro(r):
    def wins(b, p):
        lines = list(b)
        lines += ["".join(b[i][j] for i in range(3)) for j in range(3)]
        lines += [b[0][0] + b[1][1] + b[2][2], b[0][2] + b[1][1] + b[2][0]]
        return p * 3 in lines

    tests = [
        "XO.\nXO.\nX..\n",
        "...\n...\n...\n",
        "X.O\nXO.\nO.X\n",
        "XOX\nXOO\nOXX\n",
        "OOO\nXX.\nX.X\n",
        "XOO\n.XO\n..X\n",
    ]
    while len(tests) < 10:
        b = ["".join(r.choice("XO.") for _ in range(3)) for _ in range(3)]
        t = "\n".join(b) + "\n"
        if not (wins(b, "X") and wins(b, "O")) and t not in tests:
            tests.append(t)
    return tests


@problem(
    title="Ai thắng ván cờ ca-rô 3x3?",
    difficulty=2,
    statement="""
        An cầm quân X, Bình cầm quân O, hai bạn chơi cờ ca-rô trên bàn cờ 3 hàng, 3 cột.
        Một bạn thắng nếu có 3 quân của mình nằm thẳng hàng: cùng một hàng, cùng một cột,
        hoặc trên một trong hai đường chéo của bàn cờ. Nhìn bàn cờ, em hãy cho biết ai thắng.

        Đầu vào:
        - Gồm 3 dòng, mỗi dòng có đúng 3 ký tự viết liền nhau: 'X' (quân của An), 'O' (chữ O in hoa, quân của Bình) hoặc '.' (ô trống).

        Đầu ra:
        - In ra X nếu An thắng, O nếu Bình thắng, DRAW nếu chưa bạn nào có 3 quân thẳng hàng.

        Giới hạn:
        - Dữ liệu đảm bảo không có chuyện cả hai bạn cùng có 3 quân thẳng hàng.
    """,
    tests=_tests_caro,
)
def ai_thang_caro(inp):
    b = inp.split()[:3]
    lines = list(b)
    for j in range(3):
        lines.append(b[0][j] + b[1][j] + b[2][j])
    lines.append(b[0][0] + b[1][1] + b[2][2])
    lines.append(b[0][2] + b[1][1] + b[2][0])
    if "XXX" in lines:
        return "X\n"
    if "OOO" in lines:
        return "O\n"
    return "DRAW\n"


def _tests_than_ky(r):
    def siam(n, add=0):
        a = [[0] * n for _ in range(n)]
        i, j = 0, n // 2
        for k in range(1, n * n + 1):
            a[i][j] = k + add
            ni, nj = (i - 1) % n, (j + 1) % n
            if a[ni][nj]:
                ni, nj = (i + 1) % n, j
            i, j = ni, nj
        return a

    five = siam(5)
    five[0][0], five[0][1] = five[0][1], five[0][0]
    return [
        _square([[2, 7, 6], [9, 5, 1], [4, 3, 8]]),
        _square([[7]]),
        _square([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]),
        _square([[1, 2, 3], [2, 3, 1], [3, 1, 2]]),
        _square([[5] * 4 for _ in range(4)]),
        _square(siam(5)),
        _square(five),
        _square(siam(7, 51)),
        _square(_rand(r, 6, 6, 1, 100)),
        _square([[1, 2], [2, 1]]),
    ]


@problem(
    title="Hình vuông thần kỳ của phù thủy nhỏ",
    difficulty=2,
    statement="""
        Phù thủy nhỏ Mi có một bảng số hình vuông n hàng, n cột. Mi nói bảng là "thần kỳ" nếu tổng các số
        trên mỗi hàng, tổng trên mỗi cột và tổng trên cả hai đường chéo đều bằng nhau.
        Đường chéo chính đi từ góc trên bên trái xuống góc dưới bên phải; đường chéo phụ đi từ góc trên bên phải xuống góc dưới bên trái.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n.
        - n dòng tiếp theo, mỗi dòng chứa n số nguyên cách nhau một dấu cách.

        Đầu ra:
        - In ra YES nếu bảng là thần kỳ, ngược lại in ra NO.

        Giới hạn:
        - 1 ≤ n ≤ 10.
        - Mỗi số từ 1 đến 100.

        Gợi ý:
        - Lấy tổng hàng đầu tiên làm "mốc", rồi so sánh mọi tổng khác với mốc đó.
    """,
    tests=_tests_than_ky,
)
def hinh_vuong_than_ky(inp):
    data = inp.split()
    n = int(data[0])
    a = [[int(data[1 + i * n + j]) for j in range(n)] for i in range(n)]
    sums = [sum(row) for row in a]
    for j in range(n):
        sums.append(sum(a[i][j] for i in range(n)))
    sums.append(sum(a[i][i] for i in range(n)))
    sums.append(sum(a[i][n - 1 - i] for i in range(n)))
    for s in sums:
        if s != sums[0]:
            return "NO\n"
    return "YES\n"


@problem(
    title="Bản đồ dò mìn của đội đặc nhiệm nhí",
    difficulty=2,
    comparator="lines",
    statement="""
        Đội đặc nhiệm nhí nhận được bản đồ một bãi đất gồm n hàng và m cột ô: ô có mìn ký hiệu '*', ô an toàn ký hiệu '.'.
        Em hãy vẽ lại bản đồ để cả đội đi cho an toàn: ô có mìn giữ nguyên '*', còn mỗi ô an toàn được thay bằng
        một chữ số cho biết có bao nhiêu quả mìn ở các ô xung quanh nó.
        Mỗi ô có tối đa 8 ô xung quanh: các ô chung cạnh hoặc chung góc với nó.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo, mỗi dòng gồm đúng m ký tự '*' hoặc '.' viết liền nhau.

        Đầu ra:
        - In ra n dòng, mỗi dòng gồm đúng m ký tự viết liền nhau (không có dấu cách): bản đồ mới.

        Giới hạn:
        - 1 ≤ n, m ≤ 50.
    """,
    tests=lambda r: [
        "3 4\n*...\n..*.\n....\n",
        "1 1\n.\n",
        "1 1\n*\n",
        "3 3\n***\n*.*\n***\n",
        _chars(4, 5, ["." * 5] * 4),
        _grid(r, 1, 30, 0.3, "*"),
        _grid(r, 10, 12, 0.2, "*"),
        _grid(r, 50, 50, 0.25, "*"),
        _grid(r, 25, 40, 0.5, "*"),
    ],
)
def ban_do_do_min(inp):
    data = inp.split()
    n, m = int(data[0]), int(data[1])
    g = data[2:2 + n]
    lines = []
    for i in range(n):
        row = []
        for j in range(m):
            if g[i][j] == "*":
                row.append("*")
                continue
            cnt = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    x, y = i + di, j + dj
                    if (di or dj) and 0 <= x < n and 0 <= y < m and g[x][y] == "*":
                        cnt += 1
            row.append(str(cnt))
        lines.append("".join(row))
    return "\n".join(lines) + "\n"


def _tests_o_chu(r):
    def board(n, m, letters):
        return [[r.choice(letters) for _ in range(m)] for _ in range(n)]

    def text(g, w):
        return f"{len(g)} {len(g[0])}\n" + "\n".join("".join(row) for row in g) + "\n" + w + "\n"

    tests = [
        "4 5\nMEOXA\nCAQTB\nHOAYC\nOPIZD\nMEO\n",
        "1 1\nA\nA\n",
        "1 1\nA\nB\n",
        "3 3\nCAT\nXAX\nXTX\nTAC\n",
        "3 3\nABC\nDEF\nGHI\nAEI\n",
        "3 4\nBANH\nOTAX\nNGYZ\nBON\n",
        "2 3\nABC\nDEF\nABCD\n",
    ]
    # tu dat theo hang ngang
    g = board(20, 25, "ABCDE")
    w = "".join(r.choice("ABCDE") for _ in range(6))
    i, j = r.randint(0, 19), r.randint(0, 25 - 6)
    for k, ch in enumerate(w):
        g[i][j + k] = ch
    tests.append(text(g, w))
    # tu dat theo cot doc, sat mep duoi
    g = board(30, 30, "ABCDE")
    w = "".join(r.choice("ABCDE") for _ in range(8))
    j = r.randint(0, 29)
    for k, ch in enumerate(w):
        g[30 - 8 + k][j] = ch
    tests.append(text(g, w))
    # tu co chu Z khong co trong bang
    g = board(25, 30, "ABCDE")
    tests.append(text(g, "ABZ"))
    return tests


@problem(
    title="Tìm tên bạn trong bảng ô chữ",
    difficulty=2,
    statement="""
        Trong trò chơi ô chữ, bảng có n hàng và m cột, mỗi ô là một chữ cái in hoa.
        Một từ được coi là có trong bảng nếu đọc được nó trên các ô liền nhau theo hàng ngang từ trái sang phải,
        hoặc theo cột dọc từ trên xuống dưới. Đọc ngược (phải sang trái, dưới lên trên) hay đọc chéo đều không tính.
        Em hãy kiểm tra xem từ bạn đố có trong bảng không.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo, mỗi dòng gồm đúng m chữ cái in hoa viết liền nhau.
        - Dòng cuối cùng chứa từ cần tìm (gồm các chữ cái in hoa).

        Đầu ra:
        - In ra YES nếu tìm thấy từ trong bảng, ngược lại in ra NO.

        Giới hạn:
        - 1 ≤ n, m ≤ 30.
        - Từ cần tìm dài từ 1 đến 30 chữ cái.
    """,
    tests=_tests_o_chu,
)
def tim_tu_o_chu(inp):
    data = inp.split()
    n, m = int(data[0]), int(data[1])
    g = data[2:2 + n]
    w = data[2 + n]
    for row in g:
        if w in row:
            return "YES\n"
    for j in range(m):
        col = "".join(g[i][j] for i in range(n))
        if w in col:
            return "YES\n"
    return "NO\n"


def _tests_yen_ngua(r):
    tall = _rand(r, 10, 10, 0, 99)
    tall[3] = [100] * 10
    return [
        "3 3\n5 6 7\n1 9 2\n4 8 3\n",
        "1 1\n5\n",
        _const(3, 4, 7),
        "2 2\n1 4\n3 2\n",
        f"10 10\n{_fmt(tall)}\n",
        _mat(r, 5, 5, 0, 3),
        _mat(r, 50, 50, 0, 100),
        _mat(r, 1, 8, 0, 9),
        _mat(r, 8, 1, 0, 9),
    ]


@problem(
    title="Điểm yên ngựa trên bản đồ đồi núi",
    difficulty=2,
    statement="""
        Bản đồ đồi núi là một bảng n hàng, m cột, mỗi ô ghi độ cao của mặt đất ở đó.
        Nhà thám hiểm nhí gọi một ô là "điểm yên ngựa" nếu thỏa mãn cả hai điều sau:
        - trong cùng hàng với nó không có ô nào thấp hơn nó (nó là thấp nhất trong hàng, có thể bằng ô khác);
        - trong cùng cột với nó không có ô nào cao hơn nó (nó là cao nhất trong cột, có thể bằng ô khác).
        Em hãy đếm xem bản đồ có bao nhiêu điểm yên ngựa.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo, mỗi dòng chứa m số nguyên cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên: số điểm yên ngựa (có thể bằng 0).

        Giới hạn:
        - 1 ≤ n, m ≤ 50.
        - Mỗi độ cao từ 0 đến 100.

        Gợi ý:
        - Tính trước số nhỏ nhất của từng hàng và số lớn nhất của từng cột.
    """,
    tests=_tests_yen_ngua,
)
def diem_yen_ngua(inp):
    data = inp.split()
    n, m = int(data[0]), int(data[1])
    a = [[int(data[2 + i * m + j]) for j in range(m)] for i in range(n)]
    row_min = [min(row) for row in a]
    col_max = [max(a[i][j] for i in range(n)) for j in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == row_min[i] and a[i][j] == col_max[j]:
                count += 1
    return f"{count}\n"


def _tests_can_tin(r):
    tests = [
        "6\n+ 3\n+ 7\n-\n+ 5\n-\n-\n",
        "1\n-\n",
        "3\n+ 10\n-\n-\n",
        "4\n+ 1\n+ 2\n+ 3\n-\n",
    ]
    for q, p in ((30, 0.5), (200, 0.6), (1000, 0.5), (500, 0.35)):
        ev = []
        for _ in range(q - 1):
            ev.append(f"+ {r.randint(1, 1000)}" if r.random() < p else "-")
        ev.append("-")
        tests.append(f"{q}\n" + "\n".join(ev) + "\n")
    return tests


@problem(
    title="Xếp hàng mua bánh ở căng tin trường",
    difficulty=2,
    statement="""
        Giờ ra chơi, các bạn xếp hàng mua bánh ở căng tin. Mỗi bạn có một số thẻ học sinh.
        Lần lượt xảy ra q sự kiện, mỗi sự kiện thuộc một trong hai loại:
        - "+ x": bạn có số thẻ x đến đứng vào cuối hàng;
        - "-": cô bán hàng phục vụ bạn đang đứng đầu hàng, bạn đó mua xong thì rời khỏi hàng.
        Em hãy cho biết mỗi lần cô phục vụ thì đó là bạn nào.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên q.
        - q dòng tiếp theo, mỗi dòng là một sự kiện: hoặc dấu '+', một dấu cách rồi số nguyên x; hoặc chỉ một dấu '-'.

        Đầu ra:
        - Với mỗi sự kiện "-", theo đúng thứ tự, in trên một dòng số thẻ của bạn được phục vụ.
        - Nếu lúc đó hàng không có ai thì in TRONG.

        Giới hạn:
        - 1 ≤ q ≤ 1000; 1 ≤ x ≤ 1000.
        - Có ít nhất một sự kiện "-".
    """,
    tests=_tests_can_tin,
)
def hang_doi_can_tin(inp):
    from collections import deque

    data = inp.split()
    q = int(data[0])
    pos = 1
    line = deque()
    out = []
    for _ in range(q):
        kind = data[pos]
        pos += 1
        if kind == "+":
            line.append(int(data[pos]))
            pos += 1
        elif line:
            out.append(str(line.popleft()))
        else:
            out.append("TRONG")
    return "\n".join(out) + "\n"


@problem(
    title="Bé Na leo cầu thang một hay hai bậc",
    difficulty=2,
    statement="""
        Cầu thang lên nhà bà có n bậc. Mỗi bước, bé Na leo lên 1 bậc hoặc 2 bậc.
        Hỏi có bao nhiêu cách khác nhau để Na leo từ chân cầu thang lên đúng bậc thứ n?
        Hai cách là khác nhau nếu dãy các bước khác nhau. Chẳng hạn với 3 bậc có 3 cách: 1+1+1, 1+2 và 2+1.

        Đầu vào:
        - Một dòng chứa số nguyên n.

        Đầu ra:
        - Một số nguyên: số cách leo lên bậc thứ n.

        Giới hạn:
        - 1 ≤ n ≤ 45.

        Gợi ý:
        - Bước cuối cùng Na đứng ở bậc n - 1 (rồi leo 1 bậc) hoặc ở bậc n - 2 (rồi leo 2 bậc).
          Vậy số cách lên bậc n = số cách lên bậc n - 1 + số cách lên bậc n - 2.
    """,
    tests=["4\n", "1\n", "2\n", "3\n", "10\n", "20\n", "33\n", "45\n"],
)
def leo_cau_thang(inp):
    n = int(inp.split()[0])
    prev, cur = 1, 1  # so cach len bac 0 va bac 1
    for _ in range(n - 1):
        prev, cur = cur, prev + cur
    return f"{cur}\n"


@problem(
    title="Hàng thứ k của tam giác Pascal",
    difficulty=2,
    statement="""
        Nhà toán học nhí xếp các số thành tam giác Pascal như sau: hàng 1 chỉ có một số 1;
        mỗi hàng sau dài hơn hàng trước một số, hai đầu hàng luôn là 1, còn mỗi số ở giữa
        bằng tổng của hai số đứng ngay phía trên nó ở hàng trước. Bốn hàng đầu tiên là:
          1
          1 1
          1 2 1
          1 3 3 1
        Em hãy in ra hàng thứ k của tam giác.

        Đầu vào:
        - Một dòng chứa số nguyên k.

        Đầu ra:
        - In ra trên một dòng k số nguyên của hàng thứ k, cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ k ≤ 31.

        Gợi ý:
        - Bắt đầu từ hàng [1], mỗi lần tạo hàng mới từ hàng cũ, lặp lại k - 1 lần.
    """,
    tests=["5\n", "1\n", "2\n", "3\n", "10\n", "17\n", "24\n", "31\n"],
)
def tam_giac_pascal(inp):
    k = int(inp.split()[0])
    row = [1]
    for _ in range(k - 1):
        mid = [row[i] + row[i + 1] for i in range(len(row) - 1)]
        row = [1] + mid + [1]
    return " ".join(str(v) for v in row) + "\n"


# ================================================================ KHÓ (8)

@problem(
    title="Ốc sên bò xoắn ốc quanh vườn rau",
    difficulty=3,
    statement="""
        Vườn rau hình chữ nhật có n hàng và m cột ô, mỗi ô ghi một số.
        Ốc sên bắt đầu ở ô góc trên bên trái và bò sang phải. Mỗi khi gặp mép vườn hoặc ô đã đi qua,
        ốc rẽ phải (theo thứ tự: sang phải, xuống dưới, sang trái, lên trên, rồi lại sang phải...),
        cứ thế bò xoắn ốc vào trong cho đến khi đi qua mỗi ô đúng một lần.
        Em hãy in các số theo đúng thứ tự ốc sên bò qua.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo, mỗi dòng chứa m số nguyên cách nhau một dấu cách.

        Đầu ra:
        - In ra trên một dòng n·m số nguyên cách nhau một dấu cách, theo thứ tự ốc sên đi qua.

        Giới hạn:
        - 1 ≤ n, m ≤ 20.
        - Mỗi số từ 0 đến 999.
    """,
    tests=lambda r: [
        "3 4\n1 2 3 4\n5 6 7 8\n9 10 11 12\n",
        "1 1\n5\n",
        "1 5\n1 2 3 4 5\n",
        "5 1\n1\n2\n3\n4\n5\n",
        "2 2\n1 2\n3 4\n",
        f"4 4\n{_fmt([[i * 4 + j + 1 for j in range(4)] for i in range(4)])}\n",
        _mat(r, 7, 2, 0, 999),
        _mat(r, 3, 7, 0, 99),
        _mat(r, 20, 20, 0, 999),
    ],
)
def oc_sen_xoan_oc(inp):
    data = inp.split()
    n, m = int(data[0]), int(data[1])
    a = [[data[2 + i * m + j] for j in range(m)] for i in range(n)]
    seen = [[False] * m for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = c = d = 0
    out = []
    for _ in range(n * m):
        out.append(str(int(a[r][c])))
        seen[r][c] = True
        nr, nc = r + dr[d], c + dc[d]
        if not (0 <= nr < n and 0 <= nc < m) or seen[nr][nc]:
            d = (d + 1) % 4
            nr, nc = r + dr[d], c + dc[d]
        r, c = nr, nc
    return " ".join(out) + "\n"


@problem(
    title="Một ngày trong thành phố vi khuẩn",
    difficulty=3,
    comparator="lines",
    statement="""
        Thành phố vi khuẩn là một bảng n hàng, m cột; mỗi ô hoặc có một con vi khuẩn ('#'), hoặc trống ('.').
        Mỗi ô có tối đa 8 ô hàng xóm (chung cạnh hoặc chung góc); phần ngoài bảng coi như trống.
        Sau một ngày, MỌI ô cùng thay đổi một lúc theo luật:
        - Ô có vi khuẩn: nếu có đúng 2 hoặc 3 hàng xóm có vi khuẩn thì vi khuẩn sống tiếp, ngược lại nó chết (ô thành trống).
        - Ô trống: nếu có đúng 3 hàng xóm có vi khuẩn thì sinh ra một vi khuẩn mới, ngược lại vẫn trống.
        Em hãy vẽ thành phố sau đúng một ngày.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo, mỗi dòng gồm đúng m ký tự '#' hoặc '.' viết liền nhau.

        Đầu ra:
        - In ra n dòng, mỗi dòng gồm đúng m ký tự '#' hoặc '.': thành phố sau một ngày.

        Giới hạn:
        - 1 ≤ n, m ≤ 50.

        Gợi ý:
        - Luôn đếm hàng xóm trên bảng CŨ và ghi kết quả vào một bảng MỚI, đừng sửa trực tiếp bảng cũ.
    """,
    tests=lambda r: [
        "5 5\n.....\n..#..\n..#..\n..#..\n.....\n",
        "1 1\n#\n",
        "1 1\n.\n",
        _chars(4, 4, ["####"] * 4),
        "4 4\n....\n.##.\n.##.\n....\n",
        "6 6\n.#....\n..#...\n###...\n......\n......\n......\n",
        _grid(r, 1, 20, 0.6),
        _grid(r, 20, 30, 0.5),
        _grid(r, 50, 50, 0.35),
    ],
)
def thanh_pho_vi_khuan(inp):
    data = inp.split()
    n, m = int(data[0]), int(data[1])
    g = data[2:2 + n]
    lines = []
    for i in range(n):
        row = []
        for j in range(m):
            cnt = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    x, y = i + di, j + dj
                    if (di or dj) and 0 <= x < n and 0 <= y < m and g[x][y] == "#":
                        cnt += 1
            if g[i][j] == "#":
                row.append("#" if cnt in (2, 3) else ".")
            else:
                row.append("#" if cnt == 3 else ".")
        lines.append("".join(row))
    return "\n".join(lines) + "\n"


def _tests_xo_son(r):
    def with_fill(n, m, rows):
        return _chars(n, m, rows) + f"{r.randint(1, n)} {r.randint(1, m)} {r.choice('xyz')}\n"

    checker = ["".join("ab"[(i + j) % 2] for j in range(6)) for i in range(6)]
    return [
        "4 5\naabba\nabbba\naabcc\nccccc\n2 3 r\n",
        "1 1\na\n1 1 b\n",
        "2 2\nab\nba\n1 1 a\n",
        _chars(6, 6, checker) + "3 3 c\n",
        _chars(50, 50, ["g" * 50] * 50) + "25 25 z\n",
        with_fill(50, 50, _grid_rows(r, 50, 50, 0.45, "a", "b")),
        with_fill(30, 30, ["".join(r.choice("abc") for _ in range(30)) for _ in range(30)]),
        with_fill(40, 20, _grid_rows(r, 40, 20, 0.3, "b", "a")),
        with_fill(1, 50, _grid_rows(r, 1, 50, 0.2, "b", "a")),
    ]


@problem(
    title="Xô sơn thần kỳ của họa sĩ nhí",
    difficulty=3,
    comparator="lines",
    statement="""
        Bức tranh có n hàng và m cột ô, mỗi ô được tô một màu, ghi bằng một chữ cái thường (a, b, c, ...).
        Họa sĩ nhí đổ xô sơn màu ch vào ô ở hàng r, cột c. Sơn loang từ ô đó sang các ô kề cạnh
        (trên, dưới, trái, phải; không tính chéo) có CÙNG màu với ô ban đầu, rồi lại loang tiếp từ những ô vừa được sơn, cứ thế mãi.
        Mọi ô sơn loang tới đều đổi thành màu ch. Em hãy vẽ bức tranh sau khi đổ sơn.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo, mỗi dòng gồm đúng m chữ cái thường viết liền nhau.
        - Dòng cuối cùng chứa hai số nguyên r, c và một chữ cái thường ch, cách nhau một dấu cách.
        - Hàng được đánh số từ 1 đến n từ trên xuống dưới, cột từ 1 đến m từ trái sang phải.

        Đầu ra:
        - In ra n dòng, mỗi dòng gồm đúng m chữ cái: bức tranh sau khi đổ sơn.

        Giới hạn:
        - 1 ≤ n, m ≤ 50; 1 ≤ r ≤ n; 1 ≤ c ≤ m.
        - Nếu ch trùng với màu của ô (r, c) thì bức tranh không thay đổi.

        Gợi ý:
        - Dùng một hàng đợi (BFS) chứa các ô vừa được sơn để loang tiếp sang hàng xóm của chúng.
    """,
    tests=_tests_xo_son,
)
def xo_son_than_ky(inp):
    from collections import deque

    data = inp.split()
    n, m = int(data[0]), int(data[1])
    g = [list(row) for row in data[2:2 + n]]
    r, c, ch = int(data[2 + n]) - 1, int(data[3 + n]) - 1, data[4 + n]
    old = g[r][c]
    if old != ch:
        g[r][c] = ch
        queue = deque([(r, c)])
        while queue:
            x, y = queue.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == old:
                    g[nx][ny] = ch
                    queue.append((nx, ny))
    return "\n".join("".join(row) for row in g) + "\n"


@problem(
    title="Đếm hòn đảo trên bản đồ kho báu",
    difficulty=3,
    statement="""
        Thuyền trưởng Râu Đỏ có tấm bản đồ kho báu gồm n hàng và m cột ô: '#' là đất, '.' là nước.
        Hai ô đất thuộc cùng một hòn đảo nếu có thể đi từ ô này sang ô kia, mỗi bước bước sang
        một ô đất kề cạnh (trên, dưới, trái, phải). Đi chéo không được tính.
        Em hãy đếm xem trên bản đồ có bao nhiêu hòn đảo.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo, mỗi dòng gồm đúng m ký tự '#' hoặc '.' viết liền nhau.

        Đầu ra:
        - Một số nguyên: số hòn đảo (bằng 0 nếu không có ô đất nào).

        Giới hạn:
        - 1 ≤ n, m ≤ 50.

        Gợi ý:
        - Duyệt từng ô; gặp một ô đất chưa đánh dấu thì tăng số đảo lên 1 và loang (BFS) để đánh dấu cả hòn đảo đó.
    """,
    tests=lambda r: [
        "4 5\n##..#\n#...#\n..#..\n.....\n",
        "1 1\n#\n",
        _chars(3, 3, ["..."] * 3),
        _chars(50, 50, ["#" * 50] * 50),
        _chars(50, 50, ["".join("#."[(i + j) % 2] for j in range(50)) for i in range(50)]),
        "3 3\n#.#\n.#.\n#.#\n",
        _grid(r, 50, 50, 0.45),
        _grid(r, 30, 40, 0.6),
        _grid(r, 1, 50, 0.5),
    ],
)
def dem_hon_dao(inp):
    from collections import deque

    data = inp.split()
    n, m = int(data[0]), int(data[1])
    g = data[2:2 + n]
    seen = [[False] * m for _ in range(n)]
    islands = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] != "#" or seen[i][j]:
                continue
            islands += 1
            seen[i][j] = True
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == "#" and not seen[nx][ny]:
                        seen[nx][ny] = True
                        queue.append((nx, ny))
    return f"{islands}\n"


@problem(
    title="Nhím con nhặt nấm nhiều nhất",
    difficulty=3,
    statement="""
        Khu rừng là một bảng n hàng, m cột ô, mỗi ô có một số cây nấm.
        Nhím con đi từ ô (1, 1) ở góc trên bên trái đến ô (n, m) ở góc dưới bên phải;
        mỗi bước nhím chỉ được sang phải một ô hoặc xuống dưới một ô. Nhím nhặt hết nấm ở mọi ô mình đi qua,
        kể cả ô đầu tiên và ô cuối cùng. Hỏi nhím nhặt được nhiều nhất bao nhiêu cây nấm?

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo, mỗi dòng chứa m số nguyên cách nhau một dấu cách: số nấm ở từng ô.
        - Ô (i, j) là ô ở hàng i (đếm từ trên xuống), cột j (đếm từ trái sang).

        Đầu ra:
        - Một số nguyên: số nấm nhiều nhất nhím có thể nhặt.

        Giới hạn:
        - 1 ≤ n, m ≤ 50.
        - Mỗi ô có từ 0 đến 100 cây nấm.

        Gợi ý:
        - Gọi best[i][j] là số nấm nhiều nhất khi đi tới ô (i, j). Khi đó best[i][j] bằng số nấm ở ô (i, j)
          cộng với số lớn hơn trong best của ô ngay phía trên và best của ô ngay bên trái (nếu có).
    """,
    tests=lambda r: [
        "3 3\n1 3 1\n1 5 1\n4 2 1\n",
        "1 1\n7\n",
        "1 6\n3 1 4 1 5 9\n",
        "6 1\n2\n7\n1\n8\n2\n8\n",
        _const(4, 4, 0),
        _const(50, 50, 100),
        _mat(r, 2, 40, 0, 100),
        _mat(r, 20, 30, 0, 9),
        _mat(r, 50, 50, 0, 100),
    ],
)
def nhim_nhat_nam(inp):
    data = inp.split()
    n, m = int(data[0]), int(data[1])
    a = [[int(data[2 + i * m + j]) for j in range(m)] for i in range(n)]
    best = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                before = 0
            elif i == 0:
                before = best[i][j - 1]
            elif j == 0:
                before = best[i - 1][j]
            else:
                before = max(best[i - 1][j], best[i][j - 1])
            best[i][j] = a[i][j] + before
    return f"{best[n - 1][m - 1]}\n"


def _tests_tho_con(r):
    def field(n, m, p):
        rows = [list(row) for row in _grid_rows(r, n, m, p)]
        rows[0][0] = "."
        rows[n - 1][m - 1] = "."
        return _chars(n, m, ["".join(row) for row in rows])

    return [
        "3 3\n...\n.#.\n...\n",
        "1 1\n.\n",
        "2 2\n#.\n..\n",
        _chars(15, 15, ["." * 15] * 15),
        "3 4\n....\n####\n....\n",
        "1 10\n..........\n",
        "10 1\n.\n.\n.\n.\n#\n.\n.\n.\n.\n.\n",
        field(15, 15, 0.15),
        field(10, 12, 0.25),
        field(15, 14, 0.1),
    ]


@problem(
    title="Thỏ con tìm đường về hang tránh đá",
    difficulty=3,
    statement="""
        Cánh đồng là một bảng n hàng, m cột ô: '.' là ô cỏ, '#' là ô có tảng đá.
        Thỏ con đang ở ô (1, 1) góc trên bên trái, còn hang của thỏ ở ô (n, m) góc dưới bên phải.
        Mỗi bước thỏ chỉ nhảy sang phải một ô hoặc xuống dưới một ô, và không được nhảy vào ô có đá.
        Hỏi có bao nhiêu đường đi khác nhau để thỏ về tới hang?

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo, mỗi dòng gồm đúng m ký tự '.' hoặc '#' viết liền nhau.
        - Ô (i, j) là ô ở hàng i (đếm từ trên xuống), cột j (đếm từ trái sang).

        Đầu ra:
        - Một số nguyên: số đường đi khác nhau. Nếu ô (1, 1) hoặc ô (n, m) có đá, hoặc không có đường nào, in 0.

        Giới hạn:
        - 1 ≤ n, m ≤ 15.

        Gợi ý:
        - Số đường tới một ô cỏ = số đường tới ô ngay phía trên + số đường tới ô ngay bên trái. Ô có đá có 0 đường.
    """,
    tests=_tests_tho_con,
)
def tho_con_ve_hang(inp):
    data = inp.split()
    n, m = int(data[0]), int(data[1])
    g = data[2:2 + n]
    ways = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if g[i][j] == "#":
                ways[i][j] = 0
            elif i == 0 and j == 0:
                ways[i][j] = 1
            else:
                up = ways[i - 1][j] if i > 0 else 0
                left = ways[i][j - 1] if j > 0 else 0
                ways[i][j] = up + left
    return f"{ways[n - 1][m - 1]}\n"


def _tests_doi_xu(r):
    def ways(coins, s):
        w = [1] + [0] * s
        for c in coins:
            for t in range(c, s + 1):
                w[t] += w[t - c]
        return w[s]

    tests = [
        "3 5\n1 2 5\n",
        "1 7\n2\n",
        "1 6\n2\n",
        "2 10\n3 4\n",
        "8 200\n1 2 5 10 20 50 100 200\n",
        "3 1000\n100 200 500\n",
    ]
    while len(tests) < 10:
        k = r.randint(3, 8)
        coins = r.sample(range(1, 101), k)
        s = r.randint(100, 1000)
        if 0 < ways(coins, s) <= 10 ** 9:
            tests.append(f"{k} {s}\n" + " ".join(str(c) for c in coins) + "\n")
    return tests


@problem(
    title="Bao nhiêu cách trả tiền xu ở tiệm kẹo",
    difficulty=3,
    statement="""
        Tiệm kẹo của cô Ba nhận k loại đồng xu có mệnh giá khác nhau, mỗi loại có rất nhiều đồng (dùng bao nhiêu cũng được).
        Bạn Tùng muốn trả đúng s đồng. Hỏi có bao nhiêu cách chọn các đồng xu để tổng đúng bằng s?
        Hai cách chỉ khác nhau về thứ tự đưa tiền thì coi là một cách: ta chỉ quan tâm mỗi loại xu dùng bao nhiêu đồng.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên k và s.
        - Dòng thứ hai chứa k số nguyên khác nhau, cách nhau một dấu cách: mệnh giá các loại xu.

        Đầu ra:
        - Một số nguyên: số cách trả đúng s đồng (bằng 0 nếu không thể trả).

        Giới hạn:
        - 1 ≤ k ≤ 10; 1 ≤ mệnh giá ≤ 200; 1 ≤ s ≤ 1000.
        - Dữ liệu đảm bảo đáp số không vượt quá 10^9.

        Gợi ý:
        - Gọi cach[t] là số cách trả t đồng, ban đầu cach[0] = 1 và các ô khác bằng 0.
          Lần lượt xét từng loại xu có mệnh giá c: với t đi từ c lên s, cộng thêm cach[t - c] vào cach[t].
    """,
    tests=_tests_doi_xu,
)
def doi_tien_xu(inp):
    data = inp.split()
    k, s = int(data[0]), int(data[1])
    coins = [int(x) for x in data[2:2 + k]]
    ways = [0] * (s + 1)
    ways[0] = 1
    for c in coins:
        for t in range(c, s + 1):
            ways[t] += ways[t - c]
    return f"{ways[s]}\n"


def _tests_me_cung(r):
    def random_maze(n, m, p):
        rows = [list(row) for row in _grid_rows(r, n, m, p)]
        cells = r.sample([(i, j) for i in range(n) for j in range(m)], 2)
        (si, sj), (ei, ej) = cells
        rows[si][sj] = "S"
        rows[ei][ej] = "E"
        return _chars(n, m, ["".join(row) for row in rows])

    snake = []
    for i in range(49):
        if i % 2 == 0:
            snake.append(["."] * 50)
        else:
            row = ["#"] * 50
            row[49 if (i // 2) % 2 == 0 else 0] = "."
            snake.append(row)
    snake[0][0] = "S"
    snake[48][49] = "E"
    open_field = [["."] * 50 for _ in range(50)]
    open_field[0][0] = "S"
    open_field[49][49] = "E"
    return [
        "4 6\nS.#...\n..#.#.\n.##.#.\n....#E\n",
        "1 2\nSE\n",
        "1 3\nS#E\n",
        "3 3\nS#.\n##.\n..E\n",
        _chars(50, 50, ["".join(row) for row in open_field]),
        _chars(49, 50, ["".join(row) for row in snake]),
        random_maze(50, 50, 0.25),
        random_maze(30, 40, 0.3),
        random_maze(20, 20, 0.2),
    ]


@problem(
    title="Đường ngắn nhất thoát khỏi mê cung",
    difficulty=3,
    statement="""
        Bạn Khoa bị lạc trong một mê cung hình chữ nhật gồm n hàng và m cột ô:
        '#' là tường, '.' là lối đi, 'S' là chỗ Khoa đang đứng, 'E' là cửa ra.
        Mỗi bước Khoa đi sang một ô kề cạnh (trên, dưới, trái, phải) không phải tường và không ra ngoài mê cung.
        Hỏi Khoa cần ít nhất bao nhiêu bước để tới cửa ra?

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và m.
        - n dòng tiếp theo, mỗi dòng gồm đúng m ký tự '#', '.', 'S' hoặc 'E' viết liền nhau.
        - Mê cung có đúng một chữ 'S' và đúng một chữ 'E'.

        Đầu ra:
        - Một số nguyên: số bước ít nhất để đi từ S tới E. Nếu không thể tới được, in -1.

        Giới hạn:
        - 1 ≤ n, m ≤ 50.

        Gợi ý:
        - Dùng BFS: loang từ S theo từng lớp, trước hết là các ô cách S 1 bước, rồi các ô cách S 2 bước, ...
          Lần đầu tiên chạm tới E chính là số bước ít nhất.
    """,
    tests=_tests_me_cung,
)
def thoat_me_cung(inp):
    from collections import deque

    data = inp.split()
    n, m = int(data[0]), int(data[1])
    g = data[2:2 + n]
    dist = [[-1] * m for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if g[i][j] == "S":
                dist[i][j] = 0
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        if g[x][y] == "E":
            return f"{dist[x][y]}\n"
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != "#" and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return "-1\n"
