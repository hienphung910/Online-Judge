"""
Chu de 1: Lam quen - Nhap va xuat (K001-K030).

Nhung chuong trinh DAU TIEN cua cac em: doc du lieu, in ket qua, ghep chu va so
dung dinh dang. Khong dung if/else, khong vong lap, khong mang. Bai "Kho" o day
chi kho ve DINH DANG (bu so 0, dau ngan cach, nhieu dong co nhan).
"""

from kidslib import problem

TOPIC = "nhap-xuat"


# =====================================================================
#                              DỄ (10 bài)
# =====================================================================

@problem(
    title="Con vẹt Lóc Cóc nhại số",
    difficulty=1,
    statement="""
        Con vẹt Lóc Cóc rất thích bắt chước. Ai đọc cho nó nghe số nào, nó nhắc lại
        đúng số đó. Em hãy viết chương trình làm chú vẹt nhé!

        Đầu vào:
        - Một dòng chứa một số nguyên n.

        Đầu ra:
        - In ra đúng số n.

        Giới hạn:
        - -10^9 ≤ n ≤ 10^9.

        Gợi ý:
        - Đọc số vào một biến rồi in biến đó ra màn hình.
    """,
    tests=["7", "0", "-5", "1000000000", "-1000000000", "2024", "123456789", "-42"],
)
def solve(inp):
    n = int(inp.split()[0])
    return f"{n}\n"


@problem(
    title="Robot Bi chào bạn mới",
    difficulty=1,
    statement="""
        Robot Bi vừa được lắp loa và đang tập nói. Mỗi khi gặp một bạn mới,
        Bi muốn chào thật lễ phép.

        Đầu vào:
        - Một dòng chứa tên của bạn mới (chỉ gồm chữ cái tiếng Anh, không có dấu cách).

        Đầu ra:
        - In ra một dòng: Xin chao, <tên>!
        - Chú ý: có dấu phẩy ngay sau chữ "chao" và dấu chấm than viết liền ngay sau tên.

        Giới hạn:
        - Tên dài từ 1 đến 20 ký tự.
    """,
    tests=["An", "Binh", "X", "Phuong", "Hoangminhkhoa", "Lan", "Khoa", "Bi"],
)
def solve(inp):
    name = inp.split()[0]
    return f"Xin chao, {name}!\n"


@problem(
    title="Tiếng vọng trong hang núi",
    difficulty=1,
    statement="""
        Tí đứng trước cửa hang núi và hét thật to một từ. Tiếng vọng dội lại
        đúng ba lần!

        Đầu vào:
        - Một dòng chứa một từ (chỉ gồm chữ cái tiếng Anh, không có dấu cách).

        Đầu ra:
        - In từ đó ba lần trên cùng một dòng, giữa hai từ có một dấu cách.

        Giới hạn:
        - Từ dài từ 1 đến 20 ký tự.
    """,
    tests=["alo", "a", "Hello", "meo", "XinChao", "OiOi", "bum", "Tarzan"],
)
def solve(inp):
    w = inp.split()[0]
    return f"{w} {w} {w}\n"


@problem(
    title="Bạn nhỏ năm nay mấy tuổi",
    difficulty=1,
    statement="""
        Ngày đầu năm học, cô giáo giới thiệu từng bạn trong lớp bằng một câu
        thật ngắn. Em hãy giúp cô viết câu giới thiệu.

        Đầu vào:
        - Dòng 1: tên của bạn (chỉ gồm chữ cái tiếng Anh, không có dấu cách).
        - Dòng 2: một số nguyên là tuổi của bạn.

        Đầu ra:
        - In ra một dòng: Ban <tên> nam nay <tuổi> tuoi

        Giới hạn:
        - Tên dài không quá 20 ký tự.
        - 1 ≤ tuổi ≤ 100.
    """,
    tests=["An\n9", "Binh\n10", "Chi\n1", "Bao\n100", "Lan\n8", "Tuan\n14", "Hoa\n7", "Quan\n12"],
)
def solve(inp):
    name, age = inp.split()[:2]
    return f"Ban {name} nam nay {int(age)} tuoi\n"


