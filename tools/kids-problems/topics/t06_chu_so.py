"""
Chu de 6 - Chu so va so hoc vui (K151-K180).

Tach chu so cua mot so, uoc so, so nguyen to, UCLN / BCNN, he nhi phan.
Chi dung nhap/xuat, phep tinh, if/else va vong lap (co the long nhau).
"""

from kidslib import problem

TOPIC = "chu-so"


# =====================================================================
# DỄ (difficulty = 1)
# =====================================================================

@problem(
    title="Số kẹo của cô Mai có mấy chữ số?",
    difficulty=1,
    statement="""
        Cô Mai vừa đếm xong số kẹo trong cửa hàng: có tất cả n viên. Bé Na tò mò muốn biết số n được viết bằng bao nhiêu chữ số.

        Đầu vào:
        - Một số nguyên n (0 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra số chữ số của n.

        Gợi ý:
        - Mỗi lần chia n cho 10 lấy phần nguyên (n / 10 trong C++/Java, n // 10 trong Python) thì n mất đi chữ số cuối cùng. Hãy đếm xem phải chia bao nhiêu lần thì n chỉ còn một chữ số; số chữ số của n bằng số lần chia đó cộng thêm 1.
        - Chú ý: số 0 cũng có 1 chữ số.
    """,
    tests=lambda r: ["2024", "0", "7", "10", "99999", "1000000000", "123456789",
                     str(r.randint(100, 999999)), str(r.randint(10**7, 10**9 - 1))],
)
def dem_chu_so(inp):
    n = int(inp.split()[0])
    count = 1
    while n >= 10:
        n //= 10
        count += 1
    return f"{count}\n"


@problem(
    title="Cộng chữ số trên biển số nhà",
    difficulty=1,
    statement="""
        Nhà bạn Tí mang số n. Mỗi lần đi học về, Tí lại chơi trò cộng tất cả các chữ số của số nhà lại với nhau.

        Đầu vào:
        - Một số nguyên n (0 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra tổng các chữ số của n.

        Gợi ý:
        - n % 10 cho ta chữ số hàng đơn vị, còn phép chia lấy phần nguyên cho 10 bỏ đi chữ số đó. Lặp lại cho đến khi n bằng 0.
    """,
    tests=lambda r: ["1234", "0", "5", "1000000000", "999999999", "908070", "19",
                     str(r.randint(10**5, 10**9)), str(r.randint(100, 9999))],
)
def tong_chu_so(inp):
    n = int(inp.split()[0])
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return f"{total}\n"


@problem(
    title="Robot Bi chỉ nhìn rõ chữ số đầu tiên",
    difficulty=1,
    statement="""
        Robot Bi bị cận thị nên chỉ nhìn rõ chữ số đầu tiên (chữ số ngoài cùng bên trái) của mỗi số. Em hãy viết chương trình giúp Bi đọc chữ số đó.

        Đầu vào:
        - Một số nguyên n (0 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra chữ số ngoài cùng bên trái của n. Với n = 0 thì in ra 0.

        Gợi ý:
        - Chia n cho 10 (lấy phần nguyên) liên tục cho đến khi n nhỏ hơn 10.
    """,
    tests=lambda r: ["4096", "0", "7", "10", "1000000000", "987654321", "59", "300",
                     str(r.randint(10**6, 10**9 - 1))],
)
def chu_so_dau(inp):
    n = int(inp.split()[0])
    while n >= 10:
        n //= 10
    return f"{n}\n"


@problem(
    title="Mật mã chữ số chẵn của mèo Mướp",
    difficulty=1,
    statement="""
        Chú mèo Mướp đặt mật mã cho hộp cá khô là số n. Mướp chỉ thích các chữ số chẵn nên muốn biết trong mật mã có bao nhiêu chữ số chẵn.

        Chữ số chẵn là một trong các chữ số 0, 2, 4, 6, 8.

        Đầu vào:
        - Một số nguyên n (0 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra số lượng chữ số chẵn trong cách viết của n. Chữ số nào xuất hiện nhiều lần thì đếm đủ tất cả các lần.

        Chú ý:
        - Số 0 có một chữ số là 0 (chữ số chẵn), nên với n = 0 thì kết quả là 1.
    """,
    tests=lambda r: ["123456", "0", "13579", "2468", "1000000000", "7", "880088008",
                     str(r.randint(10**6, 10**9 - 1)), str(r.randint(1000, 99999))],
)
def dem_chu_so_chan(inp):
    n = int(inp.split()[0])
    count = 0
    while True:
        if (n % 10) % 2 == 0:
            count += 1
        n //= 10
        if n == 0:
            break
    return f"{count}\n"


