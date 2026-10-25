// V103 - Ba lo 0/1: dp mot chieu, duyet khoi luong giam dan
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, W;
    cin >> n >> W;
    vector<long long> dp(W + 1, 0);
    for (int i = 0; i < n; i++) {
        int w;
        long long v;
        cin >> w >> v;
        for (int c = W; c >= w; c--)   // giam dan: moi mon dung toi da 1 lan
            dp[c] = max(dp[c], dp[c - w] + v);
    }
    cout << dp[W] << "\n";
    return 0;
}
