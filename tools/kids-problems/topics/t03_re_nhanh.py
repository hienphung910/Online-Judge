"""Chu de 3: Re nhanh if / else (K061-K090).

Chi dung: nhap/xuat, phep tinh, if / else if / else, va / hoac.
Khong dung vong lap, khong dung mang.
"""

from kidslib import problem

TOPIC = "re-nhanh"


# ===================================================================== DỄ (1)

@problem(
    title="Mướp đếm cá: chẵn hay lẻ?",
    difficulty=1,
    statement="""
        Chú mèo Mướp vừa câu được n con cá. Mướp muốn chia đều số cá cho mình và em gái, nên cần biết n là số chẵn hay số lẻ.

        Đầu vào:
        - Một số nguyên n là số con cá Mướp câu được.

        Đầu ra:
        - In ra CHAN nếu n là số chẵn, in ra LE nếu n là số lẻ (viết hoa, không dấu).

        Giới hạn:
        - 0 ≤ n ≤ 10^9

        Gợi ý:
        - n là số chẵn khi n chia cho 2 có số dư bằng 0. Số 0 cũng là số chẵn.
    """,
    tests=["12", "7", "0", "1", "2", "345", "999999999", "1000000000"],
)
def solve(inp):
    n = int(inp.split()[0])
    if n % 2 == 0:
        return "CHAN\n"
    else:
        return "LE\n"


@problem(
    title="Nhiệt kế của gấu trắng Bắc Cực",
    difficulty=1,
    statement="""
        Gấu trắng Pô sống ở Bắc Cực. Sáng nào Pô cũng xem nhiệt kế để biết hôm nay trời trên 0 độ, dưới 0 độ hay đúng bằng 0 độ.

        Đầu vào:
        - Một số nguyên t là nhiệt độ hôm nay (độ C).

        Đầu ra:
        - In ra DUONG nếu t lớn hơn 0.
        - In ra AM nếu t nhỏ hơn 0.
        - In ra KHONG nếu t bằng 0.

        Giới hạn:
        - -100 ≤ t ≤ 100
    """,
    tests=["-15", "8", "0", "-1", "1", "100", "-100", "-37"],
)
def solve(inp):
    t = int(inp.split()[0])
    if t > 0:
        return "DUONG\n"
    elif t < 0:
        return "AM\n"
    else:
        return "KHONG\n"


@problem(
    title="Ếch Xanh cách nhà bao nhiêu bước?",
    difficulty=1,
    statement="""
        Ếch Xanh sống bên một con đường thẳng được đánh số giống trục số, nhà của ếch ở vị trí 0. Bây giờ ếch đang đứng ở vị trí x, mỗi bước nhảy dài đúng 1 đơn vị. Hỏi ếch phải nhảy bao nhiêu bước để về đến nhà?

        Đầu vào:
        - Một số nguyên x là vị trí hiện tại của ếch (có thể âm).

        Đầu ra:
        - In ra một số nguyên là số bước ếch cần nhảy, tức là khoảng cách từ x đến 0.

        Giới hạn:
        - -10^9 ≤ x ≤ 10^9

        Gợi ý:
        - Nếu x nhỏ hơn 0 thì khoảng cách là -x, ngược lại khoảng cách là x.
    """,
    tests=["-7", "5", "0", "-1", "42", "-999", "1000000000", "-1000000000"],
)
def solve(inp):
    x = int(inp.split()[0])
    if x < 0:
        x = -x
    return f"{x}\n"


@problem(
    title="Điền dấu so sánh giúp cô giáo",
    difficulty=1,
    statement="""
        Cô giáo viết hai số a và b lên bảng và để trống một ô ở giữa. Em hãy giúp cô điền dấu đúng vào ô trống: lớn hơn, bé hơn hay bằng nhau.

        Đầu vào:
        - Một dòng chứa hai số nguyên a và b, cách nhau một dấu cách.

        Đầu ra:
        - In ra đúng một ký tự: > nếu a lớn hơn b, < nếu a bé hơn b, = nếu a bằng b.

        Giới hạn:
        - -10^9 ≤ a, b ≤ 10^9
    """,
    tests=["5 3", "2 9", "4 4", "-3 -5", "-8 1", "0 0",
           "1000000000 -1000000000", "-1000000000 -999999999"],
)
def solve(inp):
    a, b = map(int, inp.split()[:2])
    if a > b:
        return ">\n"
    elif a < b:
        return "<\n"
    else:
        return "=\n"


@problem(
    title="Bạn Sóc thi bằng lái xe đạp",
    difficulty=1,
    statement="""
        Khu rừng Xanh tổ chức thi bằng lái xe đạp cho các con vật. Bài thi chấm theo thang điểm 100, ai được từ 80 điểm trở lên thì đạt. Bạn Sóc vừa thi xong và rất hồi hộp chờ kết quả.

        Đầu vào:
        - Một số nguyên d là điểm thi của Sóc.

        Đầu ra:
        - In ra DAT nếu d lớn hơn hoặc bằng 80.
        - Ngược lại in ra CHUA DAT.

        Giới hạn:
        - 0 ≤ d ≤ 100
    """,
    tests=["92", "45", "80", "79", "100", "0", "81", "60"],
)
def solve(inp):
    d = int(inp.split()[0])
    if d >= 80:
        return "DAT\n"
    else:
        return "CHUA DAT\n"


