"""Chu de 5: Ve hinh bang ky tu (K121-K150).

Moi bai deu ve mot buc tranh bang ky tu nen dung comparator="lines":
khoang trang DAU dong phai dung, khoang trang CUOI dong va dong trong o cuoi
duoc bo qua. Loi giai mau luon rstrip tung dong va ket thuc bang "\\n".
"""

from kidslib import problem

TOPIC = "ve-hinh"


# ============================================================ DỄ (10 bài)

@problem(
    title="Sân gạch vuông của mèo Mướp",
    difficulty=1,
    comparator="lines",
    statement="""
        Mèo Mướp muốn lát một cái sân hình vuông để nằm phơi nắng. Mỗi viên gạch
        được vẽ bằng một dấu *. Em hãy vẽ giúp Mướp cái sân có n hàng, mỗi hàng n viên gạch nhé!

        Đầu vào:
        - Một số nguyên n là độ dài cạnh của sân.

        Đầu ra:
        - In ra n dòng, mỗi dòng gồm đúng n dấu * viết liền nhau (không có dấu cách xen giữa).

        Giới hạn:
        - 1 ≤ n ≤ 20.

        Gợi ý:
        - Dùng hai vòng lặp lồng nhau: vòng ngoài chạy qua từng dòng, vòng trong in các dấu * của dòng đó.
        - Với n = 2, em in 2 dòng, mỗi dòng gồm 2 dấu * viết liền nhau.
    """,
    tests=["4\n", "1\n", "2\n", "3\n", "6\n", "9\n", "13\n", "20\n"],
)
def solve_san_gach(inp):
    n = int(inp.split()[0])
    lines = []
    for _ in range(n):
        lines.append("*" * n)
    return "\n".join(lines) + "\n"


@problem(
    title="Thanh sô-cô-la của bé Na",
    difficulty=1,
    comparator="lines",
    statement="""
        Bé Na được mẹ mua cho một thanh sô-cô-la hình chữ nhật gồm nhiều miếng nhỏ.
        Mỗi miếng sô-cô-la được vẽ bằng một dấu #. Em hãy vẽ thanh sô-cô-la có a hàng và b cột.

        Đầu vào:
        - Một dòng gồm hai số nguyên a và b cách nhau một dấu cách: a là số hàng, b là số cột.

        Đầu ra:
        - In ra a dòng, mỗi dòng gồm đúng b dấu # viết liền nhau.

        Giới hạn:
        - 1 ≤ a ≤ 20, 1 ≤ b ≤ 20.

        Gợi ý:
        - Chú ý đừng nhầm: số dòng là a, số dấu # trên mỗi dòng là b.
    """,
    tests=["3 5\n", "1 1\n", "1 7\n", "6 1\n", "4 4\n", "10 3\n", "2 20\n", "20 15\n"],
)
def solve_socola(inp):
    a, b = map(int, inp.split()[:2])
    lines = []
    for _ in range(a):
        lines.append("#" * b)
    return "\n".join(lines) + "\n"


@problem(
    title="Thang dây của chú khỉ Bông",
    difficulty=1,
    comparator="lines",
    statement="""
        Chú khỉ Bông cần một cái thang dây để trèo lên cây dừa. Thang có hai sợi dây dọc
        (vẽ bằng dấu |) và n bậc thang nằm ngang (vẽ bằng dấu -), mỗi bậc rộng w ký tự.

        Đầu vào:
        - Một dòng gồm hai số nguyên n và w cách nhau một dấu cách: n là số bậc, w là độ rộng của thang.

        Đầu ra:
        - In ra 2n + 1 dòng.
        - Các dòng thứ 1, 3, 5, ... (dòng lẻ) là khoảng trống giữa hai bậc: một dấu |, rồi đúng w dấu cách, rồi một dấu |.
        - Các dòng thứ 2, 4, 6, ... (dòng chẵn) là bậc thang: một dấu |, rồi đúng w dấu - viết liền nhau, rồi một dấu |.

        Giới hạn:
        - 1 ≤ n ≤ 10, 1 ≤ w ≤ 10.

        Gợi ý:
        - Với n = 1 và w = 2, thang có 3 dòng: dòng 1 là "|  |", dòng 2 là "|--|", dòng 3 là "|  |" (không in dấu ngoặc kép).
    """,
    tests=["3 2\n", "1 1\n", "1 5\n", "2 3\n", "4 1\n", "5 4\n", "8 6\n", "10 10\n"],
)
def solve_thang_day(inp):
    n, w = map(int, inp.split()[:2])
    lines = []
    for k in range(1, 2 * n + 2):
        if k % 2 == 1:
            lines.append("|" + " " * w + "|")
        else:
            lines.append("|" + "-" * w + "|")
    return "\n".join(lines) + "\n"


@problem(
    title="Tam giác kẹo dẻo của bé Thỏ",
    difficulty=1,
    comparator="lines",
    statement="""
        Bé Thỏ xếp kẹo dẻo thành hình tam giác: hàng trên cùng có 1 viên, mỗi hàng
        bên dưới nhiều hơn hàng trên 1 viên. Mỗi viên kẹo là một dấu *.

        Đầu vào:
        - Một số nguyên n là số hàng kẹo.

        Đầu ra:
        - In ra n dòng. Dòng thứ i (i = 1, 2, ..., n) gồm đúng i dấu * viết liền nhau.
        - Các dòng đều bắt đầu sát lề trái (không có dấu cách ở đầu dòng).

        Giới hạn:
        - 1 ≤ n ≤ 20.

        Gợi ý:
        - Với n = 2: dòng 1 là *, dòng 2 là **.
    """,
    tests=["4\n", "1\n", "2\n", "3\n", "5\n", "8\n", "12\n", "20\n"],
)
def solve_keo_deo(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, n + 1):
        lines.append("*" * i)
    return "\n".join(lines) + "\n"


