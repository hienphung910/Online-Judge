"""Chu de 9: Sap xep va tim kiem (K241-K270)."""

from kidslib import problem

TOPIC = "sap-xep"


# ----------------------------------------------------------- tro giup sinh test
# (chi dung de sinh input; cac ham loi giai ben duoi KHONG dung chung)

def _line(a):
    return " ".join(str(x) for x in a)


def _arr(a, head=None):
    """Input dang 'n' (hoac head) tren dong 1, day so tren dong 2."""
    if head is None:
        head = len(a)
    return f"{head}\n{_line(a)}\n"


def _rand_list(r, n, lo, hi):
    return [r.randint(lo, hi) for _ in range(n)]


def _rand_word(r, lo, hi, letters="abcdefghijklmnopqrstuvwxyz"):
    return "".join(r.choice(letters) for _ in range(r.randint(lo, hi)))


def _distinct_words(r, n, lo, hi):
    seen = []
    pool = set()
    while len(seen) < n:
        w = _rand_word(r, lo, hi)
        if w not in pool:
            pool.add(w)
            seen.append(w)
    return seen


def _shuffled(r, a):
    a = list(a)
    r.shuffle(a)
    return a


# =================================================================== DỄ (1)

@problem(
    title="Cô giáo xếp hàng từ thấp đến cao",
    difficulty=1,
    statement="""
        Sáng thứ Hai, cô giáo muốn cả lớp xếp hàng chào cờ thật ngay ngắn:
        bạn thấp nhất đứng đầu, bạn cao nhất đứng cuối. Em hãy giúp cô sắp xếp nhé!

        Đầu vào:
        - Dòng 1: số nguyên n là số bạn trong lớp.
        - Dòng 2: n số nguyên là chiều cao (cm) của từng bạn, cách nhau một dấu cách.

        Đầu ra:
        - Một dòng gồm n chiều cao đã xếp theo thứ tự tăng dần (bằng nhau thì đứng cạnh nhau),
          cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n ≤ 1000; 100 ≤ chiều cao ≤ 200.

        Gợi ý:
        - Em có thể tự viết sắp xếp nổi bọt, hoặc dùng hàm sắp xếp có sẵn của ngôn ngữ.
    """,
    tests=lambda r: [
        "5\n132 120 145 128 120\n",
        "1\n150\n",
        _arr([101, 105, 110, 120, 130, 140]),
        _arr([190, 180, 170, 160, 150, 140, 130]),
        _arr([125] * 4),
        _arr(_rand_list(r, 20, 100, 200)),
        _arr(_rand_list(r, 300, 100, 200)),
        _arr(_rand_list(r, 1000, 100, 200)),
    ],
)
def xep_hang_tang_dan(inp):
    d = inp.split()
    n = int(d[0])
    a = sorted(int(x) for x in d[1:1 + n])
    return " ".join(str(x) for x in a) + "\n"


@problem(
    title="Bảng điểm đố vui từ cao xuống thấp",
    difficulty=1,
    statement="""
        Câu lạc bộ Đố vui vừa chấm xong bài. Thầy chủ nhiệm muốn dán bảng điểm
        lên tường, điểm cao nhất ở trên cùng để cả lớp cùng chúc mừng.

        Đầu vào:
        - Dòng 1: số nguyên n là số bài thi.
        - Dòng 2: n số nguyên là điểm của từng bài, cách nhau một dấu cách.

        Đầu ra:
        - Một dòng gồm n điểm xếp theo thứ tự giảm dần (từ lớn đến nhỏ), cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n ≤ 1000; 0 ≤ điểm ≤ 100.

        Gợi ý:
        - Sắp xếp tăng dần rồi in ngược từ cuối về đầu cũng được.
    """,
    tests=lambda r: [
        "6\n70 100 35 85 100 50\n",
        "1\n0\n",
        _arr([5, 10, 20, 40, 80, 100]),
        _arr([99, 77, 55, 33, 11]),
        _arr([0] * 6),
        _arr(_rand_list(r, 50, 0, 100)),
        _arr(_rand_list(r, 1000, 0, 100)),
    ],
)
def bang_diem_giam_dan(inp):
    d = inp.split()
    n = int(d[0])
    a = sorted((int(x) for x in d[1:1 + n]), reverse=True)
    return " ".join(str(x) for x in a) + "\n"


@problem(
    title="Bạn đứng chính giữa hàng cao bao nhiêu?",
    difficulty=1,
    statement="""
        Lớp của An có một số lẻ học sinh. Sau khi xếp hàng từ thấp đến cao, bạn
        đứng chính giữa hàng sẽ được cầm cờ. Em hãy cho biết bạn ấy cao bao nhiêu.

        Đầu vào:
        - Dòng 1: số nguyên lẻ n là số học sinh.
        - Dòng 2: n số nguyên là chiều cao (cm) của các bạn, cách nhau một dấu cách
          (chưa được sắp xếp).

        Đầu ra:
        - Một số nguyên: chiều cao của bạn đứng ở vị trí thứ (n + 1) / 2 sau khi
          xếp hàng tăng dần theo chiều cao.

        Giới hạn:
        - 1 ≤ n ≤ 999, n là số lẻ; 100 ≤ chiều cao ≤ 200.
    """,
    tests=lambda r: [
        "5\n140 128 135 150 131\n",
        "1\n123\n",
        _arr([130] * 7),
        _arr([101, 104, 109, 115, 122, 130, 139, 149, 160]),
        _arr([199, 190, 181, 172, 163, 154, 145, 136, 127, 118, 109]),
        _arr(_rand_list(r, 101, 100, 200)),
        _arr(_rand_list(r, 999, 100, 200)),
    ],
)
def chieu_cao_o_giua(inp):
    d = inp.split()
    n = int(d[0])
    a = sorted(int(x) for x in d[1:1 + n])
    return f"{a[n // 2]}\n"


@problem(
    title="Mướp tìm hộp cá có số x",
    difficulty=1,
    statement="""
        Chú mèo Mướp có một dãy hộp cá xếp thành hàng, mỗi hộp dán một con số.
        Mướp chỉ thích hộp có số x. Em hãy giúp Mướp tìm hộp đầu tiên (tính từ trái
        sang phải) có số x nhé.

        Đầu vào:
        - Dòng 1: hai số nguyên n và x.
        - Dòng 2: n số nguyên là số dán trên các hộp, từ trái sang phải, cách nhau một dấu cách.

        Đầu ra:
        - Vị trí của hộp đầu tiên có số x (các hộp được đánh số từ 1 đến n tính từ trái).
        - Nếu không có hộp nào mang số x thì in -1.

        Giới hạn:
        - 1 ≤ n ≤ 1000; 1 ≤ x, số trên hộp ≤ 1000.

        Gợi ý:
        - Tìm kiếm tuần tự: đi lần lượt từng hộp, gặp số x là dừng lại ngay.
    """,
    tests=lambda r: [
        "6 7\n3 7 2 7 9 1\n",
        "1 5\n5\n",
        "1 5\n4\n",
        "5 9\n1 2 3 4 9\n",
        "5 9\n9 9 9 9 9\n",
        (lambda a: _arr(a, head=f"{len(a)} 13"))([v for v in _rand_list(r, 60, 1, 20) if v != 13]),
        (lambda a: f"1000 {a[r.randint(300, 999)]}\n{_line(a)}\n")(_rand_list(r, 1000, 1, 1000)),
        (lambda a: f"1000 {a[r.randint(0, 50)]}\n{_line(a)}\n")(_rand_list(r, 1000, 1, 1000)),
    ],
)
def muop_tim_hop_ca(inp):
    d = inp.split()
    n, x = int(d[0]), int(d[1])
    a = [int(v) for v in d[2:2 + n]]
    for i in range(n):
        if a[i] == x:
            return f"{i + 1}\n"
    return "-1\n"


