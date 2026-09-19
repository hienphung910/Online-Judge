import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Thuat toan dung nhung in chu thuong (yes/no).
 * Bai P002 dung comparator "exact" nen day la WA - minh hoa vai tro cua Strategy so sanh.
 */
public class PrimeWA {

    static boolean isPrime(long n) {
        if (n < 2) return false;
        if (n % 2 == 0) return n == 2;
        for (long i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        for (int i = 0; i < t; i++) {
            long n = Long.parseLong(br.readLine().trim());
            System.out.println(isPrime(n) ? "yes" : "no");
        }
    }
}
