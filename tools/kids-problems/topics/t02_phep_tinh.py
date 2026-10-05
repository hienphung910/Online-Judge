"""
Chu de 2: Phep tinh va cong thuc (K031-K060).

Chi dung nhap/xuat + cac phep + - * / % va cong thuc co dinh.
KHONG dung if/else, KHONG dung vong lap: moi dap an tinh duoc bang mot cong thuc.
"""

from kidslib import problem

TOPIC = "phep-tinh"


# =====================================================================
#  DE (difficulty = 1)
# =====================================================================

@problem(
    title="Hàng rào quanh vườn rau nhà An",
    difficulty=1,
    statement="""
        Bố của An muốn làm hàng rào bao quanh mảnh vườn rau hình chữ nhật
        có chiều dài a mét và chiều rộng b mét. Em hãy giúp bố tính xem
        hàng rào dài tổng cộng bao nhiêu mét nhé!

        Đầu vào:
        - Một dòng chứa hai số nguyên a và b, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là chu vi mảnh vườn (số mét hàng rào cần làm).

        Giới hạn:
        - 1 ≤ a, b ≤ 10000.

        Gợi ý:
        - Chu vi hình chữ nhật = (chiều dài + chiều rộng) × 2.
    """,
    tests=lambda r: ["5 3", "1 1", "10000 10000", "1 10000", "7 7", "12 4"]
    + [f"{r.randint(1, 10000)} {r.randint(1, 10000)}" for _ in range(2)],
)
def solve(inp):
    a, b = map(int, inp.split())
    return f"{(a + b) * 2}\n"


@problem(
    title="Tấm thảm hình chữ nhật của mèo Mướp",
    difficulty=1,
    statement="""
        Mèo Mướp rất thích nằm ngủ trên tấm thảm hình chữ nhật trong phòng khách.
        Tấm thảm dài a mét và rộng b mét. Hỏi diện tích tấm thảm là bao nhiêu mét vuông?

        Đầu vào:
        - Một dòng chứa hai số nguyên a và b, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là diện tích tấm thảm.

        Giới hạn:
        - 1 ≤ a, b ≤ 10000.

        Gợi ý:
        - Diện tích hình chữ nhật = chiều dài × chiều rộng.
    """,
    tests=lambda r: ["4 3", "1 1", "10000 10000", "1 9999", "250 40", "13 17"]
    + [f"{r.randint(1, 10000)} {r.randint(1, 10000)}" for _ in range(2)],
)
def solve(inp):
    a, b = map(int, inp.split())
    return f"{a * b}\n"


@problem(
    title="Viên gạch vuông lát sân trường",
    difficulty=1,
    statement="""
        Sân trường của em được lát bằng những viên gạch hình vuông, mỗi cạnh
        dài a xăng-ti-mét. Em hãy tính chu vi và diện tích của một viên gạch.

        Đầu vào:
        - Một dòng chứa số nguyên a là độ dài cạnh viên gạch.

        Đầu ra:
        - Dòng thứ nhất: chu vi viên gạch.
        - Dòng thứ hai: diện tích viên gạch.

        Giới hạn:
        - 1 ≤ a ≤ 10000.

        Gợi ý:
        - Chu vi hình vuông = cạnh × 4, diện tích hình vuông = cạnh × cạnh.
    """,
    tests=lambda r: ["30", "1", "10000", "2", "45", "4"]
    + [str(r.randint(5, 9999)) for _ in range(2)],
)
def solve(inp):
    a = int(inp.split()[0])
    return f"{a * 4}\n{a * a}\n"


@problem(
    title="Hộp quà lập phương của robot Bi",
    difficulty=1,
    statement="""
        Robot Bi gói quà sinh nhật trong một chiếc hộp hình lập phương có cạnh
        dài a xăng-ti-mét. Hỏi thể tích chiếc hộp là bao nhiêu xăng-ti-mét khối?

        Đầu vào:
        - Một dòng chứa số nguyên a là độ dài cạnh của hộp.

        Đầu ra:
        - Một số nguyên là thể tích của hộp.

        Giới hạn:
        - 1 ≤ a ≤ 1000.

        Gợi ý:
        - Thể tích hình lập phương = cạnh × cạnh × cạnh.
    """,
    tests=lambda r: ["3", "1", "1000", "10", "999", "2"]
    + [str(r.randint(11, 998)) for _ in range(2)],
)
def solve(inp):
    a = int(inp.split()[0])
    return f"{a * a * a}\n"


