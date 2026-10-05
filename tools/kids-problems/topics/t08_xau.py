"""Chu de 8: Xau ky tu (K211-K240)."""

from kidslib import problem

TOPIC = "xau"

# ------------------------------------------------ tien ich CHI dung de sinh test
# (loi giai mau ben duoi khong duoc dung cac ham/bien nay)

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = LOWER.upper()
LETTERS = LOWER + UPPER
DIGITS = "0123456789"

WORDS = [
    "cat", "dog", "sun", "moon", "star", "apple", "banana", "robot", "pizza", "tiger",
    "rabbit", "monkey", "rainbow", "dragon", "candy", "school", "friend", "music", "panda",
    "turtle", "garden", "rocket", "pencil", "cookie", "river", "flower", "kitten", "puppy",
    "ocean", "castle", "piano", "jungle", "orange", "lemon", "zebra", "happy", "magic",
    "winter", "summer", "planet", "a", "i", "go", "we", "big", "red", "sky", "fly",
]

NAME_WORDS = [
    "nguyen", "tran", "le", "pham", "hoang", "vu", "dang", "bui", "do", "ngo", "van",
    "thi", "minh", "an", "binh", "chi", "dung", "lan", "hoa", "khoa", "linh", "nam",
    "phuong", "quang", "tam", "thao", "tuan", "vy", "gia", "bao", "ngoc", "hai",
]


def rword(r, lo, hi, alpha=LOWER):
    """Mot tu ngau nhien dai lo..hi, chi gom ky tu trong alpha (khong co xuong dong)."""
    return "".join(r.choice(alpha) for _ in range(r.randint(lo, hi)))


def rsentence(r, lo, hi, words=WORDS):
    """Mot cau ngau nhien lo..hi tu, cach nhau dung mot dau cach."""
    return " ".join(r.choice(words) for _ in range(r.randint(lo, hi)))


def rmixcase(r, s):
    """Doi ngau nhien hoa/thuong tung chu cai."""
    return "".join(c.upper() if r.random() < 0.5 else c.lower() for c in s)


def rruns(r, total_lo, total_hi, alpha, run_hi):
    """Xau gom cac nhom chu cai giong nhau dung lien nhau (de thu bai nen xau)."""
    target = r.randint(total_lo, total_hi)
    out = ""
    while len(out) < target:
        out += r.choice(alpha) * r.randint(1, run_hi)
    return out[:target]


# =================================================================== DE (1)


@problem(
    title="Tên chú rồng dài mấy chữ cái?",
    difficulty=1,
    statement="""
        Bé Na vừa đặt tên cho chú rồng bông của mình. Em hãy giúp Na đếm xem
        tên chú rồng có bao nhiêu chữ cái nhé!

        Đầu vào:
        - Một dòng chứa tên chú rồng: một từ gồm các chữ cái tiếng Anh (hoa hoặc thường),
          không có dấu cách.

        Đầu ra:
        - In ra một số nguyên: số chữ cái trong tên.

        Giới hạn:
        - Tên dài từ 1 đến 100 chữ cái.

        Gợi ý:
        - Độ dài xâu s: Python dùng len(s), C++ và Java dùng s.length().
    """,
    tests=lambda r: [
        "Lucky\n",
        "A\n",
        "Toothless\n",
        "x" * 100 + "\n",
        "Ab\n",
        rword(r, 10, 30, LETTERS),
        rword(r, 40, 99, LOWER),
        rword(r, 3, 8, UPPER),
    ],
)
def k211_do_dai_ten(inp):
    s = inp.split()[0]
    return str(len(s)) + "\n"


@problem(
    title="Loa phóng thanh của robot Bi",
    difficulty=1,
    statement="""
        Robot Bi có một chiếc loa phóng thanh thần kỳ: từ nào đi qua loa cũng được
        VIẾT HOA toàn bộ để cả sân trường nghe thật rõ.

        Đầu vào:
        - Một dòng chứa một từ gồm các chữ cái tiếng Anh (có thể lẫn chữ hoa và chữ thường),
          không có dấu cách.

        Đầu ra:
        - In ra từ đó sau khi đổi mọi chữ cái thành chữ hoa.

        Giới hạn:
        - Từ dài từ 1 đến 100 chữ cái.

        Gợi ý:
        - Python có s.upper(), Java có s.toUpperCase(), C++ có toupper() cho từng ký tự.
    """,
    tests=lambda r: [
        "hello\n",
        "a\n",
        "Z\n",
        "ABC\n",
        "robotBi\n",
        "mIxEdCaSe\n",
        rword(r, 20, 60, LETTERS),
        rword(r, 80, 100, LOWER),
    ],
)
def k212_viet_hoa(inp):
    s = inp.split()[0]
    return s.upper() + "\n"


@problem(
    title="Chữ cái mở đầu và chữ cái kết thúc",
    difficulty=1,
    statement="""
        Trong trò chơi nối từ, bạn Tí cần biết chữ cái đầu tiên và chữ cái cuối cùng
        của mỗi từ. Em hãy giúp Tí nhé!

        Đầu vào:
        - Một dòng chứa một từ gồm các chữ cái tiếng Anh (hoa hoặc thường), không có dấu cách.

        Đầu ra:
        - In ra chữ cái đầu tiên và chữ cái cuối cùng của từ, cách nhau một dấu cách.
        - Giữ nguyên chữ hoa/chữ thường như trong từ.
        - Nếu từ chỉ có 1 chữ cái thì chữ đó vừa là đầu vừa là cuối, nên in chữ đó hai lần.

        Giới hạn:
        - Từ dài từ 1 đến 100 chữ cái.
    """,
    tests=lambda r: [
        "banana\n",
        "Q\n",
        "Hello\n",
        "noon\n",
        "xY\n",
        "Elephant\n",
        rword(r, 10, 40, LETTERS),
        rword(r, 60, 100, LOWER),
    ],
)
def k213_dau_cuoi(inp):
    s = inp.split()[0]
    return s[0] + " " + s[-1] + "\n"


