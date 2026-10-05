"""Chu de 7: Mang (danh sach) - bai K181..K210."""

from kidslib import problem

TOPIC = "mang"


# ------------------------------------------------ tien ich sinh test (khong xuat ra bai nop)

def _line(a):
    return " ".join(map(str, a))


def _arr(a):
    """Dong 1: n, dong 2: n phan tu cach nhau mot dau cach."""
    return f"{len(a)}\n{_line(a)}\n"


def _rnd(r, n, lo, hi):
    return [r.randint(lo, hi) for _ in range(n)]


# =================================================================== DỄ

@problem(
    title="Đoàn tàu đồ chơi chạy lùi",
    difficulty=1,
    statement="""
        Bạn An có một đoàn tàu đồ chơi gồm n toa, trên toa thứ i có ghi số a[i].
        Khi tàu chạy lùi, toa cuối cùng lại đi đầu tiên! Em hãy giúp An đọc các con số
        theo thứ tự từ toa cuối về toa đầu nhé.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số toa tàu.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - In ra trên một dòng các số a[n], a[n-1], ..., a[1], cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 0 ≤ a[i] ≤ 10^6

        Gợi ý:
        - Lưu cả dãy vào một mảng, rồi dùng vòng lặp đi từ vị trí n lùi về vị trí 1.
    """,
    tests=lambda r: [
        "5\n3 8 1 9 4\n",
        "1\n42\n",
        "2\n0 1000000\n",
        _arr([7] * 6),
        _arr(list(range(1, 21))),
        _arr(_rnd(r, 10, 0, 100)),
        _arr(_rnd(r, 100, 0, 10**6)),
        _arr(_rnd(r, 1000, 0, 10**6)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    return " ".join(str(a[i]) for i in range(n - 1, -1, -1)) + "\n"


@problem(
    title="Tổng số kẹo trong các hũ của cô Lan",
    difficulty=1,
    statement="""
        Cô Lan có một cửa hàng kẹo với n chiếc hũ xếp trên kệ, hũ thứ i đựng a[i] viên kẹo.
        Cuối ngày cô muốn biết cả cửa hàng có tất cả bao nhiêu viên kẹo. Em hãy tính giúp cô nhé!

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số hũ kẹo.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên duy nhất — tổng số viên kẹo trong tất cả các hũ.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 0 ≤ a[i] ≤ 10^6

        Gợi ý:
        - Dùng một biến tong bắt đầu bằng 0, rồi lần lượt cộng từng a[i] vào tong.
    """,
    tests=lambda r: [
        "4\n12 5 30 8\n",
        "1\n0\n",
        "1\n1000000\n",
        _arr([10**6] * 1000),
        _arr(_rnd(r, 10, 0, 50)),
        _arr(_rnd(r, 500, 0, 10**6)),
        _arr(_rnd(r, 1000, 0, 10**6)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    tong = 0
    for i in range(n):
        tong += int(data[1 + i])
    return f"{tong}\n"


@problem(
    title="Bóng bay mang số chẵn ở hội chợ",
    difficulty=1,
    statement="""
        Ở hội chợ có n quả bóng bay, quả thứ i ghi số a[i]. Bạn Bình chỉ thích những quả bóng
        mang số chẵn (số chia hết cho 2, kể cả số 0). Em hãy đếm xem có bao nhiêu quả bóng như vậy.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số quả bóng bay.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên — số quả bóng mang số chẵn.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 0 ≤ a[i] ≤ 10^6

        Gợi ý:
        - Số x là số chẵn khi x % 2 == 0.
    """,
    tests=lambda r: [
        "6\n3 8 0 15 22 7\n",
        "1\n0\n",
        "1\n7\n",
        _arr([1, 3, 5, 7, 9, 11]),
        _arr([2, 4, 6, 8, 1000000]),
        _arr(_rnd(r, 20, 0, 100)),
        _arr(_rnd(r, 1000, 0, 10**6)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    dem = 0
    for i in range(n):
        if int(data[1 + i]) % 2 == 0:
            dem += 1
    return f"{dem}\n"


@problem(
    title="Bạn cao nhất trong hàng chào cờ",
    difficulty=1,
    statement="""
        Trong giờ chào cờ, n bạn đứng thành một hàng dọc. Cô giáo đo chiều cao của từng bạn
        (đơn vị xăng-ti-mét) để chọn bạn cao nhất cầm cờ. Các vị trí trong hàng được đánh số
        từ 1 đến n, tính từ đầu hàng.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số bạn trong hàng.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách;
          a[i] là chiều cao của bạn đứng ở vị trí i.

        Đầu ra:
        - In ra hai số nguyên cách nhau một dấu cách: chiều cao lớn nhất và vị trí của bạn
          có chiều cao đó.
        - Nếu có nhiều bạn cùng cao nhất, in vị trí nhỏ nhất (bạn đứng gần đầu hàng nhất).

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 100 ≤ a[i] ≤ 200
    """,
    tests=lambda r: [
        "6\n135 142 128 150 150 139\n",
        "1\n120\n",
        _arr([140] * 5),
        _arr([110, 120, 130, 140, 150, 160, 170]),
        _arr([200, 150, 200, 180]),
        _arr(_rnd(r, 30, 100, 200)),
        _arr(_rnd(r, 1000, 100, 200)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    lon_nhat = a[0]
    vi_tri = 1
    for i in range(1, n):
        if a[i] > lon_nhat:
            lon_nhat = a[i]
            vi_tri = i + 1
    return f"{lon_nhat} {vi_tri}\n"


@problem(
    title="Đêm lạnh nhất ở Sa Pa",
    difficulty=1,
    statement="""
        Trạm khí tượng ở Sa Pa ghi lại nhiệt độ lúc nửa đêm của n đêm mùa đông liên tiếp.
        Trời rất lạnh nên có những đêm nhiệt độ xuống dưới 0 độ (là số âm).
        Em hãy tìm nhiệt độ thấp nhất trong các đêm đó.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số đêm.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách;
          a[i] là nhiệt độ của đêm thứ i.

        Đầu ra:
        - Một số nguyên — nhiệt độ thấp nhất.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - -50 ≤ a[i] ≤ 50
    """,
    tests=lambda r: [
        "5\n3 -2 5 0 -1\n",
        "1\n25\n",
        _arr([5, 8, 12, 30, 7]),
        _arr([-3, -15, -7, -50, -1]),
        _arr([0, 0, 0, 0]),
        _arr(_rnd(r, 30, -20, 50)),
        _arr(_rnd(r, 1000, -50, 50)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    nho_nhat = a[0]
    for i in range(1, n):
        if a[i] < nho_nhat:
            nho_nhat = a[i]
    return f"{nho_nhat}\n"


def _t_ca(r):
    a1 = _rnd(r, 50, 1, 10)
    a2 = _rnd(r, 1000, 1, 20)
    a3 = _rnd(r, 1000, 1, 1000)
    return [
        "7\n5 3 5 2 5 8 3\n5\n",
        "1\n4\n4\n",
        "1\n4\n9\n",
        _arr([6] * 10) + "6\n",
        _arr([1, 2, 3, 4, 5]) + "10\n",
        _arr(a1) + f"{r.randint(1, 10)}\n",
        _arr(a2) + "7\n",
        _arr(a3) + f"{a3[r.randrange(1000)]}\n",
    ]


@problem(
    title="Mèo Mướp đếm cá nặng đúng x gam",
    difficulty=1,
    statement="""
        Mèo Mướp vừa đi chợ về với n con cá, con thứ i nặng a[i] gam. Hôm nay Mướp chỉ muốn ăn
        những con cá nặng đúng x gam. Em hãy đếm giúp Mướp xem có bao nhiêu con cá như thế.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số con cá.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.
        - Dòng thứ ba chứa số nguyên x.

        Đầu ra:
        - Một số nguyên — số con cá nặng đúng x gam (in 0 nếu không có con nào).

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 1 ≤ a[i] ≤ 1000, 1 ≤ x ≤ 1000
    """,
    tests=_t_ca,
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(v) for v in data[1:1 + n]]
    x = int(data[1 + n])
    dem = 0
    for i in range(n):
        if a[i] == x:
            dem += 1
    return f"{dem}\n"


def _t_hop_qua(r):
    a1 = _rnd(r, 1000, 0, 10**6)
    a2 = _rnd(r, 200, 0, 50)
    return [
        "6\n4 7 2 7 9 1\n7\n",
        "1\n5\n5\n",
        "1\n5\n3\n",
        _arr([3, 1, 4, 1, 5, 9, 2, 6]) + "8\n",
        _arr([2, 7, 1, 8, 2, 8]) + "8\n",
        _arr([5] * 999 + [9]) + "9\n",
        _arr(a1) + f"{a1[r.randrange(500, 1000)]}\n",
        _arr(a2) + f"{r.randint(0, 50)}\n",
    ]


@problem(
    title="Tìm hộp quà đầu tiên có x viên kẹo",
    difficulty=1,
    statement="""
        Ông già Noel xếp n hộp quà thành một hàng, đánh số từ 1 đến n từ trái sang phải.
        Hộp thứ i có a[i] viên kẹo. Bạn Chi muốn mở hộp đầu tiên (gần bên trái nhất)
        có đúng x viên kẹo.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số hộp quà.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.
        - Dòng thứ ba chứa số nguyên x.

        Đầu ra:
        - Một số nguyên — vị trí i nhỏ nhất mà a[i] = x.
        - Nếu không có hộp nào có đúng x viên kẹo, in ra -1.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 0 ≤ a[i] ≤ 10^6, 0 ≤ x ≤ 10^6
    """,
    tests=_t_hop_qua,
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(v) for v in data[1:1 + n]]
    x = int(data[1 + n])
    for i in range(n):
        if a[i] == x:
            return f"{i + 1}\n"
    return "-1\n"


@problem(
    title="Ếch con nhặt sao trên các lá súng lẻ",
    difficulty=1,
    statement="""
        Ếch con đứng trước một dãy n chiếc lá súng, đánh số từ 1 đến n. Trên lá thứ i có a[i]
        ngôi sao lấp lánh. Ếch chỉ đáp xuống các lá ở vị trí lẻ: lá 1, lá 3, lá 5, ...
        và nhặt hết sao trên những lá đó. Hỏi ếch nhặt được tất cả bao nhiêu ngôi sao?

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số lá súng.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên — tổng a[1] + a[3] + a[5] + ... (lấy mọi vị trí lẻ không vượt quá n).

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 0 ≤ a[i] ≤ 10^6

        Gợi ý:
        - Cho biến vị trí chạy 1, 3, 5, ... bằng cách mỗi lần tăng thêm 2.
        - Nếu mảng của em đánh chỉ số từ 0 thì lá ở vị trí 1 nằm ở chỉ số 0.
    """,
    tests=lambda r: [
        "5\n2 9 4 1 6\n",
        "1\n7\n",
        "2\n0 100\n",
        _arr([0, 5, 0, 5, 0, 5]),
        _arr([10**6] * 1000),
        _arr(_rnd(r, 11, 0, 20)),
        _arr(_rnd(r, 999, 0, 10**6)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    tong = 0
    for i in range(0, n, 2):
        tong += a[i]
    return f"{tong}\n"


@problem(
    title="Robot Bi xoá điểm âm",
    difficulty=1,
    statement="""
        Robot Bi chơi một trò chơi điện tử gồm n lượt. Sau mỗi lượt Bi được một số điểm,
        nhưng có lượt bị trừ điểm (điểm âm). Bi quyết định "xoá buồn": lượt nào có điểm âm
        thì coi như được 0 điểm. Em hãy in ra dãy điểm mới của Bi.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số lượt chơi.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - In ra trên một dòng n số, cách nhau một dấu cách: số thứ i bằng 0 nếu a[i] < 0,
          ngược lại bằng a[i].

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - -1000 ≤ a[i] ≤ 1000
    """,
    tests=lambda r: [
        "6\n5 -3 0 7 -1 2\n",
        "1\n-5\n",
        "1\n8\n",
        _arr([-1, -2, -3, -4]),
        _arr([1, 2, 3, 0, 4]),
        _arr(_rnd(r, 20, -10, 10)),
        _arr(_rnd(r, 1000, -1000, 1000)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    for i in range(n):
        if a[i] < 0:
            a[i] = 0
    return " ".join(str(v) for v in a) + "\n"


@problem(
    title="Cây cao nhất hơn cây thấp nhất bao nhiêu?",
    difficulty=1,
    statement="""
        Lớp em trồng n cây non trong vườn trường. Bạn Dũng đo chiều cao từng cây
        (đơn vị mi-li-mét). Hỏi cây cao nhất cao hơn cây thấp nhất bao nhiêu mi-li-mét?

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số cây.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách;
          a[i] là chiều cao của cây thứ i.

        Đầu ra:
        - Một số nguyên — chiều cao lớn nhất trừ đi chiều cao nhỏ nhất.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 1 ≤ a[i] ≤ 10^6
    """,
    tests=lambda r: [
        "5\n120 85 230 150 99\n",
        "1\n500\n",
        _arr([77] * 8),
        _arr([1, 1000000]),
        _arr([1000000, 3, 999999, 2]),
        _arr(_rnd(r, 20, 1, 1000)),
        _arr(_rnd(r, 1000, 1, 10**6)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    lon = a[0]
    nho = a[0]
    for i in range(1, n):
        if a[i] > lon:
            lon = a[i]
        if a[i] < nho:
            nho = a[i]
    return f"{lon - nho}\n"


# =================================================================== VỪA

@problem(
    title="Trung bình bàn thắng của đội bóng nhí",
    difficulty=2,
    statement="""
        Đội bóng nhí của phường có n cầu thủ. Trong mùa giải, bạn thứ i ghi được a[i] bàn thắng.
        Huấn luyện viên muốn biết trung bình mỗi bạn ghi được bao nhiêu bàn, nhưng chỉ cần
        phần nguyên thôi.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số cầu thủ.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên — phần nguyên của phép chia (a[1] + a[2] + ... + a[n]) cho n.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 0 ≤ a[i] ≤ 10^6

        Gợi ý:
        - Tính tổng S trước, rồi lấy S chia lấy phần nguyên cho n
          (C++/Java: S / n với hai số nguyên; Python: S // n).
    """,
    tests=lambda r: [
        "4\n3 5 2 7\n",
        "1\n9\n",
        _arr([0] * 5),
        "2\n1 2\n",
        _arr([10**6] * 1000),
        _arr(_rnd(r, 30, 0, 20)),
        _arr(_rnd(r, 1000, 0, 10**6)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    tong = 0
    for i in range(n):
        tong += int(data[1 + i])
    return f"{tong // n}\n"


@problem(
    title="Hoa hướng dương cao hơn mức trung bình",
    difficulty=2,
    statement="""
        Bạn Hoa trồng n cây hướng dương, cây thứ i cao a[i] xăng-ti-mét. Hoa muốn đếm xem
        có bao nhiêu cây cao hơn chiều cao trung bình của cả vườn. Cây cao đúng bằng
        mức trung bình thì không được tính.

        Chiều cao trung bình bằng S chia cho n, với S = a[1] + a[2] + ... + a[n]
        (kết quả phép chia này có thể không phải số nguyên).

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số cây.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên — số cây có chiều cao lớn hơn hẳn chiều cao trung bình.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 1 ≤ a[i] ≤ 10^6

        Gợi ý:
        - Để không phải dùng số thập phân, hãy so sánh a[i] × n với S:
          cây thứ i cao hơn trung bình khi và chỉ khi a[i] × n > S.
    """,
    tests=lambda r: [
        "5\n10 20 30 40 50\n",
        "1\n100\n",
        _arr([7] * 6),
        "3\n1 2 2\n",
        _arr([1, 1, 1, 1, 100]),
        _arr(_rnd(r, 25, 1, 100)),
        _arr(_rnd(r, 1000, 1, 10**6)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    tong = 0
    for v in a:
        tong += v
    dem = 0
    for v in a:
        if v * n > tong:
            dem += 1
    return f"{dem}\n"


@problem(
    title="Chú cún Bơ tăng bao nhiêu gam mỗi ngày?",
    difficulty=2,
    statement="""
        Bạn Vy cân chú cún Bơ vào mỗi buổi sáng trong n ngày liên tiếp, ngày thứ i Bơ nặng a[i] gam.
        Em hãy cho biết từ mỗi ngày sang ngày hôm sau, cân nặng của Bơ thay đổi bao nhiêu gam.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số ngày.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - Một dòng gồm n - 1 số nguyên, cách nhau một dấu cách: số thứ i là a[i+1] - a[i]
          (số âm nghĩa là hôm sau Bơ nhẹ đi).

        Giới hạn:
        - 2 ≤ n ≤ 1000
        - 500 ≤ a[i] ≤ 20000

        Gợi ý:
        - Đọc cả dãy vào mảng trước, rồi mới tính hiệu của từng cặp ngày liền nhau.
    """,
    tests=lambda r: [
        "5\n1200 1250 1250 1230 1300\n",
        "2\n800 900\n",
        "2\n900 800\n",
        _arr([1500] * 6),
        _arr(list(range(1000, 2001, 100))),
        _arr(_rnd(r, 30, 500, 20000)),
        _arr(_rnd(r, 1000, 500, 20000)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    hieu = [str(a[i + 1] - a[i]) for i in range(n - 1)]
    return " ".join(hieu) + "\n"


@problem(
    title="Cầu thang không bao giờ đi xuống",
    difficulty=2,
    statement="""
        Robot Bi leo một cầu thang có n bậc, bậc thứ i có độ cao a[i]. Bi sẽ rất vui nếu
        suốt đường đi không bao giờ phải bước xuống, tức là mỗi bậc cao bằng hoặc cao hơn
        bậc ngay trước nó.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số bậc thang.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - In YES nếu a[1] ≤ a[2] ≤ ... ≤ a[n], ngược lại in NO.
        - Cầu thang chỉ có 1 bậc (n = 1) thì in YES.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 0 ≤ a[i] ≤ 10^6
    """,
    tests=lambda r: [
        "5\n1 3 3 7 9\n",
        "1\n5\n",
        _arr([4] * 7),
        _arr([1, 2, 3, 5, 4]),
        _arr([9, 1, 2, 3]),
        _arr(sorted(_rnd(r, 1000, 0, 10**6))),
        _arr([2 * i if i != 300 else 597 for i in range(500)]),
        _arr(_rnd(r, 50, 0, 100)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    for i in range(1, n):
        if a[i] < a[i - 1]:
            return "NO\n"
    return "YES\n"


def _t_guong(r):
    h1 = _rnd(r, 500, 0, 10**6)
    h2 = _rnd(r, 300, 0, 10**6)
    h3 = _rnd(r, 10, 0, 9)
    gan_dung = h3 + h3[::-1]
    gan_dung[3] += 1
    return [
        "6\n4 7 1 1 7 4\n",
        "1\n9\n",
        "2\n3 5\n",
        _arr([5, 0, 8, 0, 5]),
        _arr(h1 + h1[::-1]),
        _arr(h2 + [r.randint(0, 10**6)] + h2[::-1]),
        _arr(gan_dung),
        _arr(_rnd(r, 100, 0, 10)),
    ]


@problem(
    title="Dãy số soi gương",
    difficulty=2,
    statement="""
        Một dãy số được gọi là "dãy soi gương" nếu đọc từ trái sang phải hay từ phải sang trái
        đều giống hệt nhau. Chẳng hạn dãy 1 2 3 2 1 là dãy soi gương, còn dãy 1 2 3 1 thì không.
        Em hãy kiểm tra xem dãy số của bạn Lan có phải dãy soi gương hay không.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số phần tử của dãy.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - In YES nếu a[i] = a[n+1-i] với mọi i từ 1 đến n, ngược lại in NO.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 0 ≤ a[i] ≤ 10^6
    """,
    tests=_t_guong,
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    for i in range(n // 2):
        if a[i] != a[n - 1 - i]:
            return "NO\n"
    return "YES\n"


@problem(
    title="Ghế trống trong rạp múa rối",
    difficulty=2,
    statement="""
        Rạp múa rối nước có m ghế, đánh số từ 1 đến m. Hôm nay cô bán vé đã bán được n vé, mỗi vé
        ghi một số ghế và không có hai vé nào trùng ghế. Em hãy liệt kê các ghế còn trống để cô
        mời những vị khách đến sau.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên m và n, cách nhau một dấu cách.
        - Dòng thứ hai chứa n số nguyên khác nhau là số ghế đã bán, mỗi số từ 1 đến m.

        Đầu ra:
        - Dòng đầu tiên in số k — số ghế còn trống.
        - Nếu k > 0, dòng thứ hai in k số ghế trống theo thứ tự tăng dần, cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n ≤ m ≤ 1000

        Gợi ý:
        - Dùng một mảng đánh dấu da_ban[1..m], ban đầu toàn là "chưa bán". Đọc từng vé thì đánh dấu
          ghế đó, cuối cùng đi qua mảng từ 1 đến m để in các ghế chưa được đánh dấu.
    """,
    tests=lambda r: [
        "8 5\n3 1 8 4 6\n",
        "1 1\n1\n",
        "5 5\n5 4 3 2 1\n",
        "6 1\n4\n",
        "10 3\n1 2 10\n",
        "%d %d\n%s\n" % (40, 25, " ".join(map(str, r.sample(range(1, 41), 25)))),
        "%d %d\n%s\n" % (1000, 600, " ".join(map(str, r.sample(range(1, 1001), 600)))),
    ],
)
def solve(inp):
    data = inp.split()
    m, n = int(data[0]), int(data[1])
    da_ban = [False] * (m + 1)
    for x in data[2:2 + n]:
        da_ban[int(x)] = True
    trong = [str(g) for g in range(1, m + 1) if not da_ban[g]]
    if not trong:
        return "0\n"
    return f"{len(trong)}\n" + " ".join(trong) + "\n"


@problem(
    title="Heo đất tổng dồn từng ngày",
    difficulty=2,
    statement="""
        Bạn Lan nuôi một chú heo đất. Ngày thứ i, Lan bỏ vào heo a[i] nghìn đồng (có ngày quên
        không bỏ thì a[i] = 0). Lúc đầu heo đất rỗng. Lan muốn biết sau mỗi ngày, trong heo
        có tổng cộng bao nhiêu tiền.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số ngày.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - In ra trên một dòng n số, cách nhau một dấu cách: số thứ i là a[1] + a[2] + ... + a[i].

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 0 ≤ a[i] ≤ 10^6

        Gợi ý:
        - Dùng một biến cộng dồn: sau khi cộng thêm a[i] thì ghi lại giá trị của biến đó.
    """,
    tests=lambda r: [
        "5\n2 5 0 3 10\n",
        "1\n0\n",
        "1\n7\n",
        _arr([0, 0, 4, 0, 0]),
        _arr([10**6] * 1000),
        _arr(_rnd(r, 15, 0, 50)),
        _arr(_rnd(r, 500, 0, 10**6)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    tong = 0
    kq = []
    for v in a:
        tong += v
        kq.append(tong)
    return " ".join(str(v) for v in kq) + "\n"


@problem(
    title="Hai toa tàu hàng liền nhau nặng nhất",
    difficulty=2,
    statement="""
        Một đoàn tàu hàng có n toa, đánh số từ 1 đến n, toa thứ i chở a[i] tấn hàng.
        Chú lái tàu muốn tìm hai toa đứng cạnh nhau (toa i và toa i+1) có tổng khối lượng hàng
        lớn nhất để kiểm tra kỹ hơn.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số toa tàu.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - In ra hai số nguyên cách nhau một dấu cách: tổng lớn nhất a[i] + a[i+1] và vị trí i
          của toa đứng trước trong cặp đó.
        - Nếu có nhiều cặp cùng tổng lớn nhất, chọn cặp có i nhỏ nhất.

        Giới hạn:
        - 2 ≤ n ≤ 1000
        - 1 ≤ a[i] ≤ 10^6
    """,
    tests=lambda r: [
        "6\n4 2 9 3 8 6\n",
        "2\n5 7\n",
        _arr([3] * 6),
        _arr([1, 9, 1, 1, 9, 1]),
        _arr([1, 1, 1, 500, 600]),
        _arr(_rnd(r, 30, 1, 20)),
        _arr(_rnd(r, 1000, 1, 10**6)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    tot_nhat = a[0] + a[1]
    vi_tri = 1
    for i in range(1, n - 1):
        if a[i] + a[i + 1] > tot_nhat:
            tot_nhat = a[i] + a[i + 1]
            vi_tri = i + 1
    return f"{tot_nhat} {vi_tri}\n"


@problem(
    title="Đổi chỗ quả táo nặng nhất và nhẹ nhất",
    difficulty=2,
    statement="""
        Trên bàn có n quả táo xếp thành một hàng, đánh số từ 1 đến n, quả thứ i nặng a[i] gam.
        Bạn Tí muốn đổi chỗ quả nặng nhất và quả nhẹ nhất cho nhau.
        - Nếu có nhiều quả cùng nặng nhất, chọn quả có vị trí nhỏ nhất. Quả nhẹ nhất cũng chọn
          giống như vậy.
        - Nếu quả nặng nhất và quả nhẹ nhất là cùng một quả (khi mọi quả nặng bằng nhau)
          thì hàng táo giữ nguyên.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số quả táo.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - In ra trên một dòng n số — khối lượng các quả táo theo thứ tự trong hàng sau khi
          đổi chỗ, cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 1 ≤ a[i] ≤ 1000
    """,
    tests=lambda r: [
        "6\n150 90 200 120 90 200\n",
        "1\n100\n",
        _arr([80] * 5),
        "2\n300 120\n",
        _arr([5, 1, 9, 1, 9, 5]),
        _arr(_rnd(r, 20, 1, 50)),
        _arr(_rnd(r, 1000, 1, 1000)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    vt_lon = 0
    vt_nho = 0
    for i in range(1, n):
        if a[i] > a[vt_lon]:
            vt_lon = i
        if a[i] < a[vt_nho]:
            vt_nho = i
    a[vt_lon], a[vt_nho] = a[vt_nho], a[vt_lon]
    return " ".join(str(v) for v in a) + "\n"


@problem(
    title="Kiểm phiếu bầu lớp trưởng",
    difficulty=2,
    statement="""
        Lớp 4B có m bạn ứng cử lớp trưởng, đánh số từ 1 đến m. Mỗi lá phiếu ghi số của một bạn
        ứng cử. Cô giáo nhờ em đếm xem mỗi bạn ứng cử được bao nhiêu phiếu.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên m và n — số bạn ứng cử và số lá phiếu.
        - Dòng thứ hai chứa n số nguyên, mỗi số từ 1 đến m, là số ghi trên từng lá phiếu.

        Đầu ra:
        - Một dòng gồm m số nguyên, cách nhau một dấu cách: số thứ i là số phiếu của bạn ứng cử
          thứ i (bạn không có phiếu nào thì in 0).

        Giới hạn:
        - 1 ≤ m ≤ 100
        - 1 ≤ n ≤ 1000

        Gợi ý:
        - Dùng mảng dem[1..m] ban đầu toàn số 0; đọc lá phiếu ghi số x thì tăng dem[x] thêm 1.
    """,
    tests=lambda r: [
        "3 7\n1 3 3 2 3 1 3\n",
        "1 4\n1 1 1 1\n",
        "5 2\n5 2\n",
        "4 8\n4 4 3 3 2 2 1 1\n",
        "%d %d\n%s\n" % (10, 50, " ".join(str(r.randint(1, 10)) for _ in range(50))),
        "%d %d\n%s\n" % (100, 1000, " ".join(str(r.randint(1, 100)) for _ in range(1000))),
        "%d %d\n%s\n" % (30, 200, " ".join(str(r.randint(1, 7)) for _ in range(200))),
    ],
)
def solve(inp):
    data = inp.split()
    m, n = int(data[0]), int(data[1])
    dem = [0] * (m + 1)
    for x in data[2:2 + n]:
        dem[int(x)] += 1
    return " ".join(str(dem[i]) for i in range(1, m + 1)) + "\n"


@problem(
    title="Bảng đèn cổng trường xoay trái k lần",
    difficulty=2,
    statement="""
        Bảng đèn điện tử ở cổng trường hiển thị n con số thành một hàng. Mỗi giây, bảng xoay trái
        một lần: số đứng đầu tiên chạy xuống cuối hàng, các số còn lại dịch lên trước một chỗ.
        Chẳng hạn hàng 1 2 3 sau một lần xoay trái trở thành 2 3 1. Hỏi sau k giây bảng đèn
        hiển thị gì?

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và k, cách nhau một dấu cách.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n] — các số trên bảng lúc đầu,
          từ trái sang phải.

        Đầu ra:
        - In ra trên một dòng n số trên bảng sau k lần xoay, từ trái sang phải,
          cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 0 ≤ k ≤ 10^9
        - 0 ≤ a[i] ≤ 10^6

        Gợi ý:
        - Cứ xoay đủ n lần thì hàng số lại trở về như cũ, nên chỉ cần xoay k % n lần.
          Khi đó số đứng đầu hàng là số ở vị trí (k % n) + 1.
    """,
    tests=lambda r: [
        "5 2\n4 8 15 16 23\n",
        "1 1000000000\n7\n",
        "4 0\n1 2 3 4\n",
        "4 4\n1 2 3 4\n",
        "3 7\n10 20 30\n",
        "6 1000000000\n1 2 3 4 5 6\n",
        f"10 {r.randint(11, 30)}\n{_line(_rnd(r, 10, 0, 100))}\n",
        f"1000 {r.randint(0, 10**9)}\n{_line(_rnd(r, 1000, 0, 10**6))}\n",
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    k = int(data[1])
    a = [int(x) for x in data[2:2 + n]]
    k = k % n
    kq = []
    for i in range(n):
        kq.append(a[(i + k) % n])
    return " ".join(str(v) for v in kq) + "\n"


def _hai_hang(a, b):
    return f"{len(a)}\n{_line(a)}\n{len(b)}\n{_line(b)}\n"


@problem(
    title="Hai hàng xen kẽ vào lớp 3A",
    difficulty=2,
    statement="""
        Lớp 3A xếp hai hàng trước cửa lớp: hàng thứ nhất có n bạn, hàng thứ hai có m bạn, mỗi bạn
        đeo một thẻ số. Cô giáo cho các bạn vào lớp xen kẽ: bạn đầu hàng thứ nhất, rồi bạn đầu hàng
        thứ hai, rồi bạn tiếp theo của hàng thứ nhất, rồi bạn tiếp theo của hàng thứ hai, ...
        Khi một hàng đã vào hết, các bạn còn lại của hàng kia lần lượt vào theo thứ tự.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n] — thẻ số của hàng thứ nhất,
          từ đầu hàng đến cuối hàng.
        - Dòng thứ ba chứa số nguyên m.
        - Dòng thứ tư chứa m số nguyên b[1], b[2], ..., b[m] — thẻ số của hàng thứ hai.

        Đầu ra:
        - In ra trên một dòng n + m thẻ số theo thứ tự các bạn vào lớp, cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n ≤ 1000, 1 ≤ m ≤ 1000
        - 1 ≤ a[i] ≤ 1000, 1 ≤ b[j] ≤ 1000
    """,
    tests=lambda r: [
        "3\n1 3 5\n5\n2 4 6 8 10\n",
        "1\n7\n1\n9\n",
        "4\n1 1 1 1\n1\n2\n",
        "2\n5 6\n2\n7 8\n",
        _hai_hang(_rnd(r, 10, 1, 100), _rnd(r, 4, 1, 100)),
        _hai_hang(_rnd(r, 300, 1, 1000), _rnd(r, 700, 1, 1000)),
        _hai_hang(_rnd(r, 1000, 1, 1000), _rnd(r, 1000, 1, 1000)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    m = int(data[1 + n])
    b = [int(x) for x in data[2 + n:2 + n + m]]
    kq = []
    i = 0
    while i < n or i < m:
        if i < n:
            kq.append(a[i])
        if i < m:
            kq.append(b[i])
        i += 1
    return " ".join(str(v) for v in kq) + "\n"


# =================================================================== KHÓ

def _t_cap(r):
    a1 = _rnd(r, 100, 1, 20)
    a2 = _rnd(r, 100, 1, 1000)
    a3 = _rnd(r, 50, 1, 10)
    return [
        "6 10\n3 7 5 5 2 8\n",
        "1 10\n5\n",
        "5 6\n3 3 3 3 3\n",
        "4 100\n1 2 3 4\n",
        f"100 2000\n{_line([1000] * 100)}\n",
        f"100 {r.randint(2, 40)}\n{_line(a1)}\n",
        f"100 {a2[0] + a2[1]}\n{_line(a2)}\n",
        f"50 11\n{_line(a3)}\n",
    ]


@problem(
    title="Ghép đôi thẻ bài có tổng bằng s",
    difficulty=3,
    statement="""
        Bạn An có n tấm thẻ bài xếp thành hàng, đánh số từ 1 đến n, tấm thứ i ghi số a[i].
        An muốn chọn ra hai tấm thẻ khác nhau sao cho tổng hai số trên đó bằng đúng s.
        Hỏi An có bao nhiêu cách chọn? Hai cách chọn là khác nhau nếu cặp vị trí (i, j)
        của chúng khác nhau (luôn lấy i < j).

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và s, cách nhau một dấu cách.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên — số cặp vị trí (i, j) với 1 ≤ i < j ≤ n và a[i] + a[j] = s
          (in 0 nếu không có cặp nào).

        Giới hạn:
        - 1 ≤ n ≤ 100
        - 1 ≤ a[i] ≤ 1000
        - 2 ≤ s ≤ 2000

        Gợi ý:
        - Dùng hai vòng lặp lồng nhau: i chạy từ 1 đến n, j chạy từ i + 1 đến n.
    """,
    tests=_t_cap,
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    s = int(data[1])
    a = [int(x) for x in data[2:2 + n]]
    dem = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] == s:
                dem += 1
    return f"{dem}\n"


@problem(
    title="Dải bóng bay cùng màu dài nhất",
    difficulty=3,
    statement="""
        Dọc hàng rào trường em treo n quả bóng bay thành một hàng, quả thứ i có mã màu a[i].
        Em hãy tìm đoạn dài nhất gồm các quả bóng đứng liền nhau và có cùng một màu.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số quả bóng.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên — số quả bóng trong đoạn dài nhất các quả liền nhau cùng màu.
          Một quả bóng đứng một mình cũng là một đoạn dài 1.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 1 ≤ a[i] ≤ 10

        Gợi ý:
        - Dùng biến dem để đếm độ dài đoạn hiện tại: nếu a[i] = a[i-1] thì tăng dem thêm 1,
          ngược lại đặt dem = 1. Luôn nhớ giá trị dem lớn nhất từng gặp.
    """,
    tests=lambda r: [
        "9\n2 2 5 5 5 1 5 5 3\n",
        "1\n4\n",
        _arr([7] * 1000),
        _arr(list(range(1, 11))),
        _arr([1, 2, 2, 3, 3, 3, 3]),
        _arr(_rnd(r, 50, 1, 3)),
        _arr(_rnd(r, 1000, 1, 2)),
        _arr(_rnd(r, 1000, 1, 10)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    dem = 1
    dai_nhat = 1
    for i in range(1, n):
        if a[i] == a[i - 1]:
            dem += 1
        else:
            dem = 1
        if dem > dai_nhat:
            dai_nhat = dem
    return f"{dai_nhat}\n"


@problem(
    title="Con dốc dài nhất trên đường đạp xe",
    difficulty=3,
    statement="""
        Bạn Khoa đạp xe trên một con đường và ghi lại độ cao của n điểm liên tiếp trên đường.
        Một đoạn leo dốc là một đoạn gồm các điểm liền nhau mà mỗi điểm cao hơn hẳn điểm
        ngay trước nó. Em hãy tìm xem đoạn leo dốc dài nhất có bao nhiêu điểm.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số điểm.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên — độ dài lớn nhất của một đoạn liên tiếp a[l], a[l+1], ..., a[r]
          thoả mãn a[l] < a[l+1] < ... < a[r]. Một điểm đứng một mình cũng là đoạn dài 1.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 0 ≤ a[i] ≤ 10^6
    """,
    tests=lambda r: [
        "8\n3 5 7 7 2 4 6 9\n",
        "1\n10\n",
        _arr([5] * 6),
        _arr(list(range(1000))),
        _arr(list(range(50, 0, -1))),
        _arr([1, 2, 3, 1, 2, 3, 4, 0]),
        _arr(_rnd(r, 40, 0, 20)),
        _arr(_rnd(r, 1000, 0, 10**6)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    dem = 1
    dai_nhat = 1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            dem += 1
        else:
            dem = 1
        if dem > dai_nhat:
            dai_nhat = dem
    return f"{dai_nhat}\n"


@problem(
    title="Những ngày liên tiếp bán nhiều kem nhất",
    difficulty=3,
    statement="""
        Tiệm kem của chú Tư ghi lại số que kem bán được trong n ngày, ngày thứ i bán được a[i] que.
        Chú muốn tìm k ngày liên tiếp bán được nhiều kem nhất. Các ngày được đánh số từ 1 đến n.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và k, cách nhau một dấu cách.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - In ra hai số nguyên cách nhau một dấu cách: tổng số que kem lớn nhất của k ngày
          liên tiếp, và ngày bắt đầu của đoạn k ngày đó.
        - Nếu có nhiều đoạn cùng tổng lớn nhất, chọn đoạn bắt đầu sớm nhất.

        Giới hạn:
        - 1 ≤ k ≤ n ≤ 1000
        - 0 ≤ a[i] ≤ 10^6

        Gợi ý:
        - Đoạn bắt đầu ở ngày i gồm các ngày i, i+1, ..., i+k-1, nên i chạy từ 1 đến n-k+1.
        - Khi dời đoạn sang phải một ngày, chỉ cần cộng thêm ngày mới và trừ đi ngày cũ nhất.
    """,
    tests=lambda r: [
        "7 3\n5 1 8 6 2 9 4\n",
        "1 1\n0\n",
        "5 5\n1 2 3 4 5\n",
        "6 1\n4 9 2 9 1 3\n",
        "6 2\n5 5 1 1 5 5\n",
        f"30 4\n{_line(_rnd(r, 30, 0, 20))}\n",
        f"1000 7\n{_line(_rnd(r, 1000, 0, 10))}\n",
        f"1000 100\n{_line(_rnd(r, 1000, 0, 10**6))}\n",
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    k = int(data[1])
    a = [int(x) for x in data[2:2 + n]]
    tong = 0
    for i in range(k):
        tong += a[i]
    tot_nhat = tong
    bat_dau = 1
    for i in range(k, n):
        tong += a[i] - a[i - k]
        if tong > tot_nhat:
            tot_nhat = tong
            bat_dau = i - k + 2
    return f"{tot_nhat} {bat_dau}\n"


@problem(
    title="Bộ sưu tập thẻ hình không trùng nhau",
    difficulty=3,
    statement="""
        Bạn Bình sưu tầm thẻ hình, mỗi tấm thẻ có một mã số. Bình xếp n tấm thẻ thành một hàng,
        tấm thứ i có mã a[i]. Bình chỉ muốn giữ mỗi mã một tấm: đi từ trái sang phải, tấm thẻ nào
        có mã đã xuất hiện ở bên trái nó thì bỏ đi.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số tấm thẻ.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - Dòng đầu tiên in số k — số tấm thẻ còn lại.
        - Dòng thứ hai in k mã số của các tấm thẻ còn lại theo đúng thứ tự trong hàng,
          cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 1 ≤ a[i] ≤ 10^6
    """,
    tests=lambda r: [
        "8\n5 3 5 1 3 3 9 1\n",
        "1\n42\n",
        _arr([6] * 10),
        _arr([10, 20, 30, 40]),
        _arr([1, 2, 1, 2, 1, 2, 3]),
        _arr(_rnd(r, 30, 1, 10)),
        _arr(_rnd(r, 1000, 1, 50)),
        _arr(_rnd(r, 1000, 1, 10**6)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    giu = []
    da_co = set()
    for v in a:
        if v not in da_co:
            da_co.add(v)
            giu.append(v)
    return f"{len(giu)}\n" + " ".join(str(v) for v in giu) + "\n"


@problem(
    title="Món đồ chơi được cả lớp bình chọn nhiều nhất",
    difficulty=3,
    statement="""
        Lớp em bình chọn món đồ chơi yêu thích cho góc vui chơi. Mỗi bạn viết lên phiếu mã số
        của một món đồ chơi. Có tất cả n phiếu, phiếu thứ i ghi mã a[i]. Em hãy tìm món đồ chơi
        được nhiều phiếu nhất.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số phiếu bầu.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - In ra hai số nguyên cách nhau một dấu cách: mã số của món được nhiều phiếu nhất
          và số phiếu của món đó.
        - Nếu có nhiều món cùng có số phiếu nhiều nhất, chọn món có mã số nhỏ nhất.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 1 ≤ a[i] ≤ 1000

        Gợi ý:
        - Dùng mảng đếm dem, trong đó dem[v] là số phiếu ghi mã v (v từ 1 đến 1000).
    """,
    tests=lambda r: [
        "9\n4 7 4 2 7 9 7 4 1\n",
        "1\n500\n",
        _arr([10, 9, 8, 7, 6]),
        _arr([3] * 8),
        _arr([1000, 1000, 1, 2, 3]),
        _arr(_rnd(r, 50, 1, 10)),
        _arr(_rnd(r, 1000, 1, 30)),
        _arr(_rnd(r, 1000, 1, 1000)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    dem = [0] * 1001
    for i in range(n):
        dem[int(data[1 + i])] += 1
    ma = 1
    for v in range(2, 1001):
        if dem[v] > dem[ma]:
            ma = v
    return f"{ma} {dem[ma]}\n"


def _cau_hoi(a, qs):
    dong = [f"{len(a)} {len(qs)}", _line(a)] + [f"{l} {r}" for l, r in qs]
    return "\n".join(dong) + "\n"


def _t_doc_truyen(r):
    def ngau_nhien(n, q):
        qs = []
        for _ in range(q):
            x, y = r.randint(1, n), r.randint(1, n)
            qs.append((min(x, y), max(x, y)))
        return qs

    return [
        "5 3\n10 20 5 15 30\n1 3\n2 4\n5 5\n",
        "1 1\n7\n1 1\n",
        "4 2\n0 0 0 0\n1 4\n2 3\n",
        _cau_hoi([10**6] * 1000, [(1, 1000), (1, 1), (500, 1000)]),
        _cau_hoi(_rnd(r, 10, 0, 30), ngau_nhien(10, 5)),
        _cau_hoi(_rnd(r, 200, 0, 1000), ngau_nhien(200, 50)),
        _cau_hoi(_rnd(r, 1000, 0, 10**6), ngau_nhien(1000, 1000)),
    ]


@problem(
    title="Mai đọc bao nhiêu trang từ ngày l đến ngày r?",
    difficulty=3,
    statement="""
        Trong n ngày nghỉ hè, ngày thứ i bạn Mai đọc được a[i] trang truyện. Mẹ hỏi Mai q câu,
        mỗi câu có dạng: "Từ ngày l đến ngày r (tính cả hai ngày đó), con đọc được tổng cộng
        bao nhiêu trang?". Em hãy giúp Mai trả lời thật nhanh nhé.

        Đầu vào:
        - Dòng đầu tiên chứa hai số nguyên n và q, cách nhau một dấu cách.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.
        - q dòng tiếp theo, mỗi dòng chứa hai số nguyên l và r (1 ≤ l ≤ r ≤ n).

        Đầu ra:
        - In ra q dòng, dòng thứ j là câu trả lời cho câu hỏi thứ j: a[l] + a[l+1] + ... + a[r].

        Giới hạn:
        - 1 ≤ n ≤ 1000, 1 ≤ q ≤ 1000
        - 0 ≤ a[i] ≤ 10^6

        Gợi ý:
        - Tạo mảng tổng dồn p với p[0] = 0 và p[i] = p[i-1] + a[i].
          Khi đó tổng từ ngày l đến ngày r bằng p[r] - p[l-1].
    """,
    tests=_t_doc_truyen,
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    q = int(data[1])
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = p[i - 1] + int(data[1 + i])
    kq = []
    vt = 2 + n
    for _ in range(q):
        lo = int(data[vt])
        hi = int(data[vt + 1])
        vt += 2
        kq.append(str(p[hi] - p[lo - 1]))
    return "\n".join(kq) + "\n"


@problem(
    title="Những ngọn hải đăng nhìn thấy biển",
    difficulty=3,
    statement="""
        Dọc bờ biển có n ngọn hải đăng đứng thành một hàng từ trái sang phải, đánh số từ 1 đến n,
        ngọn thứ i cao a[i] mét. Biển nằm ở phía bên phải của hàng. Ngọn hải đăng thứ i nhìn thấy
        biển nếu nó cao hơn hẳn tất cả các ngọn đứng bên phải nó. Ngọn cuối cùng luôn nhìn thấy
        biển vì không có gì che.

        Đầu vào:
        - Dòng đầu tiên chứa số nguyên n — số ngọn hải đăng.
        - Dòng thứ hai chứa n số nguyên a[1], a[2], ..., a[n], cách nhau một dấu cách.

        Đầu ra:
        - In ra trên một dòng vị trí của các ngọn hải đăng nhìn thấy biển, theo thứ tự
          tăng dần, cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n ≤ 1000
        - 1 ≤ a[i] ≤ 10^6

        Gợi ý:
        - Duyệt từ phải sang trái và luôn nhớ chiều cao lớn nhất đã gặp.
    """,
    tests=lambda r: [
        "6\n5 8 3 6 6 2\n",
        "1\n10\n",
        _arr([4] * 5),
        _arr([9, 7, 5, 3, 1]),
        _arr([1, 2, 3, 4, 5]),
        _arr(_rnd(r, 30, 1, 20)),
        _arr(_rnd(r, 1000, 1, 10**6)),
    ],
)
def solve(inp):
    data = inp.split()
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    thay = []
    cao_nhat = 0
    for i in range(n - 1, -1, -1):
        if a[i] > cao_nhat:
            thay.append(i + 1)
            cao_nhat = a[i]
    thay.reverse()
    return " ".join(str(v) for v in thay) + "\n"
