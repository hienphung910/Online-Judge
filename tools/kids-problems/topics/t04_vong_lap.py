"""Chủ đề 4: Vòng lặp (for / while) — bài K091–K120."""

from kidslib import problem

TOPIC = "vong-lap"


# =====================================================================
#                              BÀI DỄ
# =====================================================================

@problem(
    title="Bé Na tập đếm đến n",
    difficulty=1,
    statement="""
        Bé Na vừa vào lớp 1 và đang tập đếm. Em hãy viết chương trình đếm giúp Na
        từ 1 cho đến n nhé!

        Đầu vào:
        - Một dòng chứa số nguyên n.

        Đầu ra:
        - In các số 1, 2, 3, ..., n trên cùng một dòng, các số cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ n ≤ 100.

        Gợi ý:
        - Dùng vòng lặp for cho biến i chạy từ 1 đến n và in i ra.
    """,
    tests=["5", "1", "2", "10", "100", "37", "64", "99"],
)
def solve_dem_den_n(inp):
    n = int(inp.split()[0])
    nums = []
    for i in range(1, n + 1):
        nums.append(str(i))
    return " ".join(nums) + "\n"


@problem(
    title="Đếm ngược phóng tên lửa giấy",
    difficulty=1,
    statement="""
        Cả lớp vừa gấp xong một chiếc tên lửa giấy thật to! Trước khi phóng, mọi người
        cùng đếm ngược từ n về 1, rồi đồng thanh hô "Phong!".

        Đầu vào:
        - Một dòng chứa số nguyên n.

        Đầu ra:
        - n dòng đầu tiên lần lượt là các số n, n - 1, ..., 2, 1 (mỗi số trên một dòng).
        - Dòng cuối cùng in chữ: Phong!

        Giới hạn:
        - 1 ≤ n ≤ 100.
    """,
    tests=["5", "1", "2", "10", "100", "23", "58"],
)
def solve_ten_lua(inp):
    n = int(inp.split()[0])
    lines = []
    i = n
    while i >= 1:
        lines.append(str(i))
        i -= 1
    lines.append("Phong!")
    return "\n".join(lines) + "\n"


@problem(
    title="Thỏ con chỉ nhảy lên bậc chẵn",
    difficulty=1,
    statement="""
        Cầu thang trước nhà có n bậc, đánh số từ 1 (dưới cùng) đến n (trên cùng).
        Thỏ con rất thích số chẵn nên chỉ đặt chân lên những bậc có số thứ tự là số chẵn.
        Em hãy liệt kê các bậc mà thỏ con đã đặt chân lên.

        Đầu vào:
        - Một dòng chứa số nguyên n.

        Đầu ra:
        - In các số chẵn từ 2 đến n theo thứ tự tăng dần, trên cùng một dòng,
          các số cách nhau một dấu cách.

        Giới hạn:
        - 2 ≤ n ≤ 200.
    """,
    tests=["9", "2", "3", "4", "200", "199", "57", "100"],
)
def solve_bac_chan(inp):
    n = int(inp.split()[0])
    nums = []
    for i in range(2, n + 1, 2):
        nums.append(str(i))
    return " ".join(nums) + "\n"


@problem(
    title="Vẹt Kiki đọc bảng nhân",
    difficulty=1,
    statement="""
        Chú vẹt Kiki rất thông minh, chú muốn học thuộc bảng nhân của số n
        (từ n nhân 1 đến n nhân 10). Em hãy in bảng nhân đó ra để Kiki đọc theo.

        Đầu vào:
        - Một dòng chứa số nguyên n.

        Đầu ra:
        - Gồm 10 dòng. Dòng thứ i (i từ 1 đến 10) có dạng: <n> x <i> = <tích của n và i>
        - Giữa các phần trên mỗi dòng có đúng một dấu cách, dùng chữ x thường làm dấu nhân.

        Giới hạn:
        - 1 ≤ n ≤ 100.
    """,
    tests=["3", "1", "2", "9", "10", "100", "47", "13"],
)
def solve_bang_nhan(inp):
    n = int(inp.split()[0])
    lines = []
    for i in range(1, 11):
        lines.append(f"{n} x {i} = {n * i}")
    return "\n".join(lines) + "\n"


@problem(
    title="Những hộp kẹo xếp thành hàng",
    difficulty=1,
    statement="""
        Cửa hàng kẹo xếp n chiếc hộp thành một hàng. Hộp thứ nhất có 1 viên kẹo,
        hộp thứ hai có 2 viên, hộp thứ ba có 3 viên, ..., hộp thứ n có n viên.
        Hỏi cả hàng có tất cả bao nhiêu viên kẹo?

        Đầu vào:
        - Một dòng chứa số nguyên n.

        Đầu ra:
        - Một số nguyên là tổng số viên kẹo trong n hộp.

        Giới hạn:
        - 1 ≤ n ≤ 10000.

        Gợi ý:
        - Tạo biến tong = 0, rồi dùng vòng lặp cộng dồn lần lượt 1, 2, ..., n vào tong.
    """,
    tests=["4", "1", "2", "10", "100", "10000", "777", "2024"],
)
def solve_hop_keo(inp):
    n = int(inp.split()[0])
    total = 0
    for i in range(1, n + 1):
        total += i
    return f"{total}\n"


