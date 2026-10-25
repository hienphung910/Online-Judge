// V213 - Chia can: gan gia tri tai mot vi tri, hoi tong doan
// Chia day thanh cac khoi do dai B ~ sqrt(n), luu san tong moi khoi.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    int B = max(1, (int)sqrt((double)n));
    vector<long long> a(n), blk(n / B + 1, 0);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        blk[i / B] += a[i];
    }
    while (q--) {
        int t, x, y;
        cin >> t >> x >> y;
        if (t == 1) {                 // a[x] = y: chi sua tong cua mot khoi
            x--;
            blk[x / B] += y - a[x];
            a[x] = y;
        } else {                      // tong doan [x, y]
            int l = x - 1, r = y - 1;
            long long s = 0;
            while (l <= r && l % B != 0) s += a[l++];         // manh le ben trai
            while (l + B - 1 <= r) { s += blk[l / B]; l += B; } // cac khoi tron
            while (l <= r) s += a[l++];                        // manh le ben phai
            cout << s << '\n';
        }
    }
    return 0;
}