def _tests_k214(r):
    tests = ["rainbow\n3\n", "a\n1\n", "Hello\n1\n", "Hello\n5\n", "Mississippi\n6\n"]
    for lo, hi in ((10, 30), (40, 70), (80, 100)):
        s = rword(r, lo, hi, LETTERS)
        tests.append(f"{s}\n{r.randint(1, len(s))}\n")
    return tests


@problem(
    title="Ô vuông thứ k chứa chữ gì?",
    difficulty=1,
    statement="""
        Bạn Mi viết một từ lên tờ giấy kẻ ô, mỗi ô vuông một chữ cái. Các ô được đánh số
        1, 2, 3, ... từ trái sang phải. Em hãy cho Mi biết ô thứ k chứa chữ cái nào.

        Đầu vào:
        - Dòng 1: một từ s gồm các chữ cái tiếng Anh (hoa hoặc thường), không có dấu cách.
        - Dòng 2: một số nguyên k.

        Đầu ra:
        - In ra chữ cái ở vị trí thứ k của từ (đếm từ 1, từ trái sang phải),
          giữ nguyên chữ hoa/chữ thường.

        Giới hạn:
        - Từ dài từ 1 đến 100 chữ cái; 1 ≤ k ≤ độ dài của từ.

        Gợi ý:
        - Trong Python, C++ và Java, vị trí trong xâu được đánh số từ 0,
          nên chữ cái thứ k nằm ở chỉ số k - 1.
    """,
    tests=_tests_k214,
)
def k214_o_thu_k(inp):
    parts = inp.split()
    s = parts[0]
    k = int(parts[1])
    return s[k - 1] + "\n"


@problem(
    title="Gương thần đọc ngược từ",
    difficulty=1,
    statement="""
        Trong lâu đài có một chiếc gương thần: từ nào soi vào gương cũng bị đọc ngược,
        từ chữ cái cuối cùng về chữ cái đầu tiên. Em hãy viết chương trình làm chiếc gương ấy.

        Đầu vào:
        - Một dòng chứa một từ gồm các chữ cái tiếng Anh (hoa hoặc thường), không có dấu cách.

        Đầu ra:
        - In ra từ đó viết theo thứ tự ngược lại, giữ nguyên chữ hoa/chữ thường.

        Giới hạn:
        - Từ dài từ 1 đến 100 chữ cái.

        Gợi ý:
        - Dùng vòng lặp đi từ chữ cái cuối cùng về chữ cái đầu tiên.
    """,
    tests=lambda r: [
        "mirror\n",
        "a\n",
        "Hello\n",
        "level\n",
        "ab\n",
        "Programming\n",
        rword(r, 30, 60, LETTERS),
        rword(r, 100, 100, LOWER),
    ],
)
def k215_dao_nguoc(inp):
    s = inp.split()[0]
    return s[::-1] + "\n"


@problem(
    title="Mèo Mướp đếm chữ cái yêu thích",
    difficulty=1,
    statement="""
        Mèo Mướp rất mê một chữ cái. Mỗi khi nhìn thấy một từ, Mướp lại đếm xem
        chữ cái yêu thích của mình xuất hiện trong từ đó bao nhiêu lần.

        Đầu vào:
        - Dòng 1: một từ s gồm các chữ cái tiếng Anh (hoa hoặc thường), không có dấu cách.
        - Dòng 2: một chữ cái c (chữ cái yêu thích của Mướp).

        Đầu ra:
        - In ra số lần chữ c xuất hiện trong từ s (có thể là 0).
        - Phân biệt chữ hoa và chữ thường: chữ a và chữ A là hai chữ khác nhau.

        Giới hạn:
        - Từ dài từ 1 đến 100 chữ cái.
    """,
    tests=lambda r: [
        "banana\na\n",
        "Anna\na\n",
        "Anna\nA\n",
        "xyz\nq\n",
        "aaaaa\na\n",
        "m\nm\n",
        rword(r, 30, 80, "abc") + "\nb\n",
        rword(r, 50, 100, "xXyY") + "\nX\n",
    ],
)
def k216_dem_chu_cai(inp):
    parts = inp.split()
    s, c = parts[0], parts[1]
    count = 0
    for ch in s:
        if ch == c:
            count += 1
    return str(count) + "\n"


@problem(
    title="Nguyên âm trong tên thú cưng",
    difficulty=1,
    statement="""
        Cô giáo dạy tiếng Anh nói rằng các nguyên âm là a, e, i, o, u. Bạn Bin muốn biết
        tên chú cún của mình có bao nhiêu nguyên âm.

        Đầu vào:
        - Một dòng chứa một từ gồm các chữ cái tiếng Anh viết thường, không có dấu cách.

        Đầu ra:
        - In ra số nguyên âm có trong từ.
        - Chỉ 5 chữ a, e, i, o, u là nguyên âm. Chữ y KHÔNG được tính là nguyên âm.

        Giới hạn:
        - Từ dài từ 1 đến 100 chữ cái.
    """,
    tests=lambda r: [
        "bingo\n",
        "rhythm\n",
        "aeiou\n",
        "y\n",
        "a\n",
        "queue\n",
        "b\n",
        rword(r, 30, 80, LOWER),
        rword(r, 90, 100, LOWER),
    ],
)
def k217_dem_nguyen_am(inp):
    s = inp.split()[0]
    count = 0
    for ch in s:
        if ch in "aeiou":
            count += 1
    return str(count) + "\n"


def _tests_k218(r):
    tests = ["racecar\n", "a\n", "ab\n", "aa\n", "abca\n", "kayak\n", "abccba\n", "abcdba\n"]
    half = rword(r, 10, 25)
    tests.append(half + r.choice(LOWER) + half[::-1] + "\n")
    while True:
        s = rword(r, 20, 40)
        if s != s[::-1]:
            break
    tests.append(s + "\n")
    return tests