@problem(
    title="Chữ số to nhất và chữ số bé nhất",
    difficulty=1,
    statement="""
        Thầy giáo viết số n lên bảng. Bạn An phải tìm chữ số lớn nhất, còn bạn Bình phải tìm chữ số nhỏ nhất có mặt trong số đó.

        Đầu vào:
        - Một số nguyên n (0 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra hai số trên một dòng, cách nhau một dấu cách: chữ số lớn nhất và chữ số nhỏ nhất của n.

        Chú ý:
        - Nếu n chỉ có một chữ số thì chữ số lớn nhất và nhỏ nhất đều là chính nó.
    """,
    tests=lambda r: ["5381", "0", "7", "1000000000", "999999999", "2024", "56473",
                     str(r.randint(10**5, 10**9 - 1))],
)
def chu_so_lon_nho(inp):
    n = int(inp.split()[0])
    biggest = n % 10
    smallest = n % 10
    while n > 0:
        d = n % 10
        if d > biggest:
            biggest = d
        if d < smallest:
            smallest = d
        n //= 10
    return f"{biggest} {smallest}\n"


@problem(
    title="Phép nhân chữ số của phù thủy nhỏ",
    difficulty=1,
    statement="""
        Cô phù thủy nhỏ có một câu thần chú: biến một số thành tích (phép nhân) của tất cả các chữ số của nó. Em hãy tính trước kết quả của câu thần chú.

        Đầu vào:
        - Một số nguyên n (0 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra tích của tất cả các chữ số của n.

        Chú ý:
        - Chỉ cần một chữ số 0 là cả tích bằng 0. Số 0 có một chữ số là 0 nên kết quả của n = 0 là 0.
    """,
    tests=lambda r: ["234", "0", "8", "999999999", "105", "1111111", "987654321",
                     "".join(str(r.randint(1, 9)) for _ in range(7)),
                     "".join(str(r.randint(2, 9)) for _ in range(5))],
)
def tich_chu_so(inp):
    n = int(inp.split()[0])
    product = n % 10
    n //= 10
    while n > 0:
        product *= n % 10
        n //= 10
    return f"{product}\n"


@problem(
    title="Chữ số yêu thích của bạn Hoa",
    difficulty=1,
    statement="""
        Bạn Hoa rất thích chữ số d. Mỗi khi nhìn thấy một số n, Hoa lại đếm xem chữ số d xuất hiện bao nhiêu lần trong số đó.

        Đầu vào:
        - Một dòng gồm hai số nguyên n và d, cách nhau một dấu cách (0 ≤ n ≤ 1 000 000 000, 0 ≤ d ≤ 9).

        Đầu ra:
        - In ra số lần chữ số d xuất hiện trong cách viết của n.

        Chú ý:
        - Số 0 được viết bằng đúng một chữ số 0.
    """,
    tests=lambda r: ["1771 7", "0 0", "0 5", "1000000000 0", "123456789 9", "777777777 7",
                     "2024 2", f"{r.randint(10**6, 10**9)} {r.randint(0, 9)}",
                     f"{r.randint(1000, 99999)} {r.randint(0, 9)}"],
)
def dem_chu_so_d(inp):
    n, d = map(int, inp.split()[:2])
    count = 0
    while True:
        if n % 10 == d:
            count += 1
        n //= 10
        if n == 0:
            break
    return f"{count}\n"


@problem(
    title="Chú vẹt Kiki nhại số từ phải sang trái",
    difficulty=1,
    statement="""
        Chú vẹt Kiki rất thích nhại lại các con số, nhưng lần nào Kiki cũng đọc từ phải sang trái. Em hãy cho biết Kiki đọc số n thành số nào.

        Đầu vào:
        - Một số nguyên n (0 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra số nhận được khi viết các chữ số của n theo thứ tự ngược lại.
        - Các chữ số 0 đứng đầu số mới thì bỏ đi, ví dụ 3500 đọc ngược thành 53. Số 0 đọc ngược vẫn là 0.

        Gợi ý:
        - Bắt đầu với kq = 0. Mỗi bước lấy chữ số cuối d = n % 10, cập nhật kq = kq * 10 + d rồi bỏ chữ số cuối của n.
    """,
    tests=lambda r: ["1234", "0", "1200", "7", "1000000000", "123454321", "908070",
                     str(r.randint(10**6, 10**9 - 1))],
)
def dao_nguoc_so(inp):
    n = int(inp.split()[0])
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    return f"{result}\n"