@problem(
    title="Ếch xanh nhảy đều trên các viên đá",
    difficulty=1,
    statement="""
        Trên mặt hồ có một hàng viên đá được đánh số 1, 2, 3, ... Chú ếch xanh đang đứng
        ở viên đá số a. Mỗi lần nhảy, ếch tiến thêm đúng k viên đá. Ếch không bao giờ nhảy
        tới viên đá có số lớn hơn b, nên nếu lần nhảy tiếp theo vượt quá b thì ếch dừng lại.

        Đầu vào:
        - Một dòng chứa ba số nguyên a, b, k, cách nhau một dấu cách.

        Đầu ra:
        - In số thứ tự của các viên đá mà ếch đã đứng lên (kể cả viên đá số a lúc đầu),
          theo thứ tự ếch đi qua, trên cùng một dòng, các số cách nhau một dấu cách.

        Giới hạn:
        - 1 ≤ a ≤ b ≤ 500.
        - 1 ≤ k ≤ 100.
    """,
    tests=["2 15 3", "1 1 1", "5 5 7", "3 10 100", "1 500 1",
           "10 100 10", "7 500 99", "123 456 7"],
)
def solve_ech_nhay(inp):
    a, b, k = map(int, inp.split()[:3])
    nums = []
    x = a
    while x <= b:
        nums.append(str(x))
        x += k
    return " ".join(nums) + "\n"


@problem(
    title="Nhặt trứng ở trang trại của ông",
    difficulty=1,
    statement="""
        Ông của Tâm nuôi một đàn gà ở trang trại. Suốt n ngày, mỗi ngày ông đều ghi lại
        số quả trứng nhặt được. Em hãy giúp ông tính tổng số trứng của cả n ngày.

        Đầu vào:
        - Dòng thứ nhất chứa số nguyên n.
        - Dòng thứ hai chứa n số nguyên, là số trứng nhặt được trong từng ngày,
          các số cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là tổng số trứng.

        Giới hạn:
        - 1 ≤ n ≤ 100.
        - Số trứng mỗi ngày từ 0 đến 1000.

        Gợi ý:
        - Không cần nhớ cả dãy số: đọc được số nào thì cộng ngay số đó vào tổng.
    """,
    tests=lambda r: [
        "5\n3 7 0 12 5\n",
        "1\n0\n",
        "1\n1000\n",
        "100\n" + " ".join(["1000"] * 100) + "\n",
        "3\n0 0 1\n",
        "10\n" + " ".join(str(r.randint(0, 50)) for _ in range(10)) + "\n",
        "40\n" + " ".join(str(r.randint(0, 1000)) for _ in range(40)) + "\n",
        "100\n" + " ".join(str(r.randint(0, 1000)) for _ in range(100)) + "\n",
    ],
)
def solve_nhat_trung(inp):
    data = inp.split()
    n = int(data[0])
    total = 0
    for i in range(1, n + 1):
        total += int(data[i])
    return f"{total}\n"


@problem(
    title="Bao nhiêu bạn qua bài kiểm tra?",
    difficulty=1,
    statement="""
        Cô giáo vừa chấm xong bài kiểm tra của n bạn trong lớp. Bạn nào được từ 5 điểm
        trở lên thì qua bài. Em hãy đếm xem có bao nhiêu bạn qua bài kiểm tra.

        Đầu vào:
        - Dòng thứ nhất chứa số nguyên n.
        - Dòng thứ hai chứa n số nguyên là điểm của từng bạn, các số cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là số bạn được từ 5 điểm trở lên.

        Giới hạn:
        - 1 ≤ n ≤ 100.
        - Mỗi điểm là số nguyên từ 0 đến 10.
    """,
    tests=lambda r: [
        "6\n7 4 10 5 3 8\n",
        "1\n4\n",
        "1\n5\n",
        "5\n0 0 0 0 0\n",
        "8\n10 10 10 10 10 10 10 10\n",
        "12\n4 5 4 5 4 5 4 5 4 5 4 5\n",
        "30\n" + " ".join(str(r.randint(0, 10)) for _ in range(30)) + "\n",
        "100\n" + " ".join(str(r.randint(0, 10)) for _ in range(100)) + "\n",
    ],
)
def solve_qua_bai(inp):
    data = inp.split()
    n = int(data[0])
    count = 0
    for i in range(1, n + 1):
        if int(data[i]) >= 5:
            count += 1
    return f"{count}\n"


@problem(
    title="Mèo Mướp chỉ được ăn cá vào ngày chẵn",
    difficulty=1,
    statement="""
        Bà thưởng cá cho mèo Mướp theo một luật rất lạ: vào ngày thứ i, nếu i là số chẵn
        thì Mướp được i con cá, còn nếu i là số lẻ thì hôm đó Mướp không được con nào.
        Hỏi trong n ngày (từ ngày 1 đến ngày n), Mướp được tất cả bao nhiêu con cá?

        Đầu vào:
        - Một dòng chứa số nguyên n.

        Đầu ra:
        - Một số nguyên là tổng số cá Mướp nhận được.

        Giới hạn:
        - 1 ≤ n ≤ 10000.
    """,
    tests=["6", "1", "2", "3", "10000", "9999", "500", "1234"],
)
def solve_meo_muop(inp):
    n = int(inp.split()[0])
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return f"{total}\n"


