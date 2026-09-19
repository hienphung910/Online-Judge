import java.util.Scanner;

/** Chia cho 0 -> nem ArithmeticException, exit code khac 0 -> ky vong RE. */
public class SumRE {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        long zero = a - a;
        System.out.println((a + b) / zero);
    }
}
