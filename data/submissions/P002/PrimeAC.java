import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/** Kiem tra nguyen to bang sang can bac hai -> ky vong AC. */
public class PrimeAC {

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
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            long n = Long.parseLong(br.readLine().trim());
            sb.append(isPrime(n) ? "YES" : "NO").append(System.lineSeparator());
        }
        System.out.print(sb);
    }
}