@problem(
    title="An và Bình, ai lớn tuổi hơn?",
    difficulty=1,
    statement="""
        An và Bình tranh luận xem ai lớn tuổi hơn. Hai bạn quyết định chỉ so năm sinh: ai sinh vào năm nhỏ hơn thì người đó lớn tuổi hơn, sinh cùng năm thì coi như bằng tuổi.

        Đầu vào:
        - Một dòng chứa hai số nguyên a và b, cách nhau một dấu cách: a là năm sinh của An, b là năm sinh của Bình.

        Đầu ra:
        - In ra AN nếu An lớn tuổi hơn.
        - In ra BINH nếu Bình lớn tuổi hơn.
        - In ra BANG TUOI nếu hai bạn sinh cùng năm.

        Giới hạn:
        - 1900 ≤ a, b ≤ 2025
    """,
    tests=["2014 2016", "2017 2013", "2015 2015", "1900 2025",
           "2025 1900", "2012 2013", "2020 2020", "2011 2010"],
)
def solve(inp):
    a, b = map(int, inp.split()[:2])
    if a < b:
        return "AN\n"
    elif a > b:
        return "BINH\n"
    else:
        return "BANG TUOI\n"


@problem(
    title="Con số thần kỳ của Thỏ Ngọc",
    difficulty=1,
    statement="""
        Thỏ Ngọc rất thích các con số. Thỏ gọi một số là "thần kỳ" nếu nó chia hết cho cả 3 và 5. Em hãy giúp Thỏ kiểm tra số n.

        Đầu vào:
        - Một số nguyên n.

        Đầu ra:
        - In ra YES nếu n chia hết cho cả 3 và 5.
        - Ngược lại in ra NO.

        Giới hạn:
        - 1 ≤ n ≤ 10^9

        Gợi ý:
        - Dùng phép "và" để ghép hai điều kiện: n chia 3 dư 0 và n chia 5 dư 0.
    """,
    tests=["30", "9", "10", "15", "7", "1", "45", "999999990", "1000000000"],
)
def solve(inp):
    n = int(inp.split()[0])
    if n % 3 == 0 and n % 5 == 0:
        return "YES\n"
    else:
        return "NO\n"


@problem(
    title="Bốn mùa trong năm của Gấu Con",
    difficulty=1,
    statement="""
        Gấu Con hỏi bà: "Tháng này là mùa gì hả bà?". Bà dạy Gấu Con: tháng 1, 2, 3 là mùa xuân; tháng 4, 5, 6 là mùa hạ; tháng 7, 8, 9 là mùa thu; tháng 10, 11, 12 là mùa đông.

        Đầu vào:
        - Một số nguyên m là số thứ tự của tháng.

        Đầu ra:
        - In ra tên mùa, viết hoa không dấu: XUAN, HA, THU hoặc DONG.

        Giới hạn:
        - 1 ≤ m ≤ 12
    """,
    tests=["5", "1", "3", "4", "6", "7", "9", "10", "12"],
)
def solve(inp):
    m = int(inp.split()[0])
    if m <= 3:
        return "XUAN\n"
    elif m <= 6:
        return "HA\n"
    elif m <= 9:
        return "THU\n"
    else:
        return "DONG\n"


@problem(
    title="Giá vé vào Vườn thú Rừng Xanh",
    difficulty=1,
    statement="""
        Vườn thú Rừng Xanh bán vé theo tuổi của khách. Em hãy giúp cô bán vé tính giá vé cho từng người nhé!

        Bảng giá vé:
        - Dưới 6 tuổi: miễn phí (0 đồng).
        - Từ 6 đến 15 tuổi: 20000 đồng.
        - Từ 16 đến 59 tuổi: 50000 đồng.
        - Từ 60 tuổi trở lên: 25000 đồng.

        Đầu vào:
        - Một số nguyên t là tuổi của khách.

        Đầu ra:
        - In ra một số nguyên là giá vé (đồng). Nếu được miễn phí thì in 0.

        Giới hạn:
        - 0 ≤ t ≤ 120
    """,
    tests=["10", "3", "0", "5", "6", "15", "16", "59", "60", "90"],
)
def solve(inp):
    t = int(inp.split()[0])
    if t < 6:
        price = 0
    elif t <= 15:
        price = 20000
    elif t <= 59:
        price = 50000
    else:
        price = 25000
    return f"{price}\n"