@problem(
    title="Đếm chân gà và chó ở trang trại",
    difficulty=1,
    statement="""
        Trang trại của bà có c con gà và d con chó. Mỗi con gà có 2 chân,
        mỗi con chó có 4 chân. Em hãy đếm giúp bà xem tất cả có bao nhiêu cái chân nhé!

        Đầu vào:
        - Một dòng chứa hai số nguyên c và d (số gà và số chó), cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là tổng số chân của cả gà và chó.

        Giới hạn:
        - 0 ≤ c, d ≤ 1000000.
    """,
    tests=lambda r: ["3 2", "0 0", "1000000 1000000", "5 0", "0 7", "1 1"]
    + [f"{r.randint(0, 1000000)} {r.randint(0, 1000000)}" for _ in range(2)],
)
def solve(inp):
    c, d = map(int, inp.split())
    return f"{c * 2 + d * 4}\n"


@problem(
    title="Mua bút chì và tẩy cho năm học mới",
    difficulty=1,
    statement="""
        Năm học mới sắp đến, mẹ đưa An đi nhà sách. Mẹ mua n cây bút chì,
        mỗi cây giá a đồng, và m cục tẩy, mỗi cục giá b đồng.
        Hỏi mẹ phải trả tất cả bao nhiêu tiền?

        Đầu vào:
        - Dòng thứ nhất chứa hai số nguyên n và a, cách nhau một dấu cách.
        - Dòng thứ hai chứa hai số nguyên m và b, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là tổng số tiền mẹ phải trả (đồng).

        Giới hạn:
        - 0 ≤ n, m ≤ 1000.
        - 1 ≤ a, b ≤ 100000.
    """,
    tests=lambda r: [
        "3 5000\n2 3000",
        "0 5000\n0 3000",
        "1000 100000\n1000 100000",
        "1 1\n0 7",
        "10 4500\n0 2000",
        "0 1000\n5 2500",
    ] + [f"{r.randint(0, 1000)} {r.randint(1, 100000)}\n{r.randint(0, 1000)} {r.randint(1, 100000)}"
         for _ in range(2)],
)
def solve(inp):
    n, a, m, b = map(int, inp.split())
    return f"{n * a + m * b}\n"


@problem(
    title="Quãng đường đến nhà bà ngoại tính bằng mét",
    difficulty=1,
    statement="""
        Cuối tuần, An đạp xe đến nhà bà ngoại. Quãng đường dài a ki-lô-mét
        và b mét. Em hãy đổi cả quãng đường đó ra mét.

        Đầu vào:
        - Một dòng chứa hai số nguyên a (số ki-lô-mét) và b (số mét), cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là độ dài quãng đường tính bằng mét.

        Giới hạn:
        - 0 ≤ a ≤ 1000.
        - 0 ≤ b ≤ 999.

        Gợi ý:
        - 1 ki-lô-mét = 1000 mét.
    """,
    tests=lambda r: ["2 350", "0 0", "1000 999", "0 5", "7 0", "1 1"]
    + [f"{r.randint(2, 999)} {r.randint(1, 998)}" for _ in range(2)],
)
def solve(inp):
    a, b = map(int, inp.split())
    return f"{a * 1000 + b}\n"


@problem(
    title="Bộ phim hoạt hình dài bao nhiêu phút?",
    difficulty=1,
    statement="""
        Bộ phim hoạt hình mà Lan thích nhất dài h giờ m phút.
        Hỏi bộ phim dài tất cả bao nhiêu phút?

        Đầu vào:
        - Một dòng chứa hai số nguyên h (số giờ) và m (số phút), cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là độ dài bộ phim tính bằng phút.

        Giới hạn:
        - 0 ≤ h ≤ 24.
        - 0 ≤ m ≤ 59.

        Gợi ý:
        - 1 giờ = 60 phút.
    """,
    tests=lambda r: ["1 30", "0 0", "24 59", "0 45", "3 0", "2 5"]
    + [f"{r.randint(4, 23)} {r.randint(1, 58)}" for _ in range(2)],
)
def solve(inp):
    h, m = map(int, inp.split())
    return f"{h * 60 + m}\n"


