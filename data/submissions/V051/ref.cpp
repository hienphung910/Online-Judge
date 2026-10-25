// V051 - Duyet moi tap con bang bitmask, loai tap co cap cai nhau hoac vuot ngan sach
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    long long B;
    cin >> n >> m >> B;
    vector<long long> w(n), v(n);
    for (int i = 0; i < n; i++) cin >> w[i] >> v[i];
    vector<int> ghet(n, 0);                 // ghet[i]: bitmask nhung ban cai nhau voi i
    for (int k = 0; k < m; k++) {
        int x, y;
        cin >> x >> y;
        x--; y--;
        ghet[x] |= 1 << y;
        ghet[y] |= 1 << x;
    }
    long long best = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        long long tongW = 0, tongV = 0;
        bool hopLe = true;
        for (int i = 0; i < n && hopLe; i++) {
            if (!(mask >> i & 1)) continue;
            if (mask & ghet[i]) hopLe = false;
            tongW += w[i];
            tongV += v[i];
        }
        if (hopLe && tongW <= B) best = max(best, tongV);
    }
    cout << best << "\n";
    return 0;
}
