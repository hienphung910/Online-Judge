// V018 - Viet trinh cham cho bai "tim hai so co tong bang S", O(n log n)
// Kiem tra co ton tai cap hay khong bang sap xep + hai con tro, roi doi chieu voi cau tra loi.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    ll S;
    cin >> n >> S;
    vector<ll> a(n);
    for (auto &x : a) cin >> x;
    vector<ll> ans;            // cau tra loi: 1 so (-1) hoac 2 so (i j)
    ll t;
    while (cin >> t) ans.push_back(t);

    // co ton tai hai chi so khac nhau co tong bang S khong?
    vector<ll> b = a;
    sort(b.begin(), b.end());
    bool exists = false;
    int lo = 0, hi = n - 1;
    while (lo < hi) {
        ll s = b[lo] + b[hi];
        if (s == S) { exists = true; break; }
        if (s < S) lo++; else hi--;
    }

    bool ok;
    if (ans.size() == 1) {
        ok = !exists;                          // tra loi -1: dung khi that su khong co cap nao
    } else {
        ll i = ans[0], j = ans[1];
        ok = 1 <= i && i <= n && 1 <= j && j <= n && i != j && a[i - 1] + a[j - 1] == S;
    }
    cout << (ok ? "DUNG" : "SAI") << "\n";
    return 0;
}