@problem(
    title="Heo đất tiết kiệm của bạn Lan",
    difficulty=1,
    statement="""
        Trong heo đất của Lan đang có s đồng. Từ hôm nay, mỗi ngày Lan bỏ thêm
        vào heo đúng x đồng. Hỏi sau d ngày, trong heo đất của Lan có bao nhiêu tiền?

        Đầu vào:
        - Một dòng chứa ba số nguyên s, x và d, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là số tiền trong heo đất sau d ngày.

        Giới hạn:
        - 0 ≤ s ≤ 1000000.
        - 0 ≤ x ≤ 10000.
        - 0 ≤ d ≤ 10000.
    """,
    tests=lambda r: ["5000 2000 3", "0 0 0", "1000000 10000 10000", "0 5000 7", "12000 3000 0", "300 0 25"]
    + [f"{r.randint(0, 1000000)} {r.randint(1, 10000)} {r.randint(1, 10000)}" for _ in range(2)],
)
def solve(inp):
    s, x, d = map(int, inp.split())
    return f"{s + x * d}\n"


@problem(
    title="Điểm trung bình ba bài kiểm tra của An",
    difficulty=1,
    statement="""
        An vừa làm xong ba bài kiểm tra và được a, b, c điểm. An muốn biết
        điểm trung bình của mình, nhưng chỉ lấy phần nguyên (bỏ phần lẻ phía sau).

        Đầu vào:
        - Một dòng chứa ba số nguyên a, b, c, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là phần nguyên của điểm trung bình.

        Giới hạn:
        - 0 ≤ a, b, c ≤ 10.

        Gợi ý:
        - Cộng ba điểm lại rồi chia lấy phần nguyên cho 3.
    """,
    tests=["9 8 6", "0 0 0", "10 10 10", "10 10 9", "5 6 6", "1 0 0", "7 8 10", "3 9 2"],
)
def solve(inp):
    a, b, c = map(int, inp.split())
    return f"{(a + b + c) // 3}\n"


# =====================================================================
#  VUA (difficulty = 2)
# =====================================================================

@problem(
    title="Cô giáo chia kẹo đều cho cả nhóm",
    difficulty=2,
    statement="""
        Cô giáo có n viên kẹo và muốn chia đều cho k bạn trong nhóm: bạn nào cũng
        được số kẹo như nhau và nhiều nhất có thể. Số kẹo còn thừa cô cất lại vào hộp.

        Đầu vào:
        - Một dòng chứa hai số nguyên n và k, cách nhau một dấu cách.

        Đầu ra:
        - Dòng thứ nhất: số kẹo mỗi bạn nhận được.
        - Dòng thứ hai: số kẹo còn thừa.

        Giới hạn:
        - 0 ≤ n ≤ 1000000000.
        - 1 ≤ k ≤ 1000000.

        Gợi ý:
        - Dùng phép chia lấy phần nguyên và phép chia lấy dư.
    """,
    tests=lambda r: ["17 5", "0 3", "1000000000 1", "4 7", "30 6", "999999999 1000000"]
    + [f"{r.randint(0, 1000000000)} {r.randint(2, 1000000)}" for _ in range(2)],
)
def solve(inp):
    n, k = map(int, inp.split())
    return f"{n // k}\n{n % k}\n"


@problem(
    title="Robot Bi chơi game bao nhiêu giờ?",
    difficulty=2,
    statement="""
        Cuối tuần, robot Bi chơi game tổng cộng m phút. Em hãy đổi khoảng thời gian
        đó ra giờ và phút giúp Bi.

        Đầu vào:
        - Một dòng chứa số nguyên m.

        Đầu ra:
        - Một dòng gồm hai số nguyên: số giờ và số phút (số phút nhỏ hơn 60),
          cách nhau một dấu cách.

        Giới hạn:
        - 0 ≤ m ≤ 1000000.

        Gợi ý:
        - 1 giờ = 60 phút.
    """,
    tests=lambda r: ["135", "0", "59", "60", "1000000", "1439"]
    + [str(r.randint(61, 999999)) for _ in range(2)],
)
def solve(inp):
    m = int(inp.split()[0])
    return f"{m // 60} {m % 60}\n"


@problem(
    title="Cân túi táo: bao nhiêu ki-lô-gam?",
    difficulty=2,
    statement="""
        Bác bán hoa quả xếp n quả táo vào một cái túi, quả nào cũng nặng đúng w gam.
        Em hãy cho biết túi táo nặng bao nhiêu ki-lô-gam và bao nhiêu gam.

        Đầu vào:
        - Một dòng chứa hai số nguyên n và w, cách nhau một dấu cách.

        Đầu ra:
        - Một dòng gồm hai số nguyên: số ki-lô-gam và số gam (số gam nhỏ hơn 1000),
          cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n ≤ 1000.
        - 1 ≤ w ≤ 1000.

        Gợi ý:
        - 1 ki-lô-gam = 1000 gam. Hãy tính tổng số gam trước.
    """,
    tests=lambda r: ["6 250", "1 1", "1000 1000", "4 250", "3 333", "7 180"]
    + [f"{r.randint(2, 999)} {r.randint(2, 999)}" for _ in range(2)],
)
def solve(inp):
    n, w = map(int, inp.split())
    total = n * w
    return f"{total // 1000} {total % 1000}\n"


