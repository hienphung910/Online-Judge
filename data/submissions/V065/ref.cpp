// V065 - To hop C(n, k) mod m (m co the la hop so) bang tam giac Pascal
#include <bits/stdc++.h>
using namespace std;

const int N = 2000;
int C[N + 1][N + 1];   // C[n][k] mod m, mac dinh 0 khi k > n

int main() {
    long long m;
    int q;
    scanf("%lld %d", &m, &q);
    for (int n = 0; n <= N; n++) {
        C[n][0] = 1 % m;
        for (int k = 1; k <= n; k++)
            C[n][k] = (C[n - 1][k - 1] + (long long)C[n - 1][k]) % m;
    }
    while (q--) {
        int n, k;
        scanf("%d %d", &n, &k);
        printf("%d\n", C[n][k]);
    }
    return 0;
}
