import java.util.Scanner;

/** Vong lap vo han -> ky vong TLE, tien trinh bi Judge cuong che dung. */
public class SumTLE {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        long sum = 0;
        while (true) {
            sum += a + b;
            if (sum == Long.MIN_VALUE) break;   // thuc te khong bao gio thoat
        }
    }
}
