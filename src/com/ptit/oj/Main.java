package com.ptit.oj;

import com.ptit.oj.core.ConsoleJudgeListener;
import com.ptit.oj.database.DatabaseConfig;
import com.ptit.oj.database.MySqlDatabaseManager;
import com.ptit.oj.exception.DataAccessException;
import com.ptit.oj.exception.ProblemLoadException;
import com.ptit.oj.service.AuthService;
import com.ptit.oj.service.JudgeService;
import com.ptit.oj.service.PasswordService;
import com.ptit.oj.test.IntegrationTests;
import com.ptit.oj.ui.ConsoleApp;
import com.ptit.oj.web.ApiServer;

import java.io.FileDescriptor;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.io.UnsupportedEncodingException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Diem vao chuong trinh.
 *
 * Cach chay:
 *   java -cp "out;lib/*" com.ptit.oj.Main                -> menu tuong tac (can dang nhap)
 *   java -cp "out;lib/*" com.ptit.oj.Main --demo         -> cham loat bai nop mau (bo nho tam)
 *   java -cp "out;lib/*" com.ptit.oj.Main --selftest     -> cham va doi chieu verdict ky vong
 *   java -cp "out;lib/*" com.ptit.oj.Main --apitest      -> kiem thu tich hop API + MySQL
 *   java -cp "out;lib/*" com.ptit.oj.Main --serve        -> mo giao dien web tai http://localhost:8080
 *   java -cp "out;lib/*" com.ptit.oj.Main --serve=9000   -> chon cong khac
 *   java -cp "out;lib/*" com.ptit.oj.Main --no-db        -> menu console, kho du lieu RAM
 *   java -cp "out;lib/*" com.ptit.oj.Main --serve --no-db -> giao dien web, kho du lieu RAM
 *   java -cp "out;lib/*" com.ptit.oj.Main --data=E:\duong\dan\data
 *   java -cp "out;lib/*" com.ptit.oj.Main --db-url=jdbc:mysql://localhost:3306/online_judge?...
 *
 * Cau hinh MySQL lay tu BIEN MOI TRUONG (xem .env.example):
 *   OJ_DB_URL / OJ_DB_USER / OJ_DB_PASSWORD
 * Mat khau KHONG BAO GIO nhan qua dong lenh de khong bi luu vao lich su shell.
 *
 * Che do --demo va --selftest dung kho du lieu trong BO NHO nen khong can MySQL
 * va khong lam ban lich su that.
 *
 * Co --no-db mo rong y do tren cho CA menu console va giao dien web: day du tinh
 * nang (dang ky, dang nhap, phan quyen, nop bai, bang xep hang, thong ke, quan tri
 * de bai) nhung tai khoan va lich su nop bai nam trong RAM nen mat khi tat chuong
 * trinh. Lam duoc vi ConsoleApp va ApiServer chi phu thuoc JudgeService chu khong
 * biet gi ve MySQL - doi kho du lieu la doi mot cho duy nhat o day.
 */
public class Main {

    private static final int DEFAULT_PORT = 8080;

    /** Mat khau cua cac tai khoan mau, chi dung lan dau khi bang users con trong. */
    private static final String SEED_PASSWORD_ENV = "OJ_SEED_PASSWORD";
    private static final String DEFAULT_SEED_PASSWORD = "ptit@2026";