@problem(
    title="Chia đều kẹo cho cả nhóm bạn",
    difficulty=1,
    statement="""
        An có n viên kẹo và muốn chia hết cho một nhóm bạn sao cho bạn nào cũng được số kẹo bằng nhau, không thừa viên nào. Hãy liệt kê tất cả các số bạn mà nhóm có thể có.

        Số d được gọi là ước của n nếu n chia hết cho d (tức là n % d bằng 0). Các số bạn cần tìm chính là các ước của n, kể cả 1 và chính n.

        Đầu vào:
        - Một số nguyên n (1 ≤ n ≤ 1 000 000).

        Đầu ra:
        - In ra tất cả các ước của n theo thứ tự tăng dần, trên một dòng, cách nhau một dấu cách.
    """,
    tests=lambda r: ["12", "1", "13", "36", "1000000", "720720", "997",
                     str(r.randint(2, 10**6)), str(r.randint(100, 9999))],
)
def liet_ke_uoc(inp):
    n = int(inp.split()[0])
    small, large = [], []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            if d != n // d:
                large.append(n // d)
        d += 1
    divisors = small + large[::-1]
    return " ".join(map(str, divisors)) + "\n"


@problem(
    title="Xếp hàng tập thể dục giữa giờ",
    difficulty=1,
    statement="""
        Lớp học có n bạn xếp hàng tập thể dục giữa giờ. Cô giáo muốn xếp thành một số hàng sao cho hàng nào cũng có số bạn bằng nhau (có thể chỉ xếp 1 hàng, hoặc mỗi hàng chỉ có 1 bạn). Hỏi cô có bao nhiêu cách chọn số hàng?

        Đầu vào:
        - Một số nguyên n (1 ≤ n ≤ 1 000 000).

        Đầu ra:
        - In ra số cách chọn số hàng.

        Gợi ý:
        - Số hàng k chọn được khi và chỉ khi n chia hết cho k, tức là k là một ước của n. Vậy em cần đếm số ước của n.
    """,
    tests=lambda r: ["12", "1", "17", "100", "1000000", "720720", "999983",
                     str(r.randint(2, 10**6)), str(r.randint(50, 5000))],
)
def dem_uoc(inp):
    n = int(inp.split()[0])
    count = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            count += 1 if d * d == n else 2
        d += 1
    return f"{count}\n"


# =====================================================================
# VỪA (difficulty = 2)
# =====================================================================

@problem(
    title="Số lộc phát của ông nội",
    difficulty=2,
    statement="""
        Ông nội cho rằng những số chỉ gồm các chữ số 6 và 8 là "số lộc phát" mang lại may mắn. Em hãy giúp ông kiểm tra số n có phải số lộc phát không.

        Số lộc phát là số mà mọi chữ số của nó đều là 6 hoặc 8. Số chỉ gồm toàn chữ số 6, hoặc toàn chữ số 8, cũng là số lộc phát.

        Đầu vào:
        - Một số nguyên n (1 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra YES nếu n là số lộc phát, ngược lại in ra NO.
    """,
    tests=["686", "6", "1", "68", "8886", "686868688", "1000000000", "678",
           "888888889", "86"],
)
def so_loc_phat(inp):
    n = int(inp.split()[0])
    ok = True
    while n > 0:
        d = n % 10
        if d != 6 and d != 8:
            ok = False
        n //= 10
    return ("YES" if ok else "NO") + "\n"


@problem(
    title="Con số soi gương thần",
    difficulty=2,
    statement="""
        Khi đặt một số trước gương thần, gương hiện ra số đó viết theo chiều ngược lại. Một số được gọi là số đối xứng nếu đọc từ trái sang phải hay từ phải sang trái đều giống nhau, ví dụ 121 hay 4554. Khi đó số trong gương giống hệt số ban đầu.

        Đầu vào:
        - Một số nguyên n (0 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra YES nếu n là số đối xứng, ngược lại in ra NO.

        Chú ý:
        - Mọi số có một chữ số (kể cả 0) đều là số đối xứng.

        Gợi ý:
        - Tạo số đảo ngược của n rồi so sánh với n.
    """,
    tests=["12321", "0", "7", "10", "1000000000", "123454321", "1221", "123456",
           "998", "900000009"],
)
def so_doi_xung(inp):
    n = int(inp.split()[0])
    m, rev = n, 0
    while m > 0:
        rev = rev * 10 + m % 10
        m //= 10
    return ("YES" if rev == n else "NO") + "\n"


@problem(
    title="Nhà khoa học nhí săn số nguyên tố",
    difficulty=2,
    statement="""
        Bạn Khoa mơ ước trở thành nhà khoa học và đang sưu tầm các số nguyên tố. Hãy giúp Khoa kiểm tra số n.

        Số nguyên tố là số tự nhiên lớn hơn 1 và chỉ có đúng hai ước là 1 và chính nó. Ví dụ 2, 3, 5, 7, 11 là số nguyên tố, còn 9 = 3 × 3 thì không. Số 1 không phải là số nguyên tố.

        Đầu vào:
        - Một số nguyên n (1 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra YES nếu n là số nguyên tố, ngược lại in ra NO.

        Gợi ý:
        - Thử chia n cho mọi số từ 2 đến n - 1 sẽ quá chậm. Nếu n có một ước d (2 ≤ d < n) thì luôn có một ước như vậy thỏa mãn d × d ≤ n, nên chỉ cần thử d = 2, 3, 4, ... trong khi d × d ≤ n.
    """,
    tests=["17", "1", "2", "4", "999999937", "1000000000", "998001", "998812807",
           "97", "999999999"],
)
def kiem_tra_nguyen_to(inp):
    n = int(inp.split()[0])
    prime = n >= 2
    d = 2
    while d * d <= n:
        if n % d == 0:
            prime = False
            break
        d += 1
    return ("YES" if prime else "NO") + "\n"


@problem(
    title="Đi tìm số hoàn hảo",
    difficulty=2,
    statement="""
        Người Hy Lạp cổ đại rất yêu quý những "số hoàn hảo". Em hãy kiểm tra xem số n có hoàn hảo không nhé.

        Ước thật sự của n là các ước của n nhỏ hơn n. Số n được gọi là số hoàn hảo nếu n bằng tổng các ước thật sự của nó. Ví dụ 6 là số hoàn hảo vì 6 = 1 + 2 + 3.

        Đầu vào:
        - Một số nguyên n (1 ≤ n ≤ 1 000 000).

        Đầu ra:
        - In ra YES nếu n là số hoàn hảo, ngược lại in ra NO.

        Chú ý:
        - Số 1 không có ước thật sự nào (tổng bằng 0) nên 1 không phải số hoàn hảo.
    """,
    tests=["28", "6", "1", "12", "496", "8128", "1000000", "999983", "2", "8127"],
)
def so_hoan_hao(inp):
    n = int(inp.split()[0])
    total = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            total += d
            if d != n // d:
                total += n // d
        d += 1
    total -= n
    return ("YES" if total == n else "NO") + "\n"


@problem(
    title="Phép thuật thu nhỏ con số",
    difficulty=2,
    statement="""
        Pháp sư nhí có một phép thuật: biến một số thành tổng các chữ số của nó. Pháp sư cứ làm phép mãi cho đến khi số chỉ còn một chữ số. Ví dụ: 59 → 14 → 5, tức là làm phép 2 lần và được chữ số 5.

        Đầu vào:
        - Một số nguyên n (0 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra hai số trên một dòng, cách nhau một dấu cách: chữ số cuối cùng nhận được và số lần làm phép.

        Chú ý:
        - Nếu n đã có một chữ số thì không cần làm phép: in ra chính n và số lần là 0.
    """,
    tests=lambda r: ["9875", "0", "7", "10", "999999999", "1000000000", "199",
                     "199999999", str(r.randint(10**4, 10**9))],
)
def can_so(inp):
    n = int(inp.split()[0])
    steps = 0
    while n >= 10:
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        n = s
        steps += 1
    return f"{n} {steps}\n"


@problem(
    title="Chia quà bánh kẹo được nhiều túi nhất",
    difficulty=2,
    statement="""
        Cô giáo có a cái bánh và b cái kẹo. Cô muốn chia hết vào các túi quà sao cho túi nào cũng có số bánh bằng nhau và số kẹo bằng nhau, không thừa cái nào. Hỏi cô chia được nhiều nhất bao nhiêu túi?

        Đáp số chính là ước chung lớn nhất (ƯCLN) của a và b: số lớn nhất mà cả a và b đều chia hết cho nó.

        Đầu vào:
        - Một dòng gồm hai số nguyên a và b, cách nhau một dấu cách (1 ≤ a, b ≤ 1 000 000 000).

        Đầu ra:
        - In ra ƯCLN của a và b.

        Gợi ý (thuật toán Euclid):
        - Trong khi b khác 0: tính r = a % b, rồi gán a = b và b = r. Khi b bằng 0 thì a chính là ƯCLN.
    """,
    tests=lambda r: ["12 18", "1 1", "7 13", "1000000000 999999999", "1000000000 500000000",
                     "36 36", "17 34", "1 1000000000",
                     (lambda g: f"{g * r.randint(1, 10**5)} {g * r.randint(1, 10**5)}")(r.randint(2, 10**4))],
)
def ucln(inp):
    a, b = map(int, inp.split()[:2])
    while b != 0:
        a, b = b, a % b
    return f"{a}\n"


@problem(
    title="Hai chuyến xe buýt cùng xuất bến",
    difficulty=2,
    statement="""
        Ở bến xe, xe buýt màu xanh cứ a phút lại xuất bến một chuyến, xe buýt màu đỏ cứ b phút một chuyến. Lúc 7 giờ đúng cả hai xe cùng xuất bến. Hỏi sau ít nhất bao nhiêu phút nữa thì hai xe lại cùng xuất bến?

        Đáp số là bội chung nhỏ nhất (BCNN) của a và b: số dương nhỏ nhất chia hết cho cả a và b.

        Đầu vào:
        - Một dòng gồm hai số nguyên a và b, cách nhau một dấu cách (1 ≤ a, b ≤ 40 000).

        Đầu ra:
        - In ra BCNN của a và b.

        Gợi ý:
        - BCNN(a, b) = a × b / ƯCLN(a, b). ƯCLN tính bằng thuật toán Euclid.
    """,
    tests=lambda r: ["4 6", "1 1", "7 7", "40000 39999", "12 18", "5 25", "9 28",
                     f"{r.randint(1000, 40000)} {r.randint(1000, 40000)}",
                     f"{r.randint(2, 100)} {r.randint(2, 100)}"],
)
def bcnn(inp):
    a, b = map(int, inp.split()[:2])
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    return f"{a // x * b}\n"


@problem(
    title="Rút gọn phần bánh pizza",
    difficulty=2,
    statement="""
        Mỗi chiếc bánh pizza được cắt thành b miếng bằng nhau, và Minh có a miếng, tức là a/b chiếc bánh. Hãy viết phân số a/b dưới dạng tối giản: tử số và mẫu số không còn ước chung nào lớn hơn 1.

        Đầu vào:
        - Một dòng gồm hai số nguyên a và b, cách nhau một dấu cách (1 ≤ a, b ≤ 1 000 000 000).

        Đầu ra:
        - In ra phân số tối giản dạng p/q: tử số, dấu /, mẫu số viết liền nhau, không có dấu cách.
        - Luôn in cả mẫu số, kể cả khi mẫu số bằng 1 (ví dụ 4/1).

        Gợi ý:
        - Chia cả a và b cho ƯCLN(a, b).
    """,
    tests=lambda r: ["6 8", "1 1", "5 1", "7 13", "1000000000 250000000",
                     "999999999 1000000000", "36 48", "1 1000000000",
                     (lambda g: f"{g * r.randint(1, 10**6)} {g * r.randint(1, 10**6)}")(r.randint(2, 1000))],
)
def rut_gon_phan_so(inp):
    a, b = map(int, inp.split()[:2])
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    return f"{a // x}/{b // x}\n"


@problem(
    title="Robot nói tiếng nhị phân",
    difficulty=2,
    statement="""
        Máy tính chỉ dùng hai chữ số 0 và 1 để viết mọi số, gọi là hệ nhị phân. Trong hệ nhị phân, các chữ số tính từ phải sang trái có giá trị 1, 2, 4, 8, 16, ... Ví dụ số 6 viết thành 110 vì 6 = 4 + 2. Em hãy giúp robot đổi số n sang hệ nhị phân.

        Đầu vào:
        - Một số nguyên n (0 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra cách viết của n trong hệ nhị phân: các chữ số 0, 1 viết liền nhau, không có chữ số 0 thừa ở đầu. Số 0 viết là 0.

        Gợi ý:
        - Chia n cho 2 liên tục và ghi lại các số dư cho đến khi n bằng 0. Đọc các số dư theo thứ tự ngược lại (từ lần chia cuối về lần chia đầu) chính là kết quả.
    """,
    tests=lambda r: ["13", "0", "1", "2", "1000000000", "1023", "1024", "170",
                     str(r.randint(10**5, 10**9))],
)
def doi_nhi_phan(inp):
    n = int(inp.split()[0])
    if n == 0:
        return "0\n"
    digits = ""
    while n > 0:
        digits = str(n % 2) + digits
        n //= 2
    return digits + "\n"


@problem(
    title="Giải mã tin nhắn nhị phân",
    difficulty=2,
    statement="""
        Robot gửi cho em một con số viết trong hệ nhị phân (chỉ gồm chữ số 0 và 1). Trong hệ nhị phân, các chữ số tính từ phải sang trái có giá trị 1, 2, 4, 8, 16, ... Ví dụ 110 trong hệ nhị phân là 4 + 2 = 6. Hãy đổi số robot gửi về số thường (hệ thập phân).

        Đầu vào:
        - Một số nhị phân gồm không quá 18 chữ số, chỉ có chữ số 0 và 1, không có chữ số 0 thừa ở đầu (trừ chính số 0).

        Đầu ra:
        - In ra giá trị của số đó trong hệ thập phân.

        Gợi ý:
        - Có thể đọc vào như một số nguyên 64-bit (long long trong C++, long trong Java) rồi tách từng chữ số bằng % 10 và / 10. Chữ số cuối nhân 1, chữ số tiếp theo nhân 2, rồi nhân 4, 8, ...
    """,
    tests=lambda r: ["1101", "0", "1", "10", "111111111111111111", "100000000000000000",
                     "101010", "1" + "".join(r.choice("01") for _ in range(r.randint(8, 17))),
                     "1" + "".join(r.choice("01") for _ in range(r.randint(3, 6)))],
)
def nhi_phan_sang_thap_phan(inp):
    s = inp.split()[0]
    value = 0
    for c in s:
        value = value * 2 + (ord(c) - ord("0"))
    return f"{value}\n"


@problem(
    title="Số Armstrong kiêu hãnh",
    difficulty=2,
    statement="""
        Có những con số rất "kiêu hãnh" vì chúng tự tạo ra chính mình từ các chữ số của mình, gọi là số Armstrong.

        Gọi k là số chữ số của n. Số n là số Armstrong nếu tổng các chữ số của n, mỗi chữ số nâng lên lũy thừa k, bằng đúng n. Ở đây a^k nghĩa là a nhân với chính nó k lần. Ví dụ 407 có 3 chữ số và 4^3 + 0^3 + 7^3 = 64 + 0 + 343 = 407, nên 407 là số Armstrong. Mọi số có một chữ số đều là số Armstrong.

        Đầu vào:
        - Một số nguyên n (1 ≤ n ≤ 99 999 999).

        Đầu ra:
        - In ra YES nếu n là số Armstrong, ngược lại in ra NO.
    """,
    tests=["153", "1", "10", "370", "9474", "9475", "88593477", "99999999",
           "548834", "100"],
)
def so_armstrong(inp):
    n = int(inp.split()[0])
    k = 0
    m = n
    while m > 0:
        k += 1
        m //= 10
    total = 0
    m = n
    while m > 0:
        d = m % 10
        p = 1
        for _ in range(k):
            p *= d
        total += p
        m //= 10
    return ("YES" if total == n else "NO") + "\n"


@problem(
    title="Đếm số chính phương trong vườn hoa",
    difficulty=2,
    statement="""
        Bác làm vườn thích trồng hoa thành mảnh vườn hình vuông: k hàng, mỗi hàng k bông. Số bông hoa khi đó là k × k, và những số như vậy gọi là số chính phương: 1, 4, 9, 16, 25, ...

        Hãy đếm xem từ a đến b có bao nhiêu số chính phương.

        Đầu vào:
        - Một dòng gồm hai số nguyên a và b, cách nhau một dấu cách (1 ≤ a ≤ b ≤ 1 000 000 000).

        Đầu ra:
        - In ra số lượng số chính phương x thỏa mãn a ≤ x ≤ b.

        Gợi ý:
        - Thử k = 1, 2, 3, ... trong khi k × k ≤ b, đếm những k có k × k ≥ a. Số k cần thử không vượt quá 31 623.
    """,
    tests=lambda r: ["1 10", "1 1", "2 3", "16 16", "1 1000000000",
                     "999950884 1000000000", "26 35", "100 10000",
                     (lambda a: f"{a} {r.randint(a, 10**9)}")(r.randint(1, 10**8))],
)
def dem_chinh_phuong(inp):
    a, b = map(int, inp.split()[:2])
    count = 0
    k = 1
    while k * k <= b:
        if k * k >= a:
            count += 1
        k += 1
    return f"{count}\n"


# =====================================================================
# KHÓ (difficulty = 3)
# =====================================================================

@problem(
    title="Chiếc sàng số nguyên tố của Eratosthenes",
    difficulty=3,
    statement="""
        Nhà toán học Hy Lạp Eratosthenes nghĩ ra cách "sàng" số: viết các số từ 2 đến n, rồi lần lượt gạch bỏ các bội của 2, các bội của 3, các bội của 5, ... (không gạch chính số đó). Những số còn lại chính là các số nguyên tố.

        Nhắc lại: số nguyên tố là số tự nhiên lớn hơn 1 chỉ có đúng hai ước là 1 và chính nó.

        Đầu vào:
        - Một số nguyên n (2 ≤ n ≤ 10 000).

        Đầu ra:
        - In ra tất cả các số nguyên tố không vượt quá n theo thứ tự tăng dần, trên một dòng, cách nhau một dấu cách.
    """,
    tests=lambda r: ["20", "2", "3", "10", "10000", "97", "100", str(r.randint(200, 9999))],
)
def sang_nguyen_to(inp):
    n = int(inp.split()[0])
    crossed = [False] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if not crossed[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                crossed[j] = True
    return " ".join(map(str, primes)) + "\n"


@problem(
    title="Số nhà nguyên tố trên đường đến trường",
    difficulty=3,
    statement="""
        Trên đường đến trường, bạn Bông đi qua các ngôi nhà mang số a, a + 1, a + 2, ..., b. Bông muốn biết có bao nhiêu ngôi nhà mang số là số nguyên tố.

        Nhắc lại: số nguyên tố là số tự nhiên lớn hơn 1 chỉ có đúng hai ước là 1 và chính nó. Số 1 không phải là số nguyên tố.

        Đầu vào:
        - Một dòng gồm hai số nguyên a và b, cách nhau một dấu cách (1 ≤ a ≤ b ≤ 100 000).

        Đầu ra:
        - In ra số lượng số nguyên tố x thỏa mãn a ≤ x ≤ b.

        Gợi ý:
        - Kiểm tra từng số bằng cách thử chia cho d trong khi d × d ≤ x, hoặc dùng sàng Eratosthenes.
    """,
    tests=lambda r: ["10 30", "1 1", "2 2", "1 100000", "14 16", "99990 100000",
                     "1 10", "50000 60000",
                     (lambda a: f"{a} {r.randint(a, 100000)}")(r.randint(1, 50000))],
)
def dem_nguyen_to_doan(inp):
    a, b = map(int, inp.split()[:2])
    crossed = [False] * (b + 1)
    count = 0
    for i in range(2, b + 1):
        if not crossed[i]:
            if i >= a:
                count += 1
            for j in range(i * i, b + 1, i):
                crossed[j] = True
    return f"{count}\n"


@problem(
    title="Tách số chẵn thành hai số nguyên tố",
    difficulty=3,
    statement="""
        Nhà toán học Goldbach đoán rằng mọi số chẵn lớn hơn 2 đều viết được thành tổng của hai số nguyên tố, ví dụ 16 = 3 + 13 = 5 + 11. Em hãy kiểm tra điều đó với số chẵn n.

        Nhắc lại: số nguyên tố là số tự nhiên lớn hơn 1 chỉ có đúng hai ước là 1 và chính nó.

        Đầu vào:
        - Một số nguyên chẵn n (4 ≤ n ≤ 1 000 000).

        Đầu ra:
        - In ra hai số nguyên tố p và q trên một dòng, cách nhau một dấu cách, sao cho p + q = n và p ≤ q.
        - Nếu có nhiều cách, chọn cách có p nhỏ nhất.

        Gợi ý:
        - Thử p = 2, 3, 4, ... và dừng ở p đầu tiên mà cả p và n - p đều là số nguyên tố.
    """,
    tests=lambda r: ["10", "4", "6", "1000000", "8", "98", "999998", "128",
                     str(2 * r.randint(1000, 500000))],
)
def goldbach(inp):
    n = int(inp.split()[0])
    crossed = [False] * (n + 1)
    crossed[0] = crossed[1] = True
    i = 2
    while i * i <= n:
        if not crossed[i]:
            for j in range(i * i, n + 1, i):
                crossed[j] = True
        i += 1
    p = 2
    while crossed[p] or crossed[n - p]:
        p += 1
    return f"{p} {n - p}\n"


@problem(
    title="Phân tích số ra thừa số nguyên tố",
    difficulty=3,
    statement="""
        Mọi số tự nhiên n ≥ 2 đều viết được thành tích của các số nguyên tố, giống như xếp hình từ những viên gạch nhỏ nhất. Ví dụ 360 = 2 × 2 × 2 × 3 × 3 × 5.

        Đầu vào:
        - Một số nguyên n (2 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra các thừa số nguyên tố khác nhau của n theo thứ tự tăng dần, mỗi thừa số viết dạng p^k, trong đó k là số lần p xuất hiện trong tích. Nếu k = 1 thì chỉ viết p.
        - Giữa hai thừa số in một dấu cách, dấu *, rồi một dấu cách. Ví dụ với n = 360 thì in ra: 2^3 * 3^2 * 5
        - Nếu n là số nguyên tố thì chỉ in ra n.

        Gợi ý:
        - Thử chia n cho d = 2, 3, 4, ... trong khi d × d ≤ n. Khi n chia hết cho d thì chia mãi cho d và đếm số lần chia. Cuối cùng, nếu n còn lớn hơn 1 thì phần còn lại là một số nguyên tố.
    """,
    tests=lambda r: ["84", "2", "97", "1024", "1000000000", "999999937", "999999999",
                     "30030", "998812807", str(r.randint(10**5, 10**9))],
)
def phan_tich_thua_so(inp):
    n = int(inp.split()[0])
    parts = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            k = 0
            while n % d == 0:
                n //= d
                k += 1
            parts.append(f"{d}^{k}" if k > 1 else str(d))
        d += 1
    if n > 1:
        parts.append(str(n))
    return " * ".join(parts) + "\n"


@problem(
    title="Bao nhiêu số 0 ở cuối giai thừa?",
    difficulty=3,
    statement="""
        Giai thừa của n, viết là n!, là tích 1 × 2 × 3 × ... × n. Riêng 0! = 1. Ví dụ 7! = 5040 có một chữ số 0 ở cuối. Số n! lớn rất nhanh, nhưng bạn Tùng chỉ muốn biết n! có bao nhiêu chữ số 0 liên tiếp ở cuối.

        Đầu vào:
        - Một số nguyên n (0 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra số chữ số 0 liên tiếp ở cuối của n!.

        Gợi ý:
        - Không thể tính trực tiếp n! vì nó quá lớn. Mỗi chữ số 0 ở cuối sinh ra từ một cặp 2 × 5, mà thừa số 2 luôn nhiều hơn thừa số 5. Vậy chỉ cần đếm thừa số 5: kết quả là n/5 + n/25 + n/125 + ... (chia lấy phần nguyên, dừng khi bằng 0).
    """,
    tests=lambda r: ["10", "0", "4", "5", "25", "100", "1000000000", "124", "125",
                     str(r.randint(10**4, 10**9))],
)
def so_0_cuoi_giai_thua(inp):
    n = int(inp.split()[0])
    count = 0
    while n > 0:
        n //= 5
        count += n
    return f"{count}\n"


@problem(
    title="Đồng hồ cây số đối xứng tiếp theo",
    difficulty=3,
    statement="""
        Đồng hồ đo quãng đường trên xe của bố đang chỉ n km. Bé Su muốn biết khi xe chạy thêm, lần đầu tiên đồng hồ hiện một số đối xứng (lớn hơn n) là lúc chỉ bao nhiêu km.

        Số đối xứng là số đọc từ trái sang phải hay từ phải sang trái đều giống nhau, ví dụ 7, 44, 121. Mọi số có một chữ số đều là số đối xứng.

        Đầu vào:
        - Một số nguyên n (0 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra số đối xứng nhỏ nhất lớn hơn n (chú ý: phải lớn hơn hẳn n, kể cả khi n đã là số đối xứng).

        Gợi ý:
        - Thử lần lượt n + 1, n + 2, ... cho đến khi gặp số đối xứng. Hai số đối xứng liên tiếp không cách nhau quá xa nên cách này đủ nhanh.
    """,
    tests=lambda r: ["123", "0", "9", "99", "999999999", "1000000000", "12321", "808",
                     "1991", str(r.randint(10**6, 10**9))],
)
def doi_xung_tiep_theo(inp):
    n = int(inp.split()[0])
    x = n + 1
    while True:
        m, rev = x, 0
        while m > 0:
            rev = rev * 10 + m % 10
            m //= 10
        if rev == x:
            return f"{x}\n"
        x += 1


@problem(
    title="Đi tìm số vui vẻ",
    difficulty=3,
    statement="""
        Từ số n, ta thay n bằng tổng bình phương các chữ số của nó (bình phương của a là a × a), rồi cứ lặp lại như thế. Nếu đến một lúc nào đó dãy số (tính cả chính n) gặp số 1 thì n được gọi là số vui vẻ. Như vậy số 1 cũng là số vui vẻ.

        Ví dụ: 7 → 49 → 97 → 130 → 10 → 1, nên 7 là số vui vẻ.

        Nếu n không phải số vui vẻ thì dãy sẽ quay vòng mãi mãi. Người ta đã chứng minh rằng khi đó dãy chắc chắn sẽ đi qua số 4 (vòng lặp 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4).

        Đầu vào:
        - Một số nguyên n (1 ≤ n ≤ 1 000 000 000).

        Đầu ra:
        - In ra YES nếu n là số vui vẻ, ngược lại in ra NO.

        Gợi ý:
        - Lặp cho đến khi gặp số 1 (in YES) hoặc gặp số 4 (in NO).
    """,
    tests=lambda r: ["19", "1", "4", "2", "1000000000", "999999999", "100", "989", "68",
                     str(r.randint(10**5, 10**9))],
)
def so_vui_ve(inp):
    n = int(inp.split()[0])
    while n != 1 and n != 4:
        s = 0
        while n > 0:
            d = n % 10
            s += d * d
            n //= 10
        n = s
    return ("YES" if n == 1 else "NO") + "\n"


@problem(
    title="Hằng số bí ẩn 6174 của Kaprekar",
    difficulty=3,
    statement="""
        Nhà toán học Ấn Độ Kaprekar phát hiện một trò chơi kỳ diệu với số có 4 chữ số. Mỗi lượt chơi gồm:
        - Xếp 4 chữ số theo thứ tự giảm dần được số lớn, xếp theo thứ tự tăng dần được số bé.
        - Lấy số lớn trừ số bé, được số mới để chơi lượt tiếp theo.
        Kỳ lạ thay, nếu 4 chữ số không giống hệt nhau thì sau vài lượt ta luôn gặp số 6174!

        Luôn coi số có đủ 4 chữ số, thiếu thì thêm chữ số 0 ở đầu. Ví dụ hiệu bằng 999 thì coi là 0999: số lớn là 9990, số bé là 0999 = 999. Tương tự, với 1000 thì số bé là 0001 = 1.

        Đầu vào:
        - Một số nguyên n (1000 ≤ n ≤ 9999), bốn chữ số của n không giống hệt nhau (không phải 1111, 2222, ..., 9999).

        Đầu ra:
        - In ra số lượt chơi cần thực hiện để lần đầu tiên gặp số 6174. Nếu n = 6174 thì in ra 0.
    """,
    tests=lambda r: ["3524", "6174", "1000", "2111", "9998", "1112", "4321", "8082",
                     "9831", str(r.choice([x for x in range(1000, 10000) if len(set(str(x))) > 1]))],
)
def kaprekar(inp):
    n = int(inp.split()[0])
    steps = 0
    while n != 6174:
        digits = [n // 1000 % 10, n // 100 % 10, n // 10 % 10, n % 10]
        digits.sort()
        small = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]
        big = digits[3] * 1000 + digits[2] * 100 + digits[1] * 10 + digits[0]
        n = big - small
        steps += 1
    return f"{steps}\n"
