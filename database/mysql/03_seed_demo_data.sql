-- =====================================================================
--  PTIT Online Judge - DU LIEU MAU DE THUC HANH SQL
-- =====================================================================
--  File nay do cong cu sinh tu dong - KHONG sua tay.
--
--  Cach nap:
--      mysql -u oj_app -p online_judge < database/mysql/03_seed_demo_data.sql
--
--  Yeu cau: da chay 02_schema.sql (hoac da khoi dong ung dung mot lan)
--  de cac bang ton tai san.
--
--  Chay lai nhieu lan an toan: dung INSERT ... ON DUPLICATE KEY UPDATE
--  nen khong tao ban ghi trung.
--
--  Mat khau moi tai khoan mau: ptit@2026
-- =====================================================================

-- BAT BUOC: file nay chua ten tieng Viet co dau (UTF-8).
-- Tren Windows, mysql.exe mac dinh khai bao charset la codepage cua console
-- (thuong cp850/cp437) nen server se hieu sai byte UTF-8 -> ten bi loi thanh
-- "Nguyễn" => "Nguyß╗àn". Dong SET NAMES duoi day sua dut diem loi do,
-- bat ke nap file bang cach nao.
SET NAMES utf8mb4;

START TRANSACTION;

-- 12 sinh vien + 2 giang vien. Mat khau chung: ptit@2026
-- Moi tai khoan co MUOI RIENG nen password_hash khac nhau hoan toan.
INSERT INTO users
    (id, username, full_name, role, student_code, class_name, department,
     password_hash, password_salt, password_iterations, created_at)
VALUES
    ('U-SEED-SV01', 'sv01', 'Nguyễn Minh Hiển', 'STUDENT', 'B24DCCN199', 'D24CQCN01', NULL, 'EjulgCYY5r5jawXm4VBrcnnEd8wPmM2vFXYDxuoa7Ec=', 'oaxYpSETliVM+hd4sT+H3Q==', 120000, '2026-07-04 08:00:00'),
    ('U-SEED-SV02', 'sv02', 'Trần Lan Anh', 'STUDENT', 'B24DCCN042', 'D24CQCN01', NULL, 'KxlzkAw8ifZzHv63cZoyshPm/w8rcQuKfT8Ip0q4ttU=', 'owUCEo8ejtNYHe0d8T8DIQ==', 120000, '2026-07-04 08:01:00'),
    ('U-SEED-SV03', 'sv03', 'Phạm Văn Tuấn', 'STUDENT', 'B24DCCN311', 'D24CQCN01', NULL, '4e853phieQtKmtspADB0B48pI3d38accDbgUOzhOTTk=', 'zsuGRPIw789Vk+gssdBikA==', 120000, '2026-07-04 08:02:00'),
    ('U-SEED-SV04', 'sv04', 'Lê Thu Hà', 'STUDENT', 'B24DCCN078', 'D24CQCN01', NULL, '0Go6MXREP5pugyOvHjUX5L1W7eVisl/Fqc86qQKpUWM=', 'idZDs/O7I8qSpZQ3Y1tgmw==', 120000, '2026-07-04 08:03:00'),
    ('U-SEED-SV05', 'sv05', 'Đỗ Quang Huy', 'STUDENT', 'B24DCCN154', 'D24CQCN01', NULL, 'UplnJyTGJy7tjtv+KZihCz06X/a80bSO9aE/Sycok1s=', 'EIXYRBJiuQyKbE0K+K1kRQ==', 120000, '2026-07-04 08:04:00'),
    ('U-SEED-SV06', 'sv06', 'Vũ Thị Mai', 'STUDENT', 'B24DCCN205', 'D24CQCN02', NULL, 'r+mys0IKjAVp/gCzVnLfdLpTUwT0XxvKjBj3OarDAw0=', 'sVD3aWKU7Ear3HZnz46VQg==', 120000, '2026-07-04 08:05:00'),
    ('U-SEED-SV07', 'sv07', 'Hoàng Đức Long', 'STUDENT', 'B24DCCN267', 'D24CQCN02', NULL, 'hkBqyNhQIY5ezFwQWT/UAU7krJMtWjkrgl0Q6r9bjxk=', 'sfNKW9wuAzC8Rgjv6uGYmw==', 120000, '2026-07-04 08:06:00'),
    ('U-SEED-SV08', 'sv08', 'Bùi Khánh Linh', 'STUDENT', 'B24DCCN023', 'D24CQCN02', NULL, 'CndpAjCyzuLZGoGLvr5vmFTD2T4rxlQLbMKTQC1Wr3o=', 'ZHu1l+hJqa+83nUSOgu98A==', 120000, '2026-07-04 08:07:00'),
    ('U-SEED-SV09', 'sv09', 'Đặng Tiến Dũng', 'STUDENT', 'B24DCCN190', 'D24CQCN02', NULL, 'cwROmYdbLbJdBXYYkozgzyzVnOoeb58Svd51qTP3/5U=', 'pHVSF45KY3o8zBvWx3w0Wg==', 120000, '2026-07-04 08:08:00'),
    ('U-SEED-SV10', 'sv10', 'Ngô Phương Thảo', 'STUDENT', 'B24DCCN341', 'D24CQCN02', NULL, 'UhjS+MxeAqFPGoerI53O2qvMtCajiaIHqkf48xnkXkM=', 'jP/kcEQHgWgwQxk7NVsQeA==', 120000, '2026-07-04 08:09:00'),
    ('U-SEED-SV11', 'sv11', 'Trịnh Bảo Nam', 'STUDENT', 'B24DCCN112', 'D24CQCN03', NULL, 'qjfLZ72jXjrq42+/VEKQecMpxgxaM8xqcQf8UTO5p3Q=', 'XKcF7Gvc6NR5GtjajyQmJQ==', 120000, '2026-07-04 08:10:00'),
    ('U-SEED-SV12', 'sv12', 'Cao Diệu Linh', 'STUDENT', 'B24DCCN088', 'D24CQCN03', NULL, 'HDcanqeQdvT6uykiuEfVDmUAZsoFEfFa4MFGP0aFlww=', 'hqytB9HWB0bSO8mzwGeY9g==', 120000, '2026-07-04 08:11:00'),
    ('U-SEED-GV01', 'gv01', 'Lê Minh Thành', 'TEACHER', NULL, NULL, 'Khoa học máy tính', 'r01t3yLA3Ybo+7LwUx9FDD/lfKD+cXI2nV/mghYfQt4=', '+LOXrBT6nWhYBXLZT9/3XA==', 120000, '2026-07-03 08:00:00'),
    ('U-SEED-GV02', 'gv02', 'Phan Thu Trang', 'TEACHER', NULL, NULL, 'Công nghệ phần mềm', 'V5aAaJAo5+karkpc40l4jfsLwoMGk0QpMmeIRRWJc0I=', 'Q2FcDAJHFaprHbpc+gzBSg==', 120000, '2026-07-03 08:01:00')
ON DUPLICATE KEY UPDATE full_name = VALUES(full_name);

-- Bai nop cua 12 sinh vien, trai tren khoang 2 tuan.
-- Trinh do tung sinh vien khac nhau -> ti le AC va xep hang phan hoa ro.
-- Luu y: bai CE KHONG co dong nao trong test_case_results
-- (bien dich loi thi khong test nao duoc chay) - rat huu ich de tap JOIN.
INSERT INTO submissions
    (id, user_id, problem_id, problem_title, language, file_name, source_code,
     submitted_at, verdict, score, max_points, max_runtime_ms, judge_time_ms, global_message)
