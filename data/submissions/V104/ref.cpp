// V104 - Ba lo khong gioi han so luong (unbounded knapsack)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, W;
    cin >> n >> W;
    vector<int> w(n);
    vector<long long> v(n);
    for (int i = 0; i < n; i++) cin >> w[i] >> v[i];
    vector<long long> dp(W + 1, 0);
    for (int c = 1; c <= W; c++) {   // tang dan: moi loai dung nhieu lan
        dp[c] = dp[c - 1];
        for (int i = 0; i < n; i++)
            if (w[i] <= c) dp[c] = max(dp[c], dp[c - w[i]] + v[i]);
    }
    cout << dp[W] << "\n";
    return 0;
}
