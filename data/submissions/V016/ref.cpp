// V016 - Dem so gia tri phan biet trong doan bang thuat toan Mo, O((n + q) * sqrt(n))
// Nen gia tri ve 0..n-1, sap xep truy van theo (khoi cua l, r), di chuyen hai con tro.
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    for (auto &x : a) cin >> x;

    // nen toa do: a[i] -> thu tu cua no trong mang da sap xep
    vector<int> s = a;
    sort(s.begin(), s.end());
    s.erase(unique(s.begin(), s.end()), s.end());
    for (auto &x : a) x = lower_bound(s.begin(), s.end(), x) - s.begin();

    vector<int> L(q), R(q), id(q);
    for (int i = 0; i < q; i++) {
        cin >> L[i] >> R[i];
        L[i]--, R[i]--;
        id[i] = i;
    }
    int B = max(1, (int)(n / sqrt((double)q)));
    sort(id.begin(), id.end(), [&](int x, int y) {
        int bx = L[x] / B, by = L[y] / B;
        if (bx != by) return bx < by;
        return (bx & 1) ? R[x] > R[y] : R[x] < R[y];   // dao chieu r o khoi le cho nhanh hon
    });

    vector<int> cnt(s.size(), 0), ans(q);
    int curL = 0, curR = -1, distinct = 0;
    auto add = [&](int i) { if (cnt[a[i]]++ == 0) distinct++; };
    auto del = [&](int i) { if (--cnt[a[i]] == 0) distinct--; };
    for (int k : id) {
        while (curR < R[k]) add(++curR);
        while (curL > L[k]) add(--curL);
        while (curR > R[k]) del(curR--);
        while (curL < L[k]) del(curL++);
        ans[k] = distinct;
    }

    string out;
    for (int i = 0; i < q; i++) out += to_string(ans[i]) + '\n';
    cout << out;
    return 0;
}