@problem(
    title="Xếp que diêm thành dãy ô vuông",
    difficulty=2,
    statement="""
        Bạn Nam dùng que diêm xếp thành một dãy ô vuông nằm liền nhau trên một hàng ngang.
        Hai ô đứng cạnh nhau dùng chung một que ở giữa.
        Hỏi để xếp được n ô vuông như vậy, Nam cần bao nhiêu que diêm?

        Đầu vào:
        - Một dòng chứa số nguyên n là số ô vuông.

        Đầu ra:
        - Một số nguyên là số que diêm cần dùng.

        Giới hạn:
        - 1 ≤ n ≤ 1000000.

        Gợi ý:
        - Ô đầu tiên cần 4 que. Mỗi ô xếp thêm về sau chỉ cần thêm 3 que.
    """,
    tests=lambda r: ["3", "1", "2", "1000000", "10", "57"]
    + [str(r.randint(100, 999999)) for _ in range(2)],
)
def solve(inp):
    n = int(inp.split()[0])
    return f"{3 * n + 1}\n"


@problem(
    title="Trồng cây xanh hai bên đường làng",
    difficulty=2,
    statement="""
        Làng em vừa làm một con đường dài L mét và trồng cây xanh ở cả hai bên đường.
        Ở mỗi bên, cứ cách k mét lại trồng một cây, và có trồng cây ở cả hai đầu đường.
        Hỏi cần tất cả bao nhiêu cây?

        Đầu vào:
        - Một dòng chứa hai số nguyên L và k, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là tổng số cây ở cả hai bên đường.

        Giới hạn:
        - 1 ≤ k ≤ L ≤ 1000000.
        - L chia hết cho k.

        Gợi ý:
        - Mỗi bên đường được chia thành (L chia cho k) khoảng. Số cây nhiều hơn số khoảng đúng 1 cây.
        - Dùng phép chia lấy phần nguyên để kết quả là số nguyên.
    """,
    tests=lambda r: ["20 5", "1 1", "1000000 1", "1000000 1000000", "100 10", "36 4"]
    + [f"{k * r.randint(1, 1000000 // k)} {k}" for k in (r.randint(1, 1000), r.randint(1, 1000))],
)
def solve(inp):
    L, k = map(int, inp.split())
    return f"{(L // k + 1) * 2}\n"


@problem(
    title="Lát gạch hoa cho phòng học",
    difficulty=2,
    statement="""
        Phòng học hình chữ nhật dài a mét, rộng b mét. Chú thợ lát nền bằng những viên
        gạch hoa hình vuông có cạnh s xăng-ti-mét, xếp kín cả sàn mà không phải cắt viên nào.
        Hỏi chú cần bao nhiêu viên gạch?

        Đầu vào:
        - Một dòng chứa ba số nguyên a, b và s, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là số viên gạch cần dùng.

        Giới hạn:
        - 1 ≤ a, b ≤ 100.
        - s là một trong các số 10, 20, 25, 50, 100.

        Gợi ý:
        - 1 mét = 100 xăng-ti-mét. Hãy tính mỗi hàng có bao nhiêu viên và sàn có bao nhiêu hàng.
    """,
    tests=lambda r: ["6 4 50", "1 1 100", "100 100 10", "1 1 10", "8 5 25", "3 7 20"]
    + [f"{r.randint(2, 99)} {r.randint(2, 99)} {s}" for s in (r.choice([10, 20, 25]), r.choice([50, 100]))],
)
def solve(inp):
    a, b, s = map(int, inp.split())
    return f"{(a * 100 // s) * (b * 100 // s)}\n"


@problem(
    title="Xếp bánh quy vào hộp",
    difficulty=2,
    statement="""
        Mẹ nướng n chiếc bánh quy và xếp vào các hộp, mỗi hộp đựng được nhiều nhất k chiếc.
        Hỏi mẹ cần ít nhất bao nhiêu hộp để đựng hết số bánh?

        Đầu vào:
        - Một dòng chứa hai số nguyên n và k, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là số hộp ít nhất cần dùng.

        Giới hạn:
        - 0 ≤ n ≤ 1000000.
        - 1 ≤ k ≤ 1000.

        Gợi ý:
        - Nếu chia n cho k còn dư thì cần thêm một hộp nữa cho số bánh lẻ.
        - Mẹo: số hộp bằng phần nguyên của phép chia (n + k - 1) cho k.
    """,
    tests=lambda r: ["25 10", "0 5", "30 10", "1 1000", "1000000 1", "1000000 7", "999 1000"]
    + [f"{r.randint(1, 1000000)} {r.randint(2, 1000)}" for _ in range(2)],
)
def solve(inp):
    n, k = map(int, inp.split())
    return f"{(n + k - 1) // k}\n"


