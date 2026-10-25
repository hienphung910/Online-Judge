// V293 - Cai tui 0/1 voi hai rang buoc (khoi luong va the tich)
// dp[a][b] = tong do can thiet lon nhat khi tong khoi luong <= a, tong the tich <= b.
// Moi mon chi dung mot lan nen duyet a, b giam dan (giong cai tui 0/1 mot chieu).
#include <bits/stdc++.h>
using namespace std;

long long dp[301][301];

int main() {
    int n, W, V;
    cin >> n >> W >> V;
    for (int i = 0; i < n; i++) {
        int w, t;
        long long p;
        cin >> w >> t >> p;
        for (int a = W; a >= w; a--)
            for (int b = V; b >= t; b--)
                dp[a][b] = max(dp[a][b], dp[a - w][b - t] + p);
    }
    cout << dp[W][V] << "\n";
    return 0;
}