@problem(
    title="Từ đối xứng của cô tiên",
    difficulty=1,
    statement="""
        Cô tiên chỉ thích những từ đối xứng: đọc xuôi từ trái sang phải hay đọc ngược
        từ phải sang trái đều giống hệt nhau, ví dụ như từ "noon". Em hãy giúp cô tiên
        kiểm tra một từ nhé.

        Đầu vào:
        - Một dòng chứa một từ gồm các chữ cái tiếng Anh viết thường, không có dấu cách.

        Đầu ra:
        - In ra YES nếu từ đó đối xứng, ngược lại in ra NO.

        Giới hạn:
        - Từ dài từ 1 đến 100 chữ cái.
    """,
    tests=_tests_k218,
)
def k218_doi_xung(inp):
    s = inp.split()[0]
    return ("YES" if s == s[::-1] else "NO") + "\n"


@problem(
    title="Mật mã két sắt chỉ có chữ số?",
    difficulty=1,
    statement="""
        Chiếc két sắt của ông nội chỉ nhận mật mã gồm toàn chữ số. Bạn Tôm vừa nghĩ ra
        một mật mã. Em hãy kiểm tra xem mật mã đó có dùng được cho két sắt không.

        Đầu vào:
        - Một dòng chứa mật mã: một xâu gồm các chữ cái tiếng Anh và chữ số, không có dấu cách.

        Đầu ra:
        - In ra YES nếu mọi ký tự trong xâu đều là chữ số (từ 0 đến 9), ngược lại in ra NO.

        Giới hạn:
        - Xâu dài từ 1 đến 50 ký tự.

        Gợi ý:
        - Hãy đọc mật mã như một xâu, không đọc như một số.
    """,
    tests=lambda r: [
        "2024\n",
        "0\n",
        "a\n",
        "12a45\n",
        "abc\n",
        "00000\n",
        "1234O\n",
        "9876543210\n",
        rword(r, 50, 50, DIGITS),
        rword(r, 20, 40, DIGITS) + "x" + rword(r, 1, 5, DIGITS) + "\n",
    ],
)
def k219_toan_chu_so(inp):
    s = inp.split()[0]
    ok = True
    for ch in s:
        if ch not in "0123456789":
            ok = False
    return ("YES" if ok else "NO") + "\n"


@problem(
    title="Cây bút thần đổi chữ",
    difficulty=1,
    statement="""
        Bạn Mã Lương có một cây bút thần: chỉ cần vẽ một nét là mọi chữ x trong từ
        đều biến thành chữ y. Em hãy viết chương trình làm phép thuật của cây bút nhé.

        Đầu vào:
        - Dòng 1: một từ s gồm các chữ cái tiếng Anh (hoa hoặc thường), không có dấu cách.
        - Dòng 2: hai chữ cái x và y, cách nhau một dấu cách.

        Đầu ra:
        - In ra từ s sau khi thay mọi chữ x bằng chữ y. Các chữ khác giữ nguyên.
        - Phân biệt chữ hoa và chữ thường: nếu x là chữ a thì chỉ thay chữ a,
          không thay chữ A.

        Giới hạn:
        - Từ dài từ 1 đến 100 chữ cái.
    """,
    tests=lambda r: [
        "banana\na o\n",
        "a\na b\n",
        "Anna\nn m\n",
        "Anna\na e\n",
        "hello\nz q\n",
        "mmmm\nm M\n",
        "cat\nc c\n",
        rword(r, 40, 80, "abcAB") + "\nb z\n",
    ],
)
def k220_doi_chu(inp):
    parts = inp.split()
    s, x, y = parts[0], parts[1], parts[2]
    result = ""
    for ch in s:
        result += y if ch == x else ch
    return result + "\n"


# =================================================================== VUA (2)


@problem(
    title="Câu chuyện của bà có mấy từ?",
    difficulty=2,
    statement="""
        Tối qua bà kể cho bạn Ốc nghe một câu chuyện cổ tích. Ốc chép lại một câu
        trong truyện và muốn biết câu đó có bao nhiêu từ.

        Đầu vào:
        - Một dòng (có thể có dấu cách) chứa câu văn. Mỗi từ gồm các chữ cái tiếng Anh
          (hoa hoặc thường); hai từ liền nhau cách nhau đúng một dấu cách; không có dấu cách
          ở đầu và cuối dòng.

        Đầu ra:
        - In ra số từ trong câu.

        Giới hạn:
        - Dòng dài không quá 300 ký tự và có ít nhất một từ.

        Gợi ý:
        - Vì giữa hai từ có đúng một dấu cách, số từ = số dấu cách + 1.
    """,
    tests=lambda r: [
        "once upon a time there was a little dragon\n",
        "Hello\n",
        "a b c d e\n",
        "I am happy\n",
        rsentence(r, 10, 20) + "\n",
        rsentence(r, 25, 35) + "\n",
        rsentence(r, 2, 4) + "\n",
        "Bi\n",
    ],
)
def k221_dem_tu(inp):
    line = inp.split("\n")[0].rstrip("\r")
    return str(len(line.split())) + "\n"


def _tests_k222(r):
    tests = ["choo choo train\n", "a\n", "a  b   c\n", "I love Viet Nam\n", "x y\n", "NoSpacesHere\n"]
    words = [r.choice(WORDS) for _ in range(r.randint(8, 15))]
    line = words[0]
    for w in words[1:]:
        line += " " * r.randint(1, 4) + w
    tests.append(line + "\n")
    tests.append(rmixcase(r, rsentence(r, 15, 25)) + "\n")
    return tests


@problem(
    title="Nối liền đoàn tàu chữ cái",
    difficulty=2,
    statement="""
        Các toa tàu chữ cái đang bị tách rời bởi những khoảng trống. Em hãy nối chúng lại
        thành một đoàn tàu liền mạch bằng cách xóa hết các dấu cách.

        Đầu vào:
        - Một dòng (có thể có dấu cách) gồm các chữ cái tiếng Anh (hoa hoặc thường) và dấu cách.
        - Giữa hai từ có thể có một hoặc nhiều dấu cách; không có dấu cách ở đầu và cuối dòng.

        Đầu ra:
        - In ra dòng đó sau khi xóa hết mọi dấu cách. Các chữ cái giữ nguyên thứ tự
          và giữ nguyên chữ hoa/chữ thường.

        Giới hạn:
        - Dòng dài không quá 300 ký tự và có ít nhất một chữ cái.
    """,
    tests=_tests_k222,
)
def k222_xoa_dau_cach(inp):
    line = inp.split("\n")[0].rstrip("\r")
    result = ""
    for ch in line:
        if ch != " ":
            result += ch
    return result + "\n"


