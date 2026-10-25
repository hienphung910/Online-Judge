// V179 - Cay phan doan gop nut: doan con lien tiep co tong lon nhat, gan mot diem, O((n + q) log n)
// Moi nut luu 4 so cua doan no quan ly:
//   sum  = tong ca doan
//   pre  = tong tien to lon nhat (khong rong)
//   suf  = tong hau to lon nhat (khong rong)
//   best = tong doan con lien tiep lon nhat (khong rong)
// Gop trai L voi phai R: best moi = max(L.best, R.best, L.suf + R.pre).
#include <bits/stdc++.h>
using namespace std;

struct Node {
    long long sum, pre, suf, best;
};

Node leaf(long long x) { return {x, x, x, x}; }

Node merge(const Node &L, const Node &R) {
    Node res;
    res.sum = L.sum + R.sum;
    res.pre = max(L.pre, L.sum + R.pre);
    res.suf = max(R.suf, R.sum + L.suf);
    res.best = max({L.best, R.best, L.suf + R.pre});
    return res;
}

int n;
vector<Node> t;

void update(int node, int l, int r, int pos, long long val) {
    if (l == r) { t[node] = leaf(val); return; }
    int mid = (l + r) / 2;
    if (pos <= mid) update(2 * node, l, mid, pos, val);
    else update(2 * node + 1, mid + 1, r, pos, val);
    t[node] = merge(t[2 * node], t[2 * node + 1]);
}

Node query(int node, int l, int r, int u, int v) {   // goi khi [l, r] giao [u, v] khac rong
    if (u <= l && r <= v) return t[node];
    int mid = (l + r) / 2;
    if (v <= mid) return query(2 * node, l, mid, u, v);
    if (u > mid) return query(2 * node + 1, mid + 1, r, u, v);
    return merge(query(2 * node, l, mid, u, v), query(2 * node + 1, mid + 1, r, u, v));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    t.assign(4 * n, leaf(0));
    for (int i = 1; i <= n; i++) {
        long long a;
        cin >> a;
        update(1, 1, n, i, a);
    }
    while (q--) {
        int type, x;
        long long y;
        cin >> type >> x >> y;
        if (type == 1) update(1, 1, n, x, y);
        else cout << query(1, 1, n, x, (int)y).best << '\n';
    }
    return 0;
}