@problem(
    title="Hàng của lớp đã ngay ngắn chưa?",
    difficulty=1,
    statement="""
        Robot Bi làm lớp trưởng. Bi đi dọc hàng và kiểm tra xem các bạn đã đứng
        đúng thứ tự từ thấp đến cao chưa (hai bạn cao bằng nhau đứng cạnh nhau vẫn được).

        Đầu vào:
        - Dòng 1: số nguyên n là số bạn trong hàng.
        - Dòng 2: n số nguyên a1, a2, ..., an là chiều cao của các bạn từ đầu đến cuối hàng.

        Đầu ra:
        - In YES nếu a1 ≤ a2 ≤ ... ≤ an, ngược lại in NO.

        Giới hạn:
        - 1 ≤ n ≤ 1000; 1 ≤ ai ≤ 100000.

        Gợi ý:
        - Chỉ cần so sánh từng cặp hai bạn đứng cạnh nhau.
    """,
    tests=lambda r: [
        "5\n1 3 3 7 9\n",
        "1\n42\n",
        "4\n9 7 5 2\n",
        _arr([8] * 6),
        "3\n2 1 3\n",
        _arr(sorted(_rand_list(r, 1000, 1, 100000))),
        (lambda a: _arr(a[:-2] + [a[-1], a[-2]]))(sorted(r.sample(range(1, 100001), 1000))),
        _arr(_rand_list(r, 500, 1, 100000)),
    ],
)
def hang_ngay_ngan(inp):
    d = inp.split()
    n = int(d[0])
    a = [int(v) for v in d[1:1 + n]]
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            return "NO\n"
    return "YES\n"


@problem(
    title="Viên bi nhỏ thứ k của An",
    difficulty=1,
    statement="""
        An có n viên bi, mỗi viên ghi một con số. An xếp các viên bi từ số nhỏ đến
        số lớn rồi đố em: viên bi đứng thứ k trong hàng ghi số mấy?

        Đầu vào:
        - Dòng 1: hai số nguyên n và k.
        - Dòng 2: n số nguyên là số ghi trên các viên bi (chưa sắp xếp), cách nhau một dấu cách.

        Đầu ra:
        - Số ghi trên viên bi đứng ở vị trí thứ k (đếm từ 1) sau khi xếp tăng dần.
          Các viên bi có số giống nhau vẫn được đếm riêng từng viên.

        Giới hạn:
        - 1 ≤ k ≤ n ≤ 1000; 1 ≤ số trên bi ≤ 10000.
    """,
    tests=lambda r: [
        "6 2\n9 4 7 4 1 8\n",
        "1 1\n77\n",
        "5 5\n3 8 1 9 2\n",
        "5 1\n3 8 1 9 2\n",
        "6 4\n5 5 5 5 5 5\n",
        _arr(_rand_list(r, 200, 1, 10000), head="200 100"),
        _arr(_rand_list(r, 1000, 1, 10000), head="1000 %d" % r.randint(1, 1000)),
        _arr(_rand_list(r, 1000, 1, 50), head="1000 777"),
    ],
)
def bi_nho_thu_k(inp):
    d = inp.split()
    n, k = int(d[0]), int(d[1])
    a = sorted(int(v) for v in d[2:2 + n])
    return f"{a[k - 1]}\n"


@problem(
    title="Bục vinh quang ba hạng đầu",
    difficulty=1,
    statement="""
        Hội thi "Bé giỏi toán" sắp trao giải. Ban tổ chức cần biết ba điểm số cao
        nhất để mời các bạn lên bục vinh quang.

        Đầu vào:
        - Dòng 1: số nguyên n là số thí sinh.
        - Dòng 2: n số nguyên là điểm của các thí sinh, cách nhau một dấu cách.

        Đầu ra:
        - Một dòng gồm 3 số: ba số đứng đầu của dãy điểm sau khi xếp giảm dần,
          cách nhau một dấu cách. Nếu có điểm bằng nhau thì vẫn tính là các bạn
          khác nhau (một điểm có thể được in nhiều lần).

        Giới hạn:
        - 3 ≤ n ≤ 1000; 0 ≤ điểm ≤ 100.
    """,
    tests=lambda r: [
        "7\n65 90 78 90 55 82 70\n",
        "3\n10 20 30\n",
        _arr([50] * 5),
        _arr(list(range(1, 11))),
        _arr([100, 99, 98, 97, 96, 95]),
        _arr(_rand_list(r, 50, 0, 100)),
        _arr(_rand_list(r, 1000, 0, 100)),
    ],
)
def ba_diem_cao_nhat(inp):
    d = inp.split()
    n = int(d[0])
    a = sorted((int(v) for v in d[1:1 + n]), reverse=True)
    return " ".join(str(x) for x in a[:3]) + "\n"


@problem(
    title="Sổ điểm danh xếp theo vần ABC",
    difficulty=1,
    statement="""
        Cô giáo muốn viết lại sổ điểm danh sao cho tên các bạn được xếp theo thứ
        tự bảng chữ cái, giống như trong từ điển. Em hãy giúp cô nhé!

        Đầu vào:
        - Dòng 1: số nguyên n là số bạn.
        - n dòng tiếp theo, mỗi dòng một tên gồm chữ cái tiếng Anh viết thường (a-z),
          không có dấu cách. Có thể có hai bạn trùng tên.

        Đầu ra:
        - n dòng, mỗi dòng một tên, theo thứ tự từ điển tăng dần: so sánh từng chữ cái
          từ trái sang phải theo bảng chữ cái a, b, c, ..., z; nếu một tên là phần đầu
          của tên kia (như an và anh) thì tên ngắn hơn đứng trước.

        Giới hạn:
        - 1 ≤ n ≤ 200; mỗi tên dài từ 1 đến 10 chữ cái.
    """,
    tests=lambda r: [
        "5\nmai\nan\nbinh\nanh\nlan\n",
        "1\nkhoa\n",
        "4\nanh\nab\nan\na\n",
        "5\nan\nbao\nchi\ndung\nem\n",
        "5\nyen\nvy\nthu\nson\nlinh\n",
        "6\nlan\nan\nlan\nbao\nan\nlan\n",
        "%d\n%s\n" % (200, "\n".join(_rand_word(r, 1, 10) for _ in range(200))),
        "%d\n%s\n" % (60, "\n".join(_rand_word(r, 1, 4, "abc") for _ in range(60))),
    ],
)
def so_diem_danh(inp):
    d = inp.split()
    n = int(d[0])
    names = sorted(d[1:1 + n])
    return "\n".join(names) + "\n"