@problem(
    title="Bắt tay làm quen ngày khai giảng",
    difficulty=2,
    statement="""
        Ngày khai giảng, có n bạn mới gặp nhau lần đầu. Mỗi bạn bắt tay với mỗi bạn khác
        đúng một lần. Hỏi có tất cả bao nhiêu cái bắt tay?

        Đầu vào:
        - Một dòng chứa số nguyên n là số bạn.

        Đầu ra:
        - Một số nguyên là tổng số cái bắt tay.

        Giới hạn:
        - 1 ≤ n ≤ 40000.

        Gợi ý:
        - Mỗi bạn bắt tay n - 1 bạn khác, nhưng như vậy mỗi cái bắt tay bị đếm hai lần.
          Vì thế số cái bắt tay là n × (n - 1) chia cho 2
          (dùng phép chia lấy phần nguyên để kết quả là số nguyên).
    """,
    tests=lambda r: ["4", "1", "2", "40000", "3", "100"]
    + [str(r.randint(101, 39999)) for _ in range(2)],
)
def solve(inp):
    n = int(inp.split()[0])
    return f"{n * (n - 1) // 2}\n"


@problem(
    title="Tháp kẹo bậc thang của mèo Mướp",
    difficulty=2,
    statement="""
        Mèo Mướp xếp kẹo thành một cái tháp bậc thang: bậc trên cùng có 1 viên,
        bậc thứ hai có 2 viên, bậc thứ ba có 3 viên, ... và bậc dưới cùng có n viên.
        Hỏi cả cái tháp có bao nhiêu viên kẹo?

        Đầu vào:
        - Một dòng chứa số nguyên n là số viên kẹo ở bậc dưới cùng.

        Đầu ra:
        - Một số nguyên là tổng số viên kẹo của cái tháp.

        Giới hạn:
        - 1 ≤ n ≤ 40000.

        Gợi ý:
        - Không cần cộng từng số! Có công thức: 1 + 2 + ... + n = n × (n + 1) chia cho 2
          (dùng phép chia lấy phần nguyên để kết quả là số nguyên).
    """,
    tests=lambda r: ["4", "1", "40000", "2", "10", "100"]
    + [str(r.randint(101, 39999)) for _ in range(2)],
)
def solve(inp):
    n = int(inp.split()[0])
    return f"{n * (n + 1) // 2}\n"


@problem(
    title="Thời gian đạp xe từ nhà đến trường",
    difficulty=2,
    statement="""
        An đạp xe rời nhà lúc h1 giờ m1 phút và đến trường lúc h2 giờ m2 phút
        (trong cùng một ngày). Hỏi An đã đạp xe trong bao nhiêu phút?

        Đầu vào:
        - Dòng thứ nhất chứa hai số nguyên h1 và m1 (lúc rời nhà), cách nhau một dấu cách.
        - Dòng thứ hai chứa hai số nguyên h2 và m2 (lúc đến trường), cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là số phút An đã đạp xe.

        Giới hạn:
        - 0 ≤ h1, h2 ≤ 23 và 0 ≤ m1, m2 ≤ 59.
        - Lúc đến trường không sớm hơn lúc rời nhà.

        Gợi ý:
        - Đổi cả hai thời điểm ra số phút tính từ 0 giờ 0 phút, rồi trừ cho nhau.
    """,
    tests=lambda r: ["6 45\n7 10", "7 0\n7 0", "0 0\n23 59", "6 59\n7 0", "6 10\n6 55", "5 30\n8 15"]
    + [f"{a // 60} {a % 60}\n{b // 60} {b % 60}"
       for a, b in (sorted((r.randint(0, 1439), r.randint(0, 1439))) for _ in range(2))],
)
def solve(inp):
    h1, m1, h2, m2 = map(int, inp.split())
    return f"{(h2 * 60 + m2) - (h1 * 60 + m1)}\n"