@problem(
    title="Chim sáo đọc tên các thứ trong tuần",
    difficulty=1,
    statement="""
        Chú chim sáo nhà Na đang tập nói tên các ngày trong tuần. Na giơ một tấm thẻ ghi số từ 2 đến 8: số 2 là thứ Hai, số 3 là thứ Ba, ..., số 7 là thứ Bảy, còn số 8 là Chủ Nhật. Em hãy giúp sáo đọc đúng tên ngày.

        Đầu vào:
        - Một số nguyên n ghi trên tấm thẻ.

        Đầu ra:
        - In ra tên ngày, viết không dấu và viết hoa chữ cái đầu mỗi từ đúng như bảng sau:
        - 2: Thu Hai
        - 3: Thu Ba
        - 4: Thu Tu
        - 5: Thu Nam
        - 6: Thu Sau
        - 7: Thu Bay
        - 8: Chu Nhat

        Giới hạn:
        - 2 ≤ n ≤ 8
    """,
    tests=["4", "2", "3", "5", "6", "7", "8"],
)
def solve(inp):
    n = int(inp.split()[0])
    if n == 2:
        name = "Thu Hai"
    elif n == 3:
        name = "Thu Ba"
    elif n == 4:
        name = "Thu Tu"
    elif n == 5:
        name = "Thu Nam"
    elif n == 6:
        name = "Thu Sau"
    elif n == 7:
        name = "Thu Bay"
    else:
        name = "Chu Nhat"
    return name + "\n"


# ==================================================================== VỪA (2)

@problem(
    title="Quả dưa hấu nặng nhất vườn ông nội",
    difficulty=2,
    statement="""
        Ông nội vừa hái được ba quả dưa hấu nặng a, b và c lạng. Bạn Tí muốn chọn quả nặng nhất để mang đi dự hội thi "Dưa hấu khổng lồ" của xóm.

        Đầu vào:
        - Một dòng chứa ba số nguyên a, b, c, cách nhau một dấu cách.

        Đầu ra:
        - In ra một số nguyên là khối lượng của quả dưa nặng nhất.

        Giới hạn:
        - 1 ≤ a, b, c ≤ 10^9

        Gợi ý:
        - Gán m = a. Nếu b lớn hơn m thì gán m = b, rồi làm tương tự với c.
    """,
    tests=["12 30 25", "50 20 10", "3 9 40", "7 7 7", "9 2 9",
           "5 8 8", "1000000000 1 999999999", "1 1 2"],
)
def solve(inp):
    a, b, c = map(int, inp.split()[:3])
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return f"{m}\n"


@problem(
    title="Ong Vàng học nguyên âm tiếng Anh",
    difficulty=2,
    statement="""
        Trong giờ học tiếng Anh, cô giáo dạy Ong Vàng: trong bảng chữ cái tiếng Anh có 5 nguyên âm là a, e, i, o, u; 21 chữ cái còn lại đều là phụ âm. Em hãy giúp Ong Vàng phân loại một chữ cái.

        Đầu vào:
        - Một chữ cái thường tiếng Anh (từ a đến z).

        Đầu ra:
        - In ra NGUYEN AM nếu chữ cái là một trong a, e, i, o, u.
        - Ngược lại in ra PHU AM.

        Gợi ý:
        - Dùng phép "hoặc" để ghép 5 điều kiện so sánh.
    """,
    tests=["e", "b", "a", "u", "z", "i", "o", "y", "m"],
)
def solve(inp):
    c = inp.split()[0]
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        return "NGUYEN AM\n"
    else:
        return "PHU AM\n"


@problem(
    title="Xếp loại bài kiểm tra của lớp 4A",
    difficulty=2,
    statement="""
        Cô giáo lớp 4A chấm bài kiểm tra theo thang điểm 100 rồi xếp loại cho từng bạn. Em hãy viết chương trình xếp loại giúp cô.

        Cách xếp loại:
        - Từ 80 điểm trở lên: Gioi
        - Từ 65 đến 79 điểm: Kha
        - Từ 50 đến 64 điểm: Trung binh
        - Dưới 50 điểm: Yeu

        Đầu vào:
        - Một số nguyên d là điểm của học sinh.

        Đầu ra:
        - In ra loại học lực, viết không dấu và đúng chữ hoa chữ thường như trên: Gioi, Kha, Trung binh hoặc Yeu.

        Giới hạn:
        - 0 ≤ d ≤ 100
    """,
    tests=["72", "80", "79", "65", "64", "50", "49", "0", "100"],
)
def solve(inp):
    d = int(inp.split()[0])
    if d >= 80:
        return "Gioi\n"
    elif d >= 65:
        return "Kha\n"
    elif d >= 50:
        return "Trung binh\n"
    else:
        return "Yeu\n"


