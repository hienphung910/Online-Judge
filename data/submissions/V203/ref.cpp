// V203 - Phan cong cong viec bang QHD bitmask, O(2^n * n)
// dp[mask] = chi phi nho nhat khi popcount(mask) ban dau tien da nhan cac viec trong mask.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int n;
    cin >> n;
    vector<vector<ll>> c(n, vector<ll>(n));
    for (auto &row : c)
        for (auto &v : row) cin >> v;

    const ll INF = LLONG_MAX / 4;
    vector<ll> dp(1 << n, INF);
    dp[0] = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        if (dp[mask] == INF) continue;
        int i = __builtin_popcount(mask);       // ban tiep theo can nhan viec
        if (i == n) continue;
        for (int j = 0; j < n; j++) {
            if ((mask >> j & 1) || c[i][j] < 0) continue;   // viec da co nguoi lam / ban i khong lam duoc
            int nm = mask | (1 << j);
            dp[nm] = min(dp[nm], dp[mask] + c[i][j]);
        }
    }
    ll ans = dp[(1 << n) - 1];
    cout << (ans == INF ? -1 : ans) << "\n";
    return 0;
}