@problem(
    title="Bậc thang xuống hầm kho báu",
    difficulty=1,
    comparator="lines",
    statement="""
        Nhóm thám hiểm tìm thấy một căn hầm bí mật! Cầu thang dẫn xuống hầm có bậc
        trên cùng dài nhất, càng xuống càng ngắn dần. Mỗi viên đá của bậc thang là một dấu #.

        Đầu vào:
        - Một số nguyên n là số bậc thang.

        Đầu ra:
        - In ra n dòng. Dòng thứ 1 có n dấu #, dòng thứ 2 có n - 1 dấu #, ..., dòng cuối có 1 dấu #.
        - Nói cách khác, dòng thứ i gồm đúng n - i + 1 dấu # viết liền nhau, bắt đầu sát lề trái.

        Giới hạn:
        - 1 ≤ n ≤ 20.
    """,
    tests=["4\n", "1\n", "2\n", "3\n", "6\n", "9\n", "15\n", "20\n"],
)
def solve_ham_kho_bau(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, n + 1):
        lines.append("#" * (n - i + 1))
    return "\n".join(lines) + "\n"


@problem(
    title="Robot Bi tập đếm theo bậc thang",
    difficulty=1,
    comparator="lines",
    statement="""
        Robot Bi đang tập đếm. Mỗi lần Bi bước lên một bậc thang, Bi đếm lại từ 1
        đến số thứ tự của bậc đó. Em hãy in ra những gì Bi đếm được nhé!

        Đầu vào:
        - Một số nguyên n là số bậc thang.

        Đầu ra:
        - In ra n dòng. Dòng thứ i gồm các chữ số 1, 2, 3, ..., i viết liền nhau (không có dấu cách xen giữa).
        - Các dòng bắt đầu sát lề trái.

        Giới hạn:
        - 1 ≤ n ≤ 9.

        Gợi ý:
        - Với n = 2: dòng 1 là 1, dòng 2 là 12.
    """,
    tests=["4\n", "1\n", "2\n", "3\n", "5\n", "7\n", "8\n", "9\n"],
)
def solve_bi_dem(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, n + 1):
        row = ""
        for j in range(1, i + 1):
            row += str(j)
        lines.append(row)
    return "\n".join(lines) + "\n"


@problem(
    title="Tháp số anh em nhà Sóc",
    difficulty=1,
    comparator="lines",
    statement="""
        Nhà Sóc có nhiều anh em. Anh cả số 1 đứng một mình ở tầng trên cùng, anh số 2
        rủ thêm một bạn số 2 nữa đứng tầng hai, anh số 3 có ba bạn số 3 ở tầng ba... Em hãy vẽ tháp số của nhà Sóc.

        Đầu vào:
        - Một số nguyên n là số tầng của tháp.

        Đầu ra:
        - In ra n dòng. Dòng thứ i gồm chữ số i được viết lặp lại đúng i lần, liền nhau.
        - Các dòng bắt đầu sát lề trái.

        Giới hạn:
        - 1 ≤ n ≤ 9.

        Gợi ý:
        - Với n = 2: dòng 1 là 1, dòng 2 là 22.
    """,
    tests=["3\n", "1\n", "2\n", "4\n", "5\n", "6\n", "8\n", "9\n"],
)
def solve_thap_soc(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, n + 1):
        lines.append(str(i) * i)
    return "\n".join(lines) + "\n"


@problem(
    title="Bậc thang bảng chữ cái ABC",
    difficulty=1,
    comparator="lines",
    statement="""
        Cô giáo dạy cả lớp đọc bảng chữ cái tiếng Anh theo kiểu bậc thang: lần đầu đọc A,
        lần sau đọc A B, lần sau nữa đọc A B C... Em hãy viết lại các bậc thang chữ cái đó.

        Đầu vào:
        - Một số nguyên n là số bậc thang.

        Đầu ra:
        - In ra n dòng. Dòng thứ i gồm i chữ cái in hoa đầu tiên của bảng chữ cái tiếng Anh
          (A, B, C, ...) viết liền nhau theo thứ tự, không có dấu cách xen giữa.
        - Các dòng bắt đầu sát lề trái.

        Giới hạn:
        - 1 ≤ n ≤ 26.

        Gợi ý:
        - Với n = 2: dòng 1 là A, dòng 2 là AB.
        - Chữ cái thứ j (tính từ 1) có thể lấy bằng chr(ord('A') + j - 1) trong Python, hoặc (char)('A' + j - 1) trong C++/Java.
    """,
    tests=["4\n", "1\n", "2\n", "5\n", "8\n", "13\n", "20\n", "26\n"],
)
def solve_chu_cai(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, n + 1):
        row = ""
        for j in range(i):
            row += chr(ord("A") + j)
        lines.append(row)
    return "\n".join(lines) + "\n"


