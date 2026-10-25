// V219 - Thuat toan Mo co cap nhat: dem so gia tri xuat hien dung 1 lan trong doan
// Cau hoi = (l, r, t); khoi kich thuoc ~ n^(2/3); sap xep theo (khoi l, khoi r, t).
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    for (auto &x : a) cin >> x;

    vector<int> up, uv;                 // lan sua thu j: vi tri up[j], gia tri uv[j]
    vector<int> L, R, T;                // cau hoi
    for (int i = 0; i < q; i++) {
        int t, x, y;
        cin >> t >> x >> y;
        if (t == 1) { up.push_back(x - 1); uv.push_back(y); }
        else { L.push_back(x - 1); R.push_back(y - 1); T.push_back(up.size()); }
    }

    // nen gia tri (ca gia tri ban dau lan gia tri sua)
    vector<int> s = a;
    s.insert(s.end(), uv.begin(), uv.end());
    sort(s.begin(), s.end());
    s.erase(unique(s.begin(), s.end()), s.end());
    auto code = [&](int x) { return int(lower_bound(s.begin(), s.end(), x) - s.begin()); };
    for (auto &x : a) x = code(x);
    for (auto &x : uv) x = code(x);

    int m = L.size();
    int B = max(1, (int)cbrt((double)n * n));
    vector<int> id(m);
    iota(id.begin(), id.end(), 0);
    sort(id.begin(), id.end(), [&](int x, int y) {
        if (L[x] / B != L[y] / B) return L[x] / B < L[y] / B;
        if (R[x] / B != R[y] / B) return R[x] / B < R[y] / B;
        return T[x] < T[y];
    });

    vector<int> cnt(s.size(), 0), ans(m);
    int once = 0, curL = 0, curR = -1, curT = 0;
    auto add = [&](int x) { cnt[x]++; if (cnt[x] == 1) once++; else if (cnt[x] == 2) once--; };
    auto del = [&](int x) { cnt[x]--; if (cnt[x] == 1) once++; else if (cnt[x] == 0) once--; };
    // ap dung / hoan tac lan sua j: doi cho a[p] voi uv[j] nen goi lai lan nua la hoan tac
    auto apply = [&](int j) {
        int p = up[j];
        if (curL <= p && p <= curR) { del(a[p]); add(uv[j]); }
        swap(a[p], uv[j]);
    };
    for (int k : id) {
        while (curT < T[k]) apply(curT++);
        while (curT > T[k]) apply(--curT);
        while (curR < R[k]) add(a[++curR]);
        while (curL > L[k]) add(a[--curL]);
        while (curR > R[k]) del(a[curR--]);
        while (curL < L[k]) del(a[curL++]);
        ans[k] = once;
    }
    for (int i = 0; i < m; i++) cout << ans[i] << '\n';
    return 0;
}