@problem(
    title="Trạm thời tiết: ngày ấm, ngày lạnh, ngày 0 độ",
    difficulty=1,
    statement="""
        Trạm thời tiết trên đỉnh núi ghi lại nhiệt độ lúc sáng sớm trong n ngày.
        Em hãy đếm xem có bao nhiêu ngày nhiệt độ dương (lớn hơn 0), bao nhiêu ngày
        nhiệt độ âm (nhỏ hơn 0) và bao nhiêu ngày nhiệt độ đúng bằng 0.

        Đầu vào:
        - Dòng thứ nhất chứa số nguyên n.
        - Dòng thứ hai chứa n số nguyên là nhiệt độ của từng ngày, các số cách nhau một dấu cách.

        Đầu ra:
        - In ba số trên một dòng, cách nhau một dấu cách: số ngày nhiệt độ dương,
          số ngày nhiệt độ âm, số ngày nhiệt độ bằng 0.

        Giới hạn:
        - 1 ≤ n ≤ 100.
        - Mỗi nhiệt độ là số nguyên từ -30 đến 30.
    """,
    tests=lambda r: [
        "7\n3 -2 0 5 -1 0 8\n",
        "1\n0\n",
        "1\n-30\n",
        "1\n30\n",
        "6\n0 0 0 0 0 0\n",
        "20\n" + " ".join(str(r.randint(-5, 5)) for _ in range(20)) + "\n",
        "50\n" + " ".join(str(r.randint(-30, 10)) for _ in range(50)) + "\n",
        "100\n" + " ".join(str(r.randint(-30, 30)) for _ in range(100)) + "\n",
    ],
)
def solve_tram_thoi_tiet(inp):
    data = inp.split()
    n = int(data[0])
    duong = am = khong = 0
    for i in range(1, n + 1):
        t = int(data[i])
        if t > 0:
            duong += 1
        elif t < 0:
            am += 1
        else:
            khong += 1
    return f"{duong} {am} {khong}\n"


# =====================================================================
#                              BÀI VỪA
# =====================================================================

@problem(
    title="Bao nhiêu cách xếp hàng chụp ảnh?",
    difficulty=2,
    statement="""
        Nhóm bạn có n người muốn đứng thành một hàng ngang để chụp ảnh kỷ niệm.
        Các bạn tò mò: có bao nhiêu cách xếp hàng khác nhau? Thầy giáo nói số cách đó
        bằng n giai thừa, viết là n! = 1 × 2 × 3 × ... × n.

        Đầu vào:
        - Một dòng chứa số nguyên n.

        Đầu ra:
        - Một số nguyên là giá trị của n!.

        Giới hạn:
        - 1 ≤ n ≤ 12.

        Gợi ý:
        - Bắt đầu với tich = 1 rồi lần lượt nhân tich với 1, 2, ..., n.
    """,
    tests=["3", "1", "2", "12", "10", "5", "7", "11"],
)
def solve_giai_thua(inp):
    n = int(inp.split()[0])
    result = 1
    for i in range(1, n + 1):
        result *= i
    return f"{result}\n"


@problem(
    title="Bèo hoa dâu nhân lên mỗi ngày",
    difficulty=2,
    statement="""
        Sáng nay trên mặt ao chỉ có đúng 1 cây bèo hoa dâu. Cứ qua mỗi ngày, mỗi cây bèo
        lại biến thành a cây, tức là số bèo trên ao được nhân lên a lần.
        Hỏi sau b ngày, trên ao có bao nhiêu cây bèo?

        Đầu vào:
        - Một dòng chứa hai số nguyên a và b, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là số cây bèo sau b ngày (chính là a mũ b).

        Giới hạn:
        - 1 ≤ a ≤ 10; 0 ≤ b ≤ 30.
        - Đảm bảo kết quả không vượt quá 1000000000.
        - Nếu b = 0 thì chưa qua ngày nào, ao vẫn có 1 cây bèo.
    """,
    tests=["2 3", "5 0", "1 30", "10 9", "2 29", "3 18", "7 10", "10 1"],
)
def solve_beo_hoa_dau(inp):
    a, b = map(int, inp.split()[:2])
    result = 1
    for _ in range(b):
        result *= a
    return f"{result}\n"


@problem(
    title="Quả dưa hấu nặng nhất và nhẹ nhất",
    difficulty=2,
    statement="""
        Bác Tư vừa thu hoạch dưa hấu và đặt lần lượt từng quả lên cân. Em hãy giúp bác
        tìm xem quả nặng nhất và quả nhẹ nhất nặng bao nhiêu gam.

        Đầu vào:
        - Dòng thứ nhất chứa số nguyên n là số quả dưa.
        - Dòng thứ hai chứa n số nguyên là cân nặng (gam) của từng quả, cách nhau một dấu cách.

        Đầu ra:
        - In hai số trên một dòng, cách nhau một dấu cách: cân nặng lớn nhất,
          rồi đến cân nặng nhỏ nhất.

        Giới hạn:
        - 1 ≤ n ≤ 100.
        - Mỗi cân nặng từ 1 đến 10000.

        Gợi ý:
        - Lấy quả đầu tiên làm mốc cho cả "nặng nhất" và "nhẹ nhất", rồi so sánh với
          từng quả tiếp theo.
    """,
    tests=lambda r: [
        "5\n2300 4100 1800 3500 4100\n",
        "1\n5000\n",
        "3\n700 700 700\n",
        "2\n1 10000\n",
        "2\n10000 1\n",
        "10\n" + " ".join(str(r.randint(1000, 6000)) for _ in range(10)) + "\n",
        "60\n" + " ".join(str(r.randint(1, 10000)) for _ in range(60)) + "\n",
        "100\n" + " ".join(str(r.randint(2000, 9000)) for _ in range(100)) + "\n",
    ],
)
def solve_dua_hau(inp):
    data = inp.split()
    n = int(data[0])
    lon = nho = int(data[1])
    for i in range(2, n + 1):
        w = int(data[i])
        if w > lon:
            lon = w
        if w < nho:
            nho = w
    return f"{lon} {nho}\n"