@problem(
    title="Hai chú thỏ đổi chỗ",
    difficulty=1,
    statement="""
        Hai chú thỏ mặc áo số a và số b đang đứng cạnh nhau. Khi chụp ảnh,
        hai chú muốn đổi chỗ cho nhau.

        Đầu vào:
        - Một dòng chứa hai số nguyên a và b, cách nhau một dấu cách.

        Đầu ra:
        - In ra b rồi đến a trên cùng một dòng, cách nhau một dấu cách.

        Giới hạn:
        - 0 ≤ a, b ≤ 10^6.
    """,
    tests=lambda r: ["3 8", "1 1", "0 5", "1000000 0"]
    + [f"{r.randint(0, 10**6)} {r.randint(0, 10**6)}" for _ in range(4)],
)
def solve(inp):
    a, b = inp.split()[:2]
    return f"{int(b)} {int(a)}\n"


@problem(
    title="Ba quả bóng bay xếp hàng dọc",
    difficulty=1,
    statement="""
        Ba quả bóng bay ghi ba con số đang nằm thành một hàng ngang. Gió thổi,
        chúng bay lên và xếp thành một cột dọc!

        Đầu vào:
        - Một dòng chứa ba số nguyên a, b, c, cách nhau một dấu cách.

        Đầu ra:
        - In ra a, b, c theo đúng thứ tự đó, mỗi số trên một dòng.

        Giới hạn:
        - -10^6 ≤ a, b, c ≤ 10^6.
    """,
    tests=lambda r: ["1 2 3", "5 5 5", "0 -1 7", "-1000000 1000000 0"]
    + [" ".join(str(r.randint(-10**6, 10**6)) for _ in range(3)) for _ in range(3)],
)
def solve(inp):
    a, b, c = (int(x) for x in inp.split()[:3])
    return f"{a}\n{b}\n{c}\n"


@problem(
    title="Bạn đứng giữa hàng",
    difficulty=1,
    statement="""
        Ba bạn nhỏ xếp thành một hàng từ thấp đến cao. Cô giáo muốn biết chiều cao
        của bạn đứng ở giữa hàng.

        Đầu vào:
        - Một dòng chứa ba số nguyên a, b, c là chiều cao (cm) của ba bạn theo thứ tự
          trong hàng, cách nhau một dấu cách.

        Đầu ra:
        - In ra chiều cao của bạn đứng giữa.

        Giới hạn:
        - 80 ≤ a ≤ b ≤ c ≤ 200.

        Gợi ý:
        - Em vẫn phải đọc đủ cả ba số, nhưng chỉ in ra một số.
    """,
    tests=lambda r: ["120 125 131", "100 100 100", "80 81 200", "80 200 200", "80 80 81"]
    + [" ".join(map(str, sorted(r.randint(80, 200) for _ in range(3)))) for _ in range(3)],
)
def solve(inp):
    a, b, c = (int(x) for x in inp.split()[:3])
    return f"{b}\n"


@problem(
    title="Cây cầu gạch ngang nối hai từ",
    difficulty=1,
    statement="""
        Mai muốn ghép hai từ thành một từ ghép. Giữa hai từ, Mai bắc một "cây cầu"
        là dấu gạch ngang.

        Đầu vào:
        - Một dòng chứa hai từ (chỉ gồm chữ cái tiếng Anh), cách nhau một dấu cách.

        Đầu ra:
        - In ra một dòng: <từ 1>-<từ 2>
        - Không có dấu cách nào trong kết quả.

        Giới hạn:
        - Mỗi từ dài từ 1 đến 20 ký tự.
    """,
    tests=["keo mut", "a b", "ban be", "mat troi", "cau vong", "Ha Noi", "XIN chao", "hoa sen"],
)
def solve(inp):
    a, b = inp.split()[:2]
    return f"{a}-{b}\n"


@problem(
    title="Hai nhà hàng xóm của số n",
    difficulty=1,
    statement="""
        Trên con đường số, mỗi số đều có hai nhà hàng xóm: số liền trước (nhỏ hơn
        nó 1 đơn vị) và số liền sau (lớn hơn nó 1 đơn vị).

        Đầu vào:
        - Một dòng chứa một số nguyên n.

        Đầu ra:
        - In ra số liền trước rồi đến số liền sau của n, trên cùng một dòng,
          cách nhau một dấu cách.

        Giới hạn:
        - -10^9 ≤ n ≤ 10^9.

        Gợi ý:
        - Số liền trước của n là n - 1, số liền sau là n + 1.
    """,
    tests=["5", "0", "1", "-1", "1000000000", "-1000000000", "99", "-73"],
)
def solve(inp):
    n = int(inp.split()[0])
    return f"{n - 1} {n + 1}\n"


