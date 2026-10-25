// V216 - Thuat toan Mo: dem so cap (i < j) trong doan [l, r] co c_i = c_j
// Them mot phan tu mau x: so cap tang them cnt[x]; bo ra: giam (cnt[x] - 1).
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> c(n);
    for (auto &x : c) cin >> x;

    // nen mau ve 0..n-1
    vector<int> s = c;
    sort(s.begin(), s.end());
    s.erase(unique(s.begin(), s.end()), s.end());
    for (auto &x : c) x = lower_bound(s.begin(), s.end(), x) - s.begin();

    vector<int> L(q), R(q), id(q);
    for (int i = 0; i < q; i++) {
        cin >> L[i] >> R[i];
        L[i]--, R[i]--;
        id[i] = i;
    }
    int B = max(1, (int)sqrt((double)n));
    sort(id.begin(), id.end(), [&](int x, int y) {
        if (L[x] / B != L[y] / B) return L[x] / B < L[y] / B;
        return R[x] < R[y];
    });

    vector<int> cnt(s.size(), 0);
    vector<long long> ans(q);
    long long pairs = 0;
    int curL = 0, curR = -1;
    auto add = [&](int i) { pairs += cnt[c[i]]; cnt[c[i]]++; };
    auto del = [&](int i) { cnt[c[i]]--; pairs -= cnt[c[i]]; };
    for (int k : id) {
        while (curR < R[k]) add(++curR);
        while (curL > L[k]) add(--curL);
        while (curR > R[k]) del(curR--);
        while (curL < L[k]) del(curL++);
        ans[k] = pairs;
    }
    for (int i = 0; i < q; i++) cout << ans[i] << '\n';
    return 0;
}
