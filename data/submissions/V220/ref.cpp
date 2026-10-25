// V220 - Chia can: bi nhay i -> i + a[i], sua a[i] va hoi o cuoi cung + so lan cham
// Moi o luu: nxt = o dau tien ngoai khoi, cnt = so lan cham trong khoi, last = o cuoi trong khoi.
#include <bits/stdc++.h>
using namespace std;

int n, B;
vector<int> a, nxt, cnt, lst;

// tinh lai mot khoi, tu phai sang trai
void build(int b) {
    int lo = b * B, hi = min(n, lo + B) - 1;
    for (int i = hi; i >= lo; i--) {
        int j = i + a[i];
        if (j > hi) { nxt[i] = j; cnt[i] = 1; lst[i] = i; }
        else { nxt[i] = nxt[j]; cnt[i] = cnt[j] + 1; lst[i] = lst[j]; }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    B = max(1, (int)sqrt((double)n));
    a.resize(n); nxt.resize(n); cnt.resize(n); lst.resize(n);
    for (auto &x : a) cin >> x;
    for (int b = 0; b * B < n; b++) build(b);
    while (q--) {
        int t, i;
        cin >> t >> i;
        i--;
        if (t == 0) {
            cin >> a[i];
            build(i / B);
        } else {
            int total = 0, last = i;
            while (i < n) {            // moi buoc nhay qua ca mot khoi
                total += cnt[i];
                last = lst[i];
                i = nxt[i];
            }
            cout << last + 1 << ' ' << total << '\n';
        }
    }
    return 0;
}
