// V053 - Nguoi giao hang: quay lui thu thu tu ghe khach, nhanh can bang tong canh ra ngan nhat
#include <bits/stdc++.h>
using namespace std;

int n;
long long c[13][13], raMin[13], best;
bool daGhe[13];

void di(int u, int soDaGhe, long long daDi, long long conLaiMin) {
    // conLaiMin: tong raMin cua cac khach chua ghe
    if (daDi + raMin[u] + conLaiMin >= best) return;          // nhanh can: khong the tot hon
    if (soDaGhe == n) { best = min(best, daDi + c[u][0]); return; }
    for (int v = 1; v < n; v++) {
        if (daGhe[v]) continue;
        daGhe[v] = true;
        di(v, soDaGhe + 1, daDi + c[u][v], conLaiMin - raMin[v]);
        daGhe[v] = false;
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cin >> c[i][j];
    if (n == 1) { cout << 0 << "\n"; return 0; }
    long long tong = 0;
    for (int i = 0; i < n; i++) {
        raMin[i] = LLONG_MAX;
        for (int j = 0; j < n; j++)
            if (j != i) raMin[i] = min(raMin[i], c[i][j]);
        if (i > 0) tong += raMin[i];
    }
    best = LLONG_MAX;
    daGhe[0] = true;
    di(0, 1, 0, tong);
    cout << best << "\n";
    return 0;
}
