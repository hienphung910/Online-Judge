// V217 - Chia can voi khoi da sap xep: gan diem, dem so phan tu <= x trong doan
// Moi khoi giu ban sao sorted; khoi tron dung upper_bound, manh le duyet truc tiep.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    int B = max(1, (int)sqrt((double)n));
    vector<int> a(n);
    vector<vector<int>> blk(n / B + 1);
    for (int i = 0; i < n; i++) { cin >> a[i]; blk[i / B].push_back(a[i]); }
    for (auto &b : blk) sort(b.begin(), b.end());

    while (q--) {
        int t;
        cin >> t;
        if (t == 1) {
            int i, v;
            cin >> i >> v;
            i--;
            vector<int> &b = blk[i / B];
            b.erase(lower_bound(b.begin(), b.end(), a[i]));   // bo gia tri cu
            b.insert(upper_bound(b.begin(), b.end(), v), v);  // chen gia tri moi, van giu thu tu
            a[i] = v;
        } else {
            int l, r, x;
            cin >> l >> r >> x;
            l--, r--;
            int cnt = 0;
            while (l <= r && l % B != 0) cnt += (a[l++] <= x);
            while (l + B - 1 <= r) {
                vector<int> &b = blk[l / B];
                cnt += upper_bound(b.begin(), b.end(), x) - b.begin();
                l += B;
            }
            while (l <= r) cnt += (a[l++] <= x);
            cout << cnt << '\n';
        }
    }
    return 0;
}
