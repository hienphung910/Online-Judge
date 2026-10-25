// V098 - Quy hoach dong tren luoi: di sang phai / xuong duoi, lay nhieu nam nhat
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> g(n);
    for (auto &s : g) cin >> s;
    const int NO = -1;   // o khong toi duoc
    vector<vector<int>> dp(n, vector<int>(m, NO));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (g[i][j] == '#') continue;
            int best = NO;
            if (i == 0 && j == 0) best = 0;
            if (i > 0) best = max(best, dp[i - 1][j]);
            if (j > 0) best = max(best, dp[i][j - 1]);
            if (best == NO) continue;
            dp[i][j] = best + (g[i][j] == 'o' ? 1 : 0);
        }
    cout << dp[n - 1][m - 1] << "\n";
    return 0;
}