@problem(
    title="Ghép họ và tên cho thẻ học sinh",
    difficulty=1,
    statement="""
        Phiếu đăng ký ghi tên trước, họ sau. Nhưng trên thẻ học sinh thì phải
        ghi họ trước rồi mới đến tên.

        Đầu vào:
        - Dòng 1: tên của học sinh.
        - Dòng 2: họ của học sinh.
        - Họ và tên đều chỉ gồm chữ cái tiếng Anh, không có dấu cách.

        Đầu ra:
        - In ra một dòng: <họ> <tên> (họ trước, tên sau, cách nhau một dấu cách).

        Giới hạn:
        - Họ và tên mỗi phần dài không quá 20 ký tự.
    """,
    tests=["An\nNguyen", "Binh\nTran", "Y\nTo", "Dung\nPham", "Hoa\nHoang", "Khoa\nVu",
           "Lan\nDang", "Minh\nBui"],
)
def solve(inp):
    first, last = inp.split()[:2]
    return f"{last} {first}\n"


# =====================================================================
#                              VỪA (12 bài)
# =====================================================================

@problem(
    title="Thẻ khám bệnh cho thú cưng",
    difficulty=2,
    statement="""
        Phòng khám thú y của bác sĩ Gấu làm cho mỗi con vật một tấm thẻ gồm ba dòng.
        Em hãy giúp bác sĩ in thẻ thật đúng mẫu.

        Đầu vào:
        - Dòng 1: tên con vật.
        - Dòng 2: loài của con vật (ví dụ: meo, cho, tho).
        - Dòng 3: một số nguyên là tuổi của con vật.

        Đầu ra:
        - Dòng 1: Ten: <tên>
        - Dòng 2: Loai: <loài>
        - Dòng 3: Tuoi: <tuổi>

        Giới hạn:
        - Tên và loài là một từ gồm chữ cái tiếng Anh, dài không quá 20 ký tự.
        - 0 ≤ tuổi ≤ 30.
    """,
    tests=["Muop\nmeo\n3", "Vang\ncho\n5", "Bong\ntho\n1", "Ki\nchim\n0", "Rua\nrua\n30",
           "Mic\nhamster\n2", "Lu\ncho\n12"],
)
def solve(inp):
    name, kind, age = inp.split()[:3]
    return f"Ten: {name}\nLoai: {kind}\nTuoi: {int(age)}\n"


@problem(
    title="Tọa độ kho báu của hải tặc",
    difficulty=2,
    statement="""
        Thuyền trưởng Râu Đỏ ghi vị trí kho báu bằng hai số x và y. Trên tấm bản đồ,
        vị trí phải được viết theo kiểu toán học, gọi là tọa độ.

        Đầu vào:
        - Một dòng chứa hai số nguyên x và y, cách nhau một dấu cách.

        Đầu ra:
        - In ra một dòng: (x, y)
        - Nghĩa là: dấu mở ngoặc tròn, số x, dấu phẩy, một dấu cách, số y,
          dấu đóng ngoặc tròn. Dấu ngoặc viết liền với số.

        Giới hạn:
        - -1000 ≤ x, y ≤ 1000.
    """,
    tests=lambda r: ["3 5", "0 0", "-1000 1000", "7 -2", "1000 -1000"]
    + [f"{r.randint(-1000, 1000)} {r.randint(-1000, 1000)}" for _ in range(3)],
)
def solve(inp):
    x, y = (int(t) for t in inp.split()[:2])
    return f"({x}, {y})\n"


@problem(
    title="Đoàn tàu năm toa quay đầu",
    difficulty=2,
    statement="""
        Đoàn tàu đồ chơi của Nam có 5 toa, mỗi toa ghi một con số. Khi tàu quay đầu,
        toa cuối cùng trở thành toa đầu tiên!

        Đầu vào:
        - Một dòng chứa đúng 5 số nguyên, cách nhau một dấu cách.

        Đầu ra:
        - In 5 số đó theo thứ tự ngược lại (số cuối in trước), trên cùng một dòng,
          cách nhau một dấu cách.

        Giới hạn:
        - Mỗi số từ 0 đến 10^6.
    """,
    tests=lambda r: ["1 2 3 4 5", "5 5 5 5 5", "0 0 0 0 1", "1000000 0 1000000 0 7"]
    + [" ".join(str(r.randint(0, 10**6)) for _ in range(5)) for _ in range(4)],
)
def solve(inp):
    a, b, c, d, e = (int(x) for x in inp.split()[:5])
    return f"{e} {d} {c} {b} {a}\n"