@problem(
    title="Vệt sao băng chéo bầu trời",
    difficulty=1,
    comparator="lines",
    statement="""
        Đêm nay có sao băng! Ngôi sao bay chéo từ góc trên bên trái xuống góc dưới bên phải,
        mỗi dòng nó lùi sang phải thêm một bước. Em hãy vẽ vệt sao băng đó.

        Đầu vào:
        - Một số nguyên n là số dòng của bức tranh.

        Đầu ra:
        - In ra n dòng. Dòng thứ i gồm đúng i - 1 dấu cách, rồi đến một dấu *.
        - Như vậy dòng 1 có dấu * nằm sát lề trái, dòng 2 có 1 dấu cách đứng trước dấu *, dòng 3 có 2 dấu cách...

        Giới hạn:
        - 1 ≤ n ≤ 20.

        Gợi ý:
        - Các dấu cách ở đầu dòng rất quan trọng, phải in đúng số lượng.
    """,
    tests=["4\n", "1\n", "2\n", "3\n", "6\n", "10\n", "15\n", "20\n"],
)
def solve_sao_bang(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, n + 1):
        lines.append(" " * (i - 1) + "*")
    return "\n".join(lines) + "\n"


@problem(
    title="Dốc trượt tuyết của chim cánh cụt",
    difficulty=1,
    comparator="lines",
    statement="""
        Các chú chim cánh cụt muốn có một con dốc tuyết để trượt chơi. Con dốc là một
        tam giác dựa vào bên phải: đỉnh nhọn ở trên, đáy rộng ở dưới, cạnh thẳng đứng nằm bên phải.

        Đầu vào:
        - Một số nguyên n là chiều cao của con dốc.

        Đầu ra:
        - In ra n dòng. Dòng thứ i gồm đúng n - i dấu cách, rồi đến i dấu * viết liền nhau.
        - Như vậy mọi dòng đều kết thúc ở cùng một cột, dòng cuối cùng có n dấu * và không có dấu cách ở đầu.

        Giới hạn:
        - 1 ≤ n ≤ 20.

        Gợi ý:
        - Với n = 2: dòng 1 gồm 1 dấu cách rồi 1 dấu *, dòng 2 gồm 2 dấu *.
    """,
    tests=["4\n", "1\n", "2\n", "3\n", "5\n", "8\n", "12\n", "20\n"],
)
def solve_doc_tuyet(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, n + 1):
        lines.append(" " * (n - i) + "*" * i)
    return "\n".join(lines) + "\n"


# ============================================================ VỪA (12 bài)

@problem(
    title="Khung cửa sổ lâu đài cát",
    difficulty=2,
    comparator="lines",
    statement="""
        Bạn An xây một lâu đài cát rất to và muốn khoét một ô cửa sổ hình vuông. Cửa sổ chỉ
        có viền bên ngoài làm bằng dấu *, còn bên trong là khoảng trống để ngắm biển.

        Đầu vào:
        - Một số nguyên n là độ dài cạnh của cửa sổ.

        Đầu ra:
        - In ra n dòng tạo thành viền của hình vuông n x n.
        - Dòng đầu tiên và dòng cuối cùng gồm n dấu * viết liền nhau.
        - Mỗi dòng ở giữa gồm một dấu *, rồi đúng n - 2 dấu cách, rồi một dấu *.
        - Nếu n = 1 thì chỉ in một dấu *.

        Giới hạn:
        - 1 ≤ n ≤ 20.

        Gợi ý:
        - Một ô nằm trên viền nếu nó ở dòng đầu, dòng cuối, cột đầu hoặc cột cuối.
    """,
    tests=["4\n", "1\n", "2\n", "3\n", "5\n", "7\n", "10\n", "20\n"],
)
def solve_cua_so(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, n + 1):
        if i == 1 or i == n:
            lines.append("*" * n)
        else:
            lines.append("*" + " " * (n - 2) + "*")
    return "\n".join(lines) + "\n"


@problem(
    title="Bàn cờ caro của ông nội",
    difficulty=2,
    comparator="lines",
    statement="""
        Ông nội muốn kẻ một bàn cờ để chơi với cháu. Bàn cờ có n hàng, m cột, các ô đen
        và ô trắng xen kẽ nhau như bàn cờ vua. Ô đen vẽ bằng dấu #, ô trắng vẽ bằng dấu chấm (.).

        Đầu vào:
        - Một dòng gồm hai số nguyên n và m cách nhau một dấu cách: n là số hàng, m là số cột.

        Đầu ra:
        - In ra n dòng, mỗi dòng gồm m ký tự viết liền nhau.
        - Đánh số hàng và cột từ 1. Ô ở hàng i, cột j là dấu # nếu i + j là số chẵn, là dấu . nếu i + j là số lẻ.
        - Như vậy ô ở góc trên bên trái luôn là dấu #.

        Giới hạn:
        - 1 ≤ n ≤ 20, 1 ≤ m ≤ 20.
    """,
    tests=["4 5\n", "1 1\n", "1 6\n", "5 1\n", "2 2\n", "3 8\n", "8 8\n", "20 15\n"],
)
def solve_ban_co(inp):
    n, m = map(int, inp.split()[:2])
    lines = []
    for i in range(1, n + 1):
        row = ""
        for j in range(1, m + 1):
            row += "#" if (i + j) % 2 == 0 else "."
        lines.append(row)
    return "\n".join(lines) + "\n"


@problem(
    title="Bánh xốp nghiêng của tiệm bánh",
    difficulty=2,
    comparator="lines",
    statement="""
        Tiệm bánh của cô Mèo Mập vừa nướng một chiếc bánh xốp, nhưng chiếc bánh bị nghiêng
        sang phải trông như hình bình hành. Mỗi lớp bánh dài m ký tự #, và lớp càng ở trên càng lệch sang phải.

        Đầu vào:
        - Một dòng gồm hai số nguyên n và m cách nhau một dấu cách: n là số lớp bánh, m là độ dài mỗi lớp.

        Đầu ra:
        - In ra n dòng. Dòng thứ i (tính từ trên xuống) gồm đúng n - i dấu cách, rồi đến m dấu # viết liền nhau.
        - Như vậy dòng cuối cùng không có dấu cách ở đầu, dòng trên cùng có n - 1 dấu cách ở đầu.

        Giới hạn:
        - 1 ≤ n ≤ 20, 1 ≤ m ≤ 20.

        Gợi ý:
        - Với n = 2 và m = 3: dòng 1 gồm 1 dấu cách rồi ###, dòng 2 là ###.
    """,
    tests=["3 4\n", "1 1\n", "1 5\n", "4 1\n", "5 3\n", "6 10\n", "10 2\n", "15 20\n"],
)
def solve_banh_xop(inp):
    n, m = map(int, inp.split()[:2])
    lines = []
    for i in range(1, n + 1):
        lines.append(" " * (n - i) + "#" * m)
    return "\n".join(lines) + "\n"


