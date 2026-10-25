// V059 - Sang Eratosthenes + mang cong don: dem so nguyen to trong [L, R]
#include <bits/stdc++.h>
using namespace std;

const int N = 1000000;
bool composite[N + 1];
int cnt[N + 1];   // cnt[x] = so luong so nguyen to <= x

int main() {
    composite[0] = composite[1] = true;
    for (int i = 2; (long long)i * i <= N; i++)
        if (!composite[i])
            for (int j = i * i; j <= N; j += i) composite[j] = true;
    for (int i = 1; i <= N; i++) cnt[i] = cnt[i - 1] + (composite[i] ? 0 : 1);

    int q;
    scanf("%d", &q);
    while (q--) {
        int l, r;
        scanf("%d %d", &l, &r);
        printf("%d\n", cnt[r] - cnt[l - 1]);
    }
    return 0;
}