@problem(
    title="Máy đếm xu dừng lại khi gặp số 0",
    difficulty=2,
    statement="""
        Tí đập heo đất và nhập lần lượt mệnh giá của từng đồng xu vào máy đếm.
        Khi hết xu, Tí nhập số 0 để báo cho máy biết. Em hãy giúp máy đếm xem có
        bao nhiêu đồng xu và tổng giá trị của chúng là bao nhiêu.

        Đầu vào:
        - Một dãy số nguyên, các số cách nhau bởi dấu cách hoặc dấu xuống dòng.
        - Dãy luôn kết thúc bằng số 0. Số 0 chỉ là dấu hiệu dừng, không phải đồng xu,
          nên không được đếm. Sau số 0 không còn số nào nữa.

        Đầu ra:
        - In hai số trên một dòng, cách nhau một dấu cách: số đồng xu và tổng mệnh giá.

        Giới hạn:
        - Có từ 0 đến 100 đồng xu (nếu số đầu tiên đã là 0 thì không có đồng xu nào).
        - Mỗi mệnh giá là một trong các số 200, 500, 1000, 2000, 5000.

        Gợi ý:
        - Dùng vòng lặp while: đọc một số, nếu khác 0 thì đếm và cộng, rồi đọc số tiếp theo.
    """,
    tests=lambda r: [
        "500 1000 200 500 0\n",
        "0\n",
        "5000 0\n",
        "200\n200\n200\n0\n",
        " ".join(["5000"] * 100) + " 0\n",
        "\n".join(r.choice(["200", "500", "1000", "2000", "5000"]) for _ in range(12)) + "\n0\n",
        " ".join(r.choice(["200", "500", "1000", "2000", "5000"]) for _ in range(37)) + " 0\n",
        " ".join(r.choice(["200", "500", "1000", "2000", "5000"]) for _ in range(100)) + "\n0\n",
    ],
)
def solve_may_dem_xu(inp):
    data = inp.split()
    count = 0
    total = 0
    pos = 0
    x = int(data[pos])
    while x != 0:
        count += 1
        total += x
        pos += 1
        x = int(data[pos])
    return f"{count} {total}\n"


@problem(
    title="Những cột đèn được sơn màu đỏ",
    difficulty=2,
    statement="""
        Con đường làng có n cột đèn, đánh số từ 1 đến n. Đội sơn quyết định: cột nào có
        số thứ tự chia hết cho 3 hoặc chia hết cho 5 thì sơn màu đỏ. Em hãy liệt kê
        các cột được sơn đỏ.

        Đầu vào:
        - Một dòng chứa số nguyên n.

        Đầu ra:
        - In số thứ tự của các cột được sơn đỏ theo thứ tự tăng dần, trên cùng một dòng,
          các số cách nhau một dấu cách.

        Giới hạn:
        - 3 ≤ n ≤ 200.
    """,
    tests=["16", "3", "4", "5", "200", "30", "99", "150"],
)
def solve_cot_den(inp):
    n = int(inp.split()[0])
    nums = []
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            nums.append(str(i))
    return " ".join(nums) + "\n"


@problem(
    title="Tháp cam xếp từng tầng vuông",
    difficulty=2,
    statement="""
        Cô bán hoa quả xếp cam thành một cái tháp n tầng. Tầng trên cùng có 1 quả,
        tầng thứ hai có 2 × 2 = 4 quả, tầng thứ ba có 3 × 3 = 9 quả, ...,
        tầng thứ n (dưới cùng) có n × n quả. Hỏi cả tháp có bao nhiêu quả cam?

        Đầu vào:
        - Một dòng chứa số nguyên n là số tầng của tháp.

        Đầu ra:
        - Một số nguyên là tổng số quả cam.

        Giới hạn:
        - 1 ≤ n ≤ 1000.
    """,
    tests=["3", "1", "2", "1000", "100", "10", "500", "37"],
)
def solve_thap_cam(inp):
    n = int(inp.split()[0])
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return f"{total}\n"


@problem(
    title="Robot Bi tiến một, lùi hai",
    difficulty=2,
    statement="""
        Robot Bi đứng ở vạch số 0 trên một đường thẳng và lần lượt đi n bước.
        Ở bước thứ i, Bi đi đúng i vạch: nếu i là số lẻ thì Bi tiến về phía trước
        (vị trí tăng thêm i), nếu i là số chẵn thì Bi lùi lại (vị trí giảm đi i).
        Hỏi sau n bước Bi đứng ở vạch số mấy? Nói cách khác, hãy tính 1 - 2 + 3 - 4 + ... (đến n).

        Đầu vào:
        - Một dòng chứa số nguyên n.

        Đầu ra:
        - Một số nguyên là vị trí cuối cùng của Bi (có thể là số âm nếu Bi lùi về sau vạch 0).

        Giới hạn:
        - 1 ≤ n ≤ 10000.
    """,
    tests=["5", "1", "2", "10000", "9999", "3", "100", "777"],
)
def solve_robot_tien_lui(inp):
    n = int(inp.split()[0])
    pos = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            pos += i
        else:
            pos -= i
    return f"{pos}\n"


@problem(
    title="Đàn thỏ nhà bác Ba sinh sôi",
    difficulty=2,
    statement="""
        Đàn thỏ nhà bác Ba tăng lên theo một quy luật đặc biệt: tháng thứ 1 có 1 đôi thỏ,
        tháng thứ 2 cũng có 1 đôi thỏ, từ tháng thứ 3 trở đi, số đôi thỏ của mỗi tháng
        bằng tổng số đôi thỏ của hai tháng liền trước nó.
        Em hãy liệt kê số đôi thỏ của n tháng đầu tiên.

        Đầu vào:
        - Một dòng chứa số nguyên n.

        Đầu ra:
        - In n số trên cùng một dòng, cách nhau một dấu cách: số đôi thỏ của tháng 1,
          tháng 2, ..., tháng n.

        Giới hạn:
        - 1 ≤ n ≤ 40.

        Gợi ý:
        - Chỉ cần nhớ hai số của hai tháng gần nhất là tính được tháng tiếp theo.
    """,
    tests=["7", "1", "2", "3", "40", "10", "25", "33"],
)
def solve_dan_tho(inp):
    n = int(inp.split()[0])
    nums = []
    a, b = 1, 1
    for _ in range(n):
        nums.append(str(a))
        a, b = b, a + b
    return " ".join(nums) + "\n"


