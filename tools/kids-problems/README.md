# Bộ 300 bài tập thiếu nhi (K001–K300)

Mỗi chủ đề trong `data/topics.txt` có đúng **30 bài**, khai báo trong `topics/tNN_<ten>.py`.
Đáp án của mọi test được **tính bằng lời giải mẫu**, không gõ tay, nên đề và đáp án luôn khớp nhau.

```bash
py tools/kids-problems/build.py check          # kiểm tra mọi chủ đề
py tools/kids-problems/build.py check t03      # chỉ kiểm tra topics/t03_*.py
py tools/kids-problems/build.py write          # kiểm tra rồi ghi ra data/problems/K001..K300
py tools/kids-problems/build.py export out-dir # xuất lời giải mẫu thành file .py để nộp thử
```

Trên Windows gọi Python bằng **`py`** (`python`/`python3` chỉ là lối tắt mở Microsoft Store).

Mã bài cố định theo vị trí: chủ đề thứ *i* trong `data/topics.txt`, bài thứ *j* trong file → `K{(i-1)*30 + j}`.
Muốn sửa một bài thì sửa trong file chủ đề rồi chạy lại `write`; **không sửa tay** trong `data/problems/K*`.

## Cách khai báo một bài

```python
from kidslib import problem

TOPIC = "nhap-xuat"          # mã chủ đề, phải có trong data/topics.txt


@problem(
    title="Chào bạn mới",    # 3-60 ký tự, không trùng với bài nào khác
    difficulty=1,            # 1 = Dễ, 2 = Vừa, 3 = Khó
    statement="""
        Robot Bi vừa học nói. Em hãy giúp Bi chào một người bạn mới.

        Đầu vào:
        - Một dòng chứa tên của bạn (chữ cái tiếng Anh, không có khoảng trắng).

        Đầu ra:
        - In ra: Xin chao, <tên>!

        Giới hạn:
        - Tên dài không quá 20 ký tự.
    """,
    tests=["An\n", "Binh\n", "Chi\n", "Dung\n", "Lan\n", "Khoa\n"],
)
def solve(inp):
    name = inp.split()[0]
    return f"Xin chao, {name}!\n"
```

- `tests` là danh sách input, hoặc một hàm `lambda r: [...]` nhận `random.Random` đã gieo hạt cố định
  (chạy lại luôn ra đúng bộ test cũ). **Test đầu tiên là test ví dụ** hiện cho học sinh xem
  (`samples=2` nếu muốn hiện 2 test đầu).
- `comparator="token"` (mặc định): so từng giá trị, bỏ qua khoảng trắng/xuống dòng thừa.
  `comparator="lines"`: so từng dòng, giữ khoảng trắng **đầu** dòng, bỏ qua khoảng trắng cuối dòng
  và dòng trống ở cuối — dùng cho bài vẽ hình.
- Hàm lời giải nhận **toàn bộ input dạng chuỗi**, trả về **chuỗi output**. Hàm phải **tự đủ**:
  chỉ dùng thư viện chuẩn và import **bên trong thân hàm**, không gọi hàm/biến khai báo ngoài nó.

## Quy tắc soạn đề

1. **Đề bằng tiếng Việt có dấu**, giọng thân thiện với trẻ em (8–14 tuổi): một câu chuyện ngắn
   1–3 câu (bạn An, chú mèo Mướp, robot Bi, cửa hàng kẹo...), rồi các mục **`Đầu vào:`**, **`Đầu ra:`**,
   có thể thêm **`Giới hạn:`** và **`Gợi ý:`** cho bài dễ. Không chép ví dụ vào đề — giao diện tự hiện test ví dụ.
2. **Dữ liệu vào/ra chỉ dùng ký tự ASCII.** Chữ trong output viết không dấu: `YES/NO`, `CHAN/LE`, `Xin chao`.
3. Mô tả định dạng rõ ràng: "các số cách nhau một dấu cách", "mỗi số trên một dòng".
4. **Không dùng số thực.** Cần chia thì hỏi phần nguyên/phần dư. Không cho số âm vào phép `/` và `%`
   (C++/Java và Python làm tròn khác nhau với số âm).
5. Kết quả phải vừa kiểu `int` 32-bit (≤ 2·10^9) trừ khi đề ghi rõ cần số lớn.
6. Mỗi bài **6–10 test**: 1 test ví dụ dễ hiểu + test biên (nhỏ nhất, lớn nhất, bằng nhau, số 0...)
   + vài test ngẫu nhiên. Các test ẩn không được ra cùng một output.
7. Trong mỗi file xếp bài **từ dễ đến khó**: khoảng 10 bài Dễ, 12 bài Vừa, 8 bài Khó.