@problem(
    title="Cô giáo viết phép cộng lên bảng",
    difficulty=2,
    statement="""
        Cô giáo đọc to hai số. Bạn trực nhật phải viết cả phép cộng lên bảng
        để cả lớp cùng xem.

        Đầu vào:
        - Một dòng chứa hai số nguyên a và b, cách nhau một dấu cách.

        Đầu ra:
        - In ra một dòng dạng: a + b = <tổng của a và b>
        - Giữa mỗi số và dấu "+", dấu "=" có đúng một dấu cách.

        Giới hạn:
        - 0 ≤ a, b ≤ 10^6.
    """,
    tests=lambda r: ["3 5", "0 0", "1000000 1000000", "0 7", "12 0"]
    + [f"{r.randint(0, 10**6)} {r.randint(0, 10**6)}" for _ in range(3)],
)
def solve(inp):
    a, b = (int(x) for x in inp.split()[:2])
    return f"{a} + {b} = {a + b}\n"


@problem(
    title="Bé Na đổi kẹo hai chiếc hộp",
    difficulty=2,
    statement="""
        Hộp A có a viên kẹo, hộp B có b viên kẹo. Bé Na đổ kẹo của hai hộp
        đổi cho nhau: kẹo hộp A sang hộp B, kẹo hộp B sang hộp A.
        Bây giờ mỗi hộp có bao nhiêu viên kẹo?

        Đầu vào:
        - Một dòng chứa hai số nguyên a và b, cách nhau một dấu cách.

        Đầu ra:
        - Dòng 1: Hop A: <số kẹo trong hộp A sau khi đổi>
        - Dòng 2: Hop B: <số kẹo trong hộp B sau khi đổi>

        Giới hạn:
        - 0 ≤ a, b ≤ 1000.
    """,
    tests=lambda r: ["4 9", "0 12", "7 7", "1000 0"]
    + [f"{r.randint(0, 1000)} {r.randint(0, 1000)}" for _ in range(4)],
)
def solve(inp):
    a, b = (int(x) for x in inp.split()[:2])
    return f"Hop A: {b}\nHop B: {a}\n"


@problem(
    title="Địa chỉ email đầu tiên của em",
    difficulty=2,
    statement="""
        Trường cấp cho mỗi học sinh một địa chỉ email. Địa chỉ được ghép từ tên,
        năm sinh và phần đuôi @school.vn.

        Đầu vào:
        - Dòng 1: tên của học sinh (chỉ gồm chữ cái thường tiếng Anh, không có dấu cách).
        - Dòng 2: một số nguyên là năm sinh.

        Đầu ra:
        - In ra một dòng: <tên><năm sinh>@school.vn
        - Các phần viết liền nhau, không có dấu cách.

        Giới hạn:
        - Tên dài không quá 15 ký tự.
        - 2005 ≤ năm sinh ≤ 2020.
    """,
    tests=["an\n2015", "binh\n2012", "chi\n2005", "khoa\n2020", "phuong\n2016", "minh\n2013",
           "y\n2018", "thanhtrung\n2010"],
)
def solve(inp):
    name, year = inp.split()[:2]
    return f"{name}{int(year)}@school.vn\n"


@problem(
    title="Tỉ số trận bóng giờ ra chơi",
    difficulty=2,
    statement="""
        Giờ ra chơi, hai đội bóng của trường thi đấu với nhau. Bác bảo vệ cần
        ghi tỉ số lên bảng thật đúng kiểu.

        Đầu vào:
        - Dòng 1: tên đội nhà và tên đội khách (mỗi tên là một từ gồm chữ cái
          tiếng Anh), cách nhau một dấu cách.
        - Dòng 2: hai số nguyên x và y là số bàn thắng của đội nhà và đội khách.

        Đầu ra:
        - In ra một dòng: <đội nhà> <x> - <y> <đội khách>
        - Các phần cách nhau đúng một dấu cách.

        Giới hạn:
        - Tên đội dài không quá 20 ký tự.
        - 0 ≤ x, y ≤ 20.
    """,
    tests=lambda r: ["SuTu HoXam\n2 1", "DaiBang CaMap\n0 0", "KienLua OngVang\n20 0",
                     "Rong Phuong\n0 20"]
    + [" ".join(r.sample(["Soc", "Voi", "Cop", "Bao", "Ngua", "Tho", "Cao", "Gau"], 2))
       + f"\n{r.randint(0, 9)} {r.randint(0, 9)}" for _ in range(4)],
)
def solve(inp):
    home, away, x, y = inp.split()[:4]
    return f"{home} {int(x)} - {int(y)} {away}\n"