@problem(
    title="Tí bỏ heo đất để mua xe đạp",
    difficulty=2,
    statement="""
        Tí muốn mua một chiếc xe đạp giá m đồng. Ngày đầu tiên Tí bỏ vào heo đất a đồng,
        và mỗi ngày sau đó Tí bỏ vào nhiều hơn ngày liền trước đúng k đồng.
        Hỏi sau ít nhất bao nhiêu ngày thì số tiền trong heo đất đủ để mua xe
        (tức là lớn hơn hoặc bằng m)?

        Đầu vào:
        - Một dòng chứa ba số nguyên m, a, k, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là số ngày ít nhất cần bỏ heo.

        Giới hạn:
        - 1 ≤ m ≤ 100000.
        - 1 ≤ a ≤ 1000; 0 ≤ k ≤ 100.

        Gợi ý:
        - Dùng vòng lặp while: còn chưa đủ tiền thì sang ngày mới và bỏ thêm tiền.
    """,
    tests=["50 5 2", "1 1 0", "1000 1000 0", "100000 1 0", "100000 1 100",
           "999 10 0", "12345 7 3", "100000 1000 100"],
)
def solve_heo_dat(inp):
    m, a, k = map(int, inp.split()[:3])
    saved = 0
    today = a
    days = 0
    while saved < m:
        days += 1
        saved += today
        today += k
    return f"{days}\n"


@problem(
    title="Ống nghiệm vi khuẩn nhân đôi",
    difficulty=2,
    statement="""
        Trong phòng thí nghiệm, một ống nghiệm lúc đầu có a con vi khuẩn. Cứ sau mỗi giờ,
        số vi khuẩn lại tăng lên gấp đôi. Hỏi phải sau ít nhất bao nhiêu giờ thì số vi khuẩn
        nhiều hơn hẳn m con (tức là lớn hơn m, bằng m thì chưa tính)?

        Đầu vào:
        - Một dòng chứa hai số nguyên a và m, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là số giờ ít nhất cần chờ.

        Giới hạn:
        - 1 ≤ a ≤ m ≤ 1000000000.
    """,
    tests=["3 20", "1 1", "1 1000000000", "1000000000 1000000000", "5 6",
           "7 1000", "123 999999999", "500000000 999999999"],
)
def solve_vi_khuan(inp):
    a, m = map(int, inp.split()[:2])
    hours = 0
    while a <= m:
        a *= 2
        hours += 1
    return f"{hours}\n"


@problem(
    title="Trận bóng bàn nhiều ván giữa An và Bình",
    difficulty=2,
    statement="""
        An và Bình chơi n ván bóng bàn. Trong mỗi ván, ai được nhiều điểm hơn thì thắng
        ván đó; nếu hai bạn bằng điểm thì ván đó hòa, không ai thắng. Cuối cùng, ai thắng
        nhiều ván hơn sẽ là người thắng chung cuộc.

        Đầu vào:
        - Dòng thứ nhất chứa số nguyên n là số ván.
        - n dòng tiếp theo, mỗi dòng chứa hai số nguyên x và y: điểm của An và điểm
          của Bình trong một ván.

        Đầu ra:
        - Dòng thứ nhất: số ván An thắng và số ván Bình thắng, cách nhau một dấu cách.
        - Dòng thứ hai: in AN nếu An thắng chung cuộc, BINH nếu Bình thắng chung cuộc,
          HOA nếu hai bạn thắng số ván bằng nhau.

        Giới hạn:
        - 1 ≤ n ≤ 50.
        - 0 ≤ x, y ≤ 30.
    """,
    tests=lambda r: [
        "5\n11 7\n9 11\n11 5\n10 10\n11 8\n",
        "1\n5 5\n",
        "1\n0 11\n",
        "2\n11 3\n4 11\n",
        "3\n11 9\n11 10\n12 10\n",
        "8\n" + "".join(f"{r.randint(5, 13)} {r.randint(5, 13)}\n" for _ in range(8)),
        "25\n" + "".join(f"{r.randint(0, 15)} {r.randint(3, 20)}\n" for _ in range(25)),
        "50\n" + "".join(f"{r.randint(0, 30)} {r.randint(0, 30)}\n" for _ in range(50)),
    ],
)
def solve_bong_ban(inp):
    data = inp.split()
    n = int(data[0])
    an = binh = 0
    pos = 1
    for _ in range(n):
        x = int(data[pos])
        y = int(data[pos + 1])
        pos += 2
        if x > y:
            an += 1
        elif y > x:
            binh += 1
    if an > binh:
        winner = "AN"
    elif binh > an:
        winner = "BINH"
    else:
        winner = "HOA"
    return f"{an} {binh}\n{winner}\n"


