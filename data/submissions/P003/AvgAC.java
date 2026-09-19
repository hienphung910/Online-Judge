import java.util.Locale;
import java.util.Scanner;

/** In 6 chu so thap phan -> nam trong sai so 1e-6 -> AC. */
public class AvgAC {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double sum = 0;
        for (int i = 0; i < n; i++) sum += sc.nextLong();
        System.out.printf(Locale.US, "%.6f%n", sum / n);
    }
}
