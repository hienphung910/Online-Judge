// V294 - QHD tong tren tap cha (SOS DP cho superset): dem va tim min
// cnt[x] = so tho co a_i chua moi bit cua x, mn[x] = tien cong nho nhat cua ho.
// Ban dau chi dat tai dung mask a_i; xu ly lan luot tung bit b:
// mask chua co bit b nhan them ket qua cua mask | (1 << b).
#include <bits/stdc++.h>
using namespace std;

const int B = 16;
const int INF = INT_MAX;

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    vector<int> cnt(1 << B, 0), mn(1 << B, INF);
    for (int i = 0; i < n; i++) {
        int a, c;
        scanf("%d %d", &a, &c);
        cnt[a]++;
        mn[a] = min(mn[a], c);
    }
    for (int b = 0; b < B; b++)
        for (int mask = 0; mask < (1 << B); mask++)
            if (!(mask >> b & 1)) {
                cnt[mask] += cnt[mask | (1 << b)];
                mn[mask] = min(mn[mask], mn[mask | (1 << b)]);
            }
    for (int k = 0; k < q; k++) {
        int x;
        scanf("%d", &x);
        printf("%d %d\n", cnt[x], cnt[x] ? mn[x] : -1);
    }
    return 0;
}