@problem(
    title="Bộ sưu tập tem không trùng mẫu",
    difficulty=1,
    statement="""
        Bạn Minh sưu tầm tem, mỗi con tem có một mã số. Có những con tem bị trùng mã.
        Minh muốn biết mình có tất cả bao nhiêu mẫu tem khác nhau.

        Đầu vào:
        - Dòng 1: số nguyên n là số con tem.
        - Dòng 2: n số nguyên là mã của từng con tem, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên: số mã tem khác nhau.

        Giới hạn:
        - 1 ≤ n ≤ 1000; 1 ≤ mã tem ≤ 100000.

        Gợi ý:
        - Sau khi sắp xếp, các tem trùng mã sẽ đứng cạnh nhau. Em chỉ cần đếm những
          chỗ mà số đứng sau khác số đứng trước.
    """,
    tests=lambda r: [
        "8\n3 5 3 9 1 5 5 2\n",
        "1\n7\n",
        _arr([4] * 5),
        _arr(_shuffled(r, range(1, 101))),
        _arr(_rand_list(r, 1000, 1, 50)),
        _arr(_rand_list(r, 1000, 1, 1000)),
        _arr(_rand_list(r, 300, 1, 100000)),
    ],
)
def dem_mau_tem(inp):
    d = inp.split()
    n = int(d[0])
    a = sorted(int(v) for v in d[1:1 + n])
    cnt = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            cnt += 1
    return f"{cnt}\n"


@problem(
    title="Tấm thẻ số bị thất lạc",
    difficulty=1,
    statement="""
        Cô giáo có n tấm thẻ đánh số từ 1 đến n, mỗi số đúng một thẻ. Gió thổi bay
        mất một tấm, các tấm còn lại bị xáo trộn. Em hãy tìm xem tấm thẻ nào bị mất.

        Đầu vào:
        - Dòng 1: số nguyên n.
        - Dòng 2: n - 1 số nguyên khác nhau là số trên các tấm thẻ còn lại (theo thứ tự bất kỳ).

        Đầu ra:
        - Số ghi trên tấm thẻ bị mất.

        Giới hạn:
        - 2 ≤ n ≤ 1000.

        Gợi ý:
        - Xếp các thẻ còn lại tăng dần, rồi tìm vị trí đầu tiên mà số trên thẻ khác số thứ tự.
    """,
    tests=lambda r: [
        "5\n3 1 5 2\n",
        "2\n1\n",
        "2\n2\n",
        _arr(_shuffled(r, range(2, 11)), head=10),
        _arr(_shuffled(r, range(1, 100)), head=100),
        (lambda m: _arr(_shuffled(r, [v for v in range(1, 1001) if v != m]), head=1000))(r.randint(2, 999)),
        (lambda m: _arr(_shuffled(r, [v for v in range(1, 538) if v != m]), head=537))(r.randint(2, 536)),
    ],
)
def the_bi_mat(inp):
    d = inp.split()
    n = int(d[0])
    a = sorted(int(v) for v in d[1:n])
    for i in range(n - 1):
        if a[i] != i + 1:
            return f"{i + 1}\n"
    return f"{n}\n"


# =================================================================== VỪA (2)

@problem(
    title="Gom thẻ trùng trong hàng đã xếp",
    difficulty=2,
    statement="""
        An xếp các tấm thẻ số thành một hàng từ nhỏ đến lớn. Có nhiều thẻ trùng số,
        An muốn giữ lại mỗi số đúng một thẻ và cất các thẻ trùng đi.

        Đầu vào:
        - Dòng 1: số nguyên n.
        - Dòng 2: n số nguyên đã được xếp không giảm (số sau lớn hơn hoặc bằng số trước).

        Đầu ra:
        - Dòng 1: số m là số giá trị khác nhau.
        - Dòng 2: m giá trị khác nhau đó theo thứ tự tăng dần, cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n ≤ 1000; 1 ≤ mỗi số ≤ 1000.
    """,
    tests=lambda r: [
        "8\n1 1 2 4 4 4 7 9\n",
        "1\n5\n",
        _arr([3] * 6),
        _arr([1, 2, 3, 4, 5]),
        _arr(sorted(_rand_list(r, 100, 1, 20))),
        _arr(sorted(_rand_list(r, 1000, 1, 300))),
        _arr(sorted(_rand_list(r, 1000, 1, 1000))),
    ],
)
def gom_the_trung(inp):
    d = inp.split()
    n = int(d[0])
    a = [int(v) for v in d[1:1 + n]]
    b = [a[0]]
    for i in range(1, n):
        if a[i] != a[i - 1]:
            b.append(a[i])
    return f"{len(b)}\n" + " ".join(str(x) for x in b) + "\n"


@problem(
    title="Số chẵn đi lên, số lẻ đi xuống",
    difficulty=2,
    statement="""
        Robot Bi chơi trò xếp số: các số chẵn phải đứng trước và xếp từ nhỏ đến lớn,
        sau đó mới đến các số lẻ, xếp từ lớn đến nhỏ.

        Đầu vào:
        - Dòng 1: số nguyên n.
        - Dòng 2: n số nguyên không âm, cách nhau một dấu cách.

        Đầu ra:
        - Một dòng gồm n số: trước hết là tất cả các số chẵn theo thứ tự tăng dần,
          tiếp theo là tất cả các số lẻ theo thứ tự giảm dần, cách nhau một dấu cách.
          Số xuất hiện nhiều lần thì in đủ bấy nhiêu lần. (Số 0 là số chẵn.)

        Giới hạn:
        - 1 ≤ n ≤ 1000; 0 ≤ mỗi số ≤ 10000.
    """,
    tests=lambda r: [
        "7\n5 8 3 2 9 4 7\n",
        "1\n6\n",
        "1\n7\n",
        _arr([9, 1, 7, 3, 5]),
        _arr([0, 4, 2, 8, 6, 0]),
        _arr(_rand_list(r, 30, 0, 50)),
        _arr(_rand_list(r, 1000, 0, 10000)),
    ],
)
def chan_len_le_xuong(inp):
    d = inp.split()
    n = int(d[0])
    a = [int(v) for v in d[1:1 + n]]
    even = sorted(x for x in a if x % 2 == 0)
    odd = sorted((x for x in a if x % 2 == 1), reverse=True)
    return " ".join(str(x) for x in even + odd) + "\n"


