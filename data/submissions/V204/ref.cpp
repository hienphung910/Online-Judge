// V204 - QHD 1D/1D toi uu bang hang doi don dieu (deque), O(n)
// dp[i] = a[i] + min(dp[j]) voi i-k <= j <= i-1 (dp[0] = 0 la diem xuat phat ao).
// Dap an = min dp[j] voi n-k+1 <= j <= n.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int n, k;
    cin >> n >> k;
    vector<ll> a(n + 1), dp(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    deque<int> dq;          // chi so j, dp[j] tang dan tu dau den cuoi
    dp[0] = 0;
    dq.push_back(0);
    for (int i = 1; i <= n; i++) {
        while (dq.front() < i - k) dq.pop_front();          // bo j qua xa
        dp[i] = a[i] + dp[dq.front()];
        while (!dq.empty() && dp[dq.back()] >= dp[i]) dq.pop_back();
        dq.push_back(i);
    }
    ll ans = LLONG_MAX;
    for (int j = n - k + 1; j <= n; j++) ans = min(ans, dp[j]);
    cout << ans << "\n";
    return 0;
}