@problem(
    title="Đồng hồ bấm giờ cuộc thi chạy",
    difficulty=2,
    statement="""
        Trong cuộc thi chạy của trường, đồng hồ bấm giờ chỉ hiện tổng số giây s
        mà bạn Minh đã chạy. Em hãy đổi s giây ra giờ, phút và giây.

        Đầu vào:
        - Một dòng chứa số nguyên s.

        Đầu ra:
        - Một dòng gồm ba số nguyên: số giờ, số phút và số giây
          (số phút và số giây đều nhỏ hơn 60), cách nhau một dấu cách.

        Giới hạn:
        - 0 ≤ s ≤ 1000000.

        Gợi ý:
        - 1 giờ = 3600 giây, 1 phút = 60 giây.
    """,
    tests=lambda r: ["3725", "0", "59", "60", "3600", "86399", "1000000"]
    + [str(r.randint(3601, 999999)) for _ in range(2)],
)
def solve(inp):
    s = int(inp.split()[0])
    return f"{s // 3600} {s % 3600 // 60} {s % 60}\n"


@problem(
    title="Robot Bi đọc ngược số ba chữ số",
    difficulty=2,
    statement="""
        Robot Bi có thói quen đọc mọi thứ từ phải sang trái. Cho một số n có đúng
        ba chữ số, em hãy in ra số mà Bi đọc được khi đọc ngược các chữ số của n.

        Đầu vào:
        - Một dòng chứa số nguyên n.

        Đầu ra:
        - Một số nguyên là số đọc ngược. Nếu số đọc ngược có chữ số 0 ở đầu
          thì không in các chữ số 0 đó.

        Giới hạn:
        - 100 ≤ n ≤ 999.

        Gợi ý:
        - Chữ số hàng trăm = phần nguyên của n chia 100.
        - Chữ số hàng chục = phần nguyên của n chia 10, rồi lấy dư khi chia cho 10.
        - Chữ số hàng đơn vị = số dư khi chia n cho 10.
    """,
    tests=["123", "100", "999", "120", "505", "910", "478", "306"],
)
def solve(inp):
    n = int(inp.split()[0])
    tram = n // 100
    chuc = n // 10 % 10
    donvi = n % 10
    return f"{donvi * 100 + chuc * 10 + tram}\n"


# =====================================================================
#  KHO (difficulty = 3)
# =====================================================================

@problem(
    title="Đồng hồ báo thức reo lúc mấy giờ?",
    difficulty=3,
    statement="""
        Bây giờ là h giờ m phút. Lan đặt đồng hồ báo thức reo sau đúng k phút nữa.
        Hỏi lúc đồng hồ reo là mấy giờ mấy phút? Đồng hồ dùng kiểu 24 giờ:
        sau 23 giờ 59 phút là 0 giờ 0 phút của ngày hôm sau.

        Đầu vào:
        - Một dòng chứa ba số nguyên h, m và k, cách nhau một dấu cách.

        Đầu ra:
        - Một dòng gồm hai số nguyên: giờ (từ 0 đến 23) và phút (từ 0 đến 59)
          lúc đồng hồ reo, cách nhau một dấu cách.

        Giới hạn:
        - 0 ≤ h ≤ 23, 0 ≤ m ≤ 59.
        - 0 ≤ k ≤ 1000000.

        Gợi ý:
        - Đổi thời điểm hiện tại ra phút rồi cộng thêm k. Đổi ngược lại ra giờ và phút,
          số giờ thì lấy dư cho 24.
    """,
    tests=lambda r: ["22 45 100", "0 0 0", "23 59 1", "6 30 45", "12 0 1440", "23 59 1000000", "10 15 59"]
    + [f"{r.randint(0, 23)} {r.randint(0, 59)} {r.randint(1441, 1000000)}" for _ in range(2)],
)
def solve(inp):
    h, m, k = map(int, inp.split())
    total = h * 60 + m + k
    return f"{total // 60 % 24} {total % 60}\n"


@problem(
    title="Sau d ngày nữa là thứ mấy?",
    difficulty=3,
    statement="""
        Bạn An đánh số các ngày trong tuần như sau: thứ Hai là 2, thứ Ba là 3, ...,
        thứ Bảy là 7 và Chủ nhật là 8. Hôm nay là ngày w. Hỏi sau d ngày nữa
        là ngày nào trong tuần?

        Đầu vào:
        - Một dòng chứa hai số nguyên w và d, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên từ 2 đến 8 là ngày trong tuần sau d ngày (theo cách đánh số ở trên).

        Giới hạn:
        - 2 ≤ w ≤ 8.
        - 0 ≤ d ≤ 1000000.

        Gợi ý:
        - Cứ 7 ngày thì các thứ lặp lại. Hãy trừ w đi 2 để được số từ 0 đến 6,
          cộng thêm d, lấy dư cho 7, rồi cộng lại 2.
    """,
    tests=lambda r: ["6 3", "2 0", "8 1", "8 0", "7 1", "2 1000000", "5 14", "3 100"]
    + [f"{r.randint(2, 8)} {r.randint(101, 999999)}" for _ in range(2)],
)
def solve(inp):
    w, d = map(int, inp.split())
    return f"{(w - 2 + d) % 7 + 2}\n"