@problem(
    title="Xứ sở đảo ngược chữ hoa chữ thường",
    difficulty=2,
    statement="""
        Ở xứ sở đảo ngược, mọi thứ đều bị lật lại: chữ hoa biến thành chữ thường,
        còn chữ thường lại biến thành chữ hoa. Em hãy viết lại một câu theo kiểu của xứ sở này.

        Đầu vào:
        - Một dòng (có thể có dấu cách) gồm các chữ cái tiếng Anh (hoa hoặc thường) và dấu cách.
          Hai từ liền nhau cách nhau đúng một dấu cách; không có dấu cách ở đầu và cuối dòng.

        Đầu ra:
        - In ra câu đó sau khi đổi mỗi chữ hoa thành chữ thường và mỗi chữ thường thành
          chữ hoa. Các dấu cách giữ nguyên.

        Giới hạn:
        - Dòng dài từ 1 đến 300 ký tự.
    """,
    tests=lambda r: [
        "Hello World\n",
        "a\n",
        "Z\n",
        "ABC def\n",
        "PtIt Online Judge\n",
        rmixcase(r, rsentence(r, 8, 15)) + "\n",
        rsentence(r, 5, 10).upper() + "\n",
        rmixcase(r, rword(r, 50, 80)) + "\n",
    ],
)
def k223_dao_hoa_thuong(inp):
    line = inp.split("\n")[0].rstrip("\r")
    result = ""
    for ch in line:
        if "a" <= ch <= "z":
            result += ch.upper()
        elif "A" <= ch <= "Z":
            result += ch.lower()
        else:
            result += ch
    return result + "\n"


@problem(
    title="Viết hoa tên truyện tranh",
    difficulty=2,
    statement="""
        Bạn Gấu muốn in tên cuốn truyện tranh lên bìa thật đẹp: chữ cái đầu tiên
        của mỗi từ phải được viết hoa.

        Đầu vào:
        - Một dòng (có thể có dấu cách) chứa tên truyện, gồm các từ viết bằng chữ cái tiếng Anh
          viết thường. Hai từ liền nhau cách nhau đúng một dấu cách; không có dấu cách
          ở đầu và cuối dòng.

        Đầu ra:
        - In ra tên truyện sau khi viết hoa chữ cái đầu tiên của mỗi từ.
          Các chữ cái còn lại vẫn viết thường, các dấu cách giữ nguyên.

        Giới hạn:
        - Dòng dài từ 1 đến 300 ký tự.
    """,
    tests=lambda r: [
        "the little prince\n",
        "a\n",
        "doraemon\n",
        "x y z\n",
        "happy new year\n",
        rsentence(r, 8, 15) + "\n",
        rsentence(r, 20, 30) + "\n",
    ],
)
def k224_viet_hoa_moi_tu(inp):
    line = inp.split("\n")[0].rstrip("\r")
    words = line.split(" ")
    result = []
    for w in words:
        result.append(w[0].upper() + w[1:])
    return " ".join(result) + "\n"


@problem(
    title="Robot Bi kiểm kê kho ký tự",
    difficulty=2,
    statement="""
        Robot Bi được giao kiểm kê một chuỗi ký tự. Bi phải chia các ký tự thành ba nhóm:
        chữ hoa, chữ thường và chữ số, rồi đếm xem mỗi nhóm có bao nhiêu ký tự.

        Đầu vào:
        - Một dòng chứa một xâu gồm các chữ cái tiếng Anh (hoa hoặc thường) và chữ số,
          không có dấu cách.

        Đầu ra:
        - In ra ba số nguyên trên một dòng, cách nhau một dấu cách, theo đúng thứ tự:
          số chữ hoa (A-Z), số chữ thường (a-z), số chữ số (0-9).

        Giới hạn:
        - Xâu dài từ 1 đến 100 ký tự.
    """,
    tests=lambda r: [
        "HelloBi2024\n",
        "a\n",
        "Z\n",
        "7\n",
        "ABCdef123\n",
        "000\n",
        rword(r, 100, 100, LETTERS + DIGITS),
        rword(r, 30, 60, UPPER + DIGITS + "xyz"),
    ],
)
def k225_kiem_ke(inp):
    s = inp.split()[0]
    upper = lower = digit = 0
    for ch in s:
        if "A" <= ch <= "Z":
            upper += 1
        elif "a" <= ch <= "z":
            lower += 1
        elif "0" <= ch <= "9":
            digit += 1
    return f"{upper} {lower} {digit}\n"


def _tests_k226(r):
    tests = ["Education\n", "b\n", "rhythm\n", "AEIOUx\n", "Banana\n", "YoYo\n", "queueing\n"]
    for lo, hi in ((30, 50), (80, 99)):
        s = rword(r, lo, hi, "aeiouAEIOUbcdkmyTRS")
        tests.append(s + "z\n")
    return tests


@problem(
    title="Bức thư bị rơi mất nguyên âm",
    difficulty=2,
    statement="""
        Chú chim sẻ đưa thư bay qua cơn gió mạnh và làm rơi mất hết các nguyên âm
        trong bức thư. Em hãy viết lại xem từ trong thư trông như thế nào sau khi mất nguyên âm.

        Đầu vào:
        - Một dòng chứa một từ gồm các chữ cái tiếng Anh (hoa hoặc thường), không có dấu cách.
        - Đảm bảo từ có ít nhất một chữ cái không phải nguyên âm.

        Đầu ra:
        - In ra từ đó sau khi xóa mọi nguyên âm.
        - Nguyên âm là a, e, i, o, u và cả dạng viết hoa A, E, I, O, U.
          Chữ y và Y không phải nguyên âm nên được giữ lại.
        - Các chữ còn lại giữ nguyên thứ tự và giữ nguyên chữ hoa/chữ thường.

        Giới hạn:
        - Từ dài từ 1 đến 100 chữ cái.
    """,
    tests=_tests_k226,
)
def k226_xoa_nguyen_am(inp):
    s = inp.split()[0]
    result = ""
    for ch in s:
        if ch not in "aeiouAEIOU":
            result += ch
    return result + "\n"