    public static void main(String[] args) {
        forceUtf8Output();

        boolean demoMode = false;
        boolean selfTest = false;
        boolean apiTest = false;
        boolean serveMode = false;
        boolean noDatabase = false;
        int port = DEFAULT_PORT;
        Path dataDir = Paths.get("data");
        Path webRoot = Paths.get("frontend", "dist");
        String databaseUrl = null;

        for (String arg : args) {
            if (arg.equals("--demo")) {
                demoMode = true;
            } else if (arg.equals("--selftest")) {
                selfTest = true;
            } else if (arg.equals("--apitest")) {
                apiTest = true;
            } else if (arg.equals("--serve")) {
                serveMode = true;
            } else if (arg.equals("--no-db")) {
                noDatabase = true;
            } else if (arg.startsWith("--serve=")) {
                serveMode = true;
                port = parsePort(arg.substring("--serve=".length()), DEFAULT_PORT);
            } else if (arg.startsWith("--data=")) {
                dataDir = Paths.get(arg.substring("--data=".length()));
            } else if (arg.startsWith("--web=")) {
                webRoot = Paths.get(arg.substring("--web=".length()));
            } else if (arg.startsWith("--db-url=")) {
                databaseUrl = arg.substring("--db-url=".length());
            } else {
                System.out.println("Tham số không hiểu: " + arg);
            }
        }

        if (apiTest) {
            if (noDatabase) {
                // --apitest kiem thu chinh tang JDBC nen bo CSDL di thi khong con gi de do.
                System.out.println("--apitest kiểm thử chính tầng MySQL nên không dùng được với --no-db.");
                System.out.println("Muốn chạy mà không cần cơ sở dữ liệu thì dùng: --selftest");
                System.exit(2);
                return;
            }
            System.exit(IntegrationTests.runAll(dataDir) == 0 ? 0 : 1);
            return;
        }

        if (!Files.isDirectory(dataDir)) {
            System.out.println("Không tìm thấy thư mục dữ liệu: " + dataDir.toAbsolutePath());
            System.out.println("Hãy chạy chương trình từ thư mục gốc của project (nơi có folder data).");
            return;
        }

        try {
            if (selfTest || demoMode) {
                // Kho du lieu tam: khong can MySQL, khong dung toi CSDL that.
                JudgeService service = JudgeService.inMemory(dataDir);
                service.getAuth().seedSampleUsersIfEmpty(DEFAULT_SEED_PASSWORD);
                ConsoleApp app = new ConsoleApp(service);
                app.loadData();
                app.useAccount(service.findUser("hiennm").orElse(null));
                if (selfTest) {
                    int mismatch = app.runSelfTest();
                    System.exit(mismatch == 0 ? 0 : 1);   // tien cho viec kiem tra tu dong
                } else {
                    app.runDemoMode();
                }
                return;
            }

            JudgeService service;
            if (noDatabase) {
                // Day du tinh nang, chi khac cho luu la RAM. Dung PasswordService()
                // mac dinh (120 000 vong PBKDF2) de dang nhap chay dung nhu ban that.
                printNoDatabaseBanner();
                service = JudgeService.inMemory(dataDir, new PasswordService());
            } else {
                MySqlDatabaseManager database = connectToMySql(databaseUrl);
                if (database == null) return;
                service = JudgeService.mysql(dataDir, database);
            }

            if (serveMode) {
                runServer(service, webRoot, port);
                return;
            }

            prepareAccounts(service);
            ConsoleApp app = new ConsoleApp(service);
            app.loadData();
            app.runInteractive();
        } catch (ProblemLoadException e) {
            System.out.println("Lỗi nạp đề bài: " + e.getMessage());
        } catch (DataAccessException e) {
            System.out.println("Lỗi cơ sở dữ liệu: " + e.getMessage());
        }
    }

    /**
     * Doc cau hinh tu bien moi truong, mo ket noi va kiem tra bang SELECT 1.
     * Tra ve null (kem huong dan) neu thieu cau hinh hoac khong ket noi duoc.
     */
    private static MySqlDatabaseManager connectToMySql(String overrideUrl) {
        DatabaseConfig config;
        try {
            config = DatabaseConfig.fromEnvironment().withUrl(overrideUrl);
        } catch (DatabaseConfig.MissingConfigException e) {
            System.out.println(e.getMessage());
            return null;
        }

        MySqlDatabaseManager database = new MySqlDatabaseManager(
                config.getUrl(), config.getUser(), config.getPassword());
        try {
            database.testConnection();
        } catch (DataAccessException e) {
            System.out.println("Không kết nối được MySQL.");
            System.out.println("  " + e.getMessage());
            System.out.println("  Xem hướng dẫn tạo cơ sở dữ liệu ở database/mysql/01_create_database.sql");
            return null;
        }
        System.out.println("MySQL: " + database.getSafeUrl() + " (user " + database.getUser() + ")");
        return database;
    }

