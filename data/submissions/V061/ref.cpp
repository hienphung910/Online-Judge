// V061 - Sang uoc nguyen to nho nhat (spf): dem so uoc va tinh tong uoc
#include <bits/stdc++.h>
using namespace std;

const int N = 1000000;
int spf[N + 1];   // spf[x] = uoc nguyen to nho nhat cua x

int main() {
    for (int i = 2; i <= N; i++)
        if (spf[i] == 0)
            for (int j = i; j <= N; j += i)
                if (spf[j] == 0) spf[j] = i;

    int n;
    scanf("%d", &n);
    while (n--) {
        int x;
        scanf("%d", &x);
        long long cnt = 1, sum = 1;
        while (x > 1) {
            int p = spf[x], e = 0;
            long long pk = 1, s = 1;      // s = 1 + p + p^2 + ... + p^e
            while (x % p == 0) {
                x /= p;
                e++;
                pk *= p;
                s += pk;
            }
            cnt *= (e + 1);
            sum *= s;
        }
        printf("%lld %lld\n", cnt, sum);
    }
    return 0;
}