@problem(
    title="Cờ đuôi nheo của đội bóng lớp em",
    difficulty=2,
    comparator="lines",
    statement="""
        Đội bóng lớp em cần một lá cờ đuôi nheo để cổ vũ. Lá cờ có hình tam giác nằm ngang,
        mũi nhọn chỉ sang phải: càng xuống thì cờ càng dài ra, tới giữa thì dài nhất, rồi ngắn lại dần.

        Đầu vào:
        - Một số nguyên n là độ dài của dòng dài nhất.

        Đầu ra:
        - In ra 2n - 1 dòng, các dòng đều bắt đầu sát lề trái và gồm các dấu * viết liền nhau.
        - Số dấu * trên các dòng lần lượt là 1, 2, 3, ..., n, rồi n - 1, n - 2, ..., 1.

        Giới hạn:
        - 1 ≤ n ≤ 20.

        Gợi ý:
        - Với n = 2, lá cờ có 3 dòng với số dấu * lần lượt là 1, 2, 1.
        - Có thể vẽ nửa trên bằng một vòng lặp tăng dần và nửa dưới bằng một vòng lặp giảm dần.
    """,
    tests=["3\n", "1\n", "2\n", "4\n", "5\n", "7\n", "10\n", "20\n"],
)
def solve_duoi_nheo(inp):
    n = int(inp.split()[0])
    lines = []
    for k in range(1, 2 * n):
        lines.append("*" * min(k, 2 * n - k))
    return "\n".join(lines) + "\n"


@problem(
    title="Kim tự tháp của Pharaoh mèo",
    difficulty=2,
    comparator="lines",
    statement="""
        Pharaoh mèo ra lệnh xây một kim tự tháp thật cân đối giữa sa mạc. Tầng trên cùng chỉ có
        1 viên đá, mỗi tầng bên dưới có thêm 2 viên, và mọi tầng đều được đặt chính giữa.

        Đầu vào:
        - Một số nguyên n là số tầng của kim tự tháp.

        Đầu ra:
        - In ra n dòng. Dòng thứ i gồm đúng n - i dấu cách, rồi đến 2i - 1 dấu * viết liền nhau.
        - Như vậy dòng cuối cùng có 2n - 1 dấu * và không có dấu cách ở đầu.

        Giới hạn:
        - 1 ≤ n ≤ 20.

        Gợi ý:
        - Với n = 2: dòng 1 gồm 1 dấu cách rồi 1 dấu *, dòng 2 gồm 3 dấu *.
    """,
    tests=["4\n", "1\n", "2\n", "3\n", "5\n", "8\n", "12\n", "20\n"],
)
def solve_kim_tu_thap(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, n + 1):
        lines.append(" " * (n - i) + "*" * (2 * i - 1))
    return "\n".join(lines) + "\n"


@problem(
    title="Chiếc phễu rót nước chanh",
    difficulty=2,
    comparator="lines",
    statement="""
        Mẹ dùng một chiếc phễu để rót nước chanh vào chai. Miệng phễu ở trên rộng nhất, càng xuống
        càng hẹp dần, và đáy phễu chỉ còn một lỗ nhỏ. Em hãy vẽ chiếc phễu bằng dấu * nhé.

        Đầu vào:
        - Một số nguyên n là số dòng của chiếc phễu.

        Đầu ra:
        - In ra n dòng. Dòng thứ i gồm đúng i - 1 dấu cách, rồi đến 2(n - i) + 1 dấu * viết liền nhau.
        - Như vậy dòng 1 có 2n - 1 dấu * và không có dấu cách ở đầu, dòng cuối có n - 1 dấu cách rồi 1 dấu *.

        Giới hạn:
        - 1 ≤ n ≤ 20.

        Gợi ý:
        - Với n = 2: dòng 1 gồm 3 dấu *, dòng 2 gồm 1 dấu cách rồi 1 dấu *.
    """,
    tests=["4\n", "1\n", "2\n", "3\n", "6\n", "9\n", "13\n", "20\n"],
)
def solve_cai_pheu(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, n + 1):
        lines.append(" " * (i - 1) + "*" * (2 * (n - i) + 1))
    return "\n".join(lines) + "\n"


@problem(
    title="Tam giác đèn nháy 0 và 1",
    difficulty=2,
    comparator="lines",
    statement="""
        Robot Bi gắn những bóng đèn nhỏ thành hình tam giác. Đèn sáng ghi là 1, đèn tắt ghi là 0,
        và các đèn được xếp xen kẽ sáng - tắt cho thật đẹp mắt.

        Đầu vào:
        - Một số nguyên n là số dòng của tam giác.

        Đầu ra:
        - In ra n dòng, các dòng bắt đầu sát lề trái. Dòng thứ i gồm đúng i chữ số viết liền nhau.
        - Đánh số dòng và vị trí từ 1. Chữ số ở dòng i, vị trí j là 1 nếu i + j là số chẵn, là 0 nếu i + j là số lẻ.

        Giới hạn:
        - 1 ≤ n ≤ 20.

        Gợi ý:
        - Dòng 1 luôn là 1, dòng 2 luôn là 01.
    """,
    tests=["4\n", "1\n", "2\n", "3\n", "5\n", "7\n", "10\n", "20\n"],
)
def solve_den_nhay(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, n + 1):
        row = ""
        for j in range(1, i + 1):
            row += "1" if (i + j) % 2 == 0 else "0"
        lines.append(row)
    return "\n".join(lines) + "\n"