@problem(
    title="Chỗ đứng cho bạn mới vào hàng",
    difficulty=2,
    statement="""
        Lớp đang xếp hàng từ thấp đến cao thì có một bạn mới chuyển đến. Bạn mới sẽ
        đứng ngay sau tất cả các bạn thấp hơn hoặc cao bằng mình, và đứng trước bạn
        đầu tiên cao hơn mình. Hỏi bạn mới đứng ở vị trí thứ mấy?

        Đầu vào:
        - Dòng 1: hai số nguyên n và x (n là số bạn đang xếp hàng, x là chiều cao của bạn mới).
        - Dòng 2: n số nguyên là chiều cao của các bạn trong hàng, đã xếp không giảm.

        Đầu ra:
        - Vị trí của bạn mới trong hàng mới (gồm n + 1 bạn, đánh số từ 1 ở đầu hàng).

        Giới hạn:
        - 1 ≤ n ≤ 1000; 100 ≤ chiều cao ≤ 200.

        Gợi ý:
        - Đáp án bằng số bạn có chiều cao nhỏ hơn hoặc bằng x, cộng thêm 1.
    """,
    tests=lambda r: [
        "6 130\n120 125 130 130 138 145\n",
        "1 100\n120\n",
        "1 150\n120\n",
        "5 110\n120 121 125 130 140\n",
        "5 200\n120 121 125 130 140\n",
        "4 135\n135 135 135 135\n",
        _arr(sorted(_rand_list(r, 1000, 100, 200)), head="1000 %d" % r.randint(100, 200)),
        _arr(sorted(_rand_list(r, 300, 100, 200)), head="300 %d" % r.randint(100, 200)),
    ],
)
def cho_dung_ban_moi(inp):
    import bisect
    d = inp.split()
    n, x = int(d[0]), int(d[1])
    a = [int(v) for v in d[2:2 + n]]
    return f"{bisect.bisect_right(a, x) + 1}\n"


@problem(
    title="Thủ thư Bi tra mã sách thật nhanh",
    difficulty=2,
    statement="""
        Thư viện trường có n cuốn sách, mã của chúng đã được ghi theo thứ tự tăng dần.
        Các bạn học sinh đến hỏi q lần: "Thư viện có sách mã x không?". Robot thủ thư Bi
        cần trả lời thật nhanh.

        Đầu vào:
        - Dòng 1: hai số nguyên n và q.
        - Dòng 2: n số nguyên là mã sách, đã xếp không giảm.
        - Dòng 3: q số nguyên x là các mã được hỏi.

        Đầu ra:
        - q dòng, dòng thứ i in YES nếu mã thứ i có trong danh sách, ngược lại in NO.

        Giới hạn:
        - 1 ≤ n, q ≤ 1000; 1 ≤ mã sách, x ≤ 100000.

        Gợi ý:
        - Tìm kiếm nhị phân: so x với mã ở giữa đoạn đang xét, rồi bỏ đi nửa không thể chứa x.
    """,
    tests=lambda r: [
        "5 4\n2 5 8 12 20\n8 3 20 1\n",
        "1 2\n7\n7 8\n",
        "6 3\n4 4 4 4 4 4\n4 3 5\n",
        (lambda a: f"100 50\n{_line(a)}\n{_line([2 * r.randint(1, 50000) - 1 for _ in range(50)])}\n")(
            sorted(2 * r.randint(1, 50000) for _ in range(100))),
        (lambda a: f"1000 1000\n{_line(a)}\n{_line([r.choice(a) if r.random() < 0.5 else r.randint(1, 100000) for _ in range(1000)])}\n")(
            sorted(_rand_list(r, 1000, 1, 100000))),
        (lambda a: f"1000 1000\n{_line(a)}\n{_line(_rand_list(r, 1000, 1, 2000))}\n")(
            sorted(_rand_list(r, 1000, 1, 2000))),
    ],
)
def thu_thu_tra_sach(inp):
    import bisect
    d = inp.split()
    n, q = int(d[0]), int(d[1])
    a = [int(v) for v in d[2:2 + n]]
    out = []
    for t in d[2 + n:2 + n + q]:
        x = int(t)
        i = bisect.bisect_left(a, x)
        out.append("YES" if i < n and a[i] == x else "NO")
    return "\n".join(out) + "\n"


@problem(
    title="Hai bạn cao gần bằng nhau nhất",
    difficulty=2,
    statement="""
        Thầy thể dục muốn chọn hai bạn có chiều cao chênh lệch ít nhất để đứng cặp
        với nhau trong tiết múa. Em hãy tính độ chênh lệch nhỏ nhất đó.

        Đầu vào:
        - Dòng 1: số nguyên n là số học sinh.
        - Dòng 2: n số nguyên là chiều cao của từng bạn, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên: giá trị nhỏ nhất của (chiều cao lớn hơn - chiều cao nhỏ hơn)
          trong mọi cặp hai bạn khác nhau. Hai bạn cao bằng nhau thì chênh lệch là 0.

        Giới hạn:
        - 2 ≤ n ≤ 1000; 1 ≤ chiều cao ≤ 1000000.

        Gợi ý:
        - Sau khi sắp xếp, cặp gần nhau nhất luôn là hai bạn đứng cạnh nhau.
    """,
    tests=lambda r: [
        "5\n140 125 133 152 131\n",
        "2\n100 160\n",
        "4\n130 145 130 160\n",
        _arr([100, 110, 120, 130, 140, 150]),
        _arr(_rand_list(r, 10, 1, 1000)),
        _arr(r.sample(range(1, 1000001, 37), 50)),
        _arr(r.sample(range(1, 1000001), 1000)),
    ],
)
def chenh_lech_nho_nhat(inp):
    d = inp.split()
    n = int(d[0])
    a = sorted(int(v) for v in d[1:1 + n])
    best = a[1] - a[0]
    for i in range(1, n - 1):
        best = min(best, a[i + 1] - a[i])
    return f"{best}\n"


@problem(
    title="Hai túi bi có giống hệt nhau không?",
    difficulty=2,
    statement="""
        An và Bình mỗi bạn có một túi n viên bi, mỗi viên ghi một số. Hai bạn muốn biết
        hai túi có giống hệt nhau không: mỗi số phải xuất hiện trong hai túi với số
        lần bằng nhau (thứ tự lấy ra không quan trọng).

        Đầu vào:
        - Dòng 1: số nguyên n.
        - Dòng 2: n số nguyên ghi trên các viên bi của An.
        - Dòng 3: n số nguyên ghi trên các viên bi của Bình.

        Đầu ra:
        - In YES nếu hai túi giống hệt nhau, ngược lại in NO.

        Giới hạn:
        - 1 ≤ n ≤ 1000; 1 ≤ số trên bi ≤ 1000.

        Gợi ý:
        - Sắp xếp cả hai dãy rồi so sánh từng vị trí.
    """,
    tests=lambda r: [
        "5\n3 1 4 1 5\n1 5 4 3 1\n",
        "3\n1 1 2\n1 2 2\n",
        "1\n9\n9\n",
        "1\n9\n8\n",
        "4\n1 2 3 4\n1 2 3 4\n",
        (lambda a: f"1000\n{_line(a)}\n{_line(_shuffled(r, a))}\n")(_rand_list(r, 1000, 1, 1000)),
        (lambda a, b: f"1000\n{_line(a)}\n{_line(b[:499] + [b[499] % 1000 + 1] + b[500:])}\n")(
            *(lambda a: (a, _shuffled(r, a)))(_rand_list(r, 1000, 1, 1000))),
        (lambda a: f"300\n{_line(a)}\n{_line(_shuffled(r, a))}\n")(_rand_list(r, 300, 1, 10)),
    ],
)
def hai_tui_bi(inp):
    d = inp.split()
    n = int(d[0])
    a = sorted(int(v) for v in d[1:1 + n])
    b = sorted(int(v) for v in d[1 + n:1 + 2 * n])
    return ("YES" if a == b else "NO") + "\n"