    /**
     * Che do web: nap du lieu roi mo may chu HTTP, chay den khi bi dung.
     *
     * Nhan san JudgeService chu khong tu tao, nho vay dung duoc cho ca kho MySQL
     * va kho RAM (--no-db) ma khong phai viet hai ban ham nay.
     */
    private static void runServer(JudgeService service, Path webRoot, int port) {
        service.addJudgeListener(new ConsoleJudgeListener(true));   // log tien trinh cham ra terminal
        service.loadData();
        prepareAccounts(service);
        System.out.printf("Đã nạp %d bài tập, %d tài khoản.%n",
                service.getProblems().size(), service.getUsers().size());

        ApiServer server = new ApiServer(service, port, webRoot);
        try {
            server.start();
        } catch (IOException e) {
            System.out.println("Không mở được cổng " + port + ": " + e.getMessage());
            System.out.println("Cổng có thể đang bị chiếm - thử --serve=8081");
            return;
        }
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            System.out.println("\nĐang dừng máy chủ...");
            server.stop();
        }));
        try {
            Thread.currentThread().join();   // giu tien trinh song cho HttpServer phuc vu
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            server.stop();
        }
    }

    /**
     * Chuan bi tai khoan cho lan chay dau tien:
     *   - tao tai khoan mau (neu bang users con hoan toan trong),
     *   - tao tai khoan ADMIN va in mat khau DUNG MOT LAN neu phai sinh ngau nhien.
     * Cac lan chay sau khong dat lai mat khau cua ai ca.
     */
    private static void prepareAccounts(JudgeService service) {
        String seedPassword = System.getenv(SEED_PASSWORD_ENV);
        if (seedPassword == null || seedPassword.trim().isEmpty()) {
            seedPassword = DEFAULT_SEED_PASSWORD;
        }
        if (service.getAuth().seedSampleUsersIfEmpty(seedPassword)) {
            System.out.println("Đã tạo 4 tài khoản mẫu (hiennm, lananh, tuanpv, gvthanh).");
            System.out.println("  Mật khẩu mẫu: " + seedPassword
                    + "   (đặt biến môi trường " + SEED_PASSWORD_ENV + " để dùng mật khẩu khác)");
        }

        AuthService.BootstrapResult admin = service.getAuth().bootstrapAdmin();
        if (!admin.isCreated()) return;

        System.out.println();
        System.out.println("==================================================");
        System.out.println(" ĐÃ TẠO TÀI KHOẢN QUẢN TRỊ");
        System.out.println("   Tên đăng nhập: " + admin.getAdmin().getUsername());
        if (admin.getGeneratedPassword() != null) {
            System.out.println("   Mật khẩu     : " + admin.getGeneratedPassword());
            System.out.println("   (chỉ hiện DUY NHẤT lần này - hãy chép lại ngay;");
            System.out.println("    cơ sở dữ liệu chỉ lưu chuỗi băm, không lưu mật khẩu)");
        } else {
            System.out.println("   Mật khẩu     : lấy từ biến môi trường "
                    + AuthService.ADMIN_PASSWORD_ENV);
        }
        System.out.println("==================================================");
        System.out.println();
    }

    /** Noi ro ngay tu dau rang du lieu se mat khi tat, de khong ai hieu nham. */
    private static void printNoDatabaseBanner() {
        System.out.println();
        System.out.println("==================================================");
        System.out.println(" CHẾ ĐỘ KHÔNG CƠ SỞ DỮ LIỆU (--no-db)");
        System.out.println("   Đầy đủ tính năng, nhưng tài khoản và lịch sử nộp");
        System.out.println("   bài chỉ nằm trong RAM: TẮT CHƯƠNG TRÌNH LÀ MẤT.");
        System.out.println("   Đề bài vẫn đọc/ghi ở data/problems/ nên còn nguyên.");
        System.out.println("   Muốn mật khẩu admin cố định thì đặt biến môi trường");
        System.out.println("   " + AuthService.ADMIN_PASSWORD_ENV + " trước khi chạy.");
        System.out.println("==================================================");
        System.out.println();
    }

    private static int parsePort(String text, int fallback) {
        try {
            int p = Integer.parseInt(text.trim());
            if (p < 1 || p > 65535) throw new NumberFormatException();
            return p;
        } catch (NumberFormatException e) {
            System.out.println("Cổng không hợp lệ (" + text + "), dùng mặc định " + fallback);
            return fallback;
        }
    }

    /** Bat buoc stdout dung UTF-8 de khong bi loi font khi in tieng Viet tren Windows. */
    private static void forceUtf8Output() {
        try {
            System.setOut(new PrintStream(new FileOutputStream(FileDescriptor.out), true, "UTF-8"));
        } catch (UnsupportedEncodingException ignored) {
            // moi JVM deu ho tro UTF-8, nhung neu that bai thi cu dung stdout mac dinh
        }
    }
}