@problem(
    title="Tam giác số của nhà toán học nhí",
    difficulty=2,
    comparator="lines",
    statement="""
        Bạn Minh, nhà toán học nhí của lớp, viết các số tự nhiên 1, 2, 3, ... liên tiếp thành hình tam giác:
        dòng 1 có 1 số, dòng 2 có 2 số, dòng 3 có 3 số... Số tiếp theo luôn nối tiếp số cuối cùng của dòng trước.

        Đầu vào:
        - Một số nguyên n là số dòng của tam giác.

        Đầu ra:
        - In ra n dòng. Dòng thứ i gồm i số nguyên liên tiếp, các số cách nhau đúng một dấu cách.
        - Dòng 1 bắt đầu bằng số 1; mỗi dòng sau bắt đầu bằng số lớn hơn số cuối cùng của dòng trước 1 đơn vị.
        - Các dòng bắt đầu sát lề trái.

        Giới hạn:
        - 1 ≤ n ≤ 15.

        Gợi ý:
        - Với n = 2: dòng 1 là 1, dòng 2 là 2 3.
        - Hãy dùng một biến đếm, mỗi lần in một số thì tăng biến đếm lên 1.
    """,
    tests=["4\n", "1\n", "2\n", "3\n", "5\n", "7\n", "10\n", "15\n"],
)
def solve_floyd(inp):
    n = int(inp.split()[0])
    lines = []
    cur = 1
    for i in range(1, n + 1):
        nums = []
        for _ in range(i):
            nums.append(str(cur))
            cur += 1
        lines.append(" ".join(nums))
    return "\n".join(lines) + "\n"


@problem(
    title="Bảng nhân tí hon của cô Mai",
    difficulty=2,
    comparator="lines",
    statement="""
        Cô Mai treo lên bảng một bảng nhân nhỏ xíu để cả lớp ôn bảng cửu chương. Bảng có n hàng và m cột,
        ô ở hàng i, cột j ghi kết quả của phép nhân i x j.

        Đầu vào:
        - Một dòng gồm hai số nguyên n và m cách nhau một dấu cách: n là số hàng, m là số cột.

        Đầu ra:
        - In ra n dòng. Dòng thứ i gồm m số: i x 1, i x 2, ..., i x m, các số cách nhau đúng một dấu cách.
        - Các dòng bắt đầu sát lề trái (không cần căn thẳng cột).

        Giới hạn:
        - 1 ≤ n ≤ 9, 1 ≤ m ≤ 9.
    """,
    tests=["3 4\n", "1 1\n", "1 9\n", "9 1\n", "2 5\n", "5 5\n", "7 3\n", "9 9\n"],
)
def solve_bang_nhan(inp):
    n, m = map(int, inp.split()[:2])
    lines = []
    for i in range(1, n + 1):
        nums = []
        for j in range(1, m + 1):
            nums.append(str(i * j))
        lines.append(" ".join(nums))
    return "\n".join(lines) + "\n"


@problem(
    title="Khung tên trên cửa lớp học",
    difficulty=2,
    comparator="lines",
    statement="""
        Lớp em muốn làm một tấm biển tên thật đẹp treo ở cửa lớp. Cái tên được đặt ở chính giữa,
        xung quanh là một khung hình chữ nhật làm bằng dấu *, giữa khung và chữ có chừa một khoảng trống.

        Đầu vào:
        - Một dòng chứa một từ S gồm chữ cái tiếng Anh hoặc chữ số, không có dấu cách. Gọi L là số ký tự của S.

        Đầu ra:
        - In ra đúng 5 dòng:
        - Dòng 1 và dòng 5: L + 4 dấu * viết liền nhau.
        - Dòng 2 và dòng 4: một dấu *, rồi L + 2 dấu cách, rồi một dấu *.
        - Dòng 3: một dấu *, một dấu cách, từ S, một dấu cách, rồi một dấu *.

        Giới hạn:
        - 1 ≤ L ≤ 20.

        Gợi ý:
        - Với S là Hi (L = 2): dòng 1 có 6 dấu *, dòng 3 là "* Hi *" (không in dấu ngoặc kép).
    """,
    tests=["Lan\n", "A\n", "Bi\n", "Minh\n", "Lop5A\n", "MeoMuop\n", "RobotBiVui\n",
           "ABCDEFGHIJKLMNOPQRST\n"],
)
def solve_khung_ten(inp):
    s = inp.split()[0]
    n = len(s)
    top = "*" * (n + 4)
    gap = "*" + " " * (n + 2) + "*"
    mid = "* " + s + " *"
    return "\n".join([top, gap, mid, gap, top]) + "\n"