@problem(
    title="Xếp từ theo độ dài rồi theo vần",
    difficulty=2,
    statement="""
        Cô giáo tiếng Anh phát cho lớp một danh sách từ mới. Để dễ học, An muốn xếp các
        từ ngắn lên trước, từ dài ra sau; các từ dài bằng nhau thì xếp theo thứ tự từ điển.

        Đầu vào:
        - Dòng 1: số nguyên n là số từ.
        - n dòng tiếp theo, mỗi dòng một từ gồm chữ cái tiếng Anh viết thường (a-z).

        Đầu ra:
        - n dòng, mỗi dòng một từ, xếp theo số chữ cái tăng dần; nếu hai từ có cùng số
          chữ cái thì từ nào đứng trước trong từ điển (so từng chữ cái theo bảng chữ
          cái a, b, ..., z) sẽ đứng trước. Từ trùng nhau thì in đủ số lần.

        Giới hạn:
        - 1 ≤ n ≤ 200; mỗi từ dài từ 1 đến 10 chữ cái.
    """,
    tests=lambda r: [
        "6\nmeo\ncho\nca\nvoi\nho\nchuot\n",
        "1\nsun\n",
        "5\nbb\nab\nba\naa\nb\n",
        "4\nabcde\nabcd\nabc\nab\n",
        "5\ncat\ncat\ndog\nant\ncat\n",
        "%d\n%s\n" % (200, "\n".join(_rand_word(r, 1, 6, "abcde") for _ in range(200))),
        "%d\n%s\n" % (100, "\n".join(_rand_word(r, 1, 10) for _ in range(100))),
    ],
)
def xep_tu_do_dai(inp):
    d = inp.split()
    n = int(d[0])
    words = sorted(d[1:1 + n], key=lambda w: (len(w), w))
    return "\n".join(words) + "\n"


@problem(
    title="Trộn hai hàng đã xếp sẵn",
    difficulty=2,
    statement="""
        Lớp 3A và lớp 3B đều đã xếp hàng từ thấp đến cao. Bây giờ hai lớp nhập lại
        thành một hàng chung, vẫn phải từ thấp đến cao. Em hãy in ra hàng mới.

        Đầu vào:
        - Dòng 1: số nguyên n là số bạn lớp 3A.
        - Dòng 2: n chiều cao của lớp 3A, đã xếp không giảm.
        - Dòng 3: số nguyên m là số bạn lớp 3B.
        - Dòng 4: m chiều cao của lớp 3B, đã xếp không giảm.

        Đầu ra:
        - Một dòng gồm n + m chiều cao của hàng chung, xếp không giảm, cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n, m ≤ 1000; 100 ≤ chiều cao ≤ 200.

        Gợi ý:
        - Dùng hai "ngón tay" chỉ vào đầu hai hàng; mỗi lần lấy bạn thấp hơn ra trước.
    """,
    tests=lambda r: [
        "4\n121 124 136 149\n3\n122 124 150\n",
        "1\n150\n1\n130\n",
        "3\n101 102 103\n3\n107 108 109\n",
        "3\n187 188 189\n2\n111 112\n",
        "4\n160 160 160 160\n3\n160 160 160\n",
        (lambda a, b: f"{len(a)}\n{_line(a)}\n{len(b)}\n{_line(b)}\n")(
            sorted(_rand_list(r, 500, 100, 200)), sorted(_rand_list(r, 700, 100, 200))),
        (lambda a, b: f"{len(a)}\n{_line(a)}\n{len(b)}\n{_line(b)}\n")(
            [155], sorted(_rand_list(r, 1000, 100, 200))),
    ],
)
def tron_hai_hang(inp):
    d = inp.split()
    n = int(d[0])
    a = [int(v) for v in d[1:1 + n]]
    m = int(d[1 + n])
    b = [int(v) for v in d[2 + n:2 + n + m]]
    i = j = 0
    c = []
    while i < n and j < m:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return " ".join(str(x) for x in c) + "\n"


@problem(
    title="Số x đứng từ đâu đến đâu trong hàng?",
    difficulty=2,
    statement="""
        Mướp xếp các con cá khô theo cân nặng từ nhẹ đến nặng. Những con nặng bằng nhau
        thì nằm liền nhau. Mướp muốn biết các con cá nặng đúng x gam nằm từ vị trí nào
        đến vị trí nào.

        Đầu vào:
        - Dòng 1: hai số nguyên n và x.
        - Dòng 2: n số nguyên là cân nặng của các con cá, đã xếp không giảm.

        Đầu ra:
        - Hai số nguyên: vị trí đầu tiên và vị trí cuối cùng (đánh số từ 1) của con cá
          nặng đúng x gam, cách nhau một dấu cách.
        - Nếu không có con cá nào nặng x gam thì in: -1 -1

        Giới hạn:
        - 1 ≤ n ≤ 1000; 1 ≤ x, cân nặng ≤ 1000.
    """,
    tests=lambda r: [
        "8 5\n1 3 5 5 5 7 8 8\n",
        "1 4\n4\n",
        "1 4\n6\n",
        "5 3\n3 3 3 3 3\n",
        "6 9\n1 2 4 6 8 9\n",
        "6 5\n1 2 4 6 8 9\n",
        (lambda a: f"1000 {r.choice(a)}\n{_line(a)}\n")(sorted(_rand_list(r, 1000, 1, 100))),
        (lambda a: f"1000 {r.choice(a)}\n{_line(a)}\n")(sorted(_rand_list(r, 1000, 1, 1000))),
    ],
)
def dau_cuoi_cua_x(inp):
    import bisect
    d = inp.split()
    n, x = int(d[0]), int(d[1])
    a = [int(v) for v in d[2:2 + n]]
    lo = bisect.bisect_left(a, x)
    hi = bisect.bisect_right(a, x)
    if lo == hi:
        return "-1 -1\n"
    return f"{lo + 1} {hi}\n"


