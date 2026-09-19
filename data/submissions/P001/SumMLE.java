import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Cap phat bo nho khong ngung -> vuot -Xmx do Judge dat ra -> ky vong MLE.
 * Judge nhan ra MLE nho thong bao OutOfMemoryError trong stderr.
 */
public class SumMLE {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();

        List<long[]> blocks = new ArrayList<>();
        while (true) {
            long[] block = new long[1_000_000];   // 8 MB moi khoi
            block[0] = a + b;
            blocks.add(block);
        }
    }
}