@problem(
    title="Trò chơi Bíp Bốp giờ ra chơi",
    difficulty=2,
    statement="""
        Giờ ra chơi, cả lớp chơi trò đếm số "Bíp Bốp". Đến lượt ai thì người đó nhận một số n và phải hô thật nhanh theo luật của trò chơi.

        Luật chơi:
        - Nếu n chia hết cho cả 3 và 5: hô BipBop
        - Nếu n chỉ chia hết cho 3: hô Bip
        - Nếu n chỉ chia hết cho 5: hô Bop
        - Nếu n không chia hết cho 3 và cũng không chia hết cho 5: đọc chính số n

        Đầu vào:
        - Một số nguyên n.

        Đầu ra:
        - In ra BipBop, Bip, Bop (đúng chữ hoa chữ thường) hoặc in ra số n.

        Giới hạn:
        - 1 ≤ n ≤ 10^9

        Gợi ý:
        - Hãy kiểm tra trường hợp chia hết cho cả 3 và 5 trước tiên.
    """,
    tests=["9", "10", "15", "7", "1", "3", "5",
           "999999990", "1000000000", "999999999"],
)
def solve(inp):
    n = int(inp.split()[0])
    if n % 3 == 0 and n % 5 == 0:
        return "BipBop\n"
    elif n % 3 == 0:
        return "Bip\n"
    elif n % 5 == 0:
        return "Bop\n"
    else:
        return f"{n}\n"


@problem(
    title="Sinh nhật 29 tháng 2 của bạn Nhím",
    difficulty=2,
    statement="""
        Bạn Nhím sinh ngày 29 tháng 2, nên chỉ được tổ chức sinh nhật đúng ngày vào những năm nhuận. Năm nhuận là năm chia hết cho 400, hoặc chia hết cho 4 nhưng không chia hết cho 100. Em hãy cho Nhím biết năm y có phải năm nhuận không.

        Đầu vào:
        - Một số nguyên y là số năm.

        Đầu ra:
        - In ra YES nếu y là năm nhuận, ngược lại in ra NO.

        Giới hạn:
        - 1 ≤ y ≤ 100000

        Gợi ý:
        - Năm 2000 là năm nhuận (chia hết cho 400), còn năm 1900 không phải năm nhuận (chia hết cho 100 nhưng không chia hết cho 400).
    """,
    tests=["2024", "2023", "1900", "2000", "2100", "2400",
           "4", "1", "100000", "2026"],
)
def solve(inp):
    y = int(inp.split()[0])
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        return "YES\n"
    else:
        return "NO\n"


@problem(
    title="Cột đèn giao thông ở ngã tư nhà Na",
    difficulty=2,
    statement="""
        Cột đèn ở ngã tư nhà Na đổi màu theo một vòng lặp dài 60 giây. Lúc bắt đầu đếm (giây thứ 0) đèn vừa chuyển sang màu xanh. Na muốn biết ở giây thứ t thì đèn đang có màu gì.

        Trong mỗi vòng 60 giây:
        - Từ giây thứ 0 đến giây thứ 29: đèn xanh.
        - Từ giây thứ 30 đến giây thứ 32: đèn vàng.
        - Từ giây thứ 33 đến giây thứ 59: đèn đỏ.
        - Giây thứ 60 đèn lại xanh giống như giây thứ 0, giây thứ 61 giống giây thứ 1, và cứ thế lặp lại.

        Đầu vào:
        - Một số nguyên t là số giây tính từ lúc bắt đầu đếm.

        Đầu ra:
        - In ra XANH, VANG hoặc DO là màu của đèn ở giây thứ t.

        Giới hạn:
        - 0 ≤ t ≤ 10^9

        Gợi ý:
        - Lấy số dư r khi chia t cho 60, rồi xem r rơi vào khoảng nào.
    """,
    tests=["45", "0", "29", "30", "32", "33", "59", "60", "92", "1000000000"],
)
def solve(inp):
    t = int(inp.split()[0])
    r = t % 60
    if r <= 29:
        return "XANH\n"
    elif r <= 32:
        return "VANG\n"
    else:
        return "DO\n"


@problem(
    title="Oẳn tù tì với robot Bi",
    difficulty=2,
    statement="""
        An chơi oẳn tù tì với robot Bi. Mỗi bên ra một trong ba thứ: Búa, Kéo hoặc Bao. Luật chơi: Búa thắng Kéo, Kéo thắng Bao, Bao thắng Búa; hai bên ra giống nhau thì hòa.

        Đầu vào:
        - Một dòng chứa hai từ cách nhau một dấu cách: từ thứ nhất là lựa chọn của An, từ thứ hai là lựa chọn của Bi. Mỗi từ là BUA, KEO hoặc BAO.

        Đầu ra:
        - In ra AN nếu An thắng.
        - In ra BI nếu Bi thắng.
        - In ra HOA nếu hai bên hòa.
    """,
    tests=["BUA KEO", "BAO BUA", "KEO BAO", "KEO BUA", "BUA BAO",
           "BAO KEO", "BUA BUA", "KEO KEO", "BAO BAO"],
)
def solve(inp):
    a, b = inp.split()[:2]
    if a == b:
        return "HOA\n"
    elif (a == "BUA" and b == "KEO") or (a == "KEO" and b == "BAO") or (a == "BAO" and b == "BUA"):
        return "AN\n"
    else:
        return "BI\n"