@problem(
    title="Đếm bài thi có điểm trong khoảng",
    difficulty=2,
    statement="""
        Trò chơi "Vượt chướng ngại vật" ghi lại điểm của n bạn. Thầy giáo hỏi q câu:
        "Có bao nhiêu bạn có điểm từ l đến r?". Em hãy trả lời giúp thầy.

        Đầu vào:
        - Dòng 1: hai số nguyên n và q.
        - Dòng 2: n số nguyên là điểm của các bạn (chưa sắp xếp).
        - q dòng tiếp theo, mỗi dòng hai số nguyên l và r (l ≤ r).

        Đầu ra:
        - q dòng, dòng thứ i là số bạn có điểm s thỏa mãn l ≤ s ≤ r của câu hỏi thứ i.

        Giới hạn:
        - 1 ≤ n, q ≤ 1000; 0 ≤ điểm, l, r ≤ 1000.

        Gợi ý:
        - Sắp xếp điểm một lần, rồi dùng tìm kiếm nhị phân để đếm cho mỗi câu hỏi.
    """,
    tests=lambda r: [
        "6 3\n7 2 9 4 4 10\n3 7\n1 1\n4 10\n",
        "1 2\n5\n5 5\n6 10\n",
        "5 3\n0 0 0 0 0\n0 0\n0 1000\n1 1000\n",
        "4 2\n1 2 3 4\n1 4\n2 3\n",
        (lambda a, qs: f"200 100\n{_line(a)}\n" + "".join(f"{l} {h}\n" for l, h in qs))(
            _rand_list(r, 200, 0, 1000),
            [tuple(sorted((r.randint(0, 1000), r.randint(0, 1000)))) for _ in range(100)]),
        (lambda a, qs: f"1000 1000\n{_line(a)}\n" + "".join(f"{l} {h}\n" for l, h in qs))(
            _rand_list(r, 1000, 0, 1000),
            [tuple(sorted((r.randint(0, 1000), r.randint(0, 1000)))) for _ in range(1000)]),
    ],
)
def dem_diem_trong_khoang(inp):
    import bisect
    d = inp.split()
    n, q = int(d[0]), int(d[1])
    a = sorted(int(v) for v in d[2:2 + n])
    out = []
    p = 2 + n
    for _ in range(q):
        lo, hi = int(d[p]), int(d[p + 1])
        p += 2
        out.append(str(bisect.bisect_right(a, hi) - bisect.bisect_left(a, lo)))
    return "\n".join(out) + "\n"


@problem(
    title="Robot Bi đoán số bằng cách chia đôi",
    difficulty=2,
    statement="""
        An nghĩ một số x trong khoảng từ 1 đến n. Robot Bi đoán theo cách chia đôi
        rất thông minh. Bi nhớ hai số lo = 1 và hi = n, rồi lặp lại:
        - Bi đoán số g = (lo + hi) / 2 (phép chia lấy phần nguyên).
        - Nếu g = x thì An nói "Đúng rồi!" và trò chơi kết thúc.
        - Nếu g < x thì An nói "Lớn hơn", Bi đặt lo = g + 1.
        - Nếu g > x thì An nói "Nhỏ hơn", Bi đặt hi = g - 1.
        Hỏi Bi phải đoán tất cả bao nhiêu lần (tính cả lần đoán đúng)?

        Đầu vào:
        - Một dòng gồm hai số nguyên n và x.

        Đầu ra:
        - Số lần đoán của Bi.

        Giới hạn:
        - 1 ≤ x ≤ n ≤ 1000000.
    """,
    tests=lambda r: [
        "10 7\n",
        "1 1\n",
        "100 50\n",
        "100 1\n",
        "100 100\n",
        "1000000 1\n",
        "1000000 999999\n",
        (lambda n: f"{n} {r.randint(1, n)}\n")(r.randint(1000, 1000000)),
        (lambda n: f"{n} {r.randint(1, n)}\n")(r.randint(10, 1000)),
    ],
)
def bi_doan_so(inp):
    d = inp.split()
    n, x = int(d[0]), int(d[1])
    lo, hi = 1, n
    cnt = 0
    while True:
        g = (lo + hi) // 2
        cnt += 1
        if g == x:
            break
        if g < x:
            lo = g + 1
        else:
            hi = g - 1
    return f"{cnt}\n"


@problem(
    title="Tìm số gần nhất với số may mắn",
    difficulty=2,
    statement="""
        Cửa hàng kẹo có n hộp kẹo, mỗi hộp có một số viên kẹo. Mỗi bạn nhỏ đến cửa hàng
        mang theo một số may mắn x và muốn nhận hộp có số viên kẹo gần x nhất.

        Đầu vào:
        - Dòng 1: hai số nguyên n và q (q là số bạn nhỏ).
        - Dòng 2: n số nguyên là số viên kẹo trong từng hộp (chưa sắp xếp).
        - Dòng 3: q số nguyên x là số may mắn của từng bạn.

        Đầu ra:
        - q dòng, dòng thứ i là số viên kẹo a của hộp gần với số may mắn thứ i nhất, tức là
          khoảng cách giữa a và x (lấy số lớn trừ số nhỏ) là nhỏ nhất. Nếu có hai giá trị
          cách x bằng nhau thì chọn giá trị nhỏ hơn. (Các hộp không bị lấy đi, mỗi bạn
          chọn độc lập.)

        Giới hạn:
        - 1 ≤ n, q ≤ 1000; 1 ≤ số viên kẹo, x ≤ 100000.
    """,
    tests=lambda r: [
        "5 3\n10 3 7 15 20\n8 5 30\n",
        "1 3\n50\n1 50 100\n",
        "4 4\n10 20 30 40\n15 25 35 45\n",
        "3 2\n5 5 5\n1 9\n",
        f"50 200\n{_line(_rand_list(r, 50, 1, 1000))}\n{_line(_rand_list(r, 200, 1, 1000))}\n",
        f"1000 1000\n{_line(_rand_list(r, 1000, 1, 100000))}\n{_line(_rand_list(r, 1000, 1, 100000))}\n",
        f"1000 1000\n{_line([2 * r.randint(1, 500) for _ in range(1000)])}\n{_line(_rand_list(r, 1000, 1, 1001))}\n",
    ],
)
def so_gan_nhat(inp):
    import bisect
    d = inp.split()
    n, q = int(d[0]), int(d[1])
    a = sorted(int(v) for v in d[2:2 + n])
    out = []
    for t in d[2 + n:2 + n + q]:
        x = int(t)
        i = bisect.bisect_left(a, x)
        cands = []
        if i < n:
            cands.append(a[i])
        if i > 0:
            cands.append(a[i - 1])
        best = min(cands, key=lambda v: (abs(v - x), v))
        out.append(str(best))
    return "\n".join(out) + "\n"


# =================================================================== KHÓ (3)

@problem(
    title="Đếm cặp quà vừa khít túi tiền",
    difficulty=3,
    statement="""
        Bình có đúng s nghìn đồng và muốn mua đúng hai món quà khác nhau trong cửa hàng
        để tiêu vừa hết số tiền. Em hãy đếm xem Bình có bao nhiêu cách chọn.

        Đầu vào:
        - Dòng 1: hai số nguyên n (số món quà) và s.
        - Dòng 2: n số nguyên a1, a2, ..., an là giá của từng món (nghìn đồng).

        Đầu ra:
        - Số cặp chỉ số (i, j) với i < j sao cho ai + aj = s. Hai món khác nhau nhưng
          cùng giá vẫn được tính là cách chọn khác nhau.

        Giới hạn:
        - 1 ≤ n ≤ 1000; 1 ≤ ai ≤ 1000; 2 ≤ s ≤ 2000.

        Gợi ý:
        - Có thể thử mọi cặp, hoặc sắp xếp rồi dùng hai "ngón tay" đi từ hai đầu dãy vào giữa.
    """,
    tests=lambda r: [
        "6 10\n3 7 5 5 2 8\n",
        "1 10\n5\n",
        "5 10\n5 5 5 5 5\n",
        "4 100\n1 2 3 4\n",
        _arr(_rand_list(r, 200, 1, 100), head="200 %d" % r.randint(50, 150)),
        _arr(_rand_list(r, 1000, 1, 50), head="1000 51"),
        _arr(_rand_list(r, 1000, 1, 1000), head="1000 %d" % r.randint(500, 1500)),
    ],
)
def dem_cap_qua(inp):
    d = inp.split()
    n, s = int(d[0]), int(d[1])
    a = [int(v) for v in d[2:2 + n]]
    seen = {}
    cnt = 0
    for v in a:
        cnt += seen.get(s - v, 0)
        seen[v] = seen.get(v, 0) + 1
    return f"{cnt}\n"


