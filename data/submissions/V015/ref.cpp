// V015 - Nguoi du lich (TSP) bang QHD bitmask, O(2^n * n^2)
// dp[mask][i] = chi phi nho nhat xuat phat tu thanh pho 0, da tham tap mask, dang dung o i.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<vector<ll>> c(n, vector<ll>(n));
    for (auto &row : c)
        for (auto &v : row) cin >> v;

    const ll INF = LLONG_MAX / 4;
    int full = 1 << n;
    vector<vector<ll>> dp(full, vector<ll>(n, INF));
    dp[1][0] = 0;
    for (int mask = 1; mask < full; mask++) {
        if (!(mask & 1)) continue;              // luon chua thanh pho xuat phat
        for (int i = 0; i < n; i++) {
            if (dp[mask][i] == INF) continue;
            for (int j = 0; j < n; j++) {
                if (mask >> j & 1) continue;    // j da tham roi
                int nm = mask | (1 << j);
                dp[nm][j] = min(dp[nm][j], dp[mask][i] + c[i][j]);
            }
        }
    }
    ll best = INF;
    for (int i = 0; i < n; i++) best = min(best, dp[full - 1][i] + c[i][0]);
    cout << best << "\n";   // n = 1: dp[1][0] + c[0][0] = 0
    return 0;
}
