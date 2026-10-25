// V019 - Tro choi boc soi (subtraction game) bang dinh ly Sprague-Grundy
// g[x] = mex{ g[x - s] : s thuoc tap nuoc di, s <= x }; nguoi di truoc thang khi XOR cac g[a_i] khac 0.
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) {
        int n, k;
        cin >> n >> k;
        vector<int> s(k), a(n);
        for (auto &x : s) cin >> x;
        for (auto &x : a) cin >> x;
        int mx = *max_element(a.begin(), a.end());

        vector<int> g(mx + 1);
        for (int x = 0; x <= mx; x++) {
            int seen = 0;                       // bit v bat neu da gap gia tri Grundy v (v <= k <= 10)
            for (int m : s)
                if (m <= x) seen |= 1 << g[x - m];
            int v = 0;
            while (seen >> v & 1) v++;          // mex
            g[x] = v;
        }
        int x = 0;
        for (int p : a) x ^= g[p];
        cout << (x ? "TI" : "TEO") << "\n";
    }
    return 0;
}