@problem(
    title="Đếm lượt đổi chỗ của sắp xếp nổi bọt",
    difficulty=3,
    statement="""
        Robot Bi sắp xếp một dãy số tăng dần bằng cách "nổi bọt", và Bi muốn biết mình
        đã đổi chỗ bao nhiêu lần. Cách làm của Bi như sau:
        - Bi đi từ đầu dãy đến cuối dãy, xét lần lượt từng cặp hai số đứng cạnh nhau
          (vị trí 1 và 2, rồi 2 và 3, ..., rồi n-1 và n). Nếu số bên trái lớn hơn số
          bên phải thì Bi đổi chỗ hai số đó và đếm thêm 1 lần đổi chỗ.
        - Bi lặp lại lượt đi như trên cho đến khi có một lượt đi không đổi chỗ lần nào.

        Đầu vào:
        - Dòng 1: số nguyên n.
        - Dòng 2: n số nguyên, cách nhau một dấu cách.

        Đầu ra:
        - Tổng số lần Bi đã đổi chỗ.

        Giới hạn:
        - 1 ≤ n ≤ 100; 1 ≤ mỗi số ≤ 1000.
    """,
    tests=lambda r: [
        "5\n5 1 4 2 8\n",
        "1\n7\n",
        _arr([1, 2, 3, 4, 5, 6]),
        _arr(list(range(100, 0, -1))),
        _arr([3] * 5),
        _arr(_rand_list(r, 20, 1, 1000)),
        _arr(_rand_list(r, 50, 1, 5)),
        _arr(_rand_list(r, 100, 1, 1000)),
    ],
)
def dem_doi_cho_noi_bot(inp):
    d = inp.split()
    n = int(d[0])
    a = [int(v) for v in d[1:1 + n]]
    total = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                total += 1
                swapped = True
    return f"{total}\n"


@problem(
    title="Bảng xếp hạng cuộc thi lập trình nhí",
    difficulty=3,
    statement="""
        Cuộc thi "Lập trình nhí" đã kết thúc. Ban tổ chức cần in bảng xếp hạng: bạn nào
        điểm cao hơn thì đứng trên; hai bạn bằng điểm thì bạn có tên đứng trước trong
        từ điển sẽ đứng trên.

        Đầu vào:
        - Dòng 1: số nguyên n là số thí sinh.
        - n dòng tiếp theo, mỗi dòng gồm tên và điểm của một thí sinh, cách nhau một dấu cách.
          Tên gồm chữ cái tiếng Anh viết thường (a-z), các tên đôi một khác nhau.

        Đầu ra:
        - n dòng, mỗi dòng gồm tên và điểm (cách nhau một dấu cách), xếp theo điểm giảm
          dần; nếu bằng điểm thì xếp theo tên tăng dần theo thứ tự từ điển (so từng chữ
          cái a, b, ..., z; tên là phần đầu của tên khác thì đứng trước).

        Giới hạn:
        - 1 ≤ n ≤ 200; tên dài 1 đến 10 chữ cái; 0 ≤ điểm ≤ 100.
    """,
    tests=lambda r: [
        "5\nan 85\nbinh 92\nchi 85\ndung 70\nem 92\n",
        "1\nkhoa 100\n",
        "4\ndung 50\nchi 50\nbinh 50\nan 50\n",
        "3\nan 0\nbinh 50\nchi 100\n",
        "4\nanh 70\nan 70\nab 70\nb 80\n",
        (lambda names: f"{len(names)}\n" + "".join(f"{w} {r.randint(0, 10)}\n" for w in names))(
            _distinct_words(r, 50, 1, 6)),
        (lambda names: f"{len(names)}\n" + "".join(f"{w} {r.randint(0, 100)}\n" for w in names))(
            _distinct_words(r, 200, 1, 10)),
    ],
)
def bang_xep_hang(inp):
    lines = inp.split("\n")
    n = int(lines[0])
    rows = []
    for i in range(1, n + 1):
        name, score = lines[i].split()
        rows.append((name, int(score)))
    rows.sort(key=lambda t: (-t[1], t[0]))
    return "".join(f"{name} {score}\n" for name, score in rows)


@problem(
    title="Số xuất hiện nhiều thì được đứng trước",
    difficulty=3,
    statement="""
        Trong trò chơi "Ai đông hơn", các con số rủ nhau xếp hàng: số nào xuất hiện nhiều
        lần hơn thì cả nhóm số đó được đứng lên trước. Em hãy in hàng số sau khi xếp.

        Đầu vào:
        - Dòng 1: số nguyên n.
        - Dòng 2: n số nguyên, cách nhau một dấu cách.

        Đầu ra:
        - Một dòng gồm n số sau khi xếp lại: các bản sao của cùng một số đứng liền nhau;
          nhóm của số xuất hiện nhiều lần hơn đứng trước; nếu hai số xuất hiện số lần
          bằng nhau thì số nhỏ hơn đứng trước. Các số cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n ≤ 1000; 1 ≤ mỗi số ≤ 1000.
    """,
    tests=lambda r: [
        "9\n2 3 1 3 2 4 3 1 5\n",
        "1\n8\n",
        _arr([5, 4, 3, 2, 1]),
        _arr([7] * 6),
        "6\n9 9 1 2 2 9\n",
        _arr(_rand_list(r, 100, 1, 100)),
        _arr(_rand_list(r, 1000, 1, 30)),
    ],
)
def xep_theo_tan_so(inp):
    d = inp.split()
    n = int(d[0])
    a = [int(v) for v in d[1:1 + n]]
    cnt = {}
    for v in a:
        cnt[v] = cnt.get(v, 0) + 1
    keys = sorted(cnt, key=lambda v: (-cnt[v], v))
    out = []
    for v in keys:
        out += [v] * cnt[v]
    return " ".join(str(x) for x in out) + "\n"


@problem(
    title="Huy chương chia đều khi bằng điểm",
    difficulty=3,
    statement="""
        Cô giáo xếp hạng cả lớp sau bài kiểm tra theo luật vui vẻ: điểm cao nhất được
        hạng 1; các bạn bằng điểm nhau thì cùng hạng; mức điểm thấp hơn kế tiếp được hạng
        tiếp theo (không bỏ qua hạng nào). Ví dụ hai bạn cùng hạng 1 thì mức điểm kế tiếp
        vẫn được hạng 2.

        Đầu vào:
        - Dòng 1: số nguyên n là số học sinh.
        - Dòng 2: n số nguyên là điểm của học sinh thứ 1, 2, ..., n.

        Đầu ra:
        - Một dòng gồm n số: hạng của học sinh thứ 1, 2, ..., n (giữ đúng thứ tự đầu vào),
          cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n ≤ 1000; 0 ≤ điểm ≤ 100.

        Gợi ý:
        - Hạng của một bạn = 1 + số mức điểm khác nhau lớn hơn điểm của bạn đó.
    """,
    tests=lambda r: [
        "6\n80 95 80 70 95 60\n",
        "1\n50\n",
        _arr([77] * 4),
        _arr([10, 20, 30, 40, 50]),
        _arr([100, 90, 90, 80, 80, 80]),
        _arr(_rand_list(r, 30, 0, 10)),
        _arr(_rand_list(r, 1000, 0, 100)),
    ],
)
def xep_hang_dong_hang(inp):
    d = inp.split()
    n = int(d[0])
    a = [int(v) for v in d[1:1 + n]]
    levels = sorted(set(a), reverse=True)
    rank = {}
    for i, v in enumerate(levels):
        rank[v] = i + 1
    return " ".join(str(rank[v]) for v in a) + "\n"