@problem(
    title="Danh sách đồ đi dã ngoại",
    difficulty=2,
    statement="""
        Ngày mai lớp em đi dã ngoại. Mẹ dặn Bin viết ra ba món đồ cần mang theo
        thành một câu cho dễ nhớ.

        Đầu vào:
        - Một dòng chứa ba từ (chỉ gồm chữ cái thường tiếng Anh), cách nhau một dấu cách.

        Đầu ra:
        - In ra một dòng: Can mang: <từ 1>, <từ 2>, <từ 3>.
        - Sau mỗi dấu phẩy có một dấu cách. Cuối dòng có dấu chấm viết liền
          ngay sau từ thứ ba.

        Giới hạn:
        - Mỗi từ dài từ 1 đến 20 ký tự.
    """,
    tests=["mu nuoc banh", "o giay keo", "a b c", "ao mu khan", "bong sach but", "tao cam nho",
           "leu den chan"],
)
def solve(inp):
    a, b, c = inp.split()[:3]
    return f"Can mang: {a}, {b}, {c}.\n"


@problem(
    title="Tên lửa giấy đếm ba nhịp",
    difficulty=2,
    statement="""
        Tên lửa giấy của Tú chỉ bay lên sau khi đếm ngược đúng ba nhịp,
        bắt đầu từ số n.

        Đầu vào:
        - Một dòng chứa một số nguyên n.

        Đầu ra:
        - In ra trên cùng một dòng: số n, số n - 1, số n - 2, rồi chữ Bay!
        - Các phần cách nhau một dấu cách.

        Giới hạn:
        - 3 ≤ n ≤ 1000.
    """,
    tests=lambda r: ["10", "3", "1000", "5", "100"]
    + [str(x) for x in r.sample([v for v in range(6, 1000) if v not in (10, 100)], 3)],
)
def solve(inp):
    n = int(inp.split()[0])
    return f"{n} {n - 1} {n - 2} Bay!\n"


@problem(
    title="Giấy khen cuối năm học",
    difficulty=2,
    statement="""
        Cuối năm học, nhà trường in giấy khen cho các bạn học sinh giỏi.
        Em hãy giúp cô văn thư in giấy khen thật đúng mẫu.

        Đầu vào:
        - Dòng 1: tên học sinh (chỉ gồm chữ cái tiếng Anh, không có dấu cách).
        - Dòng 2: lớp của học sinh (một chữ số từ 1 đến 5 và một chữ cái in hoa, ví dụ 4B).

        Đầu ra: in ra đúng 4 dòng
        - Dòng 1: GIAY KHEN
        - Dòng 2: Tang ban: <tên>
        - Dòng 3: Lop: <lớp>
        - Dòng 4: Chuc mung <tên>!

        Giới hạn:
        - Tên dài không quá 20 ký tự.
    """,
    tests=["An\n3A", "Binh\n5C", "Y\n1A", "Phuong\n4B", "Khoa\n2D", "Lan\n5A", "Tuan\n1E"],
)
def solve(inp):
    name, cls = inp.split()[:2]
    return f"GIAY KHEN\nTang ban: {name}\nLop: {cls}\nChuc mung {name}!\n"


@problem(
    title="Thiệp mừng sinh nhật tuổi mới",
    difficulty=2,
    statement="""
        Hôm nay là sinh nhật của một bạn nhỏ. Bố mẹ muốn in một tấm thiệp hai dòng:
        một lời chúc và một lời hẹn cho năm sau.

        Đầu vào:
        - Dòng 1: tên của bạn nhỏ (chỉ gồm chữ cái tiếng Anh, không có dấu cách).
        - Dòng 2: một số nguyên n là số tuổi của bạn hôm nay.

        Đầu ra:
        - Dòng 1: Chuc mung sinh nhat <tên>!
        - Dòng 2: Nam sau <tên> se <n + 1> tuoi.
        - Dòng 2 có dấu chấm viết liền ngay sau chữ "tuoi".

        Giới hạn:
        - Tên dài không quá 20 ký tự.
        - 1 ≤ n ≤ 99.
    """,
    tests=["Na\n8", "Bom\n1", "Linh\n99", "Huy\n10", "Mai\n13", "Tung\n6", "Vy\n9"],
)
def solve(inp):
    name, n = inp.split()[:2]
    n = int(n)
    return f"Chuc mung sinh nhat {name}!\nNam sau {name} se {n + 1} tuoi.\n"