def _tests_k227(r):
    tests = ["nguyen van an\n", "Lan\n", "tran thi bich ngoc\n", "Le Hoang\n", "ho Chi minh\n"]
    for lo, hi in ((2, 3), (4, 5), (6, 8)):
        tests.append(rmixcase(r, rsentence(r, lo, hi, NAME_WORDS)) + "\n")
    return tests


@problem(
    title="Chữ viết tắt trên thẻ học sinh",
    difficulty=2,
    statement="""
        Mỗi bạn trong lớp được làm một chiếc thẻ học sinh có in chữ viết tắt của họ tên:
        lấy chữ cái đầu tiên của từng từ trong họ tên rồi viết hoa lên.

        Đầu vào:
        - Một dòng (có thể có dấu cách) chứa họ tên viết không dấu. Mỗi từ gồm các chữ cái
          tiếng Anh (hoa hoặc thường); hai từ liền nhau cách nhau đúng một dấu cách;
          không có dấu cách ở đầu và cuối dòng.

        Đầu ra:
        - In ra chữ cái đầu tiên của từng từ, theo đúng thứ tự trong họ tên, tất cả viết hoa
          và viết liền nhau (không có dấu cách).

        Giới hạn:
        - Họ tên có từ 1 đến 10 từ.
    """,
    tests=_tests_k227,
)
def k227_viet_tat(inp):
    line = inp.split("\n")[0].rstrip("\r")
    result = ""
    for w in line.split():
        result += w[0].upper()
    return result + "\n"


@problem(
    title="Kho báu chữ số trong câu thần chú",
    difficulty=2,
    statement="""
        Câu thần chú của phù thủy có lẫn những chữ số. Ai cộng đúng tất cả các chữ số đó
        sẽ biết trong kho báu có bao nhiêu đồng vàng!

        Đầu vào:
        - Một dòng chứa câu thần chú: một xâu gồm các chữ cái tiếng Anh và chữ số,
          không có dấu cách.

        Đầu ra:
        - In ra tổng của các chữ số xuất hiện trong xâu. Mỗi chữ số được cộng riêng lẻ,
          ví dụ đoạn "35" được tính là 3 + 5 chứ không phải 35.
        - Nếu xâu không có chữ số nào thì in ra 0.

        Giới hạn:
        - Xâu dài từ 1 đến 100 ký tự.

        Gợi ý:
        - Giá trị của chữ số ch là ch - '0' (C++/Java) hoặc int(ch) (Python).
    """,
    tests=lambda r: [
        "abra7kad2abra\n",
        "x\n",
        "9\n",
        "a1b2c3\n",
        "0000\n",
        "9" * 100 + "\n",
        rword(r, 60, 100, LOWER + DIGITS),
        rword(r, 20, 40, "MAGICmagic" + DIGITS),
    ],
)
def k228_tong_chu_so(inp):
    s = inp.split()[0]
    total = 0
    for ch in s:
        if "0" <= ch <= "9":
            total += ord(ch) - ord("0")
    return str(total) + "\n"


@problem(
    title="Từ dài nhất trong bài thơ của Thỏ",
    difficulty=2,
    statement="""
        Thỏ Trắng vừa sáng tác một câu thơ. Thỏ muốn tô màu từ dài nhất trong câu,
        nhưng đếm mãi vẫn chưa xong. Em hãy giúp Thỏ tìm từ đó nhé.

        Đầu vào:
        - Một dòng (có thể có dấu cách) chứa câu thơ. Mỗi từ gồm các chữ cái tiếng Anh
          (hoa hoặc thường); hai từ liền nhau cách nhau đúng một dấu cách; không có dấu cách
          ở đầu và cuối dòng.

        Đầu ra:
        - In ra từ có nhiều chữ cái nhất, viết đúng như trong câu.
        - Nếu có nhiều từ cùng dài nhất thì in ra từ xuất hiện đầu tiên (bên trái nhất).

        Giới hạn:
        - Dòng dài không quá 300 ký tự và có ít nhất một từ.
    """,
    tests=lambda r: [
        "the rabbit jumps over the sleepy turtle\n",
        "cat\n",
        "a bb ccc dd\n",
        "big cat dog\n",
        "an elephant\n",
        "I am a Superhero\n",
        rsentence(r, 10, 20) + "\n",
        rmixcase(r, rsentence(r, 20, 30)) + "\n",
    ],
)
def k229_tu_dai_nhat(inp):
    line = inp.split("\n")[0].rstrip("\r")
    best = ""
    for w in line.split():
        if len(w) > len(best):
            best = w
    return best + "\n"


def _tests_k230(r):
    tests = [
        "watermelon\nmelon\n",
        "a\na\n",
        "a\nab\n",
        "abcde\nace\n",
        "Hello\nhello\n",
        "banana\nnan\n",
        "mississippi\nissip\n",
        "mississippi\nssss\n",
    ]
    s = rword(r, 60, 100, "abcAB")
    i = r.randint(0, len(s) - 10)
    tests.append(f"{s}\n{s[i:i + r.randint(3, 10)]}\n")
    s = rword(r, 60, 100, "abc")
    while True:
        t = rword(r, 5, 8, "abc")
        if t not in s:
            break
    tests.append(f"{s}\n{t}\n")
    return tests


@problem(
    title="Từ bí mật có trốn trong xâu không?",
    difficulty=2,
    statement="""
        Bạn Kiến giấu một từ bí mật t vào bên trong một xâu dài s. Em hãy kiểm tra xem
        t có thật sự nằm trong s hay không: các chữ cái của t phải xuất hiện liền một mạch,
        đúng thứ tự, không bị chữ khác chen vào giữa.

        Đầu vào:
        - Dòng 1: xâu s.
        - Dòng 2: xâu t.
        - Cả hai xâu gồm các chữ cái tiếng Anh (hoa hoặc thường), không có dấu cách.

        Đầu ra:
        - In ra YES nếu t là một đoạn liên tiếp của s, ngược lại in ra NO.
        - Phân biệt chữ hoa và chữ thường.

        Giới hạn:
        - Mỗi xâu dài từ 1 đến 100 chữ cái.
    """,
    tests=_tests_k230,
)
def k230_xau_con(inp):
    parts = inp.split()
    s, t = parts[0], parts[1]
    found = False
    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            found = True
    return ("YES" if found else "NO") + "\n"