@problem(
    title="Hôm nay có nóng hơn hôm qua không?",
    difficulty=2,
    statement="""
        Bạn Minh ghi lại nhiệt độ buổi trưa trong n ngày liên tiếp. Minh muốn biết có
        bao nhiêu ngày nóng hơn hẳn ngày ngay trước nó (nhiệt độ lớn hơn, bằng thì không tính).
        Ngày đầu tiên không có ngày trước nên không được tính.

        Đầu vào:
        - Dòng thứ nhất chứa số nguyên n.
        - Dòng thứ hai chứa n số nguyên là nhiệt độ của từng ngày theo thứ tự,
          các số cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là số ngày nóng hơn ngày liền trước.

        Giới hạn:
        - 1 ≤ n ≤ 100.
        - Mỗi nhiệt độ là số nguyên từ -20 đến 45.

        Gợi ý:
        - Dùng một biến để nhớ nhiệt độ của ngày vừa đọc trước đó.
    """,
    tests=lambda r: [
        "6\n25 27 27 30 28 31\n",
        "1\n20\n",
        "5\n5 4 3 2 1\n",
        "5\n-3 -2 -1 0 1\n",
        "4\n7 7 7 7\n",
        "15\n" + " ".join(str(r.randint(-5, 5)) for _ in range(15)) + "\n",
        "50\n" + " ".join(str(r.randint(-20, 45)) for _ in range(50)) + "\n",
        "100\n" + " ".join(str(r.randint(20, 35)) for _ in range(100)) + "\n",
    ],
)
def solve_nong_hon(inp):
    data = inp.split()
    n = int(data[0])
    prev = int(data[1])
    count = 0
    for i in range(2, n + 1):
        t = int(data[i])
        if t > prev:
            count += 1
        prev = t
    return f"{count}\n"


# =====================================================================
#                              BÀI KHÓ
# =====================================================================

@problem(
    title="Ốc sên leo giếng: ngày lên, đêm tụt",
    difficulty=3,
    statement="""
        Một chú ốc sên đang ở đáy một cái giếng sâu h mét. Ban ngày ốc leo lên được a mét,
        nhưng ban đêm ngủ quên nên bị tụt xuống b mét. Hỏi đến ngày thứ mấy thì ốc
        lên tới miệng giếng?

        Ốc lên tới miệng giếng ngay khi quãng đường đã leo được (tính từ đáy) lớn hơn hoặc
        bằng h mét trong lúc leo ban ngày. Khi đã lên tới miệng giếng, ốc không bị tụt nữa.

        Đầu vào:
        - Một dòng chứa ba số nguyên h, a, b, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là số thứ tự của ngày ốc lên tới miệng giếng (ngày đầu tiên là ngày 1).

        Giới hạn:
        - 1 ≤ h ≤ 10000.
        - 0 ≤ b < a ≤ 100.
    """,
    tests=["10 3 2", "1 1 0", "5 5 4", "6 5 4", "10000 2 1",
           "10000 100 0", "100 10 9", "777 13 12"],
)
def solve_oc_sen(inp):
    h, a, b = map(int, inp.split()[:3])
    pos = 0
    day = 0
    while True:
        day += 1
        pos += a
        if pos >= h:
            break
        pos -= b
    return f"{day}\n"


@problem(
    title="Trò chơi 3n+1 về đích số 1",
    difficulty=3,
    statement="""
        Robot Bi chơi một trò chơi với số nguyên dương n. Ở mỗi bước, nếu số đang có là
        số chẵn thì Bi chia đôi nó, còn nếu là số lẻ thì Bi nhân nó với 3 rồi cộng thêm 1.
        Bi lặp lại cho đến khi được số 1 thì dừng.
        Em hãy cho biết Bi cần bao nhiêu bước, và số lớn nhất Bi từng gặp là bao nhiêu.

        Đầu vào:
        - Một dòng chứa số nguyên n.

        Đầu ra:
        - In hai số trên một dòng, cách nhau một dấu cách: số bước để đi từ n về 1,
          và số lớn nhất xuất hiện trong cả hành trình (tính cả số n ban đầu).
        - Nếu n = 1 thì không cần bước nào: in 0 1.

        Giới hạn:
        - 1 ≤ n ≤ 10000.
        - Đảm bảo mọi số trong hành trình đều không vượt quá 100000000.
    """,
    tests=["6", "1", "2", "27", "10000", "9663", "7", "97"],
)
def solve_collatz(inp):
    n = int(inp.split()[0])
    steps = 0
    biggest = n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
        if n > biggest:
            biggest = n
    return f"{steps} {biggest}\n"


@problem(
    title="Chuỗi ngày nắng dài nhất mùa hè",
    difficulty=3,
    statement="""
        Trong n ngày nghỉ hè, mỗi ngày bạn Hà ghi số 1 nếu trời nắng và số 0 nếu trời mưa.
        Hà muốn biết chuỗi ngày nắng liên tiếp dài nhất kéo dài bao nhiêu ngày,
        để lần sau chọn lịch đi biển cho đẹp.

        Đầu vào:
        - Dòng thứ nhất chứa số nguyên n.
        - Dòng thứ hai chứa n số, mỗi số là 0 hoặc 1, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là số ngày của chuỗi ngày nắng liên tiếp dài nhất.
          Nếu không có ngày nắng nào thì in 0.

        Giới hạn:
        - 1 ≤ n ≤ 100.

        Gợi ý:
        - Dùng một biến đếm độ dài chuỗi nắng hiện tại: gặp 1 thì tăng thêm 1,
          gặp 0 thì đặt lại về 0. Mỗi lần tăng thì so sánh với kỷ lục.
    """,
    tests=lambda r: [
        "10\n1 1 0 1 1 1 0 0 1 0\n",
        "1\n0\n",
        "1\n1\n",
        "100\n" + " ".join(["1"] * 100) + "\n",
        "8\n0 0 0 0 0 0 0 0\n",
        "9\n0 1 1 0 1 1 1 1 0\n",
        "7\n1 0 1 0 1 1 1\n",
        "40\n" + " ".join(r.choice("0111") for _ in range(40)) + "\n",
        "100\n" + " ".join(r.choice("01") for _ in range(100)) + "\n",
    ],
)
def solve_ngay_nang(inp):
    data = inp.split()
    n = int(data[0])
    current = 0
    best = 0
    for i in range(1, n + 1):
        if data[i] == "1":
            current += 1
            if current > best:
                best = current
        else:
            current = 0
    return f"{best}\n"