@problem(
    title="Cánh buồm rỗng của thuyền giấy",
    difficulty=2,
    comparator="lines",
    statement="""
        Bạn Tí gấp một chiếc thuyền giấy và vẽ cánh buồm hình tam giác vuông. Cánh buồm chỉ có
        viền là dấu *, bên trong để trống cho gió thổi qua.

        Đầu vào:
        - Một số nguyên n là chiều cao của cánh buồm.

        Đầu ra:
        - In ra n dòng, các dòng bắt đầu sát lề trái.
        - Dòng 1 chỉ có một dấu *.
        - Dòng cuối cùng (dòng n) gồm n dấu * viết liền nhau.
        - Mỗi dòng i ở giữa (1 < i < n) gồm một dấu *, rồi đúng i - 2 dấu cách, rồi một dấu *.
        - Nếu n = 1 thì chỉ in một dấu *.

        Giới hạn:
        - 1 ≤ n ≤ 20.

        Gợi ý:
        - Dòng 2 (nếu không phải dòng cuối) là ** vì có 0 dấu cách ở giữa.
    """,
    tests=["5\n", "1\n", "2\n", "3\n", "4\n", "6\n", "10\n", "20\n"],
)
def solve_canh_buom(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, n + 1):
        if i == n:
            lines.append("*" * n)
        elif i == 1:
            lines.append("*")
        else:
            lines.append("*" + " " * (i - 2) + "*")
    return "\n".join(lines) + "\n"


@problem(
    title="Chữ X trên bản đồ kho báu",
    difficulty=2,
    comparator="lines",
    statement="""
        Trên tấm bản đồ của cướp biển Râu Đỏ, chỗ giấu kho báu được đánh dấu bằng một chữ X thật to.
        Chữ X được vẽ bằng hai đường chéo của một hình vuông n x n.

        Đầu vào:
        - Một số nguyên n là kích thước của hình vuông.

        Đầu ra:
        - In ra n dòng. Đánh số dòng và cột từ 1.
        - Ô ở dòng i, cột j là dấu * nếu j = i hoặc j = n + 1 - i (nằm trên một trong hai đường chéo);
          các ô còn lại là dấu cách.
        - Dấu cách ở đầu dòng và ở giữa dòng phải in đúng; dấu cách ở cuối dòng có hay không đều được.

        Giới hạn:
        - 1 ≤ n ≤ 20.

        Gợi ý:
        - Khi n lẻ, hai đường chéo gặp nhau ở ô chính giữa nên dòng giữa chỉ có một dấu *.
    """,
    tests=["5\n", "1\n", "2\n", "3\n", "4\n", "7\n", "10\n", "20\n"],
)
def solve_chu_x(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 1):
            row += "*" if (j == i or j == n + 1 - i) else " "
        lines.append(row.rstrip())
    return "\n".join(lines) + "\n"


# ============================================================ KHÓ (8 bài)

@problem(
    title="Viên kim cương của nàng tiên cá",
    difficulty=3,
    comparator="lines",
    statement="""
        Nàng tiên cá tìm được một viên kim cương lấp lánh dưới đáy biển. Viên kim cương có nửa trên
        là một kim tự tháp, nửa dưới là kim tự tháp lộn ngược, ghép lại ở dòng rộng nhất.

        Đầu vào:
        - Một số nguyên n là số dòng của nửa trên (tính cả dòng rộng nhất).

        Đầu ra:
        - In ra 2n - 1 dòng, mỗi dòng gồm một số dấu cách rồi đến các dấu * viết liền nhau.
        - Nửa trên: với i = 1, 2, ..., n, in một dòng gồm n - i dấu cách và 2i - 1 dấu *.
        - Nửa dưới: với i = n - 1, n - 2, ..., 1, in một dòng gồm n - i dấu cách và 2i - 1 dấu *.

        Giới hạn:
        - 1 ≤ n ≤ 15.

        Gợi ý:
        - Với n = 2, viên kim cương có 3 dòng: (1 dấu cách, 1 dấu *), (3 dấu *), (1 dấu cách, 1 dấu *).
    """,
    tests=["3\n", "1\n", "2\n", "4\n", "5\n", "7\n", "10\n", "15\n"],
)
def solve_kim_cuong(inp):
    n = int(inp.split()[0])
    lines = []
    for k in range(1, 2 * n):
        i = min(k, 2 * n - k)
        lines.append(" " * (n - i) + "*" * (2 * i - 1))
    return "\n".join(lines) + "\n"


@problem(
    title="Đồng hồ cát của phù thủy nhỏ",
    difficulty=3,
    comparator="lines",
    statement="""
        Cô phù thủy nhỏ dùng một chiếc đồng hồ cát để canh giờ nấu thuốc. Đồng hồ rộng ở trên và dưới,
        thắt lại ở giữa chỉ còn đúng một hạt cát.

        Đầu vào:
        - Một số nguyên n là số dòng của nửa trên (tính cả dòng thắt ở giữa).

        Đầu ra:
        - In ra 2n - 1 dòng, mỗi dòng gồm một số dấu cách rồi đến các dấu * viết liền nhau.
        - Nửa trên: với i = 1, 2, ..., n, in một dòng gồm i - 1 dấu cách và 2(n - i) + 1 dấu *.
        - Nửa dưới: với i = n - 1, n - 2, ..., 1, in một dòng gồm i - 1 dấu cách và 2(n - i) + 1 dấu *.
        - Như vậy dòng đầu và dòng cuối đều có 2n - 1 dấu *, dòng chính giữa có n - 1 dấu cách và 1 dấu *.

        Giới hạn:
        - 1 ≤ n ≤ 15.

        Gợi ý:
        - Với n = 2, đồng hồ có 3 dòng: (3 dấu *), (1 dấu cách, 1 dấu *), (3 dấu *).
    """,
    tests=["3\n", "1\n", "2\n", "4\n", "5\n", "8\n", "10\n", "15\n"],
)
def solve_dong_ho_cat(inp):
    n = int(inp.split()[0])
    lines = []
    for k in range(1, 2 * n):
        i = min(k, 2 * n - k)
        lines.append(" " * (i - 1) + "*" * (2 * (n - i) + 1))
    return "\n".join(lines) + "\n"


