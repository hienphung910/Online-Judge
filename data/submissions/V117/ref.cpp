// V117 - Bang thua (sparse table) cho max va min tren doan, truy van O(1)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    int K = 1;
    while ((1 << K) <= n) K++;
    // mx[k][i], mn[k][i]: max/min cua doan dai 2^k bat dau tai i
    vector<vector<int>> mx(K, vector<int>(n)), mn(K, vector<int>(n));
    for (int i = 0; i < n; i++) {
        cin >> mx[0][i];
        mn[0][i] = mx[0][i];
    }
    for (int k = 1; k < K; k++)
        for (int i = 0; i + (1 << k) <= n; i++) {
            mx[k][i] = max(mx[k - 1][i], mx[k - 1][i + (1 << (k - 1))]);
            mn[k][i] = min(mn[k - 1][i], mn[k - 1][i + (1 << (k - 1))]);
        }
    while (q--) {
        int l, r;
        cin >> l >> r;
        l--, r--;
        int k = 31 - __builtin_clz(r - l + 1);   // 2^k <= do dai doan
        int hi = max(mx[k][l], mx[k][r - (1 << k) + 1]);
        int lo = min(mn[k][l], mn[k][r - (1 << k) + 1]);
        cout << hi - lo << "\n";
    }
    return 0;
}