VALUES
    ('SUB-SEED-0001', 'U-SEED-SV01', 'P002', 'Kiểm tra số nguyên tố', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-04 21:35:00', 'AC', 100.0000, 100.0000, 98, 406, ''),
    ('SUB-SEED-0002', 'U-SEED-SV01', 'P003', 'Trung bình cộng dãy số', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 01:41:00', 'RE', 33.3333, 100.0000, 319, 544, ''),
    ('SUB-SEED-0003', 'U-SEED-SV01', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 07:31:00', 'AC', 100.0000, 100.0000, 203, 410, ''),
    ('SUB-SEED-0004', 'U-SEED-SV01', 'P003', 'Trung bình cộng dãy số', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 10:44:00', 'AC', 100.0000, 100.0000, 127, 403, ''),
    ('SUB-SEED-0005', 'U-SEED-SV01', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-05 17:56:00', 'AC', 100.0000, 100.0000, 181, 518, ''),
    ('SUB-SEED-0006', 'U-SEED-SV01', 'P002', 'Kiểm tra số nguyên tố', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-05 19:29:00', 'AC', 100.0000, 100.0000, 333, 681, ''),
    ('SUB-SEED-0007', 'U-SEED-SV01', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-06 03:46:00', 'AC', 100.0000, 100.0000, 88, 454, ''),
    ('SUB-SEED-0008', 'U-SEED-SV01', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-06 14:01:00', 'AC', 100.0000, 100.0000, 273, 532, ''),
    ('SUB-SEED-0009', 'U-SEED-SV01', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-06 18:33:00', 'WA', 33.3333, 100.0000, 240, 819, ''),
    ('SUB-SEED-0010', 'U-SEED-SV01', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-06 23:26:00', 'AC', 100.0000, 100.0000, 46, 556, ''),
    ('SUB-SEED-0011', 'U-SEED-SV01', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-07 07:12:00', 'AC', 100.0000, 100.0000, 181, 454, ''),
    ('SUB-SEED-0012', 'U-SEED-SV01', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-07 08:30:00', 'AC', 100.0000, 100.0000, 234, 632, ''),
    ('SUB-SEED-0013', 'U-SEED-SV01', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-07 13:12:00', 'AC', 100.0000, 100.0000, 68, 483, ''),
    ('SUB-SEED-0014', 'U-SEED-SV01', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-07 16:25:00', 'CE', 0.0000, 100.0000, 91, 623, 'Solution.java:5: error: \';\' expected'),
    ('SUB-SEED-0015', 'U-SEED-SV01', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-07 20:32:00', 'AC', 100.0000, 100.0000, 296, 639, ''),
    ('SUB-SEED-0016', 'U-SEED-SV01', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-07 22:15:00', 'AC', 100.0000, 100.0000, 288, 872, ''),
    ('SUB-SEED-0017', 'U-SEED-SV01', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-08 02:05:00', 'AC', 100.0000, 100.0000, 188, 529, ''),
    ('SUB-SEED-0018', 'U-SEED-SV01', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-08 07:01:00', 'WA', 66.6667, 100.0000, 289, 830, ''),
    ('SUB-SEED-0019', 'U-SEED-SV01', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-08 13:45:00', 'AC', 100.0000, 100.0000, 231, 514, ''),
    ('SUB-SEED-0020', 'U-SEED-SV01', 'P003', 'Trung bình cộng dãy số', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-08 19:08:00', 'AC', 100.0000, 100.0000, 262, 784, ''),
    ('SUB-SEED-0021', 'U-SEED-SV01', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-08 22:20:00', 'WA', 25.0000, 100.0000, 161, 445, ''),
    ('SUB-SEED-0022', 'U-SEED-SV01', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-09 07:05:00', 'AC', 100.0000, 100.0000, 142, 700, ''),
    ('SUB-SEED-0023', 'U-SEED-SV02', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-04 07:54:00', 'RE', 50.0000, 100.0000, 111, 500, ''),
    ('SUB-SEED-0024', 'U-SEED-SV02', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-04 18:15:00', 'AC', 100.0000, 100.0000, 90, 382, ''),
    ('SUB-SEED-0025', 'U-SEED-SV02', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-05 02:15:00', 'AC', 100.0000, 100.0000, 225, 755, ''),
    ('SUB-SEED-0026', 'U-SEED-SV02', 'P003', 'Trung bình cộng dãy số', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 07:37:00', 'AC', 100.0000, 100.0000, 184, 762, ''),
    ('SUB-SEED-0027', 'U-SEED-SV02', 'P003', 'Trung bình cộng dãy số', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-05 16:03:00', 'AC', 100.0000, 100.0000, 315, 847, ''),
    ('SUB-SEED-0028', 'U-SEED-SV02', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-05 18:31:00', 'AC', 100.0000, 100.0000, 308, 660, ''),
    ('SUB-SEED-0029', 'U-SEED-SV02', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 00:31:00', 'AC', 100.0000, 100.0000, 225, 795, ''),
    ('SUB-SEED-0030', 'U-SEED-SV02', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 04:11:00', 'AC', 100.0000, 100.0000, 157, 581, ''),
    ('SUB-SEED-0031', 'U-SEED-SV02', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-06 07:07:00', 'AC', 100.0000, 100.0000, 107, 398, ''),
    ('SUB-SEED-0032', 'U-SEED-SV02', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-06 09:19:00', 'AC', 100.0000, 100.0000, 291, 842, ''),
    ('SUB-SEED-0033', 'U-SEED-SV02', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-06 15:53:00', 'AC', 100.0000, 100.0000, 354, 810, ''),
    ('SUB-SEED-0034', 'U-SEED-SV02', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-07 02:18:00', 'TLE', 0.0000, 100.0000, 1796, 2187, ''),
    ('SUB-SEED-0035', 'U-SEED-SV02', 'P002', 'Kiểm tra số nguyên tố', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-07 11:02:00', 'AC', 100.0000, 100.0000, 43, 611, ''),
    ('SUB-SEED-0036', 'U-SEED-SV02', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-07 17:21:00', 'AC', 100.0000, 100.0000, 99, 585, ''),
    ('SUB-SEED-0037', 'U-SEED-SV02', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-08 01:48:00', 'AC', 100.0000, 100.0000, 186, 461, ''),
    ('SUB-SEED-0038', 'U-SEED-SV02', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-08 11:43:00', 'AC', 100.0000, 100.0000, 165, 475, ''),
    ('SUB-SEED-0039', 'U-SEED-SV02', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-08 14:14:00', 'AC', 100.0000, 100.0000, 309, 609, ''),
    ('SUB-SEED-0040', 'U-SEED-SV02', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-08 23:47:00', 'AC', 100.0000, 100.0000, 270, 641, ''),
    ('SUB-SEED-0041', 'U-SEED-SV02', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-09 06:41:00', 'AC', 100.0000, 100.0000, 304, 819, ''),
    ('SUB-SEED-0042', 'U-SEED-SV02', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-09 16:21:00', 'WA', 0.0000, 100.0000, 266, 844, ''),
    ('SUB-SEED-0043', 'U-SEED-SV03', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-05 06:57:00', 'AC', 100.0000, 100.0000, 225, 513, ''),
    ('SUB-SEED-0044', 'U-SEED-SV03', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 09:52:00', 'AC', 100.0000, 100.0000, 330, 610, ''),
    ('SUB-SEED-0045', 'U-SEED-SV03', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-05 20:01:00', 'AC', 100.0000, 100.0000, 234, 584, ''),
    ('SUB-SEED-0046', 'U-SEED-SV03', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-05 21:56:00', 'AC', 100.0000, 100.0000, 117, 360, ''),
    ('SUB-SEED-0047', 'U-SEED-SV03', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 07:48:00', 'WA', 0.0000, 100.0000, 100, 632, ''),
    ('SUB-SEED-0048', 'U-SEED-SV03', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 09:12:00', 'AC', 100.0000, 100.0000, 331, 819, ''),
    ('SUB-SEED-0049', 'U-SEED-SV03', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-06 19:07:00', 'AC', 100.0000, 100.0000, 244, 538, ''),
    ('SUB-SEED-0050', 'U-SEED-SV03', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 23:36:00', 'WA', 33.3333, 100.0000, 328, 912, ''),
    ('SUB-SEED-0051', 'U-SEED-SV03', 'P003', 'Trung bình cộng dãy số', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-07 03:33:00', 'AC', 100.0000, 100.0000, 142, 403, ''),
    ('SUB-SEED-0052', 'U-SEED-SV03', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-07 11:14:00', 'AC', 100.0000, 100.0000, 308, 750, ''),
    ('SUB-SEED-0053', 'U-SEED-SV03', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-07 21:01:00', 'AC', 100.0000, 100.0000, 236, 569, ''),
    ('SUB-SEED-0054', 'U-SEED-SV03', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-08 04:36:00', 'AC', 100.0000, 100.0000, 138, 496, ''),
    ('SUB-SEED-0055', 'U-SEED-SV03', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-08 13:29:00', 'AC', 100.0000, 100.0000, 55, 622, ''),
    ('SUB-SEED-0056', 'U-SEED-SV03', 'P003', 'Trung bình cộng dãy số', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-08 18:59:00', 'AC', 100.0000, 100.0000, 45, 499, ''),
    ('SUB-SEED-0057', 'U-SEED-SV03', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-08 20:39:00', 'WA', 66.6667, 100.0000, 333, 645, ''),
    ('SUB-SEED-0058', 'U-SEED-SV03', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-09 01:14:00', 'WA', 75.0000, 100.0000, 323, 569, ''),
    ('SUB-SEED-0059', 'U-SEED-SV03', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-09 04:59:00', 'TLE', 25.0000, 100.0000, 1736, 2042, ''),
    ('SUB-SEED-0060', 'U-SEED-SV03', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-09 08:45:00', 'AC', 100.0000, 100.0000, 198, 631, ''),
    ('SUB-SEED-0061', 'U-SEED-SV03', 'P002', 'Kiểm tra số nguyên tố', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-09 16:21:00', 'WA', 0.0000, 100.0000, 128, 362, ''),
    ('SUB-SEED-0062', 'U-SEED-SV03', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-09 23:28:00', 'WA', 0.0000, 100.0000, 114, 545, ''),
    ('SUB-SEED-0063', 'U-SEED-SV03', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-10 03:52:00', 'WA', 0.0000, 100.0000, 233, 618, ''),
    ('SUB-SEED-0064', 'U-SEED-SV03', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-10 05:21:00', 'AC', 100.0000, 100.0000, 274, 762, ''),
    ('SUB-SEED-0065', 'U-SEED-SV03', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-10 13:13:00', 'CE', 0.0000, 100.0000, 226, 575, 'Solution.java:5: error: \';\' expected'),
    ('SUB-SEED-0066', 'U-SEED-SV04', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 06:27:00', 'AC', 100.0000, 100.0000, 299, 816, ''),
    ('SUB-SEED-0067', 'U-SEED-SV04', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 10:17:00', 'TLE', 0.0000, 100.0000, 1518, 1830, ''),
    ('SUB-SEED-0068', 'U-SEED-SV04', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 16:34:00', 'RE', 33.3333, 100.0000, 293, 495, ''),
    ('SUB-SEED-0069', 'U-SEED-SV04', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-06 00:10:00', 'AC', 100.0000, 100.0000, 148, 592, ''),
    ('SUB-SEED-0070', 'U-SEED-SV04', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-06 08:05:00', 'RE', 33.3333, 100.0000, 177, 590, ''),
    ('SUB-SEED-0071', 'U-SEED-SV04', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 09:25:00', 'AC', 100.0000, 100.0000, 80, 316, ''),
    ('SUB-SEED-0072', 'U-SEED-SV04', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-06 16:46:00', 'AC', 100.0000, 100.0000, 187, 675, ''),
    ('SUB-SEED-0073', 'U-SEED-SV04', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 23:15:00', 'AC', 100.0000, 100.0000, 187, 405, ''),
    ('SUB-SEED-0074', 'U-SEED-SV04', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-07 07:29:00', 'AC', 100.0000, 100.0000, 89, 501, ''),
    ('SUB-SEED-0075', 'U-SEED-SV04', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-07 16:33:00', 'WA', 25.0000, 100.0000, 99, 303, ''),
    ('SUB-SEED-0076', 'U-SEED-SV04', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-08 00:22:00', 'CE', 0.0000, 100.0000, 227, 459, 'Solution.java:5: error: \';\' expected'),
    ('SUB-SEED-0077', 'U-SEED-SV04', 'P003', 'Trung bình cộng dãy số', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-08 09:04:00', 'WA', 33.3333, 100.0000, 39, 395, ''),
    ('SUB-SEED-0078', 'U-SEED-SV04', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-08 19:02:00', 'AC', 100.0000, 100.0000, 130, 357, ''),
    ('SUB-SEED-0079', 'U-SEED-SV04', 'P002', 'Kiểm tra số nguyên tố', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-08 20:27:00', 'AC', 100.0000, 100.0000, 62, 281, ''),
    ('SUB-SEED-0080', 'U-SEED-SV04', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-09 02:14:00', 'AC', 100.0000, 100.0000, 51, 572, ''),
    ('SUB-SEED-0081', 'U-SEED-SV05', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-04 04:43:00', 'AC', 100.0000, 100.0000, 67, 547, ''),
    ('SUB-SEED-0082', 'U-SEED-SV05', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-04 09:24:00', 'AC', 100.0000, 100.0000, 126, 358, ''),
    ('SUB-SEED-0083', 'U-SEED-SV05', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-04 12:48:00', 'AC', 100.0000, 100.0000, 306, 889, ''),
    ('SUB-SEED-0084', 'U-SEED-SV05', 'P003', 'Trung bình cộng dãy số', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-04 16:05:00', 'AC', 100.0000, 100.0000, 288, 589, ''),
    ('SUB-SEED-0085', 'U-SEED-SV05', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-04 23:01:00', 'AC', 100.0000, 100.0000, 65, 321, ''),
    ('SUB-SEED-0086', 'U-SEED-SV05', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-05 02:07:00', 'WA', 25.0000, 100.0000, 210, 789, ''),
    ('SUB-SEED-0087', 'U-SEED-SV05', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-05 07:06:00', 'WA', 0.0000, 100.0000, 211, 441, ''),
    ('SUB-SEED-0088', 'U-SEED-SV05', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 11:58:00', 'AC', 100.0000, 100.0000, 149, 635, ''),
    ('SUB-SEED-0089', 'U-SEED-SV05', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-05 18:10:00', 'AC', 100.0000, 100.0000, 167, 514, ''),
    ('SUB-SEED-0090', 'U-SEED-SV05', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 01:35:00', 'WA', 25.0000, 100.0000, 72, 668, ''),
    ('SUB-SEED-0091', 'U-SEED-SV05', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-06 08:23:00', 'WA', 75.0000, 100.0000, 76, 326, ''),
    ('SUB-SEED-0092', 'U-SEED-SV05', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 13:16:00', 'AC', 100.0000, 100.0000, 201, 671, ''),
    ('SUB-SEED-0093', 'U-SEED-SV05', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 21:09:00', 'AC', 100.0000, 100.0000, 237, 703, ''),
    ('SUB-SEED-0094', 'U-SEED-SV05', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 23:49:00', 'CE', 0.0000, 100.0000, 67, 422, 'Solution.java:5: error: \';\' expected'),
    ('SUB-SEED-0095', 'U-SEED-SV05', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-07 07:41:00', 'AC', 100.0000, 100.0000, 354, 765, ''),
    ('SUB-SEED-0096', 'U-SEED-SV06', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-05 05:57:00', 'AC', 100.0000, 100.0000, 276, 716, ''),
    ('SUB-SEED-0097', 'U-SEED-SV06', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-05 07:16:00', 'AC', 100.0000, 100.0000, 135, 563, ''),
    ('SUB-SEED-0098', 'U-SEED-SV06', 'P002', 'Kiểm tra số nguyên tố', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-05 17:50:00', 'TLE', 0.0000, 100.0000, 1677, 2063, ''),
    ('SUB-SEED-0099', 'U-SEED-SV06', 'P003', 'Trung bình cộng dãy số', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-05 19:21:00', 'WA', 0.0000, 100.0000, 178, 572, ''),
    ('SUB-SEED-0100', 'U-SEED-SV06', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-06 03:08:00', 'WA', 75.0000, 100.0000, 52, 271, ''),
    ('SUB-SEED-0101', 'U-SEED-SV06', 'P003', 'Trung bình cộng dãy số', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-06 12:16:00', 'WA', 33.3333, 100.0000, 40, 331, ''),
    ('SUB-SEED-0102', 'U-SEED-SV06', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-06 20:59:00', 'WA', 0.0000, 100.0000, 302, 899, ''),
    ('SUB-SEED-0103', 'U-SEED-SV06', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-06 21:40:00', 'AC', 100.0000, 100.0000, 261, 754, ''),
    ('SUB-SEED-0104', 'U-SEED-SV06', 'P003', 'Trung bình cộng dãy số', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-06 23:30:00', 'AC', 100.0000, 100.0000, 217, 484, ''),
    ('SUB-SEED-0105', 'U-SEED-SV06', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-07 00:21:00', 'AC', 100.0000, 100.0000, 213, 789, ''),
    ('SUB-SEED-0106', 'U-SEED-SV06', 'P002', 'Kiểm tra số nguyên tố', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-07 02:04:00', 'AC', 100.0000, 100.0000, 250, 698, ''),
    ('SUB-SEED-0107', 'U-SEED-SV06', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-07 07:21:00', 'WA', 0.0000, 100.0000, 146, 608, ''),
    ('SUB-SEED-0108', 'U-SEED-SV06', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-07 13:53:00', 'CE', 0.0000, 100.0000, 91, 465, 'Solution.java:5: error: \';\' expected'),
    ('SUB-SEED-0109', 'U-SEED-SV06', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-07 20:42:00', 'WA', 66.6667, 100.0000, 350, 590, ''),
    ('SUB-SEED-0110', 'U-SEED-SV06', 'P003', 'Trung bình cộng dãy số', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-07 22:23:00', 'AC', 100.0000, 100.0000, 212, 730, ''),
    ('SUB-SEED-0111', 'U-SEED-SV06', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-08 03:12:00', 'TLE', 33.3333, 100.0000, 1843, 2293, ''),
    ('SUB-SEED-0112', 'U-SEED-SV06', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-08 07:55:00', 'AC', 100.0000, 100.0000, 193, 400, ''),
    ('SUB-SEED-0113', 'U-SEED-SV06', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-08 09:47:00', 'WA', 0.0000, 100.0000, 216, 703, ''),
    ('SUB-SEED-0114', 'U-SEED-SV07', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-04 06:30:00', 'WA', 0.0000, 100.0000, 352, 760, ''),
    ('SUB-SEED-0115', 'U-SEED-SV07', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-04 12:03:00', 'TLE', 50.0000, 100.0000, 1730, 2042, ''),
    ('SUB-SEED-0116', 'U-SEED-SV07', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-04 21:06:00', 'TLE', 50.0000, 100.0000, 1579, 1997, ''),
    ('SUB-SEED-0117', 'U-SEED-SV07', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-05 06:09:00', 'AC', 100.0000, 100.0000, 296, 680, ''),
    ('SUB-SEED-0118', 'U-SEED-SV07', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-05 15:59:00', 'WA', 0.0000, 100.0000, 168, 701, ''),
    ('SUB-SEED-0119', 'U-SEED-SV07', 'P003', 'Trung bình cộng dãy số', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 17:29:00', 'WA', 66.6667, 100.0000, 52, 306, ''),
    ('SUB-SEED-0120', 'U-SEED-SV07', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-05 22:09:00', 'AC', 100.0000, 100.0000, 238, 483, ''),
    ('SUB-SEED-0121', 'U-SEED-SV07', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 05:03:00', 'AC', 100.0000, 100.0000, 271, 548, ''),
    ('SUB-SEED-0122', 'U-SEED-SV07', 'P003', 'Trung bình cộng dãy số', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-06 10:54:00', 'CE', 0.0000, 100.0000, 39, 474, 'Solution.java:5: error: \';\' expected'),
    ('SUB-SEED-0123', 'U-SEED-SV07', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 14:10:00', 'RE', 50.0000, 100.0000, 305, 773, ''),
    ('SUB-SEED-0124', 'U-SEED-SV07', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 23:01:00', 'TLE', 33.3333, 100.0000, 1788, 2059, ''),
    ('SUB-SEED-0125', 'U-SEED-SV07', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-07 04:37:00', 'WA', 0.0000, 100.0000, 258, 736, ''),
    ('SUB-SEED-0126', 'U-SEED-SV07', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-07 13:28:00', 'AC', 100.0000, 100.0000, 251, 493, ''),
    ('SUB-SEED-0127', 'U-SEED-SV07', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-07 21:37:00', 'AC', 100.0000, 100.0000, 328, 734, ''),
    ('SUB-SEED-0128', 'U-SEED-SV07', 'P003', 'Trung bình cộng dãy số', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-08 03:01:00', 'CE', 0.0000, 100.0000, 205, 501, 'Solution.java:5: error: \';\' expected'),
    ('SUB-SEED-0129', 'U-SEED-SV07', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-08 06:25:00', 'TLE', 33.3333, 100.0000, 1877, 2357, ''),
    ('SUB-SEED-0130', 'U-SEED-SV07', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-08 14:54:00', 'AC', 100.0000, 100.0000, 42, 490, ''),
    ('SUB-SEED-0131', 'U-SEED-SV07', 'P002', 'Kiểm tra số nguyên tố', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-09 00:37:00', 'WA', 0.0000, 100.0000, 35, 394, ''),
    ('SUB-SEED-0132', 'U-SEED-SV08', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-04 10:29:00', 'AC', 100.0000, 100.0000, 269, 574, ''),
    ('SUB-SEED-0133', 'U-SEED-SV08', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-04 13:35:00', 'AC', 100.0000, 100.0000, 346, 653, ''),
    ('SUB-SEED-0134', 'U-SEED-SV08', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-04 20:03:00', 'AC', 100.0000, 100.0000, 298, 810, ''),
    ('SUB-SEED-0135', 'U-SEED-SV08', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 04:54:00', 'WA', 25.0000, 100.0000, 101, 405, ''),
    ('SUB-SEED-0136', 'U-SEED-SV08', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 14:39:00', 'AC', 100.0000, 100.0000, 107, 592, ''),
    ('SUB-SEED-0137', 'U-SEED-SV08', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-05 20:38:00', 'AC', 100.0000, 100.0000, 108, 426, ''),
    ('SUB-SEED-0138', 'U-SEED-SV08', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-05 22:33:00', 'AC', 100.0000, 100.0000, 196, 539, ''),
    ('SUB-SEED-0139', 'U-SEED-SV08', 'P003', 'Trung bình cộng dãy số', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-06 08:02:00', 'AC', 100.0000, 100.0000, 351, 638, ''),
    ('SUB-SEED-0140', 'U-SEED-SV08', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 11:58:00', 'WA', 50.0000, 100.0000, 335, 695, ''),
    ('SUB-SEED-0141', 'U-SEED-SV08', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-06 14:06:00', 'WA', 25.0000, 100.0000, 134, 708, ''),
    ('SUB-SEED-0142', 'U-SEED-SV08', 'P002', 'Kiểm tra số nguyên tố', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-07 00:18:00', 'AC', 100.0000, 100.0000, 165, 631, ''),
    ('SUB-SEED-0143', 'U-SEED-SV08', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-07 07:57:00', 'AC', 100.0000, 100.0000, 325, 859, ''),
    ('SUB-SEED-0144', 'U-SEED-SV08', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-07 15:57:00', 'AC', 100.0000, 100.0000, 323, 861, ''),
    ('SUB-SEED-0145', 'U-SEED-SV08', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-07 17:40:00', 'MLE', 0.0000, 100.0000, 324, 884, ''),
    ('SUB-SEED-0146', 'U-SEED-SV08', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-07 19:21:00', 'AC', 100.0000, 100.0000, 111, 392, ''),
    ('SUB-SEED-0147', 'U-SEED-SV08', 'P002', 'Kiểm tra số nguyên tố', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-08 00:38:00', 'WA', 0.0000, 100.0000, 177, 671, ''),
    ('SUB-SEED-0148', 'U-SEED-SV09', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-03 17:04:00', 'WA', 33.3333, 100.0000, 240, 828, ''),
    ('SUB-SEED-0149', 'U-SEED-SV09', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-03 20:06:00', 'WA', 0.0000, 100.0000, 44, 419, ''),
    ('SUB-SEED-0150', 'U-SEED-SV09', 'P003', 'Trung bình cộng dãy số', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-03 22:09:00', 'AC', 100.0000, 100.0000, 59, 466, ''),
    ('SUB-SEED-0151', 'U-SEED-SV09', 'P002', 'Kiểm tra số nguyên tố', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-03 23:45:00', 'WA', 33.3333, 100.0000, 256, 602, ''),
    ('SUB-SEED-0152', 'U-SEED-SV09', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-04 08:27:00', 'WA', 33.3333, 100.0000, 130, 484, ''),
    ('SUB-SEED-0153', 'U-SEED-SV09', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-04 14:01:00', 'AC', 100.0000, 100.0000, 66, 664, ''),
    ('SUB-SEED-0154', 'U-SEED-SV09', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 00:18:00', 'WA', 0.0000, 100.0000, 49, 531, ''),
    ('SUB-SEED-0155', 'U-SEED-SV09', 'P003', 'Trung bình cộng dãy số', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-05 09:21:00', 'AC', 100.0000, 100.0000, 327, 861, ''),
    ('SUB-SEED-0156', 'U-SEED-SV09', 'P003', 'Trung bình cộng dãy số', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-05 18:35:00', 'WA', 66.6667, 100.0000, 157, 677, ''),
    ('SUB-SEED-0157', 'U-SEED-SV09', 'P003', 'Trung bình cộng dãy số', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 19:30:00', 'WA', 66.6667, 100.0000, 82, 672, ''),
    ('SUB-SEED-0158', 'U-SEED-SV09', 'P002', 'Kiểm tra số nguyên tố', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-06 02:54:00', 'TLE', 33.3333, 100.0000, 1802, 2029, ''),
    ('SUB-SEED-0159', 'U-SEED-SV09', 'P003', 'Trung bình cộng dãy số', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-06 08:37:00', 'AC', 100.0000, 100.0000, 302, 597, ''),
    ('SUB-SEED-0160', 'U-SEED-SV09', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-06 17:35:00', 'AC', 100.0000, 100.0000, 349, 627, ''),
    ('SUB-SEED-0161', 'U-SEED-SV09', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-07 04:04:00', 'AC', 100.0000, 100.0000, 298, 751, ''),
    ('SUB-SEED-0162', 'U-SEED-SV09', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-07 11:13:00', 'WA', 75.0000, 100.0000, 71, 647, ''),
    ('SUB-SEED-0163', 'U-SEED-SV09', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-07 18:18:00', 'RE', 0.0000, 100.0000, 340, 760, ''),
    ('SUB-SEED-0164', 'U-SEED-SV09', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-08 00:07:00', 'AC', 100.0000, 100.0000, 144, 518, ''),
    ('SUB-SEED-0165', 'U-SEED-SV09', 'P003', 'Trung bình cộng dãy số', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-08 07:10:00', 'WA', 33.3333, 100.0000, 353, 776, ''),
    ('SUB-SEED-0166', 'U-SEED-SV09', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-08 16:43:00', 'AC', 100.0000, 100.0000, 99, 431, ''),
    ('SUB-SEED-0167', 'U-SEED-SV09', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-09 02:40:00', 'WA', 66.6667, 100.0000, 325, 649, ''),
    ('SUB-SEED-0168', 'U-SEED-SV09', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-09 03:34:00', 'WA', 50.0000, 100.0000, 84, 674, ''),
    ('SUB-SEED-0169', 'U-SEED-SV09', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-09 11:50:00', 'AC', 100.0000, 100.0000, 93, 677, ''),
    ('SUB-SEED-0170', 'U-SEED-SV10', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-05 00:08:00', 'WA', 0.0000, 100.0000, 171, 561, ''),
    ('SUB-SEED-0171', 'U-SEED-SV10', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 06:29:00', 'WA', 50.0000, 100.0000, 261, 726, ''),
    ('SUB-SEED-0172', 'U-SEED-SV10', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 09:23:00', 'CE', 0.0000, 100.0000, 328, 721, 'Solution.java:5: error: \';\' expected'),
    ('SUB-SEED-0173', 'U-SEED-SV10', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-05 13:36:00', 'WA', 0.0000, 100.0000, 66, 544, ''),
    ('SUB-SEED-0174', 'U-SEED-SV10', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-05 15:08:00', 'RE', 0.0000, 100.0000, 167, 421, ''),
    ('SUB-SEED-0175', 'U-SEED-SV10', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-05 17:04:00', 'RE', 0.0000, 100.0000, 201, 409, ''),
    ('SUB-SEED-0176', 'U-SEED-SV10', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-05 22:57:00', 'TLE', 50.0000, 100.0000, 1638, 2226, ''),
    ('SUB-SEED-0177', 'U-SEED-SV10', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-06 05:05:00', 'AC', 100.0000, 100.0000, 149, 450, ''),
    ('SUB-SEED-0178', 'U-SEED-SV10', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-06 07:22:00', 'RE', 0.0000, 100.0000, 244, 526, ''),
    ('SUB-SEED-0179', 'U-SEED-SV10', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-06 17:11:00', 'CE', 0.0000, 100.0000, 113, 562, 'Solution.java:5: error: \';\' expected'),
    ('SUB-SEED-0180', 'U-SEED-SV10', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-07 02:35:00', 'CE', 0.0000, 100.0000, 124, 401, 'Solution.java:5: error: \';\' expected'),
    ('SUB-SEED-0181', 'U-SEED-SV10', 'P003', 'Trung bình cộng dãy số', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-07 04:33:00', 'WA', 0.0000, 100.0000, 312, 529, ''),
    ('SUB-SEED-0182', 'U-SEED-SV10', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-07 13:52:00', 'WA', 0.0000, 100.0000, 195, 761, ''),
    ('SUB-SEED-0183', 'U-SEED-SV10', 'P002', 'Kiểm tra số nguyên tố', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-07 20:46:00', 'WA', 0.0000, 100.0000, 67, 640, ''),
    ('SUB-SEED-0184', 'U-SEED-SV10', 'P003', 'Trung bình cộng dãy số', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-08 05:26:00', 'WA', 66.6667, 100.0000, 229, 799, ''),
    ('SUB-SEED-0185', 'U-SEED-SV10', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-08 10:36:00', 'RE', 25.0000, 100.0000, 309, 532, ''),
    ('SUB-SEED-0186', 'U-SEED-SV10', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-08 12:43:00', 'AC', 100.0000, 100.0000, 176, 508, ''),
    ('SUB-SEED-0187', 'U-SEED-SV10', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-08 19:56:00', 'AC', 100.0000, 100.0000, 301, 871, ''),
    ('SUB-SEED-0188', 'U-SEED-SV11', 'P003', 'Trung bình cộng dãy số', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-04 00:54:00', 'WA', 33.3333, 100.0000, 300, 647, ''),
    ('SUB-SEED-0189', 'U-SEED-SV11', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-04 10:54:00', 'WA', 25.0000, 100.0000, 174, 642, ''),
    ('SUB-SEED-0190', 'U-SEED-SV11', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-04 12:44:00', 'WA', 50.0000, 100.0000, 223, 603, ''),
    ('SUB-SEED-0191', 'U-SEED-SV11', 'P003', 'Trung bình cộng dãy số', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-04 19:22:00', 'AC', 100.0000, 100.0000, 274, 674, ''),
    ('SUB-SEED-0192', 'U-SEED-SV11', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-05 01:51:00', 'TLE', 0.0000, 100.0000, 1811, 2214, ''),
    ('SUB-SEED-0193', 'U-SEED-SV11', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-05 08:34:00', 'WA', 50.0000, 100.0000, 103, 371, ''),
    ('SUB-SEED-0194', 'U-SEED-SV11', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 18:46:00', 'WA', 33.3333, 100.0000, 272, 831, ''),
    ('SUB-SEED-0195', 'U-SEED-SV11', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-06 00:54:00', 'CE', 0.0000, 100.0000, 224, 518, 'Solution.java:5: error: \';\' expected'),
    ('SUB-SEED-0196', 'U-SEED-SV11', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-06 04:59:00', 'WA', 0.0000, 100.0000, 87, 317, ''),
    ('SUB-SEED-0197', 'U-SEED-SV11', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-06 09:20:00', 'TLE', 0.0000, 100.0000, 1758, 2321, ''),
    ('SUB-SEED-0198', 'U-SEED-SV12', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-04 16:01:00', 'WA', 0.0000, 100.0000, 163, 719, ''),
    ('SUB-SEED-0199', 'U-SEED-SV12', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-05 02:33:00', 'WA', 33.3333, 100.0000, 60, 620, ''),
    ('SUB-SEED-0200', 'U-SEED-SV12', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-05 09:34:00', 'WA', 50.0000, 100.0000, 175, 730, ''),
    ('SUB-SEED-0201', 'U-SEED-SV12', 'P002', 'Kiểm tra số nguyên tố', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 12:18:00', 'WA', 66.6667, 100.0000, 232, 635, ''),
    ('SUB-SEED-0202', 'U-SEED-SV12', 'P003', 'Trung bình cộng dãy số', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-05 21:45:00', 'TLE', 0.0000, 100.0000, 1528, 2079, ''),
    ('SUB-SEED-0203', 'U-SEED-SV12', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-06 03:13:00', 'WA', 75.0000, 100.0000, 192, 440, ''),
    ('SUB-SEED-0204', 'U-SEED-SV12', 'P002', 'Kiểm tra số nguyên tố', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-06 05:53:00', 'WA', 66.6667, 100.0000, 145, 505, ''),
    ('SUB-SEED-0205', 'U-SEED-SV12', 'P001', 'Tổng hai số nguyên', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-06 09:47:00', 'CE', 0.0000, 100.0000, 213, 724, 'Solution.java:5: error: \';\' expected'),
    ('SUB-SEED-0206', 'U-SEED-SV12', 'P002', 'Kiểm tra số nguyên tố', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-06 10:25:00', 'WA', 0.0000, 100.0000, 39, 603, ''),
    ('SUB-SEED-0207', 'U-SEED-SV12', 'P001', 'Tổng hai số nguyên', 'JavaScript', 'solution.js', 'const d=require(\'fs\').readFileSync(0,\'utf8\').split(/\\s+/);
console.log(+d[0]+ +d[1]);
', '2026-08-06 16:05:00', 'CE', 0.0000, 100.0000, 320, 860, 'Solution.java:5: error: \';\' expected'),
    ('SUB-SEED-0208', 'U-SEED-SV12', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-06 18:30:00', 'WA', 25.0000, 100.0000, 82, 485, ''),
    ('SUB-SEED-0209', 'U-SEED-SV12', 'P001', 'Tổng hai số nguyên', 'Java', 'Solution.java', 'import java.util.Scanner;
public class Solution{public static void main(String[] a){Scanner s=new Scanner(System.in);System.out.println(s.nextLong()+s.nextLong());}}
', '2026-08-06 20:27:00', 'WA', 0.0000, 100.0000, 255, 498, ''),
    ('SUB-SEED-0210', 'U-SEED-SV12', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-07 05:51:00', 'TLE', 33.3333, 100.0000, 1664, 1878, ''),
    ('SUB-SEED-0211', 'U-SEED-SV12', 'P001', 'Tổng hai số nguyên', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-07 09:18:00', 'WA', 50.0000, 100.0000, 99, 481, ''),
    ('SUB-SEED-0212', 'U-SEED-SV12', 'P003', 'Trung bình cộng dãy số', 'C++', 'solution.cpp', '#include <iostream>
int main(){long long a,b;std::cin>>a>>b;std::cout<<a+b;}
', '2026-08-07 12:34:00', 'RE', 33.3333, 100.0000, 93, 582, ''),
    ('SUB-SEED-0213', 'U-SEED-SV12', 'P003', 'Trung bình cộng dãy số', 'Python', 'solution.py', 'import sys
d=sys.stdin.read().split()
print(int(d[0])+int(d[1]))
', '2026-08-07 21:28:00', 'MLE', 0.0000, 100.0000, 257, 754, '')
ON DUPLICATE KEY UPDATE verdict = VALUES(verdict);

INSERT INTO test_case_results
    (submission_id, test_case_id, ordinal, sample, verdict,
     runtime_ms, earned_points, message)
VALUES
    ('SUB-SEED-0001', 'sample01', 0, TRUE, 'AC', 98, 33.3333, ''),
    ('SUB-SEED-0001', '02', 1, FALSE, 'AC', 94, 33.3333, ''),
    ('SUB-SEED-0001', '03', 2, FALSE, 'AC', 90, 33.3333, ''),
    ('SUB-SEED-0002', 'sample01', 0, TRUE, 'AC', 319, 33.3333, ''),
    ('SUB-SEED-0002', '02', 1, FALSE, 'RE', 315, 0.0000, ''),
    ('SUB-SEED-0002', '03', 2, FALSE, 'RE', 311, 0.0000, ''),
    ('SUB-SEED-0003', 'sample01', 0, TRUE, 'AC', 203, 25.0000, ''),
    ('SUB-SEED-0003', '02', 1, FALSE, 'AC', 199, 25.0000, ''),
    ('SUB-SEED-0003', '03', 2, FALSE, 'AC', 195, 25.0000, ''),
    ('SUB-SEED-0003', '04', 3, FALSE, 'AC', 191, 25.0000, ''),
    ('SUB-SEED-0004', 'sample01', 0, TRUE, 'AC', 127, 33.3333, ''),
    ('SUB-SEED-0004', '02', 1, FALSE, 'AC', 123, 33.3333, ''),
    ('SUB-SEED-0004', '03', 2, FALSE, 'AC', 119, 33.3333, ''),
    ('SUB-SEED-0005', 'sample01', 0, TRUE, 'AC', 181, 33.3333, ''),
    ('SUB-SEED-0005', '02', 1, FALSE, 'AC', 177, 33.3333, ''),
    ('SUB-SEED-0005', '03', 2, FALSE, 'AC', 173, 33.3333, ''),
    ('SUB-SEED-0006', 'sample01', 0, TRUE, 'AC', 333, 33.3333, ''),
    ('SUB-SEED-0006', '02', 1, FALSE, 'AC', 329, 33.3333, ''),
    ('SUB-SEED-0006', '03', 2, FALSE, 'AC', 325, 33.3333, ''),
    ('SUB-SEED-0007', 'sample01', 0, TRUE, 'AC', 88, 25.0000, ''),
    ('SUB-SEED-0007', '02', 1, FALSE, 'AC', 84, 25.0000, ''),
    ('SUB-SEED-0007', '03', 2, FALSE, 'AC', 80, 25.0000, ''),
    ('SUB-SEED-0007', '04', 3, FALSE, 'AC', 76, 25.0000, ''),
    ('SUB-SEED-0008', 'sample01', 0, TRUE, 'AC', 273, 25.0000, ''),
    ('SUB-SEED-0008', '02', 1, FALSE, 'AC', 269, 25.0000, ''),
    ('SUB-SEED-0008', '03', 2, FALSE, 'AC', 265, 25.0000, ''),
    ('SUB-SEED-0008', '04', 3, FALSE, 'AC', 261, 25.0000, ''),
    ('SUB-SEED-0009', 'sample01', 0, TRUE, 'AC', 240, 33.3333, ''),
    ('SUB-SEED-0009', '02', 1, FALSE, 'WA', 236, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0009', '03', 2, FALSE, 'WA', 232, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0010', 'sample01', 0, TRUE, 'AC', 46, 25.0000, ''),
    ('SUB-SEED-0010', '02', 1, FALSE, 'AC', 42, 25.0000, ''),
    ('SUB-SEED-0010', '03', 2, FALSE, 'AC', 38, 25.0000, ''),
    ('SUB-SEED-0010', '04', 3, FALSE, 'AC', 34, 25.0000, ''),
    ('SUB-SEED-0011', 'sample01', 0, TRUE, 'AC', 181, 33.3333, ''),
    ('SUB-SEED-0011', '02', 1, FALSE, 'AC', 177, 33.3333, ''),
    ('SUB-SEED-0011', '03', 2, FALSE, 'AC', 173, 33.3333, ''),
    ('SUB-SEED-0012', 'sample01', 0, TRUE, 'AC', 234, 25.0000, ''),
    ('SUB-SEED-0012', '02', 1, FALSE, 'AC', 230, 25.0000, ''),
    ('SUB-SEED-0012', '03', 2, FALSE, 'AC', 226, 25.0000, ''),
    ('SUB-SEED-0012', '04', 3, FALSE, 'AC', 222, 25.0000, ''),
    ('SUB-SEED-0013', 'sample01', 0, TRUE, 'AC', 68, 33.3333, ''),
    ('SUB-SEED-0013', '02', 1, FALSE, 'AC', 64, 33.3333, ''),
    ('SUB-SEED-0013', '03', 2, FALSE, 'AC', 60, 33.3333, ''),
    ('SUB-SEED-0015', 'sample01', 0, TRUE, 'AC', 296, 25.0000, ''),
    ('SUB-SEED-0015', '02', 1, FALSE, 'AC', 292, 25.0000, ''),
    ('SUB-SEED-0015', '03', 2, FALSE, 'AC', 288, 25.0000, ''),
    ('SUB-SEED-0015', '04', 3, FALSE, 'AC', 284, 25.0000, ''),
    ('SUB-SEED-0016', 'sample01', 0, TRUE, 'AC', 288, 25.0000, ''),
    ('SUB-SEED-0016', '02', 1, FALSE, 'AC', 284, 25.0000, ''),
    ('SUB-SEED-0016', '03', 2, FALSE, 'AC', 280, 25.0000, ''),
    ('SUB-SEED-0016', '04', 3, FALSE, 'AC', 276, 25.0000, ''),
    ('SUB-SEED-0017', 'sample01', 0, TRUE, 'AC', 188, 25.0000, ''),
    ('SUB-SEED-0017', '02', 1, FALSE, 'AC', 184, 25.0000, ''),
    ('SUB-SEED-0017', '03', 2, FALSE, 'AC', 180, 25.0000, ''),
    ('SUB-SEED-0017', '04', 3, FALSE, 'AC', 176, 25.0000, ''),
    ('SUB-SEED-0018', 'sample01', 0, TRUE, 'AC', 289, 33.3333, ''),
    ('SUB-SEED-0018', '02', 1, FALSE, 'AC', 285, 33.3333, ''),
    ('SUB-SEED-0018', '03', 2, FALSE, 'WA', 281, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0019', 'sample01', 0, TRUE, 'AC', 231, 33.3333, ''),
    ('SUB-SEED-0019', '02', 1, FALSE, 'AC', 227, 33.3333, ''),
    ('SUB-SEED-0019', '03', 2, FALSE, 'AC', 223, 33.3333, ''),
    ('SUB-SEED-0020', 'sample01', 0, TRUE, 'AC', 262, 33.3333, ''),
    ('SUB-SEED-0020', '02', 1, FALSE, 'AC', 258, 33.3333, ''),
    ('SUB-SEED-0020', '03', 2, FALSE, 'AC', 254, 33.3333, ''),
    ('SUB-SEED-0021', 'sample01', 0, TRUE, 'AC', 161, 25.0000, ''),
    ('SUB-SEED-0021', '02', 1, FALSE, 'WA', 157, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0021', '03', 2, FALSE, 'WA', 153, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0021', '04', 3, FALSE, 'WA', 149, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0022', 'sample01', 0, TRUE, 'AC', 142, 25.0000, ''),
    ('SUB-SEED-0022', '02', 1, FALSE, 'AC', 138, 25.0000, ''),
    ('SUB-SEED-0022', '03', 2, FALSE, 'AC', 134, 25.0000, ''),
    ('SUB-SEED-0022', '04', 3, FALSE, 'AC', 130, 25.0000, ''),
    ('SUB-SEED-0023', 'sample01', 0, TRUE, 'AC', 111, 25.0000, ''),
    ('SUB-SEED-0023', '02', 1, FALSE, 'AC', 107, 25.0000, ''),
    ('SUB-SEED-0023', '03', 2, FALSE, 'RE', 103, 0.0000, ''),
    ('SUB-SEED-0023', '04', 3, FALSE, 'RE', 99, 0.0000, ''),
    ('SUB-SEED-0024', 'sample01', 0, TRUE, 'AC', 90, 25.0000, ''),
    ('SUB-SEED-0024', '02', 1, FALSE, 'AC', 86, 25.0000, ''),
    ('SUB-SEED-0024', '03', 2, FALSE, 'AC', 82, 25.0000, ''),
    ('SUB-SEED-0024', '04', 3, FALSE, 'AC', 78, 25.0000, ''),
    ('SUB-SEED-0025', 'sample01', 0, TRUE, 'AC', 225, 25.0000, ''),
    ('SUB-SEED-0025', '02', 1, FALSE, 'AC', 221, 25.0000, ''),
    ('SUB-SEED-0025', '03', 2, FALSE, 'AC', 217, 25.0000, ''),
    ('SUB-SEED-0025', '04', 3, FALSE, 'AC', 213, 25.0000, ''),
    ('SUB-SEED-0026', 'sample01', 0, TRUE, 'AC', 184, 33.3333, ''),
    ('SUB-SEED-0026', '02', 1, FALSE, 'AC', 180, 33.3333, ''),
    ('SUB-SEED-0026', '03', 2, FALSE, 'AC', 176, 33.3333, ''),
    ('SUB-SEED-0027', 'sample01', 0, TRUE, 'AC', 315, 33.3333, ''),
    ('SUB-SEED-0027', '02', 1, FALSE, 'AC', 311, 33.3333, ''),
    ('SUB-SEED-0027', '03', 2, FALSE, 'AC', 307, 33.3333, ''),
    ('SUB-SEED-0028', 'sample01', 0, TRUE, 'AC', 308, 25.0000, ''),
    ('SUB-SEED-0028', '02', 1, FALSE, 'AC', 304, 25.0000, ''),
    ('SUB-SEED-0028', '03', 2, FALSE, 'AC', 300, 25.0000, ''),
    ('SUB-SEED-0028', '04', 3, FALSE, 'AC', 296, 25.0000, ''),
    ('SUB-SEED-0029', 'sample01', 0, TRUE, 'AC', 225, 33.3333, ''),
    ('SUB-SEED-0029', '02', 1, FALSE, 'AC', 221, 33.3333, ''),
    ('SUB-SEED-0029', '03', 2, FALSE, 'AC', 217, 33.3333, ''),
    ('SUB-SEED-0030', 'sample01', 0, TRUE, 'AC', 157, 33.3333, ''),
    ('SUB-SEED-0030', '02', 1, FALSE, 'AC', 153, 33.3333, ''),
    ('SUB-SEED-0030', '03', 2, FALSE, 'AC', 149, 33.3333, ''),
    ('SUB-SEED-0031', 'sample01', 0, TRUE, 'AC', 107, 25.0000, ''),
    ('SUB-SEED-0031', '02', 1, FALSE, 'AC', 103, 25.0000, ''),
    ('SUB-SEED-0031', '03', 2, FALSE, 'AC', 99, 25.0000, ''),
    ('SUB-SEED-0031', '04', 3, FALSE, 'AC', 95, 25.0000, ''),
    ('SUB-SEED-0032', 'sample01', 0, TRUE, 'AC', 291, 25.0000, ''),
    ('SUB-SEED-0032', '02', 1, FALSE, 'AC', 287, 25.0000, ''),
    ('SUB-SEED-0032', '03', 2, FALSE, 'AC', 283, 25.0000, ''),
    ('SUB-SEED-0032', '04', 3, FALSE, 'AC', 279, 25.0000, ''),
    ('SUB-SEED-0033', 'sample01', 0, TRUE, 'AC', 354, 25.0000, ''),
    ('SUB-SEED-0033', '02', 1, FALSE, 'AC', 350, 25.0000, ''),
    ('SUB-SEED-0033', '03', 2, FALSE, 'AC', 346, 25.0000, ''),
    ('SUB-SEED-0033', '04', 3, FALSE, 'AC', 342, 25.0000, ''),
    ('SUB-SEED-0034', 'sample01', 0, TRUE, 'TLE', 1796, 0.0000, ''),
    ('SUB-SEED-0034', '02', 1, FALSE, 'TLE', 1792, 0.0000, ''),
    ('SUB-SEED-0034', '03', 2, FALSE, 'TLE', 1788, 0.0000, ''),
    ('SUB-SEED-0034', '04', 3, FALSE, 'TLE', 1784, 0.0000, ''),
    ('SUB-SEED-0035', 'sample01', 0, TRUE, 'AC', 43, 33.3333, ''),
    ('SUB-SEED-0035', '02', 1, FALSE, 'AC', 39, 33.3333, ''),
    ('SUB-SEED-0035', '03', 2, FALSE, 'AC', 35, 33.3333, ''),
    ('SUB-SEED-0036', 'sample01', 0, TRUE, 'AC', 99, 25.0000, ''),
    ('SUB-SEED-0036', '02', 1, FALSE, 'AC', 95, 25.0000, ''),
    ('SUB-SEED-0036', '03', 2, FALSE, 'AC', 91, 25.0000, ''),
    ('SUB-SEED-0036', '04', 3, FALSE, 'AC', 87, 25.0000, ''),
    ('SUB-SEED-0037', 'sample01', 0, TRUE, 'AC', 186, 25.0000, ''),
    ('SUB-SEED-0037', '02', 1, FALSE, 'AC', 182, 25.0000, ''),
    ('SUB-SEED-0037', '03', 2, FALSE, 'AC', 178, 25.0000, ''),
    ('SUB-SEED-0037', '04', 3, FALSE, 'AC', 174, 25.0000, ''),
    ('SUB-SEED-0038', 'sample01', 0, TRUE, 'AC', 165, 25.0000, ''),
    ('SUB-SEED-0038', '02', 1, FALSE, 'AC', 161, 25.0000, ''),
    ('SUB-SEED-0038', '03', 2, FALSE, 'AC', 157, 25.0000, ''),
    ('SUB-SEED-0038', '04', 3, FALSE, 'AC', 153, 25.0000, ''),
    ('SUB-SEED-0039', 'sample01', 0, TRUE, 'AC', 309, 25.0000, ''),
    ('SUB-SEED-0039', '02', 1, FALSE, 'AC', 305, 25.0000, ''),
    ('SUB-SEED-0039', '03', 2, FALSE, 'AC', 301, 25.0000, ''),
    ('SUB-SEED-0039', '04', 3, FALSE, 'AC', 297, 25.0000, ''),
    ('SUB-SEED-0040', 'sample01', 0, TRUE, 'AC', 270, 25.0000, ''),
    ('SUB-SEED-0040', '02', 1, FALSE, 'AC', 266, 25.0000, ''),
    ('SUB-SEED-0040', '03', 2, FALSE, 'AC', 262, 25.0000, ''),
    ('SUB-SEED-0040', '04', 3, FALSE, 'AC', 258, 25.0000, ''),
    ('SUB-SEED-0041', 'sample01', 0, TRUE, 'AC', 304, 25.0000, ''),
    ('SUB-SEED-0041', '02', 1, FALSE, 'AC', 300, 25.0000, ''),
    ('SUB-SEED-0041', '03', 2, FALSE, 'AC', 296, 25.0000, ''),
    ('SUB-SEED-0041', '04', 3, FALSE, 'AC', 292, 25.0000, ''),
    ('SUB-SEED-0042', 'sample01', 0, TRUE, 'WA', 266, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0042', '02', 1, FALSE, 'WA', 262, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0042', '03', 2, FALSE, 'WA', 258, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0043', 'sample01', 0, TRUE, 'AC', 225, 25.0000, ''),
    ('SUB-SEED-0043', '02', 1, FALSE, 'AC', 221, 25.0000, ''),
    ('SUB-SEED-0043', '03', 2, FALSE, 'AC', 217, 25.0000, ''),
    ('SUB-SEED-0043', '04', 3, FALSE, 'AC', 213, 25.0000, ''),
    ('SUB-SEED-0044', 'sample01', 0, TRUE, 'AC', 330, 33.3333, ''),
    ('SUB-SEED-0044', '02', 1, FALSE, 'AC', 326, 33.3333, ''),
    ('SUB-SEED-0044', '03', 2, FALSE, 'AC', 322, 33.3333, ''),
    ('SUB-SEED-0045', 'sample01', 0, TRUE, 'AC', 234, 33.3333, ''),
    ('SUB-SEED-0045', '02', 1, FALSE, 'AC', 230, 33.3333, ''),
    ('SUB-SEED-0045', '03', 2, FALSE, 'AC', 226, 33.3333, ''),
    ('SUB-SEED-0046', 'sample01', 0, TRUE, 'AC', 117, 25.0000, ''),
    ('SUB-SEED-0046', '02', 1, FALSE, 'AC', 113, 25.0000, ''),
    ('SUB-SEED-0046', '03', 2, FALSE, 'AC', 109, 25.0000, ''),
    ('SUB-SEED-0046', '04', 3, FALSE, 'AC', 105, 25.0000, ''),
    ('SUB-SEED-0047', 'sample01', 0, TRUE, 'WA', 100, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0047', '02', 1, FALSE, 'WA', 96, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0047', '03', 2, FALSE, 'WA', 92, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0047', '04', 3, FALSE, 'WA', 88, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0048', 'sample01', 0, TRUE, 'AC', 331, 25.0000, ''),
    ('SUB-SEED-0048', '02', 1, FALSE, 'AC', 327, 25.0000, ''),
    ('SUB-SEED-0048', '03', 2, FALSE, 'AC', 323, 25.0000, ''),
    ('SUB-SEED-0048', '04', 3, FALSE, 'AC', 319, 25.0000, ''),
    ('SUB-SEED-0049', 'sample01', 0, TRUE, 'AC', 244, 25.0000, ''),
    ('SUB-SEED-0049', '02', 1, FALSE, 'AC', 240, 25.0000, ''),
    ('SUB-SEED-0049', '03', 2, FALSE, 'AC', 236, 25.0000, ''),
    ('SUB-SEED-0049', '04', 3, FALSE, 'AC', 232, 25.0000, ''),
    ('SUB-SEED-0050', 'sample01', 0, TRUE, 'AC', 328, 33.3333, ''),
    ('SUB-SEED-0050', '02', 1, FALSE, 'WA', 324, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0050', '03', 2, FALSE, 'WA', 320, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0051', 'sample01', 0, TRUE, 'AC', 142, 33.3333, ''),
    ('SUB-SEED-0051', '02', 1, FALSE, 'AC', 138, 33.3333, ''),
    ('SUB-SEED-0051', '03', 2, FALSE, 'AC', 134, 33.3333, ''),
    ('SUB-SEED-0052', 'sample01', 0, TRUE, 'AC', 308, 33.3333, ''),
    ('SUB-SEED-0052', '02', 1, FALSE, 'AC', 304, 33.3333, ''),
    ('SUB-SEED-0052', '03', 2, FALSE, 'AC', 300, 33.3333, ''),
    ('SUB-SEED-0053', 'sample01', 0, TRUE, 'AC', 236, 25.0000, ''),
    ('SUB-SEED-0053', '02', 1, FALSE, 'AC', 232, 25.0000, ''),
    ('SUB-SEED-0053', '03', 2, FALSE, 'AC', 228, 25.0000, ''),
    ('SUB-SEED-0053', '04', 3, FALSE, 'AC', 224, 25.0000, ''),
    ('SUB-SEED-0054', 'sample01', 0, TRUE, 'AC', 138, 25.0000, ''),
    ('SUB-SEED-0054', '02', 1, FALSE, 'AC', 134, 25.0000, ''),
    ('SUB-SEED-0054', '03', 2, FALSE, 'AC', 130, 25.0000, ''),
    ('SUB-SEED-0054', '04', 3, FALSE, 'AC', 126, 25.0000, ''),
    ('SUB-SEED-0055', 'sample01', 0, TRUE, 'AC', 55, 25.0000, ''),
    ('SUB-SEED-0055', '02', 1, FALSE, 'AC', 51, 25.0000, ''),
    ('SUB-SEED-0055', '03', 2, FALSE, 'AC', 47, 25.0000, ''),
    ('SUB-SEED-0055', '04', 3, FALSE, 'AC', 43, 25.0000, ''),
    ('SUB-SEED-0056', 'sample01', 0, TRUE, 'AC', 45, 33.3333, ''),
    ('SUB-SEED-0056', '02', 1, FALSE, 'AC', 41, 33.3333, ''),
    ('SUB-SEED-0056', '03', 2, FALSE, 'AC', 37, 33.3333, ''),
    ('SUB-SEED-0057', 'sample01', 0, TRUE, 'AC', 333, 33.3333, ''),
    ('SUB-SEED-0057', '02', 1, FALSE, 'AC', 329, 33.3333, ''),
    ('SUB-SEED-0057', '03', 2, FALSE, 'WA', 325, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0058', 'sample01', 0, TRUE, 'AC', 323, 25.0000, ''),
    ('SUB-SEED-0058', '02', 1, FALSE, 'AC', 319, 25.0000, ''),
    ('SUB-SEED-0058', '03', 2, FALSE, 'AC', 315, 25.0000, ''),
    ('SUB-SEED-0058', '04', 3, FALSE, 'WA', 311, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0059', 'sample01', 0, TRUE, 'AC', 1736, 25.0000, ''),
    ('SUB-SEED-0059', '02', 1, FALSE, 'TLE', 1732, 0.0000, ''),
    ('SUB-SEED-0059', '03', 2, FALSE, 'TLE', 1728, 0.0000, ''),
    ('SUB-SEED-0059', '04', 3, FALSE, 'TLE', 1724, 0.0000, ''),
    ('SUB-SEED-0060', 'sample01', 0, TRUE, 'AC', 198, 33.3333, ''),
    ('SUB-SEED-0060', '02', 1, FALSE, 'AC', 194, 33.3333, ''),
    ('SUB-SEED-0060', '03', 2, FALSE, 'AC', 190, 33.3333, ''),
    ('SUB-SEED-0061', 'sample01', 0, TRUE, 'WA', 128, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0061', '02', 1, FALSE, 'WA', 124, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0061', '03', 2, FALSE, 'WA', 120, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0062', 'sample01', 0, TRUE, 'WA', 114, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0062', '02', 1, FALSE, 'WA', 110, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0062', '03', 2, FALSE, 'WA', 106, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0063', 'sample01', 0, TRUE, 'WA', 233, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0063', '02', 1, FALSE, 'WA', 229, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0063', '03', 2, FALSE, 'WA', 225, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0064', 'sample01', 0, TRUE, 'AC', 274, 25.0000, ''),
    ('SUB-SEED-0064', '02', 1, FALSE, 'AC', 270, 25.0000, ''),
    ('SUB-SEED-0064', '03', 2, FALSE, 'AC', 266, 25.0000, ''),
    ('SUB-SEED-0064', '04', 3, FALSE, 'AC', 262, 25.0000, ''),
    ('SUB-SEED-0066', 'sample01', 0, TRUE, 'AC', 299, 25.0000, ''),
    ('SUB-SEED-0066', '02', 1, FALSE, 'AC', 295, 25.0000, ''),
    ('SUB-SEED-0066', '03', 2, FALSE, 'AC', 291, 25.0000, ''),
    ('SUB-SEED-0066', '04', 3, FALSE, 'AC', 287, 25.0000, ''),
    ('SUB-SEED-0067', 'sample01', 0, TRUE, 'TLE', 1518, 0.0000, ''),
    ('SUB-SEED-0067', '02', 1, FALSE, 'TLE', 1514, 0.0000, ''),
    ('SUB-SEED-0067', '03', 2, FALSE, 'TLE', 1510, 0.0000, ''),
    ('SUB-SEED-0067', '04', 3, FALSE, 'TLE', 1506, 0.0000, ''),
    ('SUB-SEED-0068', 'sample01', 0, TRUE, 'AC', 293, 33.3333, ''),
    ('SUB-SEED-0068', '02', 1, FALSE, 'RE', 289, 0.0000, ''),
    ('SUB-SEED-0068', '03', 2, FALSE, 'RE', 285, 0.0000, ''),
    ('SUB-SEED-0069', 'sample01', 0, TRUE, 'AC', 148, 25.0000, ''),
    ('SUB-SEED-0069', '02', 1, FALSE, 'AC', 144, 25.0000, ''),
    ('SUB-SEED-0069', '03', 2, FALSE, 'AC', 140, 25.0000, ''),
    ('SUB-SEED-0069', '04', 3, FALSE, 'AC', 136, 25.0000, ''),
    ('SUB-SEED-0070', 'sample01', 0, TRUE, 'AC', 177, 33.3333, ''),
    ('SUB-SEED-0070', '02', 1, FALSE, 'RE', 173, 0.0000, ''),
    ('SUB-SEED-0070', '03', 2, FALSE, 'RE', 169, 0.0000, ''),
    ('SUB-SEED-0071', 'sample01', 0, TRUE, 'AC', 80, 25.0000, ''),
    ('SUB-SEED-0071', '02', 1, FALSE, 'AC', 76, 25.0000, ''),
    ('SUB-SEED-0071', '03', 2, FALSE, 'AC', 72, 25.0000, ''),
    ('SUB-SEED-0071', '04', 3, FALSE, 'AC', 68, 25.0000, ''),
    ('SUB-SEED-0072', 'sample01', 0, TRUE, 'AC', 187, 33.3333, ''),
    ('SUB-SEED-0072', '02', 1, FALSE, 'AC', 183, 33.3333, ''),
    ('SUB-SEED-0072', '03', 2, FALSE, 'AC', 179, 33.3333, ''),
    ('SUB-SEED-0073', 'sample01', 0, TRUE, 'AC', 187, 33.3333, ''),
    ('SUB-SEED-0073', '02', 1, FALSE, 'AC', 183, 33.3333, ''),
    ('SUB-SEED-0073', '03', 2, FALSE, 'AC', 179, 33.3333, ''),
    ('SUB-SEED-0074', 'sample01', 0, TRUE, 'AC', 89, 25.0000, ''),
    ('SUB-SEED-0074', '02', 1, FALSE, 'AC', 85, 25.0000, ''),
    ('SUB-SEED-0074', '03', 2, FALSE, 'AC', 81, 25.0000, ''),
    ('SUB-SEED-0074', '04', 3, FALSE, 'AC', 77, 25.0000, ''),
    ('SUB-SEED-0075', 'sample01', 0, TRUE, 'AC', 99, 25.0000, ''),
    ('SUB-SEED-0075', '02', 1, FALSE, 'WA', 95, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0075', '03', 2, FALSE, 'WA', 91, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0075', '04', 3, FALSE, 'WA', 87, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0077', 'sample01', 0, TRUE, 'AC', 39, 33.3333, ''),
    ('SUB-SEED-0077', '02', 1, FALSE, 'WA', 35, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0077', '03', 2, FALSE, 'WA', 31, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0078', 'sample01', 0, TRUE, 'AC', 130, 33.3333, ''),
    ('SUB-SEED-0078', '02', 1, FALSE, 'AC', 126, 33.3333, ''),
    ('SUB-SEED-0078', '03', 2, FALSE, 'AC', 122, 33.3333, ''),
    ('SUB-SEED-0079', 'sample01', 0, TRUE, 'AC', 62, 33.3333, ''),
    ('SUB-SEED-0079', '02', 1, FALSE, 'AC', 58, 33.3333, ''),
    ('SUB-SEED-0079', '03', 2, FALSE, 'AC', 54, 33.3333, ''),
    ('SUB-SEED-0080', 'sample01', 0, TRUE, 'AC', 51, 25.0000, ''),
    ('SUB-SEED-0080', '02', 1, FALSE, 'AC', 47, 25.0000, ''),
    ('SUB-SEED-0080', '03', 2, FALSE, 'AC', 43, 25.0000, ''),
    ('SUB-SEED-0080', '04', 3, FALSE, 'AC', 39, 25.0000, ''),
    ('SUB-SEED-0081', 'sample01', 0, TRUE, 'AC', 67, 25.0000, ''),
    ('SUB-SEED-0081', '02', 1, FALSE, 'AC', 63, 25.0000, ''),
    ('SUB-SEED-0081', '03', 2, FALSE, 'AC', 59, 25.0000, ''),
    ('SUB-SEED-0081', '04', 3, FALSE, 'AC', 55, 25.0000, ''),
    ('SUB-SEED-0082', 'sample01', 0, TRUE, 'AC', 126, 25.0000, ''),
    ('SUB-SEED-0082', '02', 1, FALSE, 'AC', 122, 25.0000, ''),
    ('SUB-SEED-0082', '03', 2, FALSE, 'AC', 118, 25.0000, ''),
    ('SUB-SEED-0082', '04', 3, FALSE, 'AC', 114, 25.0000, ''),
    ('SUB-SEED-0083', 'sample01', 0, TRUE, 'AC', 306, 25.0000, ''),
    ('SUB-SEED-0083', '02', 1, FALSE, 'AC', 302, 25.0000, ''),
    ('SUB-SEED-0083', '03', 2, FALSE, 'AC', 298, 25.0000, ''),
    ('SUB-SEED-0083', '04', 3, FALSE, 'AC', 294, 25.0000, ''),
    ('SUB-SEED-0084', 'sample01', 0, TRUE, 'AC', 288, 33.3333, ''),
    ('SUB-SEED-0084', '02', 1, FALSE, 'AC', 284, 33.3333, ''),
    ('SUB-SEED-0084', '03', 2, FALSE, 'AC', 280, 33.3333, ''),
    ('SUB-SEED-0085', 'sample01', 0, TRUE, 'AC', 65, 33.3333, ''),
    ('SUB-SEED-0085', '02', 1, FALSE, 'AC', 61, 33.3333, ''),
    ('SUB-SEED-0085', '03', 2, FALSE, 'AC', 57, 33.3333, ''),
    ('SUB-SEED-0086', 'sample01', 0, TRUE, 'AC', 210, 25.0000, ''),
    ('SUB-SEED-0086', '02', 1, FALSE, 'WA', 206, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0086', '03', 2, FALSE, 'WA', 202, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0086', '04', 3, FALSE, 'WA', 198, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0087', 'sample01', 0, TRUE, 'WA', 211, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0087', '02', 1, FALSE, 'WA', 207, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0087', '03', 2, FALSE, 'WA', 203, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0087', '04', 3, FALSE, 'WA', 199, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0088', 'sample01', 0, TRUE, 'AC', 149, 33.3333, ''),
    ('SUB-SEED-0088', '02', 1, FALSE, 'AC', 145, 33.3333, ''),
    ('SUB-SEED-0088', '03', 2, FALSE, 'AC', 141, 33.3333, ''),
    ('SUB-SEED-0089', 'sample01', 0, TRUE, 'AC', 167, 25.0000, ''),
    ('SUB-SEED-0089', '02', 1, FALSE, 'AC', 163, 25.0000, ''),
    ('SUB-SEED-0089', '03', 2, FALSE, 'AC', 159, 25.0000, ''),
    ('SUB-SEED-0089', '04', 3, FALSE, 'AC', 155, 25.0000, ''),
    ('SUB-SEED-0090', 'sample01', 0, TRUE, 'AC', 72, 25.0000, ''),
    ('SUB-SEED-0090', '02', 1, FALSE, 'WA', 68, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0090', '03', 2, FALSE, 'WA', 64, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0090', '04', 3, FALSE, 'WA', 60, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0091', 'sample01', 0, TRUE, 'AC', 76, 25.0000, ''),
    ('SUB-SEED-0091', '02', 1, FALSE, 'AC', 72, 25.0000, ''),
    ('SUB-SEED-0091', '03', 2, FALSE, 'AC', 68, 25.0000, ''),
    ('SUB-SEED-0091', '04', 3, FALSE, 'WA', 64, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0092', 'sample01', 0, TRUE, 'AC', 201, 25.0000, ''),
    ('SUB-SEED-0092', '02', 1, FALSE, 'AC', 197, 25.0000, ''),
    ('SUB-SEED-0092', '03', 2, FALSE, 'AC', 193, 25.0000, ''),
    ('SUB-SEED-0092', '04', 3, FALSE, 'AC', 189, 25.0000, ''),
    ('SUB-SEED-0093', 'sample01', 0, TRUE, 'AC', 237, 25.0000, ''),
    ('SUB-SEED-0093', '02', 1, FALSE, 'AC', 233, 25.0000, ''),
    ('SUB-SEED-0093', '03', 2, FALSE, 'AC', 229, 25.0000, ''),
    ('SUB-SEED-0093', '04', 3, FALSE, 'AC', 225, 25.0000, ''),
    ('SUB-SEED-0095', 'sample01', 0, TRUE, 'AC', 354, 33.3333, ''),
    ('SUB-SEED-0095', '02', 1, FALSE, 'AC', 350, 33.3333, ''),
    ('SUB-SEED-0095', '03', 2, FALSE, 'AC', 346, 33.3333, ''),
    ('SUB-SEED-0096', 'sample01', 0, TRUE, 'AC', 276, 25.0000, ''),
    ('SUB-SEED-0096', '02', 1, FALSE, 'AC', 272, 25.0000, ''),
    ('SUB-SEED-0096', '03', 2, FALSE, 'AC', 268, 25.0000, ''),
    ('SUB-SEED-0096', '04', 3, FALSE, 'AC', 264, 25.0000, ''),
    ('SUB-SEED-0097', 'sample01', 0, TRUE, 'AC', 135, 25.0000, ''),
    ('SUB-SEED-0097', '02', 1, FALSE, 'AC', 131, 25.0000, ''),
    ('SUB-SEED-0097', '03', 2, FALSE, 'AC', 127, 25.0000, ''),
    ('SUB-SEED-0097', '04', 3, FALSE, 'AC', 123, 25.0000, ''),
    ('SUB-SEED-0098', 'sample01', 0, TRUE, 'TLE', 1677, 0.0000, ''),
    ('SUB-SEED-0098', '02', 1, FALSE, 'TLE', 1673, 0.0000, ''),
    ('SUB-SEED-0098', '03', 2, FALSE, 'TLE', 1669, 0.0000, ''),
    ('SUB-SEED-0099', 'sample01', 0, TRUE, 'WA', 178, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0099', '02', 1, FALSE, 'WA', 174, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0099', '03', 2, FALSE, 'WA', 170, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0100', 'sample01', 0, TRUE, 'AC', 52, 25.0000, ''),
    ('SUB-SEED-0100', '02', 1, FALSE, 'AC', 48, 25.0000, ''),
    ('SUB-SEED-0100', '03', 2, FALSE, 'AC', 44, 25.0000, ''),
    ('SUB-SEED-0100', '04', 3, FALSE, 'WA', 40, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0101', 'sample01', 0, TRUE, 'AC', 40, 33.3333, ''),
    ('SUB-SEED-0101', '02', 1, FALSE, 'WA', 36, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0101', '03', 2, FALSE, 'WA', 32, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0102', 'sample01', 0, TRUE, 'WA', 302, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0102', '02', 1, FALSE, 'WA', 298, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0102', '03', 2, FALSE, 'WA', 294, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0102', '04', 3, FALSE, 'WA', 290, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0103', 'sample01', 0, TRUE, 'AC', 261, 25.0000, ''),
    ('SUB-SEED-0103', '02', 1, FALSE, 'AC', 257, 25.0000, ''),
    ('SUB-SEED-0103', '03', 2, FALSE, 'AC', 253, 25.0000, ''),
    ('SUB-SEED-0103', '04', 3, FALSE, 'AC', 249, 25.0000, ''),
    ('SUB-SEED-0104', 'sample01', 0, TRUE, 'AC', 217, 33.3333, ''),
    ('SUB-SEED-0104', '02', 1, FALSE, 'AC', 213, 33.3333, ''),
    ('SUB-SEED-0104', '03', 2, FALSE, 'AC', 209, 33.3333, ''),
    ('SUB-SEED-0105', 'sample01', 0, TRUE, 'AC', 213, 25.0000, ''),
    ('SUB-SEED-0105', '02', 1, FALSE, 'AC', 209, 25.0000, ''),
    ('SUB-SEED-0105', '03', 2, FALSE, 'AC', 205, 25.0000, ''),
    ('SUB-SEED-0105', '04', 3, FALSE, 'AC', 201, 25.0000, ''),
    ('SUB-SEED-0106', 'sample01', 0, TRUE, 'AC', 250, 33.3333, ''),
    ('SUB-SEED-0106', '02', 1, FALSE, 'AC', 246, 33.3333, ''),
    ('SUB-SEED-0106', '03', 2, FALSE, 'AC', 242, 33.3333, ''),
    ('SUB-SEED-0107', 'sample01', 0, TRUE, 'WA', 146, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0107', '02', 1, FALSE, 'WA', 142, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0107', '03', 2, FALSE, 'WA', 138, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0109', 'sample01', 0, TRUE, 'AC', 350, 33.3333, ''),
    ('SUB-SEED-0109', '02', 1, FALSE, 'AC', 346, 33.3333, ''),
    ('SUB-SEED-0109', '03', 2, FALSE, 'WA', 342, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0110', 'sample01', 0, TRUE, 'AC', 212, 33.3333, ''),
    ('SUB-SEED-0110', '02', 1, FALSE, 'AC', 208, 33.3333, ''),
    ('SUB-SEED-0110', '03', 2, FALSE, 'AC', 204, 33.3333, ''),
    ('SUB-SEED-0111', 'sample01', 0, TRUE, 'AC', 1843, 33.3333, ''),
    ('SUB-SEED-0111', '02', 1, FALSE, 'TLE', 1839, 0.0000, ''),
    ('SUB-SEED-0111', '03', 2, FALSE, 'TLE', 1835, 0.0000, ''),
    ('SUB-SEED-0112', 'sample01', 0, TRUE, 'AC', 193, 33.3333, ''),
    ('SUB-SEED-0112', '02', 1, FALSE, 'AC', 189, 33.3333, ''),
    ('SUB-SEED-0112', '03', 2, FALSE, 'AC', 185, 33.3333, ''),
    ('SUB-SEED-0113', 'sample01', 0, TRUE, 'WA', 216, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0113', '02', 1, FALSE, 'WA', 212, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0113', '03', 2, FALSE, 'WA', 208, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0114', 'sample01', 0, TRUE, 'WA', 352, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0114', '02', 1, FALSE, 'WA', 348, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0114', '03', 2, FALSE, 'WA', 344, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0114', '04', 3, FALSE, 'WA', 340, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0115', 'sample01', 0, TRUE, 'AC', 1730, 25.0000, ''),
    ('SUB-SEED-0115', '02', 1, FALSE, 'AC', 1726, 25.0000, ''),
    ('SUB-SEED-0115', '03', 2, FALSE, 'TLE', 1722, 0.0000, ''),
    ('SUB-SEED-0115', '04', 3, FALSE, 'TLE', 1718, 0.0000, ''),
    ('SUB-SEED-0116', 'sample01', 0, TRUE, 'AC', 1579, 25.0000, ''),
    ('SUB-SEED-0116', '02', 1, FALSE, 'AC', 1575, 25.0000, ''),
    ('SUB-SEED-0116', '03', 2, FALSE, 'TLE', 1571, 0.0000, ''),
    ('SUB-SEED-0116', '04', 3, FALSE, 'TLE', 1567, 0.0000, ''),
    ('SUB-SEED-0117', 'sample01', 0, TRUE, 'AC', 296, 25.0000, ''),
    ('SUB-SEED-0117', '02', 1, FALSE, 'AC', 292, 25.0000, ''),
    ('SUB-SEED-0117', '03', 2, FALSE, 'AC', 288, 25.0000, ''),
    ('SUB-SEED-0117', '04', 3, FALSE, 'AC', 284, 25.0000, ''),
    ('SUB-SEED-0118', 'sample01', 0, TRUE, 'WA', 168, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0118', '02', 1, FALSE, 'WA', 164, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0118', '03', 2, FALSE, 'WA', 160, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0118', '04', 3, FALSE, 'WA', 156, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0119', 'sample01', 0, TRUE, 'AC', 52, 33.3333, ''),
    ('SUB-SEED-0119', '02', 1, FALSE, 'AC', 48, 33.3333, ''),
    ('SUB-SEED-0119', '03', 2, FALSE, 'WA', 44, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0120', 'sample01', 0, TRUE, 'AC', 238, 33.3333, ''),
    ('SUB-SEED-0120', '02', 1, FALSE, 'AC', 234, 33.3333, ''),
    ('SUB-SEED-0120', '03', 2, FALSE, 'AC', 230, 33.3333, ''),
    ('SUB-SEED-0121', 'sample01', 0, TRUE, 'AC', 271, 33.3333, ''),
    ('SUB-SEED-0121', '02', 1, FALSE, 'AC', 267, 33.3333, ''),
    ('SUB-SEED-0121', '03', 2, FALSE, 'AC', 263, 33.3333, ''),
    ('SUB-SEED-0123', 'sample01', 0, TRUE, 'AC', 305, 25.0000, ''),
    ('SUB-SEED-0123', '02', 1, FALSE, 'AC', 301, 25.0000, ''),
    ('SUB-SEED-0123', '03', 2, FALSE, 'RE', 297, 0.0000, ''),
    ('SUB-SEED-0123', '04', 3, FALSE, 'RE', 293, 0.0000, ''),
    ('SUB-SEED-0124', 'sample01', 0, TRUE, 'AC', 1788, 33.3333, ''),
    ('SUB-SEED-0124', '02', 1, FALSE, 'TLE', 1784, 0.0000, ''),
    ('SUB-SEED-0124', '03', 2, FALSE, 'TLE', 1780, 0.0000, ''),
    ('SUB-SEED-0125', 'sample01', 0, TRUE, 'WA', 258, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0125', '02', 1, FALSE, 'WA', 254, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0125', '03', 2, FALSE, 'WA', 250, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0125', '04', 3, FALSE, 'WA', 246, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0126', 'sample01', 0, TRUE, 'AC', 251, 25.0000, ''),
    ('SUB-SEED-0126', '02', 1, FALSE, 'AC', 247, 25.0000, ''),
    ('SUB-SEED-0126', '03', 2, FALSE, 'AC', 243, 25.0000, ''),
    ('SUB-SEED-0126', '04', 3, FALSE, 'AC', 239, 25.0000, ''),
    ('SUB-SEED-0127', 'sample01', 0, TRUE, 'AC', 328, 25.0000, ''),
    ('SUB-SEED-0127', '02', 1, FALSE, 'AC', 324, 25.0000, ''),
    ('SUB-SEED-0127', '03', 2, FALSE, 'AC', 320, 25.0000, ''),
    ('SUB-SEED-0127', '04', 3, FALSE, 'AC', 316, 25.0000, ''),
    ('SUB-SEED-0129', 'sample01', 0, TRUE, 'AC', 1877, 33.3333, ''),
    ('SUB-SEED-0129', '02', 1, FALSE, 'TLE', 1873, 0.0000, ''),
    ('SUB-SEED-0129', '03', 2, FALSE, 'TLE', 1869, 0.0000, ''),
    ('SUB-SEED-0130', 'sample01', 0, TRUE, 'AC', 42, 33.3333, ''),
    ('SUB-SEED-0130', '02', 1, FALSE, 'AC', 38, 33.3333, ''),
    ('SUB-SEED-0130', '03', 2, FALSE, 'AC', 34, 33.3333, ''),
    ('SUB-SEED-0131', 'sample01', 0, TRUE, 'WA', 35, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0131', '02', 1, FALSE, 'WA', 31, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0131', '03', 2, FALSE, 'WA', 27, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0132', 'sample01', 0, TRUE, 'AC', 269, 25.0000, ''),
    ('SUB-SEED-0132', '02', 1, FALSE, 'AC', 265, 25.0000, ''),
    ('SUB-SEED-0132', '03', 2, FALSE, 'AC', 261, 25.0000, ''),
    ('SUB-SEED-0132', '04', 3, FALSE, 'AC', 257, 25.0000, ''),
    ('SUB-SEED-0133', 'sample01', 0, TRUE, 'AC', 346, 25.0000, ''),
    ('SUB-SEED-0133', '02', 1, FALSE, 'AC', 342, 25.0000, ''),
    ('SUB-SEED-0133', '03', 2, FALSE, 'AC', 338, 25.0000, ''),
    ('SUB-SEED-0133', '04', 3, FALSE, 'AC', 334, 25.0000, ''),
    ('SUB-SEED-0134', 'sample01', 0, TRUE, 'AC', 298, 25.0000, ''),
    ('SUB-SEED-0134', '02', 1, FALSE, 'AC', 294, 25.0000, ''),
    ('SUB-SEED-0134', '03', 2, FALSE, 'AC', 290, 25.0000, ''),
    ('SUB-SEED-0134', '04', 3, FALSE, 'AC', 286, 25.0000, ''),
    ('SUB-SEED-0135', 'sample01', 0, TRUE, 'AC', 101, 25.0000, ''),
    ('SUB-SEED-0135', '02', 1, FALSE, 'WA', 97, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0135', '03', 2, FALSE, 'WA', 93, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0135', '04', 3, FALSE, 'WA', 89, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0136', 'sample01', 0, TRUE, 'AC', 107, 33.3333, ''),
    ('SUB-SEED-0136', '02', 1, FALSE, 'AC', 103, 33.3333, ''),
    ('SUB-SEED-0136', '03', 2, FALSE, 'AC', 99, 33.3333, ''),
    ('SUB-SEED-0137', 'sample01', 0, TRUE, 'AC', 108, 33.3333, ''),
    ('SUB-SEED-0137', '02', 1, FALSE, 'AC', 104, 33.3333, ''),
    ('SUB-SEED-0137', '03', 2, FALSE, 'AC', 100, 33.3333, ''),
    ('SUB-SEED-0138', 'sample01', 0, TRUE, 'AC', 196, 25.0000, ''),
    ('SUB-SEED-0138', '02', 1, FALSE, 'AC', 192, 25.0000, ''),
    ('SUB-SEED-0138', '03', 2, FALSE, 'AC', 188, 25.0000, ''),
    ('SUB-SEED-0138', '04', 3, FALSE, 'AC', 184, 25.0000, ''),
    ('SUB-SEED-0139', 'sample01', 0, TRUE, 'AC', 351, 33.3333, ''),
    ('SUB-SEED-0139', '02', 1, FALSE, 'AC', 347, 33.3333, ''),
    ('SUB-SEED-0139', '03', 2, FALSE, 'AC', 343, 33.3333, ''),
    ('SUB-SEED-0140', 'sample01', 0, TRUE, 'AC', 335, 25.0000, ''),
    ('SUB-SEED-0140', '02', 1, FALSE, 'AC', 331, 25.0000, ''),
    ('SUB-SEED-0140', '03', 2, FALSE, 'WA', 327, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0140', '04', 3, FALSE, 'WA', 323, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0141', 'sample01', 0, TRUE, 'AC', 134, 25.0000, ''),
    ('SUB-SEED-0141', '02', 1, FALSE, 'WA', 130, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0141', '03', 2, FALSE, 'WA', 126, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0141', '04', 3, FALSE, 'WA', 122, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0142', 'sample01', 0, TRUE, 'AC', 165, 33.3333, ''),
    ('SUB-SEED-0142', '02', 1, FALSE, 'AC', 161, 33.3333, ''),
    ('SUB-SEED-0142', '03', 2, FALSE, 'AC', 157, 33.3333, ''),
    ('SUB-SEED-0143', 'sample01', 0, TRUE, 'AC', 325, 25.0000, ''),
    ('SUB-SEED-0143', '02', 1, FALSE, 'AC', 321, 25.0000, ''),
    ('SUB-SEED-0143', '03', 2, FALSE, 'AC', 317, 25.0000, ''),
    ('SUB-SEED-0143', '04', 3, FALSE, 'AC', 313, 25.0000, ''),
    ('SUB-SEED-0144', 'sample01', 0, TRUE, 'AC', 323, 25.0000, ''),
    ('SUB-SEED-0144', '02', 1, FALSE, 'AC', 319, 25.0000, ''),
    ('SUB-SEED-0144', '03', 2, FALSE, 'AC', 315, 25.0000, ''),
    ('SUB-SEED-0144', '04', 3, FALSE, 'AC', 311, 25.0000, ''),
    ('SUB-SEED-0145', 'sample01', 0, TRUE, 'MLE', 324, 0.0000, ''),
    ('SUB-SEED-0145', '02', 1, FALSE, 'MLE', 320, 0.0000, ''),
    ('SUB-SEED-0145', '03', 2, FALSE, 'MLE', 316, 0.0000, ''),
    ('SUB-SEED-0146', 'sample01', 0, TRUE, 'AC', 111, 33.3333, ''),
    ('SUB-SEED-0146', '02', 1, FALSE, 'AC', 107, 33.3333, ''),
    ('SUB-SEED-0146', '03', 2, FALSE, 'AC', 103, 33.3333, ''),
    ('SUB-SEED-0147', 'sample01', 0, TRUE, 'WA', 177, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0147', '02', 1, FALSE, 'WA', 173, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0147', '03', 2, FALSE, 'WA', 169, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0148', 'sample01', 0, TRUE, 'AC', 240, 33.3333, ''),
    ('SUB-SEED-0148', '02', 1, FALSE, 'WA', 236, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0148', '03', 2, FALSE, 'WA', 232, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0149', 'sample01', 0, TRUE, 'WA', 44, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0149', '02', 1, FALSE, 'WA', 40, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0149', '03', 2, FALSE, 'WA', 36, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0149', '04', 3, FALSE, 'WA', 32, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0150', 'sample01', 0, TRUE, 'AC', 59, 33.3333, ''),
    ('SUB-SEED-0150', '02', 1, FALSE, 'AC', 55, 33.3333, ''),
    ('SUB-SEED-0150', '03', 2, FALSE, 'AC', 51, 33.3333, ''),
    ('SUB-SEED-0151', 'sample01', 0, TRUE, 'AC', 256, 33.3333, ''),
    ('SUB-SEED-0151', '02', 1, FALSE, 'WA', 252, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0151', '03', 2, FALSE, 'WA', 248, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0152', 'sample01', 0, TRUE, 'AC', 130, 33.3333, ''),
    ('SUB-SEED-0152', '02', 1, FALSE, 'WA', 126, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0152', '03', 2, FALSE, 'WA', 122, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0153', 'sample01', 0, TRUE, 'AC', 66, 25.0000, ''),
    ('SUB-SEED-0153', '02', 1, FALSE, 'AC', 62, 25.0000, ''),
    ('SUB-SEED-0153', '03', 2, FALSE, 'AC', 58, 25.0000, ''),
    ('SUB-SEED-0153', '04', 3, FALSE, 'AC', 54, 25.0000, ''),
    ('SUB-SEED-0154', 'sample01', 0, TRUE, 'WA', 49, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0154', '02', 1, FALSE, 'WA', 45, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0154', '03', 2, FALSE, 'WA', 41, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0154', '04', 3, FALSE, 'WA', 37, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0155', 'sample01', 0, TRUE, 'AC', 327, 33.3333, ''),
    ('SUB-SEED-0155', '02', 1, FALSE, 'AC', 323, 33.3333, ''),
    ('SUB-SEED-0155', '03', 2, FALSE, 'AC', 319, 33.3333, ''),
    ('SUB-SEED-0156', 'sample01', 0, TRUE, 'AC', 157, 33.3333, ''),
    ('SUB-SEED-0156', '02', 1, FALSE, 'AC', 153, 33.3333, ''),
    ('SUB-SEED-0156', '03', 2, FALSE, 'WA', 149, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0157', 'sample01', 0, TRUE, 'AC', 82, 33.3333, ''),
    ('SUB-SEED-0157', '02', 1, FALSE, 'AC', 78, 33.3333, ''),
    ('SUB-SEED-0157', '03', 2, FALSE, 'WA', 74, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0158', 'sample01', 0, TRUE, 'AC', 1802, 33.3333, ''),
    ('SUB-SEED-0158', '02', 1, FALSE, 'TLE', 1798, 0.0000, ''),
    ('SUB-SEED-0158', '03', 2, FALSE, 'TLE', 1794, 0.0000, ''),
    ('SUB-SEED-0159', 'sample01', 0, TRUE, 'AC', 302, 33.3333, ''),
    ('SUB-SEED-0159', '02', 1, FALSE, 'AC', 298, 33.3333, ''),
    ('SUB-SEED-0159', '03', 2, FALSE, 'AC', 294, 33.3333, ''),
    ('SUB-SEED-0160', 'sample01', 0, TRUE, 'AC', 349, 25.0000, ''),
    ('SUB-SEED-0160', '02', 1, FALSE, 'AC', 345, 25.0000, ''),
    ('SUB-SEED-0160', '03', 2, FALSE, 'AC', 341, 25.0000, ''),
    ('SUB-SEED-0160', '04', 3, FALSE, 'AC', 337, 25.0000, ''),
    ('SUB-SEED-0161', 'sample01', 0, TRUE, 'AC', 298, 25.0000, ''),
    ('SUB-SEED-0161', '02', 1, FALSE, 'AC', 294, 25.0000, ''),
    ('SUB-SEED-0161', '03', 2, FALSE, 'AC', 290, 25.0000, ''),
    ('SUB-SEED-0161', '04', 3, FALSE, 'AC', 286, 25.0000, ''),
    ('SUB-SEED-0162', 'sample01', 0, TRUE, 'AC', 71, 25.0000, ''),
    ('SUB-SEED-0162', '02', 1, FALSE, 'AC', 67, 25.0000, ''),
    ('SUB-SEED-0162', '03', 2, FALSE, 'AC', 63, 25.0000, ''),
    ('SUB-SEED-0162', '04', 3, FALSE, 'WA', 59, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0163', 'sample01', 0, TRUE, 'RE', 340, 0.0000, ''),
    ('SUB-SEED-0163', '02', 1, FALSE, 'RE', 336, 0.0000, ''),
    ('SUB-SEED-0163', '03', 2, FALSE, 'RE', 332, 0.0000, ''),
    ('SUB-SEED-0163', '04', 3, FALSE, 'RE', 328, 0.0000, ''),
    ('SUB-SEED-0164', 'sample01', 0, TRUE, 'AC', 144, 33.3333, ''),
    ('SUB-SEED-0164', '02', 1, FALSE, 'AC', 140, 33.3333, ''),
    ('SUB-SEED-0164', '03', 2, FALSE, 'AC', 136, 33.3333, ''),
    ('SUB-SEED-0165', 'sample01', 0, TRUE, 'AC', 353, 33.3333, ''),
    ('SUB-SEED-0165', '02', 1, FALSE, 'WA', 349, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0165', '03', 2, FALSE, 'WA', 345, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0166', 'sample01', 0, TRUE, 'AC', 99, 25.0000, ''),
    ('SUB-SEED-0166', '02', 1, FALSE, 'AC', 95, 25.0000, ''),
    ('SUB-SEED-0166', '03', 2, FALSE, 'AC', 91, 25.0000, ''),
    ('SUB-SEED-0166', '04', 3, FALSE, 'AC', 87, 25.0000, ''),
    ('SUB-SEED-0167', 'sample01', 0, TRUE, 'AC', 325, 33.3333, ''),
    ('SUB-SEED-0167', '02', 1, FALSE, 'AC', 321, 33.3333, ''),
    ('SUB-SEED-0167', '03', 2, FALSE, 'WA', 317, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0168', 'sample01', 0, TRUE, 'AC', 84, 25.0000, ''),
    ('SUB-SEED-0168', '02', 1, FALSE, 'AC', 80, 25.0000, ''),
    ('SUB-SEED-0168', '03', 2, FALSE, 'WA', 76, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0168', '04', 3, FALSE, 'WA', 72, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0169', 'sample01', 0, TRUE, 'AC', 93, 33.3333, ''),
    ('SUB-SEED-0169', '02', 1, FALSE, 'AC', 89, 33.3333, ''),
    ('SUB-SEED-0169', '03', 2, FALSE, 'AC', 85, 33.3333, ''),
    ('SUB-SEED-0170', 'sample01', 0, TRUE, 'WA', 171, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0170', '02', 1, FALSE, 'WA', 167, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0170', '03', 2, FALSE, 'WA', 163, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0171', 'sample01', 0, TRUE, 'AC', 261, 25.0000, ''),
    ('SUB-SEED-0171', '02', 1, FALSE, 'AC', 257, 25.0000, ''),
    ('SUB-SEED-0171', '03', 2, FALSE, 'WA', 253, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0171', '04', 3, FALSE, 'WA', 249, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0173', 'sample01', 0, TRUE, 'WA', 66, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0173', '02', 1, FALSE, 'WA', 62, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0173', '03', 2, FALSE, 'WA', 58, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0173', '04', 3, FALSE, 'WA', 54, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0174', 'sample01', 0, TRUE, 'RE', 167, 0.0000, ''),
    ('SUB-SEED-0174', '02', 1, FALSE, 'RE', 163, 0.0000, ''),
    ('SUB-SEED-0174', '03', 2, FALSE, 'RE', 159, 0.0000, ''),
    ('SUB-SEED-0175', 'sample01', 0, TRUE, 'RE', 201, 0.0000, ''),
    ('SUB-SEED-0175', '02', 1, FALSE, 'RE', 197, 0.0000, ''),
    ('SUB-SEED-0175', '03', 2, FALSE, 'RE', 193, 0.0000, ''),
    ('SUB-SEED-0175', '04', 3, FALSE, 'RE', 189, 0.0000, ''),
    ('SUB-SEED-0176', 'sample01', 0, TRUE, 'AC', 1638, 25.0000, ''),
    ('SUB-SEED-0176', '02', 1, FALSE, 'AC', 1634, 25.0000, ''),
    ('SUB-SEED-0176', '03', 2, FALSE, 'TLE', 1630, 0.0000, ''),
    ('SUB-SEED-0176', '04', 3, FALSE, 'TLE', 1626, 0.0000, ''),
    ('SUB-SEED-0177', 'sample01', 0, TRUE, 'AC', 149, 25.0000, ''),
    ('SUB-SEED-0177', '02', 1, FALSE, 'AC', 145, 25.0000, ''),
    ('SUB-SEED-0177', '03', 2, FALSE, 'AC', 141, 25.0000, ''),
    ('SUB-SEED-0177', '04', 3, FALSE, 'AC', 137, 25.0000, ''),
    ('SUB-SEED-0178', 'sample01', 0, TRUE, 'RE', 244, 0.0000, ''),
    ('SUB-SEED-0178', '02', 1, FALSE, 'RE', 240, 0.0000, ''),
    ('SUB-SEED-0178', '03', 2, FALSE, 'RE', 236, 0.0000, ''),
    ('SUB-SEED-0181', 'sample01', 0, TRUE, 'WA', 312, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0181', '02', 1, FALSE, 'WA', 308, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0181', '03', 2, FALSE, 'WA', 304, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0182', 'sample01', 0, TRUE, 'WA', 195, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0182', '02', 1, FALSE, 'WA', 191, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0182', '03', 2, FALSE, 'WA', 187, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0182', '04', 3, FALSE, 'WA', 183, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0183', 'sample01', 0, TRUE, 'WA', 67, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0183', '02', 1, FALSE, 'WA', 63, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0183', '03', 2, FALSE, 'WA', 59, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0184', 'sample01', 0, TRUE, 'AC', 229, 33.3333, ''),
    ('SUB-SEED-0184', '02', 1, FALSE, 'AC', 225, 33.3333, ''),
    ('SUB-SEED-0184', '03', 2, FALSE, 'WA', 221, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0185', 'sample01', 0, TRUE, 'AC', 309, 25.0000, ''),
    ('SUB-SEED-0185', '02', 1, FALSE, 'RE', 305, 0.0000, ''),
    ('SUB-SEED-0185', '03', 2, FALSE, 'RE', 301, 0.0000, ''),
    ('SUB-SEED-0185', '04', 3, FALSE, 'RE', 297, 0.0000, ''),
    ('SUB-SEED-0186', 'sample01', 0, TRUE, 'AC', 176, 33.3333, ''),
    ('SUB-SEED-0186', '02', 1, FALSE, 'AC', 172, 33.3333, ''),
    ('SUB-SEED-0186', '03', 2, FALSE, 'AC', 168, 33.3333, ''),
    ('SUB-SEED-0187', 'sample01', 0, TRUE, 'AC', 301, 25.0000, ''),
    ('SUB-SEED-0187', '02', 1, FALSE, 'AC', 297, 25.0000, ''),
    ('SUB-SEED-0187', '03', 2, FALSE, 'AC', 293, 25.0000, ''),
    ('SUB-SEED-0187', '04', 3, FALSE, 'AC', 289, 25.0000, ''),
    ('SUB-SEED-0188', 'sample01', 0, TRUE, 'AC', 300, 33.3333, ''),
    ('SUB-SEED-0188', '02', 1, FALSE, 'WA', 296, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0188', '03', 2, FALSE, 'WA', 292, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0189', 'sample01', 0, TRUE, 'AC', 174, 25.0000, ''),
    ('SUB-SEED-0189', '02', 1, FALSE, 'WA', 170, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0189', '03', 2, FALSE, 'WA', 166, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0189', '04', 3, FALSE, 'WA', 162, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0190', 'sample01', 0, TRUE, 'AC', 223, 25.0000, ''),
    ('SUB-SEED-0190', '02', 1, FALSE, 'AC', 219, 25.0000, ''),
    ('SUB-SEED-0190', '03', 2, FALSE, 'WA', 215, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0190', '04', 3, FALSE, 'WA', 211, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0191', 'sample01', 0, TRUE, 'AC', 274, 33.3333, ''),
    ('SUB-SEED-0191', '02', 1, FALSE, 'AC', 270, 33.3333, ''),
    ('SUB-SEED-0191', '03', 2, FALSE, 'AC', 266, 33.3333, ''),
    ('SUB-SEED-0192', 'sample01', 0, TRUE, 'TLE', 1811, 0.0000, ''),
    ('SUB-SEED-0192', '02', 1, FALSE, 'TLE', 1807, 0.0000, ''),
    ('SUB-SEED-0192', '03', 2, FALSE, 'TLE', 1803, 0.0000, ''),
    ('SUB-SEED-0192', '04', 3, FALSE, 'TLE', 1799, 0.0000, ''),
    ('SUB-SEED-0193', 'sample01', 0, TRUE, 'AC', 103, 25.0000, ''),
    ('SUB-SEED-0193', '02', 1, FALSE, 'AC', 99, 25.0000, ''),
    ('SUB-SEED-0193', '03', 2, FALSE, 'WA', 95, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0193', '04', 3, FALSE, 'WA', 91, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0194', 'sample01', 0, TRUE, 'AC', 272, 33.3333, ''),
    ('SUB-SEED-0194', '02', 1, FALSE, 'WA', 268, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0194', '03', 2, FALSE, 'WA', 264, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0196', 'sample01', 0, TRUE, 'WA', 87, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0196', '02', 1, FALSE, 'WA', 83, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0196', '03', 2, FALSE, 'WA', 79, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0196', '04', 3, FALSE, 'WA', 75, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0197', 'sample01', 0, TRUE, 'TLE', 1758, 0.0000, ''),
    ('SUB-SEED-0197', '02', 1, FALSE, 'TLE', 1754, 0.0000, ''),
    ('SUB-SEED-0197', '03', 2, FALSE, 'TLE', 1750, 0.0000, ''),
    ('SUB-SEED-0198', 'sample01', 0, TRUE, 'WA', 163, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0198', '02', 1, FALSE, 'WA', 159, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0198', '03', 2, FALSE, 'WA', 155, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0199', 'sample01', 0, TRUE, 'AC', 60, 33.3333, ''),
    ('SUB-SEED-0199', '02', 1, FALSE, 'WA', 56, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0199', '03', 2, FALSE, 'WA', 52, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0200', 'sample01', 0, TRUE, 'AC', 175, 25.0000, ''),
    ('SUB-SEED-0200', '02', 1, FALSE, 'AC', 171, 25.0000, ''),
    ('SUB-SEED-0200', '03', 2, FALSE, 'WA', 167, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0200', '04', 3, FALSE, 'WA', 163, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0201', 'sample01', 0, TRUE, 'AC', 232, 33.3333, ''),
    ('SUB-SEED-0201', '02', 1, FALSE, 'AC', 228, 33.3333, ''),
    ('SUB-SEED-0201', '03', 2, FALSE, 'WA', 224, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0202', 'sample01', 0, TRUE, 'TLE', 1528, 0.0000, ''),
    ('SUB-SEED-0202', '02', 1, FALSE, 'TLE', 1524, 0.0000, ''),
    ('SUB-SEED-0202', '03', 2, FALSE, 'TLE', 1520, 0.0000, ''),
    ('SUB-SEED-0203', 'sample01', 0, TRUE, 'AC', 192, 25.0000, ''),
    ('SUB-SEED-0203', '02', 1, FALSE, 'AC', 188, 25.0000, ''),
    ('SUB-SEED-0203', '03', 2, FALSE, 'AC', 184, 25.0000, ''),
    ('SUB-SEED-0203', '04', 3, FALSE, 'WA', 180, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0204', 'sample01', 0, TRUE, 'AC', 145, 33.3333, ''),
    ('SUB-SEED-0204', '02', 1, FALSE, 'AC', 141, 33.3333, ''),
    ('SUB-SEED-0204', '03', 2, FALSE, 'WA', 137, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0206', 'sample01', 0, TRUE, 'WA', 39, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0206', '02', 1, FALSE, 'WA', 35, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0206', '03', 2, FALSE, 'WA', 31, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0208', 'sample01', 0, TRUE, 'AC', 82, 25.0000, ''),
    ('SUB-SEED-0208', '02', 1, FALSE, 'WA', 78, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0208', '03', 2, FALSE, 'WA', 74, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0208', '04', 3, FALSE, 'WA', 70, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0209', 'sample01', 0, TRUE, 'WA', 255, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0209', '02', 1, FALSE, 'WA', 251, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0209', '03', 2, FALSE, 'WA', 247, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0209', '04', 3, FALSE, 'WA', 243, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0210', 'sample01', 0, TRUE, 'AC', 1664, 33.3333, ''),
    ('SUB-SEED-0210', '02', 1, FALSE, 'TLE', 1660, 0.0000, ''),
    ('SUB-SEED-0210', '03', 2, FALSE, 'TLE', 1656, 0.0000, ''),
    ('SUB-SEED-0211', 'sample01', 0, TRUE, 'AC', 99, 25.0000, ''),
    ('SUB-SEED-0211', '02', 1, FALSE, 'AC', 95, 25.0000, ''),
    ('SUB-SEED-0211', '03', 2, FALSE, 'WA', 91, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0211', '04', 3, FALSE, 'WA', 87, 0.0000, 'lệch tại giá trị thứ 1'),
    ('SUB-SEED-0212', 'sample01', 0, TRUE, 'AC', 93, 33.3333, ''),
    ('SUB-SEED-0212', '02', 1, FALSE, 'RE', 89, 0.0000, ''),
    ('SUB-SEED-0212', '03', 2, FALSE, 'RE', 85, 0.0000, ''),
    ('SUB-SEED-0213', 'sample01', 0, TRUE, 'MLE', 257, 0.0000, ''),
    ('SUB-SEED-0213', '02', 1, FALSE, 'MLE', 253, 0.0000, ''),
    ('SUB-SEED-0213', '03', 2, FALSE, 'MLE', 249, 0.0000, '')
ON DUPLICATE KEY UPDATE verdict = VALUES(verdict);

COMMIT;

-- Kiem tra nhanh sau khi nap:
SELECT
    (SELECT COUNT(*) FROM users)             AS so_tai_khoan,
    (SELECT COUNT(*) FROM submissions)       AS so_bai_nop,
    (SELECT COUNT(*) FROM test_case_results) AS so_ket_qua_test;