@problem(
    title="Robot Bi nhắc lại cả câu",
    difficulty=2,
    statement="""
        Robot Bi đã biết nhắc lại cả một câu dài chứ không chỉ một từ. Mỗi lần nói,
        Bi bắt đầu bằng "Bi noi:" rồi đặt cả câu vào trong dấu ngoặc kép.

        Đầu vào:
        - Một dòng là một câu gồm một hoặc nhiều từ, các từ cách nhau đúng một dấu cách.

        Đầu ra:
        - In ra một dòng: Bi noi: "<câu>"
        - Dấu ngoặc kép viết liền với chữ đầu và chữ cuối của câu.

        Giới hạn:
        - Câu dài từ 1 đến 100 ký tự, chỉ gồm chữ cái tiếng Anh, chữ số và dấu cách.

        Gợi ý:
        - Câu có dấu cách nên em phải đọc cả dòng một lần, không đọc từng từ
          (ví dụ: getline trong C++, nextLine trong Java, input() trong Python).
    """,
    tests=["Xin chao cac ban", "Hom nay troi dep qua", "A", "Toi yeu lap trinh",
           "1 2 3 Bat dau", "Bi la robot thong minh nhat lop", "Chung ta cung choi nhe", "OK"],
)
def solve(inp):
    line = inp.split("\n")[0].rstrip("\r")
    return f'Bi noi: "{line}"\n'


# =====================================================================
#                              KHÓ (8 bài)
# =====================================================================

@problem(
    title="Số báo danh bốn chữ số",
    difficulty=3,
    statement="""
        Trong kỳ thi Toán tuổi thơ, số báo danh luôn được viết đủ 4 chữ số.
        Số nào ít chữ số hơn thì thêm các chữ số 0 vào phía trước, ví dụ số 8
        được viết là 0008.

        Đầu vào:
        - Một dòng chứa một số nguyên n là số báo danh.

        Đầu ra:
        - In ra một dòng: So bao danh: <n viết đủ 4 chữ số>

        Giới hạn:
        - 1 ≤ n ≤ 9999.

        Gợi ý:
        - Python: f"{n:04d}"; C++: printf("%04d", n); Java: String.format("%04d", n).
    """,
    tests=["42", "7", "9999", "100", "1000", "1", "305", "2024", "10"],
)
def solve(inp):
    n = int(inp.split()[0])
    return f"So bao danh: {n:04d}\n"


@problem(
    title="Đồng hồ điện tử trên bụng robot",
    difficulty=3,
    statement="""
        Chiếc đồng hồ điện tử trên bụng robot Bi luôn hiện giờ và phút, mỗi phần
        đúng 2 chữ số, ngăn cách bằng dấu hai chấm. Ví dụ 6 giờ 8 phút hiện là 06:08.

        Đầu vào:
        - Một dòng chứa hai số nguyên h và m (giờ và phút), cách nhau một dấu cách.

        Đầu ra:
        - In ra một dòng: hh:mm (giờ đủ 2 chữ số, dấu hai chấm, phút đủ 2 chữ số,
          không có dấu cách).

        Giới hạn:
        - 0 ≤ h ≤ 23, 0 ≤ m ≤ 59.

        Gợi ý:
        - Python: f"{h:02d}:{m:02d}"; C++: printf("%02d:%02d", h, m).
    """,
    tests=["9 45", "0 0", "23 59", "12 0", "7 5", "10 10", "0 9", "18 3"],
)
def solve(inp):
    h, m = (int(x) for x in inp.split()[:2])
    return f"{h:02d}:{m:02d}\n"


@problem(
    title="Tờ lịch ngày sinh nhật",
    difficulty=3,
    statement="""
        Bé Thảo muốn ghi ngày sinh nhật của các bạn lên tờ lịch theo kiểu dd/mm/yyyy:
        ngày đủ 2 chữ số, tháng đủ 2 chữ số, năm đủ 4 chữ số, ngăn cách bằng dấu
        gạch chéo "/".

        Đầu vào:
        - Một dòng chứa ba số nguyên d, m, y (ngày, tháng, năm), cách nhau một dấu cách.

        Đầu ra:
        - In ra một dòng: dd/mm/yyyy (không có dấu cách).

        Giới hạn:
        - d, m, y luôn tạo thành một ngày có thật.
        - 1 ≤ d ≤ 31, 1 ≤ m ≤ 12, 1900 ≤ y ≤ 2100.

        Gợi ý:
        - Thêm chữ số 0 vào trước ngày hoặc tháng chỉ có 1 chữ số.
    """,
    tests=["5 3 2015", "1 1 2000", "31 12 2099", "29 2 2016", "10 10 2010", "9 11 1999",
           "15 6 2024", "1 10 1900"],
)
def solve(inp):
    d, m, y = (int(x) for x in inp.split()[:3])
    return f"{d:02d}/{m:02d}/{y:04d}\n"