@problem(
    title="Mật thư Caesar của đội trinh sát",
    difficulty=2,
    statement="""
        Đội trinh sát nhí mã hóa mật thư bằng cách dịch mỗi chữ cái đi k bước
        trong bảng chữ cái. Đi quá chữ z thì quay vòng lại chữ a. Em hãy giúp đội mã hóa một từ.

        Đầu vào:
        - Dòng 1: một từ gồm các chữ cái tiếng Anh viết thường, không có dấu cách.
        - Dòng 2: một số nguyên k.

        Đầu ra:
        - In ra từ sau khi mã hóa: mỗi chữ cái được thay bằng chữ cái đứng sau nó k bước
          trong bảng chữ cái a, b, c, ..., z. Sau z lại quay về a; ví dụ với k = 2
          thì y thành a và z thành b.

        Giới hạn:
        - Từ dài từ 1 đến 100 chữ cái; 0 ≤ k ≤ 25.

        Gợi ý:
        - Coi a là vị trí 0, b là 1, ..., z là 25. Vị trí mới = (vị trí cũ + k) % 26.
    """,
    tests=lambda r: [
        "hello\n3\n",
        "a\n0\n",
        "z\n1\n",
        "xyz\n2\n",
        "abc\n25\n",
        "secret\n13\n",
        rword(r, 30, 60) + f"\n{r.randint(1, 25)}\n",
        rword(r, 80, 100) + f"\n{r.randint(1, 25)}\n",
    ],
)
def k231_caesar(inp):
    parts = inp.split()
    s, k = parts[0], int(parts[1])
    result = ""
    for ch in s:
        pos = (ord(ch) - ord("a") + k) % 26
        result += chr(ord("a") + pos)
    return result + "\n"


@problem(
    title="Chữ cái nhảy múa lên xuống",
    difficulty=2,
    statement="""
        Các chữ cái đang tập nhảy: chữ thứ nhất nhảy lên cao (viết hoa), chữ thứ hai ngồi
        xuống (viết thường), chữ thứ ba lại nhảy lên, chữ thứ tư lại ngồi xuống... cứ thế
        đến hết từ.

        Đầu vào:
        - Một dòng chứa một từ gồm các chữ cái tiếng Anh (hoa hoặc thường), không có dấu cách.

        Đầu ra:
        - In ra từ đó sau khi đổi các chữ ở vị trí lẻ (thứ 1, 3, 5, ...) thành chữ hoa
          và các chữ ở vị trí chẵn (thứ 2, 4, 6, ...) thành chữ thường.
          Vị trí đếm từ 1, từ trái sang phải.

        Giới hạn:
        - Từ dài từ 1 đến 100 chữ cái.
    """,
    tests=lambda r: [
        "banana\n",
        "a\n",
        "ab\n",
        "DANCING\n",
        "hElLoWoRlD\n",
        "Z\n",
        rword(r, 30, 60, LETTERS),
        rword(r, 90, 100, LOWER),
    ],
)
def k232_nhay_mua(inp):
    s = inp.split()[0]
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].upper()
        else:
            result += s[i].lower()
    return result + "\n"


# =================================================================== KHO (3)


@problem(
    title="Nén chuỗi hạt cườm của bà",
    difficulty=3,
    statement="""
        Bà xâu một chuỗi hạt cườm, mỗi hạt mang một chữ cái. Để ghi chép cho gọn, bà viết
        mỗi nhóm hạt giống nhau đứng liền nhau thành chữ cái đó kèm theo số hạt trong nhóm.

        Đầu vào:
        - Một dòng chứa một xâu gồm các chữ cái tiếng Anh viết thường, không có dấu cách.

        Đầu ra:
        - In ra xâu đã nén: đi từ trái sang phải, mỗi nhóm chữ cái giống nhau đứng liền nhau
          được viết thành chữ cái đó rồi đến số chữ trong nhóm, viết liền, không có dấu cách.
        - Nhóm chỉ có 1 chữ vẫn phải viết số 1. Số lượng có thể từ 10 trở lên (viết đủ các chữ số).
        - Một chữ cái có thể xuất hiện ở nhiều nhóm tách rời nhau; mỗi nhóm được viết riêng.
          Ví dụ xâu abbba được nén thành a1b3a1.

        Giới hạn:
        - Xâu dài từ 1 đến 1000 chữ cái.
    """,
    tests=lambda r: [
        "aaabccdddd\n",
        "z\n",
        "aaaaaaaaaaaa\n",
        "abab\n",
        "a" * 1000 + "\n",
        "abcdefg\n",
        rruns(r, 50, 100, "abc", 5) + "\n",
        rruns(r, 300, 600, "xyz", 15) + "\n",
    ],
)
def k233_nen_xau(inp):
    s = inp.split()[0]
    result = ""
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        result += s[i] + str(j - i)
        i = j
    return result + "\n"


def _tests_k234(r):
    tests = ["a3b1c2\n", "x1\n", "a12\n", "a1b1a1\n", "z99\n", "m10n1o5\n"]
    for pairs, hi in ((8, 9), (15, 60)):
        s = ""
        for _ in range(pairs):
            s += r.choice(LOWER) + str(r.randint(1, hi))
        tests.append(s + "\n")
    return tests