@problem(
    title="Kho báu nằm ở góc phần tư nào?",
    difficulty=2,
    statement="""
        Tấm bản đồ kho báu được vẽ trên mặt phẳng tọa độ Oxy. Hai trục Ox và Oy chia bản đồ thành bốn góc phần tư. Em hãy cho đội thám hiểm biết kho báu ở điểm (x, y) nằm ở góc nào.

        Bốn góc phần tư:
        - Góc 1: x > 0 và y > 0
        - Góc 2: x < 0 và y > 0
        - Góc 3: x < 0 và y < 0
        - Góc 4: x > 0 và y < 0

        Đầu vào:
        - Một dòng chứa hai số nguyên x và y, cách nhau một dấu cách.

        Đầu ra:
        - In ra số thứ tự của góc phần tư (1, 2, 3 hoặc 4).
        - Nếu kho báu nằm ngay trên một trục tọa độ (x = 0 hoặc y = 0) thì in ra 0.

        Giới hạn:
        - -10^9 ≤ x, y ≤ 10^9
    """,
    tests=["3 5", "-2 7", "-4 -1", "6 -9", "0 5", "7 0", "0 0",
           "-1000000000 1000000000", "1 -1"],
)
def solve(inp):
    x, y = map(int, inp.split()[:2])
    if x == 0 or y == 0:
        q = 0
    elif x > 0 and y > 0:
        q = 1
    elif x < 0 and y > 0:
        q = 2
    elif x < 0 and y < 0:
        q = 3
    else:
        q = 4
    return f"{q}\n"


@problem(
    title="Đồng hồ điện tử của Tí có bị lỗi?",
    difficulty=2,
    statement="""
        Chiếc đồng hồ điện tử của Tí thỉnh thoảng bị lỗi và hiện ra những con số kỳ lạ. Một thời điểm hợp lệ phải có giờ từ 0 đến 23, phút từ 0 đến 59 và giây từ 0 đến 59. Em hãy kiểm tra giúp Tí.

        Đầu vào:
        - Một dòng chứa ba số nguyên h, m, s (giờ, phút, giây) cách nhau một dấu cách.

        Đầu ra:
        - In ra YES nếu thời điểm h giờ m phút s giây hợp lệ.
        - Ngược lại in ra NO.

        Giới hạn:
        - 0 ≤ h, m, s ≤ 99
    """,
    tests=["7 30 15", "24 0 0", "23 59 59", "0 0 0", "12 60 0",
           "12 30 60", "99 99 99", "23 0 59", "10 75 20"],
)
def solve(inp):
    h, m, s = map(int, inp.split()[:3])
    if h <= 23 and m <= 59 and s <= 59:
        return "YES\n"
    else:
        return "NO\n"


@problem(
    title="Sáng nay ai đến lớp sớm hơn?",
    difficulty=2,
    statement="""
        Sáng nay An và Bình đều đến lớp rất sớm. Cô giáo ghi lại giờ và phút lúc mỗi bạn bước vào lớp. Em hãy cho biết bạn nào đến sớm hơn.

        Đầu vào:
        - Dòng thứ nhất chứa hai số nguyên h1 và m1: An đến lớp lúc h1 giờ m1 phút.
        - Dòng thứ hai chứa hai số nguyên h2 và m2: Bình đến lớp lúc h2 giờ m2 phút.
        - Cả hai thời điểm đều trong cùng một ngày.

        Đầu ra:
        - In ra AN nếu An đến sớm hơn.
        - In ra BINH nếu Bình đến sớm hơn.
        - In ra CUNG LUC nếu hai bạn đến cùng một lúc.

        Giới hạn:
        - 5 ≤ h1, h2 ≤ 11
        - 0 ≤ m1, m2 ≤ 59

        Gợi ý:
        - Đổi mỗi thời điểm ra số phút tính từ 0 giờ: h * 60 + m, rồi so sánh hai số đó.
    """,
    tests=["6 45\n6 50", "7 5\n6 58", "6 30\n6 30", "6 59\n7 0",
           "7 0\n6 59", "6 10\n7 5", "8 5\n7 50", "5 0\n11 59", "11 59\n5 0"],
)
def solve(inp):
    h1, m1, h2, m2 = map(int, inp.split()[:4])
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    if t1 < t2:
        return "AN\n"
    elif t1 > t2:
        return "BINH\n"
    else:
        return "CUNG LUC\n"


@problem(
    title="Robot Bi phân loại ký tự bàn phím",
    difficulty=2,
    statement="""
        Robot Bi nhặt được một phím rơi ra từ chiếc bàn phím cũ. Bi muốn biết ký tự in trên phím đó là chữ hoa, chữ thường, chữ số hay một ký hiệu khác.

        Đầu vào:
        - Một ký tự ASCII nhìn thấy được (không phải dấu cách).

        Đầu ra:
        - In ra CHU HOA nếu đó là chữ cái in hoa (từ A đến Z).
        - In ra CHU THUONG nếu đó là chữ cái thường (từ a đến z).
        - In ra CHU SO nếu đó là chữ số (từ 0 đến 9).
        - In ra KHAC trong các trường hợp còn lại.

        Gợi ý:
        - Ký tự c là chữ in hoa khi c lớn hơn hoặc bằng 'A' và c nhỏ hơn hoặc bằng 'Z'.
    """,
    tests=["G", "A", "Z", "a", "z", "m", "0", "9", "@", "{"],
)
def solve(inp):
    c = inp.strip()[0]
    if "A" <= c and c <= "Z":
        return "CHU HOA\n"
    elif "a" <= c and c <= "z":
        return "CHU THUONG\n"
    elif "0" <= c and c <= "9":
        return "CHU SO\n"
    else:
        return "KHAC\n"