@problem(
    title="Tháp số soi gương",
    difficulty=3,
    comparator="lines",
    statement="""
        Robot Bi đứng trước gương và đếm: 1, 2, 3 rồi đếm ngược lại 2, 1. Bi xếp các lần đếm như thế
        thành một kim tự tháp số cân đối, nhìn từ trái sang hay từ phải sang đều giống nhau.

        Đầu vào:
        - Một số nguyên n là số tầng của tháp.

        Đầu ra:
        - In ra n dòng. Dòng thứ i gồm đúng n - i dấu cách, rồi đến các chữ số
          1, 2, ..., i - 1, i, i - 1, ..., 2, 1 viết liền nhau (không có dấu cách xen giữa).
        - Như vậy dòng thứ i có 2i - 1 chữ số và dòng cuối cùng không có dấu cách ở đầu.

        Giới hạn:
        - 1 ≤ n ≤ 9.

        Gợi ý:
        - Với n = 2: dòng 1 gồm 1 dấu cách rồi chữ số 1, dòng 2 là 121.
        - Mỗi dòng có thể in bằng hai vòng lặp: một vòng đếm lên từ 1 đến i, một vòng đếm xuống từ i - 1 về 1.
    """,
    tests=["4\n", "1\n", "2\n", "3\n", "5\n", "6\n", "8\n", "9\n"],
)
def solve_thap_soi_guong(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, n + 1):
        row = " " * (n - i)
        for x in range(1, i + 1):
            row += str(x)
        for x in range(i - 1, 0, -1):
            row += str(x)
        lines.append(row)
    return "\n".join(lines) + "\n"


@problem(
    title="Ngôi nhà nhỏ của ba chú heo",
    difficulty=3,
    comparator="lines",
    statement="""
        Ba chú heo con cùng nhau xây một ngôi nhà gạch thật chắc chắn. Ngôi nhà có mái nhọn hình
        kim tự tháp làm bằng dấu *, bên dưới là thân nhà hình chữ nhật có tường gạch làm bằng dấu #.

        Đầu vào:
        - Một số nguyên n là kích thước của ngôi nhà.

        Đầu ra:
        - In ra 2n dòng. Gọi W = 2n - 1 là chiều rộng của ngôi nhà.
        - Phần mái gồm n dòng: dòng thứ i (i = 1, 2, ..., n) gồm n - i dấu cách, rồi 2i - 1 dấu * viết liền nhau.
        - Phần thân gồm n dòng tiếp theo, không có dấu cách ở đầu:
        - Dòng đầu tiên và dòng cuối cùng của phần thân gồm W dấu # viết liền nhau.
        - Mỗi dòng ở giữa của phần thân gồm một dấu #, rồi W - 2 dấu cách, rồi một dấu #.
        - Nếu n = 1 thì phần thân chỉ có một dòng là một dấu #.

        Giới hạn:
        - 1 ≤ n ≤ 12.

        Gợi ý:
        - Phần mái giống hệt bài kim tự tháp, phần thân giống bài hình vuông rỗng nhưng là hình chữ nhật n dòng, W cột.
    """,
    tests=["3\n", "1\n", "2\n", "4\n", "5\n", "7\n", "9\n", "12\n"],
)
def solve_ngoi_nha(inp):
    n = int(inp.split()[0])
    w = 2 * n - 1
    lines = []
    for i in range(1, n + 1):
        lines.append(" " * (n - i) + "*" * (2 * i - 1))
    for r in range(1, n + 1):
        if r == 1 or r == n:
            lines.append("#" * w)
        else:
            lines.append("#" + " " * (w - 2) + "#")
    return "\n".join(lines) + "\n"


@problem(
    title="Cây thông Noel nhiều tầng",
    difficulty=3,
    comparator="lines",
    statement="""
        Giáng sinh sắp đến, cả nhà cùng vẽ một cây thông Noel gồm m tầng lá xếp chồng lên nhau,
        tầng dưới to hơn tầng trên, và một thân cây nhỏ ở dưới cùng.

        Đầu vào:
        - Một số nguyên m là số tầng lá.

        Đầu ra:
        - Các tầng lá được in lần lượt từ tầng 1 (trên cùng) đến tầng m (dưới cùng).
        - Tầng thứ t gồm t + 1 dòng; dòng thứ r của tầng đó (r = 1, 2, ..., t + 1) gồm
          đúng m + 1 - r dấu cách, rồi đến 2r - 1 dấu * viết liền nhau.
        - Sau tầng cuối cùng là thân cây gồm 2 dòng, mỗi dòng gồm đúng m dấu cách rồi một dấu #.
        - Như vậy mọi dòng đều được căn giữa trên chiều rộng 2m + 1.

        Giới hạn:
        - 1 ≤ m ≤ 8.

        Gợi ý:
        - Với m = 1, cây có 4 dòng: (1 dấu cách, 1 dấu *), (3 dấu *), rồi 2 dòng (1 dấu cách, 1 dấu #).
    """,
    tests=["2\n", "1\n", "3\n", "4\n", "5\n", "6\n", "7\n", "8\n"],
)
def solve_cay_thong(inp):
    m = int(inp.split()[0])
    lines = []
    for t in range(1, m + 1):
        for r in range(1, t + 2):
            lines.append(" " * (m + 1 - r) + "*" * (2 * r - 1))
    for _ in range(2):
        lines.append(" " * m + "#")
    return "\n".join(lines) + "\n"