@problem(
    title="Ai nhận huy chương bạc nhảy xa?",
    difficulty=3,
    statement="""
        Hội thao của trường có n bạn thi nhảy xa, mỗi bạn được một số điểm.
        Huy chương vàng dành cho điểm cao nhất, còn huy chương bạc dành cho điểm cao thứ nhì:
        đó là điểm lớn nhất trong số những điểm nhỏ hơn hẳn điểm cao nhất.
        (Nếu nhiều bạn cùng đạt điểm cao nhất thì họ đều nhận vàng, không ai trong số đó nhận bạc.)
        Em hãy tìm điểm được nhận huy chương bạc.

        Đầu vào:
        - Dòng thứ nhất chứa số nguyên n.
        - Dòng thứ hai chứa n số nguyên là điểm của từng bạn, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là điểm nhận huy chương bạc.

        Giới hạn:
        - 2 ≤ n ≤ 100.
        - Mỗi điểm từ 0 đến 1000.
        - Đảm bảo có ít nhất hai điểm khác nhau.

        Gợi ý:
        - Không cần nhớ cả dãy: dùng hai biến "nhất" và "nhì", cập nhật sau mỗi số đọc vào.
    """,
    tests=lambda r: [
        "6\n7 9 4 9 8 2\n",
        "2\n5 3\n",
        "2\n3 5\n",
        "5\n0 0 0 1 0\n",
        "4\n10 10 9 9\n",
        "5\n1000 999 1000 0 1000\n",
        "20\n" + " ".join(str(r.randint(50, 60)) for _ in range(20)) + "\n",
        "100\n" + " ".join(str(r.randint(0, 1000)) for _ in range(100)) + "\n",
    ],
)
def solve_huy_chuong_bac(inp):
    data = inp.split()
    n = int(data[0])
    nhat = -1
    nhi = -1
    for i in range(1, n + 1):
        x = int(data[i])
        if x > nhat:
            nhi = nhat
            nhat = x
        elif x < nhat and x > nhi:
            nhi = x
    return f"{nhi}\n"


@problem(
    title="Đếm đỉnh núi trên đường leo núi",
    difficulty=3,
    statement="""
        Đoàn leo núi ghi lại độ cao của n điểm mốc liên tiếp trên con đường đã đi qua.
        Một điểm mốc được gọi là đỉnh nếu nó không phải điểm đầu tiên, không phải điểm
        cuối cùng, và cao hơn hẳn cả điểm ngay trước lẫn điểm ngay sau nó.
        Em hãy đếm xem trên đường có bao nhiêu đỉnh.

        Đầu vào:
        - Dòng thứ nhất chứa số nguyên n.
        - Dòng thứ hai chứa n số nguyên là độ cao của các điểm mốc theo thứ tự,
          cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là số đỉnh.

        Giới hạn:
        - 1 ≤ n ≤ 100.
        - Mỗi độ cao từ 0 đến 1000.

        Gợi ý:
        - Chỉ cần nhớ hai độ cao vừa đọc ngay trước số hiện tại.
    """,
    tests=lambda r: [
        "8\n1 3 2 4 4 1 5 2\n",
        "1\n7\n",
        "2\n1 9\n",
        "3\n1 5 1\n",
        "5\n3 3 3 3 3\n",
        "11\n0 1 0 1 0 1 0 1 0 1 0\n",
        "30\n" + " ".join(str(r.randint(0, 6)) for _ in range(30)) + "\n",
        "100\n" + " ".join(str(r.randint(0, 1000)) for _ in range(100)) + "\n",
    ],
)
def solve_dinh_nui(inp):
    data = inp.split()
    n = int(data[0])
    count = 0
    if n >= 3:
        truoc = int(data[1])
        giua = int(data[2])
        for i in range(3, n + 1):
            sau = int(data[i])
            if giua > truoc and giua > sau:
                count += 1
            truoc = giua
            giua = sau
    return f"{count}\n"


def _bus_tests(r):
    def make(c, n, want_hi):
        lines = [f"{c} {n}"]
        on_bus = 0
        for _ in range(n):
            x = r.randint(0, on_bus)
            on_bus -= x
            y = r.randint(0, want_hi)
            on_bus += min(y, c - on_bus)
            lines.append(f"{x} {y}")
        return "\n".join(lines) + "\n"

    return [
        "10 4\n0 6\n2 7\n5 3\n0 9\n",
        "1 1\n0 0\n",
        "1 1\n0 100\n",
        "100 3\n0 100\n100 100\n50 100\n",
        "5 3\n0 2\n1 2\n3 1\n",
        make(8, 10, 6),
        make(30, 25, 20),
        make(100, 50, 100),
    ]