@problem(
    title="Ba que kem có ghép thành tam giác?",
    difficulty=2,
    statement="""
        Ăn kem xong, Tí giữ lại ba que kem dài a, b và c xăng-ti-mét. Tí muốn ghép ba que thành một hình tam giác. Ba que ghép được thành tam giác khi tổng độ dài của hai que bất kỳ luôn lớn hơn độ dài que còn lại.

        Đầu vào:
        - Một dòng chứa ba số nguyên a, b, c, cách nhau một dấu cách.

        Đầu ra:
        - In ra YES nếu ba que ghép được thành tam giác, ngược lại in ra NO.

        Giới hạn:
        - 1 ≤ a, b, c ≤ 10^6

        Gợi ý:
        - Cần kiểm tra cả ba điều kiện: a + b > c, a + c > b và b + c > a.
    """,
    tests=["3 4 5", "1 2 3", "5 5 5", "10 2 3", "2 10 3", "2 3 10",
           "2 2 3", "1000000 1000000 1", "1 1 1000000"],
)
def solve(inp):
    a, b, c = map(int, inp.split()[:3])
    if a + b > c and a + c > b and b + c > a:
        return "YES\n"
    else:
        return "NO\n"


# ===================================================================== KHÓ (3)

@problem(
    title="Bức tranh của Na có vừa khung không?",
    difficulty=3,
    statement="""
        Na vẽ một bức tranh hình chữ nhật có hai cạnh dài a và b. Na muốn lồng tranh vào một chiếc khung hình chữ nhật có hai cạnh dài c và d. Na được phép xoay tranh (đổi chiều ngang thành chiều dọc), nhưng không được đặt tranh nằm nghiêng, và tranh vừa khít với khung cũng được tính là vừa.

        Đầu vào:
        - Dòng thứ nhất chứa hai số nguyên a và b: kích thước bức tranh.
        - Dòng thứ hai chứa hai số nguyên c và d: kích thước chiếc khung.

        Đầu ra:
        - In ra YES nếu Na lồng được tranh vào khung, ngược lại in ra NO.

        Giới hạn:
        - 1 ≤ a, b, c, d ≤ 10^9

        Gợi ý:
        - Thử cả hai cách đặt tranh: (a ≤ c và b ≤ d) hoặc (a ≤ d và b ≤ c).
    """,
    tests=["20 30\n35 25", "10 20\n10 20", "5 8\n6 9", "30 10\n15 40",
           "10 50\n40 40", "41 39\n40 40", "40 40\n40 40",
           "1 1000000000\n1000000000 1", "7 7\n6 100", "3 9\n8 4"],
)
def solve(inp):
    a, b, c, d = map(int, inp.split()[:4])
    if (a <= c and b <= d) or (a <= d and b <= c):
        return "YES\n"
    else:
        return "NO\n"


@problem(
    title="Tờ lịch tháng này có mấy ngày?",
    difficulty=3,
    statement="""
        Bà nội có cuốn lịch treo tường, mỗi ngày bà xé một tờ. Bống muốn biết tháng m của năm y có bao nhiêu tờ lịch, tức là tháng đó có bao nhiêu ngày.

        Số ngày của các tháng:
        - Tháng 1, 3, 5, 7, 8, 10, 12 có 31 ngày.
        - Tháng 4, 6, 9, 11 có 30 ngày.
        - Tháng 2 có 29 ngày nếu y là năm nhuận, có 28 ngày nếu không phải.
        - Năm nhuận là năm chia hết cho 400, hoặc chia hết cho 4 nhưng không chia hết cho 100.

        Đầu vào:
        - Một dòng chứa hai số nguyên m và y (tháng và năm), cách nhau một dấu cách.

        Đầu ra:
        - In ra một số nguyên là số ngày của tháng m năm y.

        Giới hạn:
        - 1 ≤ m ≤ 12
        - 1 ≤ y ≤ 100000
    """,
    tests=["2 2024", "4 2023", "2 2023", "2 1900", "2 2000",
           "12 1", "11 100000", "7 2025", "8 2025", "6 2026"],
)
def solve(inp):
    m, y = map(int, inp.split()[:2])
    if m == 2:
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            days = 29
        else:
            days = 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        days = 30
    else:
        days = 31
    return f"{days}\n"