@problem(
    title="Chiếc diều khung tre của bạn Tí",
    difficulty=3,
    comparator="lines",
    statement="""
        Bạn Tí làm một chiếc diều hình thoi bằng những thanh tre mảnh. Chiếc diều chỉ có khung viền
        bên ngoài làm bằng dấu *, bên trong là giấy trắng nên để trống.

        Đầu vào:
        - Một số nguyên n là số dòng của nửa trên chiếc diều (tính cả dòng rộng nhất).

        Đầu ra:
        - In ra 2n - 1 dòng. Với mỗi giá trị i, dòng tương ứng được vẽ như sau:
        - Nếu i = 1: gồm n - 1 dấu cách rồi một dấu *.
        - Nếu i > 1: gồm n - i dấu cách, một dấu *, rồi 2i - 3 dấu cách, rồi một dấu *.
        - Các dòng lần lượt ứng với i = 1, 2, ..., n, rồi i = n - 1, n - 2, ..., 1.

        Giới hạn:
        - 1 ≤ n ≤ 15.

        Gợi ý:
        - Đây chính là bài viên kim cương, nhưng mỗi dòng chỉ giữ lại dấu * đầu tiên và dấu * cuối cùng.
        - Với n = 2, chiếc diều có 3 dòng: (1 dấu cách, 1 dấu *), (dấu *, 1 dấu cách, dấu *), (1 dấu cách, 1 dấu *).
    """,
    tests=["4\n", "1\n", "2\n", "3\n", "5\n", "7\n", "10\n", "15\n"],
)
def solve_dieu(inp):
    n = int(inp.split()[0])
    lines = []
    for k in range(1, 2 * n):
        i = min(k, 2 * n - k)
        if i == 1:
            lines.append(" " * (n - 1) + "*")
        else:
            lines.append(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")
    return "\n".join(lines) + "\n"


@problem(
    title="Con rắn zíc zắc trên bãi cát",
    difficulty=3,
    comparator="lines",
    statement="""
        Một chú rắn bò trên bãi cát để lại vết hình zíc zắc: bò chéo lên, rồi chéo xuống, rồi lại chéo lên...
        Em hãy vẽ lại vết rắn bò trên một bức tranh có h dòng và w cột.

        Đầu vào:
        - Một dòng gồm hai số nguyên h và w cách nhau một dấu cách: h là số dòng, w là số cột.

        Đầu ra:
        - In ra h dòng. Đánh số dòng từ 1 (trên cùng) đến h (dưới cùng), số cột từ 1 đến w.
        - Mỗi cột có đúng một dấu *, mọi ô khác là dấu cách.
        - Cột 1: dấu * ở dòng h (dưới cùng). Sang mỗi cột tiếp theo, dấu * nhích lên trên một dòng,
          cho đến khi chạm dòng 1; sau đó mỗi cột lại nhích xuống một dòng cho đến khi chạm dòng h;
          rồi lại nhích lên... cứ thế cho đến cột w.
        - Dấu cách ở đầu dòng và ở giữa dòng phải in đúng; dấu cách ở cuối dòng có hay không đều được.

        Giới hạn:
        - 2 ≤ h ≤ 6, h ≤ w ≤ 40.

        Gợi ý:
        - Với h = 2, dấu * đổi qua lại giữa dòng 2 và dòng 1 ở mỗi cột.
        - Có thể tạo một bảng h x w toàn dấu cách, đặt dấu * vào từng cột, rồi in bảng ra.
    """,
    tests=["3 9\n", "2 2\n", "2 7\n", "3 3\n", "4 10\n", "5 17\n", "6 25\n", "4 40\n"],
)
def solve_zic_zac(inp):
    h, w = map(int, inp.split()[:2])
    grid = [[" "] * w for _ in range(h)]
    period = 2 * h - 2
    for j in range(1, w + 1):
        p = (j - 1) % period
        row = h - p if p < h else p - h + 2
        grid[row - 1][j - 1] = "*"
    lines = ["".join(r).rstrip() for r in grid]
    return "\n".join(lines) + "\n"


@problem(
    title="Hình vuông lồng nhau của ốc sên",
    difficulty=3,
    comparator="lines",
    statement="""
        Chú ốc sên bò thành những vòng vuông lồng vào nhau. Ở chính giữa là vòng số 1, bao quanh nó là
        vòng số 2, rồi vòng số 3... và vòng ngoài cùng là vòng số n.

        Đầu vào:
        - Một số nguyên n là số vòng.

        Đầu ra:
        - In ra một hình vuông gồm 2n - 1 dòng, mỗi dòng gồm 2n - 1 chữ số viết liền nhau.
        - Đánh số dòng và cột từ 1. Ô ở dòng i, cột j ghi chữ số 1 + max(|i - n|, |j - n|),
          trong đó |x| là giá trị tuyệt đối của x và max(a, b) là số lớn hơn trong hai số a, b.
        - Như vậy ô chính giữa là 1 và toàn bộ viền ngoài cùng là chữ số n.

        Giới hạn:
        - 1 ≤ n ≤ 9.

        Gợi ý:
        - Với n = 2, hình vuông có 3 dòng: 222, 212, 222.
    """,
    tests=["3\n", "1\n", "2\n", "4\n", "5\n", "6\n", "8\n", "9\n"],
)
def solve_oc_sen(inp):
    n = int(inp.split()[0])
    size = 2 * n - 1
    lines = []
    for i in range(1, size + 1):
        row = ""
        for j in range(1, size + 1):
            row += str(1 + max(abs(i - n), abs(j - n)))
        lines.append(row)
    return "\n".join(lines) + "\n"
