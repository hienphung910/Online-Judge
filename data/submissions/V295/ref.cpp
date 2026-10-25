// V295 - Cai tui gioi han so luong, tach nhi phan (binary splitting)
// c mon cung loai duoc tach thanh cac goi 1, 2, 4, ..., 2^k va mot goi phan du.
// Moi so tu 0 den c deu tao duoc tu cac goi nay -> chuyen ve cai tui 0/1.
// Do phuc tap O(W * tong log c_i).
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, W;
    cin >> n >> W;
    vector<long long> dp(W + 1, 0);   // dp[j] = lai lon nhat voi tong khoi luong <= j
    for (int i = 0; i < n; i++) {
        long long w, v, c;
        cin >> w >> v >> c;
        for (long long k = 1; c > 0; k *= 2) {
            long long take = min(k, c);       // goi gom take mon
            c -= take;
            long long ww = take * w, vv = take * v;
            for (long long j = W; j >= ww; j--)
                dp[j] = max(dp[j], dp[j - ww] + vv);
        }
    }
    cout << dp[W] << "\n";
    return 0;
}