@problem(
    title="Xếp hàng từ thấp đến cao giờ thể dục",
    difficulty=3,
    statement="""
        Trong giờ thể dục, thầy giáo gọi ba bạn lên đứng thành một hàng từ thấp đến cao. Em hãy giúp thầy sắp xếp chiều cao của ba bạn mà không cần dùng vòng lặp nhé.

        Đầu vào:
        - Một dòng chứa ba số nguyên a, b, c là chiều cao của ba bạn (xăng-ti-mét), cách nhau một dấu cách.

        Đầu ra:
        - In ra ba chiều cao theo thứ tự từ nhỏ đến lớn trên một dòng, cách nhau một dấu cách. Các chiều cao bằng nhau đứng cạnh nhau.

        Giới hạn:
        - 1 ≤ a, b, c ≤ 1000

        Gợi ý:
        - Nếu a > b thì đổi chỗ a và b. Sau đó nếu b > c thì đổi chỗ b và c. Cuối cùng kiểm tra lại a và b một lần nữa.
    """,
    tests=["135 120 150", "120 135 150", "120 150 135", "135 150 120",
           "150 120 135", "150 135 120", "140 140 130", "125 140 125",
           "130 130 130"],
)
def solve(inp):
    a, b, c = map(int, inp.split()[:3])
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return f"{a} {b} {c}\n"


@problem(
    title="Hai bạn cùng ở thư viện bao nhiêu phút?",
    difficulty=3,
    statement="""
        Chiều nay An và Bình đều đến thư viện đọc truyện. Thời gian được tính bằng số phút kể từ lúc thư viện mở cửa: An ở thư viện từ phút a đến phút b, Bình ở thư viện từ phút c đến phút d. Hỏi có bao nhiêu phút cả hai bạn cùng có mặt trong thư viện?

        Đầu vào:
        - Dòng thứ nhất chứa hai số nguyên a và b: lúc An đến và lúc An về.
        - Dòng thứ hai chứa hai số nguyên c và d: lúc Bình đến và lúc Bình về.

        Đầu ra:
        - In ra một số nguyên là số phút hai bạn cùng ở thư viện.
        - Khoảng thời gian chung bắt đầu từ lúc bạn đến muộn hơn và kết thúc ở lúc bạn về sớm hơn. Nếu không có khoảng chung, hoặc người này về đúng lúc người kia đến, thì in ra 0.

        Giới hạn:
        - 0 ≤ a < b ≤ 1000
        - 0 ≤ c < d ≤ 1000

        Gợi ý:
        - Lúc bắt đầu chung là số lớn hơn trong hai số a, c; lúc kết thúc chung là số nhỏ hơn trong hai số b, d.
    """,
    tests=["10 50\n30 80", "0 100\n25 40", "30 47\n10 90", "10 20\n30 40",
           "50 60\n5 20", "10 30\n30 50", "40 95\n20 63", "0 1000\n0 1000",
           "7 8\n0 1000"],
)
def solve(inp):
    a, b, c, d = map(int, inp.split()[:4])
    start = a
    if c > start:
        start = c
    end = b
    if d < end:
        end = d
    if end > start:
        return f"{end - start}\n"
    else:
        return "0\n"


@problem(
    title="Tiền điện bậc thang nhà Bống",
    difficulty=3,
    statement="""
        Cuối tháng, mẹ nhờ Bống tính tiền điện. Nhà Bống dùng hết n số điện, và giá điện được tính theo bậc thang: dùng càng nhiều thì những số điện sau càng đắt.

        Bảng giá:
        - 50 số đầu tiên (từ số thứ 1 đến số thứ 50): 1700 đồng mỗi số.
        - Từ số thứ 51 đến số thứ 100: 1800 đồng mỗi số.
        - Từ số thứ 101 đến số thứ 200: 2100 đồng mỗi số.
        - Từ số thứ 201 trở đi: 2600 đồng mỗi số.

        Đầu vào:
        - Một số nguyên n là số điện nhà Bống đã dùng.

        Đầu ra:
        - In ra một số nguyên là tổng số tiền điện (đồng).

        Giới hạn:
        - 0 ≤ n ≤ 100000

        Gợi ý:
        - Nếu dùng 70 số thì tiền điện là 50 × 1700 + 20 × 1800.
    """,
    tests=["120", "0", "1", "50", "51", "100", "101", "200", "201", "100000"],
)
def solve(inp):
    n = int(inp.split()[0])
    if n <= 50:
        money = n * 1700
    elif n <= 100:
        money = 50 * 1700 + (n - 50) * 1800
    elif n <= 200:
        money = 50 * 1700 + 50 * 1800 + (n - 100) * 2100
    else:
        money = 50 * 1700 + 50 * 1800 + 100 * 2100 + (n - 200) * 2600
    return f"{money}\n"