@problem(
    title="Giải nén chuỗi hạt cườm",
    difficulty=3,
    statement="""
        Bạn Su tìm thấy sổ ghi chép của bà, trong đó mỗi chuỗi hạt cườm được ghi gọn thành
        các cặp "chữ cái + số lượng". Em hãy giúp Su xâu lại chuỗi hạt ban đầu.

        Đầu vào:
        - Một dòng chứa một xâu không có dấu cách, gồm nhiều cặp viết liền nhau. Mỗi cặp là
          một chữ cái tiếng Anh viết thường, ngay sau đó là một số nguyên dương
          (có 1 hoặc 2 chữ số) cho biết chữ cái đó được lặp lại bao nhiêu lần.

        Đầu ra:
        - In ra chuỗi hạt ban đầu: lần lượt từ trái sang phải, mỗi cặp được thay bằng
          chữ cái đó viết lặp lại đúng số lần đã ghi, tất cả viết liền nhau.

        Giới hạn:
        - Mỗi số lượng từ 1 đến 99; xâu kết quả dài không quá 1000 chữ cái.

        Gợi ý:
        - Số lượng có thể có 2 chữ số, nên hãy đọc hết các chữ số liền nhau rồi mới lặp.
    """,
    tests=_tests_k234,
)
def k234_giai_nen(inp):
    s = inp.split()[0]
    result = ""
    i = 0
    while i < len(s):
        letter = s[i]
        i += 1
        count = 0
        while i < len(s) and "0" <= s[i] <= "9":
            count = count * 10 + (ord(s[i]) - ord("0"))
            i += 1
        result += letter * count
    return result + "\n"


@problem(
    title="Chữ cái cô đơn đầu tiên",
    difficulty=3,
    statement="""
        Trong một từ, chữ cái "cô đơn" là chữ cái chỉ xuất hiện đúng một lần trong cả từ.
        Bạn Nhím muốn kết bạn với chữ cái cô đơn đứng đầu tiên (gần bên trái nhất).
        Em hãy giúp Nhím tìm chữ cái đó.

        Đầu vào:
        - Một dòng chứa một từ gồm các chữ cái tiếng Anh viết thường, không có dấu cách.

        Đầu ra:
        - In ra chữ cái cô đơn đứng đầu tiên trong từ.
        - Nếu từ không có chữ cái cô đơn nào thì in ra -1.

        Giới hạn:
        - Từ dài từ 1 đến 1000 chữ cái.

        Gợi ý:
        - Hãy đếm số lần xuất hiện của từng chữ cái trước, rồi đi lại từ đầu từ để tìm.
    """,
    tests=lambda r: [
        "swiss\n",
        "a\n",
        "aabb\n",
        "abcabcd\n",
        "programming\n",
        "aabbccddeeffg\n",
        "zz\n",
        rword(r, 300, 500, "abcdef") + "q" + rword(r, 300, 400, "abcdef") + "\n",
        rword(r, 30, 50, LOWER) + "\n",
    ],
)
def k235_chu_co_don(inp):
    s = inp.split()[0]
    count = [0] * 26
    for ch in s:
        count[ord(ch) - ord("a")] += 1
    for ch in s:
        if count[ord(ch) - ord("a")] == 1:
            return ch + "\n"
    return "-1\n"


def _tests_k236(r):
    tests = [
        "below\nelbow\n",
        "a\na\n",
        "a\nb\n",
        "aab\nabb\n",
        "abc\nabcd\n",
        "night\nthing\n",
        "dormitory\ndirtyroom\n",
    ]
    s = rword(r, 40, 80, "abcdefg")
    letters = list(s)
    r.shuffle(letters)
    tests.append(s + "\n" + "".join(letters) + "\n")
    s = rword(r, 40, 80, "abcdefg")
    letters = list(s)
    r.shuffle(letters)
    letters[0] = "z"
    tests.append(s + "\n" + "".join(letters) + "\n")
    return tests


@problem(
    title="Xếp lại chữ cái thành từ mới",
    difficulty=3,
    statement="""
        Hai từ được gọi là "đảo chữ" của nhau nếu ta có thể xếp lại thứ tự các chữ cái
        của từ này để được từ kia, mỗi chữ cái dùng đúng một lần. Chẳng hạn "listen" và
        "silent" là đảo chữ của nhau. Em hãy kiểm tra hai từ bạn Cún đưa ra nhé.

        Đầu vào:
        - Dòng 1: từ thứ nhất.
        - Dòng 2: từ thứ hai.
        - Cả hai từ gồm các chữ cái tiếng Anh viết thường, không có dấu cách.

        Đầu ra:
        - In ra YES nếu hai từ là đảo chữ của nhau, ngược lại in ra NO.
        - Chú ý: mỗi chữ cái phải xuất hiện cùng số lần ở cả hai từ. Hai từ giống hệt nhau
          cũng được tính là đảo chữ.

        Giới hạn:
        - Mỗi từ dài từ 1 đến 100 chữ cái.

        Gợi ý:
        - Đếm số lần xuất hiện của từng chữ cái a..z trong mỗi từ rồi so sánh.
    """,
    tests=_tests_k236,
)
def k236_dao_chu(inp):
    parts = inp.split()
    a, b = parts[0], parts[1]
    ca = [0] * 26
    cb = [0] * 26
    for ch in a:
        ca[ord(ch) - ord("a")] += 1
    for ch in b:
        cb[ord(ch) - ord("a")] += 1
    return ("YES" if ca == cb else "NO") + "\n"


@problem(
    title="Bảng thống kê chữ cái của cô thủ thư",
    difficulty=3,
    statement="""
        Cô thủ thư muốn biết trong một câu văn, mỗi chữ cái xuất hiện bao nhiêu lần
        để làm bảng thống kê dán lên tường thư viện.

        Đầu vào:
        - Một dòng (có thể có dấu cách) gồm các chữ cái tiếng Anh viết thường và dấu cách.
          Hai từ liền nhau cách nhau đúng một dấu cách; không có dấu cách ở đầu và cuối dòng.

        Đầu ra:
        - Với mỗi chữ cái CÓ xuất hiện trong câu, in một dòng gồm: chữ cái đó, một dấu cách,
          rồi số lần nó xuất hiện.
        - Các dòng xếp theo thứ tự bảng chữ cái từ a đến z. Không in chữ cái không xuất hiện.
          Không đếm dấu cách.

        Giới hạn:
        - Dòng dài từ 1 đến 300 ký tự.

        Gợi ý:
        - Dùng một mảng 26 phần tử để đếm, rồi đi từ a đến z để in.
    """,
    tests=lambda r: [
        "hello world\n",
        "a\n",
        "zzz\n",
        "the quick brown fox jumps over the lazy dog\n",
        "ab ba\n",
        "mississippi\n",
        rsentence(r, 10, 20) + "\n",
        rsentence(r, 30, 45) + "\n",
    ],
)
def k237_thong_ke(inp):
    line = inp.split("\n")[0].rstrip("\r")
    count = [0] * 26
    for ch in line:
        if "a" <= ch <= "z":
            count[ord(ch) - ord("a")] += 1
    out = []
    for i in range(26):
        if count[i] > 0:
            out.append(chr(ord("a") + i) + " " + str(count[i]))
    return "\n".join(out) + "\n"


