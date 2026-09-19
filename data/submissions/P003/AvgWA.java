import java.util.Scanner;

/** Loi kinh dien: chia nguyen lam mat phan thap phan -> WA (lech qua sai so 1e-6). */
public class AvgWA {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long sum = 0;
        for (int i = 0; i < n; i++) sum += sc.nextLong();
        System.out.println(sum / n);   // chia nguyen!
    }
}