@problem(
    title="Thuê xe buýt đi dã ngoại",
    difficulty=3,
    statement="""
        Khối lớp 4 có n học sinh đi dã ngoại. Mỗi xe buýt có c ghế, mỗi bạn ngồi một ghế.
        Nhà trường thuê ít xe nhất có thể mà vẫn chở hết mọi bạn.
        Hỏi cần thuê bao nhiêu xe, và trên các xe còn tất cả bao nhiêu ghế trống?

        Đầu vào:
        - Một dòng chứa hai số nguyên n và c, cách nhau một dấu cách.

        Đầu ra:
        - Dòng thứ nhất: số xe buýt cần thuê.
        - Dòng thứ hai: tổng số ghế còn trống.

        Giới hạn:
        - 1 ≤ n ≤ 100000.
        - 1 ≤ c ≤ 100.

        Gợi ý:
        - Số ghế trống = tổng số ghế của tất cả các xe - số học sinh.
    """,
    tests=lambda r: ["100 45", "1 1", "1 100", "100000 1", "100000 100", "99999 100", "90 45"]
    + [f"{r.randint(2, 99999)} {r.randint(2, 99)}" for _ in range(2)],
)
def solve(inp):
    n, c = map(int, inp.split())
    xe = (n + c - 1) // c
    return f"{xe}\n{xe * c - n}\n"


@problem(
    title="Trả tiền thừa bằng tờ 50, 20 và 10 nghìn",
    difficulty=3,
    statement="""
        Chú bán hàng cần trả lại cho khách a nghìn đồng bằng các tờ tiền 50 nghìn,
        20 nghìn và 10 nghìn. Chú làm như sau: lấy nhiều tờ 50 nghìn nhất có thể,
        phần còn lại lấy nhiều tờ 20 nghìn nhất có thể, cuối cùng phần còn lại
        trả bằng tờ 10 nghìn. Hỏi chú dùng bao nhiêu tờ mỗi loại?

        Đầu vào:
        - Một dòng chứa số nguyên a (số tiền tính bằng nghìn đồng).

        Đầu ra:
        - Một dòng gồm ba số nguyên: số tờ 50 nghìn, số tờ 20 nghìn và số tờ 10 nghìn,
          cách nhau một dấu cách.

        Giới hạn:
        - 0 ≤ a ≤ 1000000.
        - a chia hết cho 10.

        Gợi ý:
        - Phép chia lấy phần nguyên cho biết số tờ, phép chia lấy dư cho biết số tiền còn lại.
    """,
    tests=lambda r: ["180", "0", "10", "40", "50", "1000000", "990", "70"]
    + [str(10 * r.randint(100, 99999)) for _ in range(2)],
)
def solve(inp):
    a = int(inp.split()[0])
    to50 = a // 50
    con = a % 50
    to20 = con // 20
    to10 = con % 20 // 10
    return f"{to50} {to20} {to10}\n"


@problem(
    title="Tìm ghế ngồi trong rạp chiếu phim",
    difficulty=3,
    statement="""
        Các ghế trong rạp chiếu phim được đánh số 1, 2, 3, ... lần lượt từ trái sang phải,
        hết hàng này đến hàng sau. Mỗi hàng có đúng c ghế: hàng 1 gồm các ghế từ 1 đến c,
        hàng 2 gồm các ghế từ c + 1 đến 2 × c, ... Vé của An ghi số ghế s.
        Hỏi ghế của An ở hàng thứ mấy, và là ghế thứ mấy trong hàng đó (đếm từ trái sang)?

        Đầu vào:
        - Một dòng chứa hai số nguyên c và s, cách nhau một dấu cách.

        Đầu ra:
        - Một dòng gồm hai số nguyên: số thứ tự của hàng và vị trí của ghế trong hàng,
          cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ c ≤ 1000.
        - 1 ≤ s ≤ 1000000.

        Gợi ý:
        - Hãy thử trừ s đi 1 trước khi chia cho c, rồi nhớ cộng lại 1 vào kết quả.
    """,
    tests=lambda r: ["10 27", "1 1", "10 10", "10 11", "1 1000000", "1000 1000000", "7 50", "12 100"]
    + [f"{r.randint(2, 1000)} {r.randint(1001, 999999)}" for _ in range(2)],
)
def solve(inp):
    c, s = map(int, inp.split())
    return f"{(s - 1) // c + 1} {(s - 1) % c + 1}\n"


