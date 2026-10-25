// V063 - Sang phi Euler cho moi b <= 10^6, cong don phi(2) + ... + phi(n)
#include <bits/stdc++.h>
using namespace std;

const int N = 1000000;
int phi[N + 1];
long long total[N + 1];   // total[n] = phi(2) + ... + phi(n)

int main() {
    for (int i = 0; i <= N; i++) phi[i] = i;
    for (int p = 2; p <= N; p++)
        if (phi[p] == p)                       // p chua bi sua => p nguyen to
            for (int m = p; m <= N; m += p) phi[m] -= phi[m] / p;
    for (int b = 2; b <= N; b++) total[b] = total[b - 1] + phi[b];

    int q;
    scanf("%d", &q);
    while (q--) {
        int n;
        scanf("%d", &n);
        printf("%lld\n", total[n]);
    }
    return 0;
}