def _tests_k238(r):
    tests = [
        "abababa\naba\n",
        "a\na\n",
        "abc\nd\n",
        "aaaaa\naa\n",
        "abc\nabcd\n",
        "catcatcat\ncat\n",
    ]
    tests.append(rword(r, 300, 500, "ab") + "\naba\n")
    tests.append(rword(r, 800, 1000, "aab") + "\naa\n")
    tests.append(rword(r, 200, 300, "xyz") + "\nxyz\n")
    return tests


@problem(
    title="Đếm dấu chân không giẫm lên nhau",
    difficulty=3,
    statement="""
        Trên bãi cát có một hàng dấu chân, mỗi dấu chân là một chữ cái. Bạn Sóc muốn đếm
        xem mẫu dấu chân t xuất hiện bao nhiêu lần trong hàng s, nhưng hai lần đếm
        không được dùng chung bất kỳ dấu chân nào.

        Đầu vào:
        - Dòng 1: xâu s.
        - Dòng 2: xâu t.
        - Cả hai xâu gồm các chữ cái tiếng Anh viết thường, không có dấu cách.

        Đầu ra:
        - In ra số lần t xuất hiện trong s mà không chồng lên nhau, đếm theo cách sau:
          dò s từ trái sang phải; mỗi khi gặp một đoạn giống hệt t thì đếm thêm 1,
          rồi nhảy qua hết đoạn đó và dò tiếp từ chữ cái ngay sau đoạn vừa tìm được.
        - Ví dụ với s = aaaa và t = aa thì kết quả là 2.

        Giới hạn:
        - s dài từ 1 đến 1000 chữ cái; t dài từ 1 đến 100 chữ cái.
    """,
    tests=_tests_k238,
)
def k238_dem_khong_chong(inp):
    parts = inp.split()
    s, t = parts[0], parts[1]
    count = 0
    i = 0
    while i + len(t) <= len(s):
        if s[i:i + len(t)] == t:
            count += 1
            i += len(t)
        else:
            i += 1
    return str(count) + "\n"


@problem(
    title="Tiếng P bí mật của nhóm bạn thân",
    difficulty=3,
    statement="""
        Nhóm bạn thân của Tít nói chuyện bằng "tiếng P" để người khác không hiểu:
        ngay sau mỗi nguyên âm, chèn thêm chữ p rồi lặp lại nguyên âm đó một lần nữa.
        Chẳng hạn từ cat sẽ thành capat. Em hãy dịch một câu sang tiếng P nhé.

        Đầu vào:
        - Một dòng (có thể có dấu cách) gồm các chữ cái tiếng Anh viết thường và dấu cách.
          Hai từ liền nhau cách nhau đúng một dấu cách; không có dấu cách ở đầu và cuối dòng.

        Đầu ra:
        - In ra câu sau khi dịch sang tiếng P.
        - Nguyên âm là a, e, i, o, u; chữ y không phải nguyên âm. Mỗi nguyên âm v được thay
          bằng ba chữ v, p, v. Các chữ cái khác và các dấu cách giữ nguyên.

        Giới hạn:
        - Dòng dài từ 1 đến 200 ký tự.
    """,
    tests=lambda r: [
        "hello friend\n",
        "a\n",
        "rhythm\n",
        "i love you\n",
        "queue\n",
        "banana split\n",
        rsentence(r, 5, 10) + "\n",
        rsentence(r, 15, 25) + "\n",
    ],
)
def k239_tieng_p(inp):
    line = inp.split("\n")[0].rstrip("\r")
    result = ""
    for ch in line:
        if ch in "aeiou":
            result += ch + "p" + ch
        else:
            result += ch
    return result + "\n"


@problem(
    title="Người gác cổng mật khẩu của lớp",
    difficulty=3,
    statement="""
        Trang web của lớp có một người gác cổng chỉ nhận mật khẩu MẠNH. Mật khẩu mạnh phải
        thỏa mãn cả 4 điều kiện:
        (1) dài ít nhất 8 ký tự;
        (2) có ít nhất một chữ hoa (A-Z);
        (3) có ít nhất một chữ thường (a-z);
        (4) có ít nhất một chữ số (0-9).

        Đầu vào:
        - Một dòng chứa mật khẩu: một xâu gồm các chữ cái tiếng Anh và chữ số,
          không có dấu cách.

        Đầu ra:
        - Nếu mật khẩu thỏa mãn cả 4 điều kiện, in ra MANH.
        - Ngược lại, dòng thứ nhất in ra YEU; dòng thứ hai in ra số thứ tự của các điều kiện
          chưa thỏa mãn, theo thứ tự tăng dần, cách nhau một dấu cách.

        Giới hạn:
        - Mật khẩu dài từ 1 đến 50 ký tự.
    """,
    tests=lambda r: [
        "Abc12345\n",
        "abc\n",
        "ABCDEFGH\n",
        "12345678\n",
        "Password\n",
        "Pass1\n",
        "Z9z9Z9z9\n",
        "a\n",
        rword(r, 10, 20, LOWER + DIGITS),
        rword(r, 30, 50, LETTERS + DIGITS),
    ],
)
def k240_mat_khau(inp):
    s = inp.split()[0]
    has_upper = has_lower = has_digit = False
    for ch in s:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_digit = True
    failed = []
    if len(s) < 8:
        failed.append("1")
    if not has_upper:
        failed.append("2")
    if not has_lower:
        failed.append("3")
    if not has_digit:
        failed.append("4")
    if not failed:
        return "MANH\n"
    return "YEU\n" + " ".join(failed) + "\n"