@problem(
    title="Mã thẻ thư viện trường em",
    difficulty=3,
    statement="""
        Thư viện trường làm thẻ mượn sách cho học sinh. Mã thẻ gồm chữ TV, tên lớp
        và số thứ tự của học sinh trong lớp (luôn viết đủ 2 chữ số), nối với nhau
        bằng dấu gạch ngang.

        Đầu vào:
        - Dòng 1: tên lớp (một chữ số từ 1 đến 5 và một chữ cái in hoa, ví dụ 4B).
        - Dòng 2: một số nguyên n là số thứ tự của học sinh.

        Đầu ra:
        - In ra một dòng: TV-<lớp>-<n viết đủ 2 chữ số>
        - Không có dấu cách nào trong mã thẻ.

        Giới hạn:
        - 1 ≤ n ≤ 99.
    """,
    tests=["4B\n7", "1A\n1", "5E\n99", "3C\n10", "2D\n35", "5A\n9", "1B\n50"],
)
def solve(inp):
    cls, n = inp.split()[:2]
    return f"TV-{cls}-{int(n):02d}\n"


@problem(
    title="Phiếu báo điểm ba môn",
    difficulty=3,
    statement="""
        Cuối học kỳ, cô giáo gửi về nhà phiếu báo điểm ghi điểm ba môn Toán,
        Văn, Anh và tổng điểm của cả ba môn.

        Đầu vào:
        - Dòng 1: tên học sinh (chỉ gồm chữ cái tiếng Anh, không có dấu cách).
        - Dòng 2: ba số nguyên t, v, a là điểm Toán, Văn, Anh, cách nhau một dấu cách.

        Đầu ra: in ra đúng 5 dòng
        - Dòng 1: Hoc sinh: <tên>
        - Dòng 2: Toan: <t>
        - Dòng 3: Van: <v>
        - Dòng 4: Anh: <a>
        - Dòng 5: Tong diem: <t + v + a>

        Giới hạn:
        - 0 ≤ t, v, a ≤ 10.
    """,
    tests=lambda r: ["An\n9 8 10", "Binh\n0 0 0", "Chi\n10 10 10", "Dung\n5 0 7"]
    + [f"{name}\n{r.randint(0, 10)} {r.randint(0, 10)} {r.randint(0, 10)}"
       for name in ["Khoa", "Lan", "Minh"]],
)
def solve(inp):
    name, t, v, a = inp.split()[:4]
    t, v, a = int(t), int(v), int(a)
    return f"Hoc sinh: {name}\nToan: {t}\nVan: {v}\nAnh: {a}\nTong diem: {t + v + a}\n"


@problem(
    title="Vé xem phim cuối tuần",
    difficulty=3,
    statement="""
        Rạp chiếu phim thiếu nhi in vé cho các bạn nhỏ đi xem phim cuối tuần.
        Mỗi chiếc vé có đúng 5 dòng thông tin.

        Đầu vào:
        - Dòng 1: tên phim (một từ gồm chữ cái tiếng Anh, không có dấu cách).
        - Dòng 2: một số nguyên p là số phòng chiếu.
        - Dòng 3: hàng ghế (một chữ cái in hoa) và số ghế s, cách nhau một dấu cách.
        - Dòng 4: hai số nguyên h và m là giờ và phút của suất chiếu.

        Đầu ra: in ra đúng 5 dòng
        - Dòng 1: VE XEM PHIM
        - Dòng 2: Phim: <tên phim>
        - Dòng 3: Phong: <p>
        - Dòng 4: Ghe: <hàng ghế><s viết đủ 2 chữ số> (viết liền, ví dụ hàng C ghế 7 là C07)
        - Dòng 5: Gio chieu: <hh:mm> (giờ và phút đều đủ 2 chữ số)

        Giới hạn:
        - Tên phim dài không quá 30 ký tự.
        - 1 ≤ p ≤ 20, 1 ≤ s ≤ 30, 0 ≤ h ≤ 23, 0 ≤ m ≤ 59.
    """,
    tests=["KhoBauDaoXanh\n3\nE 12\n9 30", "MeoMuopPhieuLuu\n1\nA 1\n0 0",
           "RobotBiVaoVuTru\n20\nZ 30\n23 59", "ChuVitDiHoc\n12\nB 10\n14 5",
           "ChuyenCuaGio\n7\nH 9\n19 45", "RungXanh\n5\nK 15\n8 0", "BienXanh\n9\nD 3\n16 20"],
)
def solve(inp):
    film, p, row, s, h, m = inp.split()[:6]
    return (f"VE XEM PHIM\nPhim: {film}\nPhong: {int(p)}\n"
            f"Ghe: {row}{int(s):02d}\nGio chieu: {int(h):02d}:{int(m):02d}\n")


