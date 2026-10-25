// V297 - Dem cap AND bang 0 bang QHD tong tren tap con (SOS DP)
// (a_i AND a_j) = 0  <=>  a_j la tap con cua ~a_i (trong B bit).
// f[m] = so the co a_j la tap con cua m; dap an cua the i la f[~a_i],
// tru 1 neu a_i = 0 (vi khi do chinh the i cung duoc dem).
#include <bits/stdc++.h>
using namespace std;

const int B = 20;
const int FULL = (1 << B) - 1;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> a(n), f(1 << B, 0);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        f[a[i]]++;
    }
    for (int b = 0; b < B; b++)
        for (int m = 0; m <= FULL; m++)
            if (m >> b & 1) f[m] += f[m ^ (1 << b)];
    for (int i = 0; i < n; i++)
        printf("%d\n", f[FULL ^ a[i]] - (a[i] == 0 ? 1 : 0));
    return 0;
}