@problem(
    title="Bao giờ tuổi bố gấp đôi tuổi An?",
    difficulty=3,
    statement="""
        Năm nay bố của An F tuổi, còn An C tuổi. Hỏi sau bao nhiêu năm nữa
        thì tuổi của bố gấp đúng hai lần tuổi của An?

        Đầu vào:
        - Một dòng chứa hai số nguyên F và C, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là số năm cần chờ (bằng 0 nếu năm nay tuổi bố đã gấp đôi tuổi An).

        Giới hạn:
        - 1 ≤ C ≤ 50.
        - 2 × C ≤ F ≤ 100.

        Gợi ý:
        - Năm nào bố cũng hơn An đúng F - C tuổi. Khi tuổi bố gấp đôi tuổi An
          thì tuổi An lúc đó đúng bằng số tuổi chênh lệch ấy.
    """,
    tests=lambda r: ["36 10", "2 1", "100 1", "40 20", "100 50", "45 12", "33 8"]
    + [f"{2 * c + r.randint(1, 100 - 2 * c)} {c}" for c in (r.randint(1, 40), r.randint(1, 40))],
)
def solve(inp):
    f, c = map(int, inp.split())
    return f"{f - 2 * c}\n"


@problem(
    title="Gà và chó trong sân: đếm đầu, đếm chân",
    difficulty=3,
    statement="""
        Trong sân nhà bà có cả gà và chó. An đếm được tất cả H cái đầu và L cái chân.
        Mỗi con gà có 2 chân, mỗi con chó có 4 chân. Hỏi trong sân có bao nhiêu con gà
        và bao nhiêu con chó?

        Đầu vào:
        - Một dòng chứa hai số nguyên H và L, cách nhau một dấu cách.

        Đầu ra:
        - Một dòng gồm hai số nguyên: số con gà và số con chó, cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ H ≤ 1000000.
        - L là số chẵn và 2 × H ≤ L ≤ 4 × H (luôn có đúng một đáp án).

        Gợi ý:
        - Giả sử con nào cũng là gà thì sẽ có 2 × H chân. Mỗi con chó có nhiều hơn
          con gà 2 chân. Số chân bị thiếu cho biết có bao nhiêu con chó.
    """,
    tests=lambda r: ["10 28", "1 2", "1 4", "1000000 4000000", "1000000 2000000", "35 94", "7 20"]
    + [f"{h} {2 * h + 2 * r.randint(1, h - 1)}" for h in (r.randint(2, 1000), r.randint(1001, 999999))],
)
def solve(inp):
    h, legs = map(int, inp.split())
    cho = (legs - 2 * h) // 2
    ga = h - cho
    return f"{ga} {cho}\n"


@problem(
    title="Lối đi lát gạch quanh bể bơi",
    difficulty=3,
    statement="""
        Bể bơi của khu vui chơi hình chữ nhật dài a mét, rộng b mét. Người ta lát một
        lối đi rộng w mét chạy sát quanh mép bể, nên bể và lối đi ghép lại thành một
        hình chữ nhật lớn hơn. Hỏi lối đi có diện tích bao nhiêu mét vuông?

        Đầu vào:
        - Một dòng chứa ba số nguyên a, b và w, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là diện tích của lối đi.

        Giới hạn:
        - 1 ≤ a, b ≤ 1000.
        - 0 ≤ w ≤ 1000.

        Gợi ý:
        - Lấy diện tích hình chữ nhật lớn (cả bể và lối đi) trừ đi diện tích bể bơi.
          Chú ý: lối đi nằm ở cả hai phía của chiều dài và cả hai phía của chiều rộng.
    """,
    tests=lambda r: ["10 6 2", "1 1 0", "1 1 1", "1000 1000 1000", "1000 1000 0", "25 12 3", "5 5 1"]
    + [f"{r.randint(2, 999)} {r.randint(2, 999)} {r.randint(1, 999)}" for _ in range(2)],
)
def solve(inp):
    a, b, w = map(int, inp.split())
    return f"{(a + 2 * w) * (b + 2 * w) - a * b}\n"
