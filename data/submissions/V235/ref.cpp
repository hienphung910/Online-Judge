// V235 - Doi chieu loi giai tham lam voi loi giai QHD (stress test) cho bai doi tien
// dp[x] = so dong xu it nhat de tra x; tham lam lay dong lon nhat truoc. Tim x nho nhat ma hai ket qua khac nhau.
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) {
        int n, X;
        cin >> n >> X;
        vector<int> c(n);
        for (auto &v : c) cin >> v;

        // loi giai chuan: quy hoach dong
        vector<int> dp(X + 1, INT_MAX);
        dp[0] = 0;
        for (int x = 1; x <= X; x++)
            for (int v : c)
                if (v <= x && dp[x - v] + 1 < dp[x]) dp[x] = dp[x - v] + 1;

        // loi giai tham lam, doi chieu lan luot x = 1, 2, ..., X
        int found = -1, g = 0;
        for (int x = 1; x <= X && found == -1; x++) {
            int rem = x, cnt = 0;
            for (int i = n - 1; i >= 0; i--) {
                cnt += rem / c[i];
                rem %= c[i];
            }
            if (cnt != dp[x]) { found = x; g = cnt; }
        }
        if (found == -1) cout << -1 << "\n";
        else cout << found << " " << g << " " << dp[found] << "\n";
    }
    return 0;
}