@problem(
    title="Lịch sinh nhật cả lớp theo thứ tự",
    difficulty=3,
    statement="""
        Lớp trưởng muốn làm tấm lịch ghi ngày sinh của các bạn, xếp từ ngày sớm nhất đến
        ngày muộn nhất để không quên chúc mừng ai.

        Đầu vào:
        - Dòng 1: số nguyên n là số bạn.
        - n dòng tiếp theo, mỗi dòng ba số nguyên d m y là ngày, tháng, năm sinh
          (viết không có số 0 ở đầu, ngày luôn hợp lệ).

        Đầu ra:
        - n dòng, mỗi dòng ba số d m y (viết giống đầu vào), xếp theo thời gian từ sớm
          đến muộn: năm nhỏ hơn thì sớm hơn; cùng năm thì tháng nhỏ hơn sớm hơn; cùng
          năm và tháng thì ngày nhỏ hơn sớm hơn. Ngày trùng nhau thì in đủ số lần.

        Giới hạn:
        - 1 ≤ n ≤ 200; 2008 ≤ y ≤ 2018.
    """,
    tests=lambda r: [
        "4\n15 8 2014\n3 12 2013\n1 8 2014\n20 1 2015\n",
        "1\n29 2 2012\n",
        "5\n5 3 2015\n5 1 2015\n5 2 2015\n5 12 2015\n5 11 2015\n",
        "4\n31 12 2010\n1 1 2011\n30 12 2010\n2 1 2011\n",
        "3\n7 7 2016\n7 7 2016\n6 7 2016\n",
        "%d\n%s" % (50, "".join(f"{r.randint(1, 28)} {r.randint(1, 12)} {r.randint(2010, 2012)}\n" for _ in range(50))),
        "%d\n%s" % (200, "".join(f"{r.randint(1, 28)} {r.randint(1, 12)} {r.randint(2008, 2018)}\n" for _ in range(200))),
    ],
)
def lich_sinh_nhat(inp):
    d = inp.split()
    n = int(d[0])
    dates = []
    for i in range(n):
        day, month, year = int(d[1 + 3 * i]), int(d[2 + 3 * i]), int(d[3 + 3 * i])
        dates.append((year, month, day))
    dates.sort()
    return "".join(f"{day} {month} {year}\n" for year, month, day in dates)


@problem(
    title="Xem từng bước của sắp xếp chọn",
    difficulty=3,
    statement="""
        Robot Bi muốn cho các bạn xem tận mắt cách "sắp xếp chọn" làm việc. Với dãy
        a1, a2, ..., an, Bi làm n - 1 lượt; ở lượt thứ i (i = 1, 2, ..., n - 1):
        - Bi tìm số nhỏ nhất trong các vị trí từ i đến n. Nếu có nhiều số nhỏ nhất bằng
          nhau, Bi chọn số ở vị trí bên trái nhất.
        - Bi đổi chỗ số vừa tìm được với số ở vị trí i (nếu đó chính là vị trí i thì dãy
          giữ nguyên).
        - Bi in toàn bộ dãy sau lượt đó.

        Đầu vào:
        - Dòng 1: số nguyên n.
        - Dòng 2: n số nguyên, cách nhau một dấu cách.

        Đầu ra:
        - n - 1 dòng, dòng thứ i là dãy số sau lượt thứ i, các số cách nhau một dấu cách.

        Giới hạn:
        - 2 ≤ n ≤ 10; 1 ≤ mỗi số ≤ 100.
    """,
    tests=lambda r: [
        "4\n5 2 8 1\n",
        "2\n1 2\n",
        "2\n2 1\n",
        "3\n3 1 1\n",
        _arr([1, 2, 3, 4, 5]),
        _arr([6, 5, 4, 3, 2, 1]),
        _arr(_rand_list(r, 8, 1, 5)),
        _arr(_rand_list(r, 10, 1, 100)),
    ],
)
def tung_buoc_sap_xep_chon(inp):
    d = inp.split()
    n = int(d[0])
    a = [int(v) for v in d[1:1 + n]]
    lines = []
    for i in range(n - 1):
        j = i
        for k in range(i + 1, n):
            if a[k] < a[j]:
                j = k
        a[i], a[j] = a[j], a[i]
        lines.append(" ".join(str(x) for x in a))
    return "\n".join(lines) + "\n"


@problem(
    title="Dãy thẻ số liên tiếp dài nhất",
    difficulty=3,
    statement="""
        An có n tấm thẻ, mỗi tấm ghi một số (có thể trùng nhau). An muốn chọn ra nhiều thẻ
        nhất sao cho các số trên thẻ đã chọn là các số nguyên liên tiếp k, k + 1, k + 2, ...
        và mỗi số chỉ dùng một thẻ. Hỏi An chọn được nhiều nhất bao nhiêu thẻ?

        Đầu vào:
        - Dòng 1: số nguyên n.
        - Dòng 2: n số nguyên ghi trên các tấm thẻ, cách nhau một dấu cách.

        Đầu ra:
        - Số thẻ nhiều nhất An có thể chọn (độ dài dãy số liên tiếp dài nhất).

        Giới hạn:
        - 1 ≤ n ≤ 1000; 1 ≤ số trên thẻ ≤ 100000.

        Gợi ý:
        - Sắp xếp các số, bỏ các số trùng, rồi đếm đoạn dài nhất mà số sau hơn số trước đúng 1.
    """,
    tests=lambda r: [
        "8\n5 2 99 3 4 4 100 10\n",
        "1\n7\n",
        _arr([3] * 5),
        _arr([10, 20, 30, 40, 50]),
        _arr(_shuffled(r, range(1, 1001))),
        _arr(_rand_list(r, 100, 1, 150)),
        _arr(_rand_list(r, 1000, 1, 2000)),
        _arr(_shuffled(r, list(range(500, 800)) + list(range(900, 1200)) + _rand_list(r, 100, 500, 1200))),
    ],
)
def day_lien_tiep_dai_nhat(inp):
    d = inp.split()
    n = int(d[0])
    a = sorted(set(int(v) for v in d[1:1 + n]))
    best = cur = 1
    for i in range(1, len(a)):
        if a[i] == a[i - 1] + 1:
            cur += 1
        else:
            cur = 1
        best = max(best, cur)
    return f"{best}\n"
