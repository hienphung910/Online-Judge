// V247 - Chia de tri dem doan con co tong trong [L, R]
// Goi P la mang tong tien to P[0..n]. Doan (i, j] hop le <=> L <= P[j] - P[i] <= R, i < j.
// Dem cap (i, j) bang chia de tri kieu sap xep tron: cap nam o hai nua khac nhau
// duoc dem bang hai con tro khi ca hai nua da sap xep.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll L, R;
vector<ll> P, tmp;

ll solve(int lo, int hi) {           // dem cap trong P[lo..hi), sau do sap xep doan nay
    if (hi - lo <= 1) return 0;
    int mid = (lo + hi) / 2;
    ll cnt = solve(lo, mid) + solve(mid, hi);
    int a = lo, b = lo;              // [a, b) = cac P[i] ben trai nam trong [P[j] - R, P[j] - L]
    for (int j = mid; j < hi; j++) {
        while (b < mid && P[b] <= P[j] - L) b++;
        while (a < mid && P[a] < P[j] - R) a++;
        cnt += b - a;
    }
    merge(P.begin() + lo, P.begin() + mid, P.begin() + mid, P.begin() + hi, tmp.begin() + lo);
    copy(tmp.begin() + lo, tmp.begin() + hi, P.begin() + lo);
    return cnt;
}

int main() {
    int n;
    cin >> n >> L >> R;
    P.assign(n + 1, 0);
    tmp.assign(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        ll x;
        cin >> x;
        P[i] = P[i - 1] + x;
    }
    cout << solve(0, n + 1) << "\n";
    return 0;
}