@problem(
    title="Tin nhắn hẹn đi sở thú",
    difficulty=3,
    statement="""
        Cả lớp hẹn nhau đi sở thú xem hươu cao cổ. Lớp trưởng cần gửi tin nhắn
        ghi rõ ngày và giờ hẹn để không bạn nào đến nhầm.

        Đầu vào:
        - Dòng 1: ba số nguyên d, m, y (ngày, tháng, năm), cách nhau một dấu cách.
        - Dòng 2: hai số nguyên h, p (giờ, phút), cách nhau một dấu cách.

        Đầu ra:
        - In ra một dòng: Hen gap ngay <dd/mm/yyyy> luc <hh:mm>
        - Ngày, tháng, giờ, phút đều viết đủ 2 chữ số; năm viết đủ 4 chữ số.

        Giới hạn:
        - d, m, y luôn tạo thành một ngày có thật; 1900 ≤ y ≤ 2100.
        - 0 ≤ h ≤ 23, 0 ≤ p ≤ 59.
    """,
    tests=["20 11 2024\n7 30", "1 1 2000\n0 0", "31 12 2099\n23 59", "5 6 2025\n8 5",
           "9 9 2019\n15 0", "28 2 2023\n10 45", "15 4 2026\n9 9"],
)
def solve(inp):
    d, m, y, h, p = (int(x) for x in inp.split()[:5])
    return f"Hen gap ngay {d:02d}/{m:02d}/{y:04d} luc {h:02d}:{p:02d}\n"


@problem(
    title="Hộ chiếu của robot Bi",
    difficulty=3,
    statement="""
        Robot Bi sắp được đi du lịch vòng quanh thế giới nên cần một cuốn hộ chiếu.
        Em hãy in trang thông tin của hộ chiếu thật đúng mẫu.

        Đầu vào:
        - Dòng 1: tên robot (một từ gồm chữ cái tiếng Anh, không có dấu cách).
        - Dòng 2: một số nguyên n là số hiệu của robot.
        - Dòng 3: ba số nguyên d, m, y là ngày, tháng, năm chế tạo.
        - Dòng 4: một số nguyên c là chiều cao của robot (cm).

        Đầu ra: in ra đúng 5 dòng
        - Dòng 1: HO CHIEU ROBOT
        - Dòng 2: Ten: <tên>
        - Dòng 3: So hieu: R-<n viết đủ 3 chữ số>
        - Dòng 4: Ngay che tao: <dd/mm/yyyy>
        - Dòng 5: Chieu cao: <c> cm

        Giới hạn:
        - Tên dài không quá 20 ký tự.
        - 1 ≤ n ≤ 999; 10 ≤ c ≤ 300.
        - d, m, y luôn tạo thành một ngày có thật; 1900 ≤ y ≤ 2100.
    """,
    tests=["Bi\n7\n5 3 2024\n120", "Bo\n1\n1 1 1900\n10", "Titan\n999\n31 12 2100\n300",
           "Ben\n42\n9 9 2009\n85", "Ziko\n100\n20 10 2020\n150", "Mimi\n15\n1 6 2015\n60",
           "Rex\n500\n12 7 2030\n205"],
)
def solve(inp):
    name, n, d, m, y, c = inp.split()[:6]
    n, d, m, y, c = int(n), int(d), int(m), int(y), int(c)
    return (f"HO CHIEU ROBOT\nTen: {name}\nSo hieu: R-{n:03d}\n"
            f"Ngay che tao: {d:02d}/{m:02d}/{y:04d}\nChieu cao: {c} cm\n")