@problem(
    title="Xe buýt chật kín, ai phải chờ chuyến sau?",
    difficulty=3,
    statement="""
        Chiếc xe buýt nhỏ chỉ chở được nhiều nhất c hành khách. Xe xuất phát khi chưa có ai
        và lần lượt đi qua n trạm. Ở mỗi trạm, đầu tiên có x người xuống xe, sau đó có
        y người muốn lên xe. Nếu xe không đủ chỗ cho tất cả thì chỉ lên được đúng bằng
        số chỗ còn trống, những người còn lại phải ở lại trạm chờ chuyến sau.

        Đầu vào:
        - Dòng thứ nhất chứa hai số nguyên c và n, cách nhau một dấu cách.
        - n dòng tiếp theo, mỗi dòng chứa hai số nguyên x và y của một trạm, theo thứ tự xe đi qua.
        - Đảm bảo x không vượt quá số người đang ở trên xe khi xe tới trạm đó.

        Đầu ra:
        - In hai số trên một dòng, cách nhau một dấu cách: số hành khách trên xe sau trạm
          cuối cùng, và tổng số người phải ở lại chờ chuyến sau ở tất cả các trạm.

        Giới hạn:
        - 1 ≤ c ≤ 100; 1 ≤ n ≤ 50.
        - 0 ≤ y ≤ 100.
    """,
    tests=_bus_tests,
)
def solve_xe_buyt(inp):
    data = inp.split()
    c = int(data[0])
    n = int(data[1])
    on_bus = 0
    left = 0
    pos = 2
    for _ in range(n):
        x = int(data[pos])
        y = int(data[pos + 1])
        pos += 2
        on_bus -= x
        free = c - on_bus
        if y <= free:
            on_bus += y
        else:
            on_bus += free
            left += y - free
    return f"{on_bus} {left}\n"


@problem(
    title="Cây đậu thần vươn tới lâu đài trên mây",
    difficulty=3,
    statement="""
        Cậu bé Jack trồng một cây đậu thần cao h xăng-ti-mét. Mỗi đêm, cây cao thêm
        p phần trăm chiều cao hiện tại, nhưng chỉ lấy phần nguyên: phần cao thêm bằng
        h × p / 100, bỏ đi phần dư. Lâu đài trên mây ở độ cao t xăng-ti-mét.
        Hỏi sau ít nhất bao nhiêu đêm thì cây cao ít nhất t xăng-ti-mét?

        Đầu vào:
        - Một dòng chứa ba số nguyên h, p, t, cách nhau một dấu cách.

        Đầu ra:
        - Một số nguyên là số đêm ít nhất. Nếu ngay từ đầu cây đã cao ít nhất t thì in 0.

        Giới hạn:
        - 100 ≤ h ≤ t ≤ 10000000.
        - 1 ≤ p ≤ 100.

        Gợi ý:
        - Chẳng hạn cây đang cao 130 và p = 50 thì đêm đó cây cao thêm 130 × 50 / 100 = 65,
          thành 195. Đêm sau cao thêm 195 × 50 / 100 = 97 (bỏ phần dư), thành 292.
    """,
    tests=["100 50 1000", "100 1 100", "100 1 101", "100 100 10000000",
           "100 1 10000000", "5000 10 123456", "999 7 1000000", "123456 3 9999999"],
)
def solve_cay_dau_than(inp):
    h, p, t = map(int, inp.split()[:3])
    nights = 0
    while h < t:
        h += h * p // 100
        nights += 1
    return f"{nights}\n"


@problem(
    title="Rùa chăm chỉ, thỏ ham ngủ: ai về trước?",
    difficulty=3,
    statement="""
        Rùa và thỏ chạy thi trên đường đua dài L mét, cùng xuất phát ở phút 0.
        Rùa chạy đều, mỗi phút đi được a mét và không bao giờ nghỉ.
        Thỏ thì mỗi phút chạy được b mét, nhưng cứ chạy được k phút thì thỏ lại
        lăn ra ngủ s phút (đứng yên), rồi lại chạy k phút, ngủ s phút, cứ thế lặp lại.
        Mỗi con về đích ở cuối phút đầu tiên mà tổng quãng đường nó đã đi được lớn hơn
        hoặc bằng L mét.

        Đầu vào:
        - Một dòng chứa năm số nguyên L, a, b, k, s, cách nhau một dấu cách.

        Đầu ra:
        - Dòng thứ nhất: phút rùa về đích và phút thỏ về đích, cách nhau một dấu cách.
        - Dòng thứ hai: in RUA nếu rùa về đích trước, THO nếu thỏ về đích trước,
          HOA nếu cả hai về đích trong cùng một phút.

        Giới hạn:
        - 1 ≤ L ≤ 1000.
        - 1 ≤ a ≤ 100; 1 ≤ b ≤ 100.
        - 1 ≤ k ≤ 20; 0 ≤ s ≤ 50.
    """,
    tests=["100 5 20 2 10", "1 1 1 1 0", "1000 1 100 1 50", "1000 100 1 20 50",
           "60 3 10 3 14", "500 7 25 4 9", "999 13 40 2 30", "777 9 77 1 50"],
)
def solve_rua_tho(inp):
    L, a, b, k, s = map(int, inp.split()[:5])
    rua_dist = 0
    rua_time = 0
    while rua_dist < L:
        rua_time += 1
        rua_dist += a
    tho_dist = 0
    tho_time = 0
    run_left = k      # so phut chay con lai trong luot nay
    sleep_left = 0    # so phut ngu con lai
    while tho_dist < L:
        tho_time += 1
        if run_left > 0:
            tho_dist += b
            run_left -= 1
            if run_left == 0:
                sleep_left = s
                if s == 0:
                    run_left = k
        else:
            sleep_left -= 1
            if sleep_left == 0:
                run_left = k
    if rua_time < tho_time:
        winner = "RUA"
    elif tho_time < rua_time:
        winner = "THO"
    else:
        winner = "HOA"
    return f"{rua_time} {tho_time}\n{winner}\n"
