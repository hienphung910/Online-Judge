// V210 - QHD toi uu bao loi (convex hull trick), O(n)
// dp[i] = min_{j<i} dp[j] + (S[i] - S[j])^2 + C, S la tong tien to.
// Khai trien: dp[i] = S[i]^2 + C + min_j (-2*S[j]) * S[i] + (dp[j] + S[j]^2)
// -> moi j la mot duong thang y = m*x + b voi m = -2*S[j] giam dan, truy van x = S[i] tang dan.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct Line { ll m, b; ll val(ll x) const { return m * x + b; } };

// l2 thua (khong bao gio la min) neu giao diem cua l1, l3 nam truoc giao diem cua l1, l2
bool bad(const Line &l1, const Line &l2, const Line &l3) {
    return (l3.b - l1.b) * (l1.m - l2.m) <= (l2.b - l1.b) * (l1.m - l3.m);
}

int main() {
    int n;
    ll C;
    cin >> n >> C;
    vector<ll> S(n + 1, 0), dp(n + 1, 0);
    for (int i = 1; i <= n; i++) { ll a; cin >> a; S[i] = S[i - 1] + a; }
    deque<Line> hull;
    hull.push_back({0, 0});                     // j = 0: m = 0, b = dp[0] + 0 = 0
    for (int i = 1; i <= n; i++) {
        ll x = S[i];
        while (hull.size() >= 2 && hull[1].val(x) <= hull[0].val(x)) hull.pop_front();
        dp[i] = hull[0].val(x) + x * x + C;
        Line ln = {-2 * S[i], dp[i] + S[i] * S[i]};
        while (hull.size() >= 2 && bad(hull[hull.size() - 2], hull.back(), ln)) hull.pop_back();
        hull.push_back(ln);
    }
    cout << dp[n] << "\n";
    return 0;
}
