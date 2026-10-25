// V175 - Cay phan doan lazy: cong doan, hoi min doan, O((n + q) log n)
// lz[node] = luong da cong cho ca doan cua node nhung chua day xuong hai con.
#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> mn, lz;

void apply(int node, long long x) {   // cong x cho ca doan cua node
    mn[node] += x;
    lz[node] += x;
}

void push(int node) {
    if (lz[node] != 0) {
        apply(2 * node, lz[node]);
        apply(2 * node + 1, lz[node]);
        lz[node] = 0;
    }
}

void build(int node, int l, int r, const vector<long long> &a) {
    if (l == r) { mn[node] = a[l]; return; }
    int mid = (l + r) / 2;
    build(2 * node, l, mid, a);
    build(2 * node + 1, mid + 1, r, a);
    mn[node] = min(mn[2 * node], mn[2 * node + 1]);
}

void update(int node, int l, int r, int u, int v, long long x) {
    if (v < l || r < u) return;
    if (u <= l && r <= v) { apply(node, x); return; }
    push(node);
    int mid = (l + r) / 2;
    update(2 * node, l, mid, u, v, x);
    update(2 * node + 1, mid + 1, r, u, v, x);
    mn[node] = min(mn[2 * node], mn[2 * node + 1]);
}

long long query(int node, int l, int r, int u, int v) {
    if (v < l || r < u) return LLONG_MAX;
    if (u <= l && r <= v) return mn[node];
    push(node);
    int mid = (l + r) / 2;
    return min(query(2 * node, l, mid, u, v), query(2 * node + 1, mid + 1, r, u, v));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    mn.assign(4 * n, 0);
    lz.assign(4 * n, 0);
    build(1, 1, n, a);
    while (q--) {
        int type, l, r;
        cin >> type >> l >> r;
        if (type == 1) {
            long long x;
            cin >> x;
            update(1, 1, n, l, r, x);
        } else {
            cout << query(1, 1, n, l, r) << '\n';
        }
    }
    return 0;
}
