// V096 - Dem so phan tu trong doan [l, r] bang tim kiem nhi phan
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    for (auto &x : a) cin >> x;
    sort(a.begin(), a.end());
    while (q--) {
        int l, r;
        cin >> l >> r;
        int hi = upper_bound(a.begin(), a.end(), r) - a.begin();   // so phan tu <= r
        int lo = lower_bound(a.begin(), a.end(), l) - a.begin();   // so phan tu < l
        cout << hi - lo << "\n";
    }
    return 0;
}
