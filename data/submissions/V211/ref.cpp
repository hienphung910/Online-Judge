// V211 - QHD chia de tri (divide & conquer optimization), O(k * n log n)
// Sap xep toa do. dp[g][i] = chi phi nho nhat chia i xom dau thanh g nhom lien tiep,
// moi nhom dat tram o trung vi. opt[g][i] khong giam theo i nen tinh bang chia de tri.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, k;
vector<ll> x, P;                 // P = tong tien to cua x (da sap xep, chi so tu 1)
vector<ll> prv, cur;

ll cost(int l, int r) {          // tong khoang cach tu x[l..r] den trung vi
    int m = (l + r) / 2;
    ll left = x[m] * (m - l + 1) - (P[m] - P[l - 1]);
    ll right = (P[r] - P[m]) - x[m] * (r - m);
    return left + right;
}

// tinh cur[i] voi i trong [lo, hi], biet nhom cuoi bat dau tai j+1 voi j trong [optlo, opthi]
void solve(int lo, int hi, int optlo, int opthi) {
    if (lo > hi) return;
    int mid = (lo + hi) / 2, best = -1;
    ll bv = LLONG_MAX;
    for (int j = optlo; j <= min(mid - 1, opthi); j++) {
        if (prv[j] == LLONG_MAX) continue;
        ll v = prv[j] + cost(j + 1, mid);
        if (v < bv) { bv = v; best = j; }
    }
    cur[mid] = bv;
    solve(lo, mid - 1, optlo, best);
    solve(mid + 1, hi, best, opthi);
}

int main() {
    cin >> n >> k;
    x.assign(n + 1, 0);
    for (int i = 1; i <= n; i++) cin >> x[i];
    sort(x.begin() + 1, x.end());
    P.assign(n + 1, 0);
    for (int i = 1; i <= n; i++) P[i] = P[i - 1] + x[i];
    prv.assign(n + 1, LLONG_MAX);
    prv[0] = 0;                  // 0 nhom cho 0 xom
    cur.assign(n + 1, LLONG_MAX);
    for (int g = 1; g <= k; g++) {
        fill(cur.begin(), cur.end(), LLONG_MAX);
        solve(g, n, g - 1, n - 1);   // can it nhat g xom cho g nhom
        swap(prv, cur);
    }
    cout << prv[n] << "\n";
    return 0;
}
