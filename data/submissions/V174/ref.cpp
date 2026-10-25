// V174 - Cay phan doan luu cap (max, so lan xuat hien cua max), O((n + q) log n)
// Gop hai con: lay max lon hon; neu hai max bang nhau thi cong so lan xuat hien.
#include <bits/stdc++.h>
using namespace std;

typedef pair<long long, int> Node;   // (max, dem)
int n;
vector<Node> t;

Node merge(Node a, Node b) {
    if (a.first > b.first) return a;
    if (a.first < b.first) return b;
    return {a.first, a.second + b.second};
}

void update(int node, int l, int r, int pos, long long val) {
    if (l == r) { t[node] = {val, 1}; return; }
    int mid = (l + r) / 2;
    if (pos <= mid) update(2 * node, l, mid, pos, val);
    else update(2 * node + 1, mid + 1, r, pos, val);
    t[node] = merge(t[2 * node], t[2 * node + 1]);
}

Node query(int node, int l, int r, int u, int v) {
    if (v < l || r < u) return {-1, 0};   // phan tu trung tinh (a_i >= 0)
    if (u <= l && r <= v) return t[node];
    int mid = (l + r) / 2;
    return merge(query(2 * node, l, mid, u, v), query(2 * node + 1, mid + 1, r, u, v));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    t.assign(4 * n, {-1, 0});
    for (int i = 1; i <= n; i++) {
        long long a;
        cin >> a;
        update(1, 1, n, i, a);
    }
    while (q--) {
        int type, x;
        long long y;
        cin >> type >> x >> y;
        if (type == 1) {
            update(1, 1, n, x, y);
        } else {
            Node res = query(1, 1, n, x, (int)y);
            cout << res.first << ' ' << res.second << '\n';
        }
    }
    return 0;
}