@problem(
    title="Đồng hồ nhảy thêm một giây",
    difficulty=3,
    statement="""
        Đồng hồ của Tí đang chỉ h giờ m phút s giây. Tí muốn biết sau đúng 1 giây nữa đồng hồ sẽ chỉ mấy giờ. Đồng hồ chạy theo kiểu 24 giờ: sau 23 giờ 59 phút 59 giây là 0 giờ 0 phút 0 giây của ngày hôm sau.

        Đầu vào:
        - Một dòng chứa ba số nguyên h, m, s (giờ, phút, giây) cách nhau một dấu cách.

        Đầu ra:
        - In ra giờ, phút, giây sau 1 giây nữa trên một dòng, cách nhau một dấu cách (không cần viết thêm số 0 ở đầu).

        Giới hạn:
        - 0 ≤ h ≤ 23
        - 0 ≤ m ≤ 59
        - 0 ≤ s ≤ 59

        Gợi ý:
        - Khi giây vượt quá 59 thì giây trở về 0 và phút tăng thêm 1; phút và giờ cũng làm tương tự.
    """,
    tests=["8 15 59", "8 15 30", "8 59 59", "23 59 59", "0 0 0",
           "23 59 58", "12 59 30", "23 30 59", "22 59 59", "9 9 9"],
)
def solve(inp):
    h, m, s = map(int, inp.split()[:3])
    s = s + 1
    if s == 60:
        s = 0
        m = m + 1
        if m == 60:
            m = 0
            h = h + 1
            if h == 24:
                h = 0
    return f"{h} {m} {s}\n"


@problem(
    title="Thầy Hình Học phân loại tam giác",
    difficulty=3,
    statement="""
        Thầy Hình Học đưa cho cả lớp ba độ dài a, b, c. Thầy hỏi: ba đoạn thẳng này có tạo thành một tam giác không, và nếu có thì đó là tam giác gì?

        Đầu vào:
        - Một dòng chứa ba số nguyên a, b, c, cách nhau một dấu cách.

        Đầu ra:
        - Kiểm tra lần lượt theo thứ tự sau và in ra kết quả của điều kiện đầu tiên đúng:
        - KHONG nếu ba đoạn không tạo thành tam giác (có một đoạn lớn hơn hoặc bằng tổng hai đoạn còn lại).
        - DEU nếu cả ba cạnh bằng nhau.
        - VUONG nếu có hai cạnh mà tổng bình phương của chúng bằng bình phương cạnh còn lại.
        - CAN nếu có hai cạnh bằng nhau.
        - THUONG trong các trường hợp còn lại.

        Giới hạn:
        - 1 ≤ a, b, c ≤ 10000

        Gợi ý:
        - Không biết cạnh nào dài nhất thì hãy thử cả ba trường hợp: a*a + b*b == c*c, a*a + c*c == b*b, b*b + c*c == a*a.
    """,
    tests=["5 5 8", "7 7 7", "3 4 5", "13 12 5", "6 10 8",
           "8 5 5", "5 8 5", "4 5 6", "1 2 3", "10000 9999 1"],
)
def solve(inp):
    a, b, c = map(int, inp.split()[:3])
    if a + b <= c or a + c <= b or b + c <= a:
        return "KHONG\n"
    elif a == b and b == c:
        return "DEU\n"
    elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        return "VUONG\n"
    elif a == b or b == c or a == c:
        return "CAN\n"
    else:
        return "THUONG\n"


@problem(
    title="Ngày mai trên tờ lịch là ngày nào?",
    difficulty=3,
    statement="""
        Bống đếm từng ngày chờ đến kỳ nghỉ hè. Hôm nay là ngày d tháng m năm y, em hãy giúp Bống tìm xem ngày mai là ngày nào.

        Nhắc lại số ngày của các tháng:
        - Tháng 1, 3, 5, 7, 8, 10, 12 có 31 ngày.
        - Tháng 4, 6, 9, 11 có 30 ngày.
        - Tháng 2 có 29 ngày nếu là năm nhuận, có 28 ngày nếu không phải.
        - Năm nhuận là năm chia hết cho 400, hoặc chia hết cho 4 nhưng không chia hết cho 100.

        Đầu vào:
        - Một dòng chứa ba số nguyên d, m, y (ngày, tháng, năm) cách nhau một dấu cách. Đây luôn là một ngày có thật.

        Đầu ra:
        - In ra ngày, tháng, năm của ngày mai trên một dòng, cách nhau một dấu cách (không cần viết thêm số 0 ở đầu).

        Giới hạn:
        - 1 ≤ y ≤ 9999

        Gợi ý:
        - Tìm số ngày của tháng m trước. Nếu d chưa phải ngày cuối tháng thì chỉ cần tăng d; nếu là ngày cuối tháng thì sang ngày 1 của tháng sau (nhớ trường hợp tháng 12).
    """,
    tests=["30 4 2025", "15 8 2025", "31 12 2025", "28 2 2024", "29 2 2024",
           "28 2 2023", "28 2 1900", "28 2 2000", "30 1 2025", "31 1 2025"],
)
def solve(inp):
    d, m, y = map(int, inp.split()[:3])
    if m == 2:
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            last = 29
        else:
            last = 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        last = 30
    else:
        last = 31
    if d < last:
        d = d + 1
    else:
        d = 1
        if m < 12:
            m = m + 1
        else:
            m = 1
            y = y + 1
    return f"{d} {m} {y}\n"
