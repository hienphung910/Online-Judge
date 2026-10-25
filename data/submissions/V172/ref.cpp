// V172 - Cay phan doan (segment tree) min: gan mot diem, hoi min doan, O((n + q) log n)
#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> t;   // t[node] = min cua doan ma node quan ly

void update(int node, int l, int r, int pos, long long val) {
    if (l == r) { t[node] = val; return; }
    int mid = (l + r) / 2;
    if (pos <= mid) update(2 * node, l, mid, pos, val);
    else update(2 * node + 1, mid + 1, r, pos, val);
    t[node] = min(t[2 * node], t[2 * node + 1]);
}

long long query(int node, int l, int r, int u, int v) {
    if (v < l || r < u) return LLONG_MAX;        // nam ngoai doan hoi
    if (u <= l && r <= v) return t[node];         // nam tron trong doan hoi
    int mid = (l + r) / 2;
    return min(query(2 * node, l, mid, u, v), query(2 * node + 1, mid + 1, r, u, v));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    t.assign(4 * n, LLONG_MAX);
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
        else cout << query(1, 1, n, x, (int)y) << '\n';
    }
    return 0;
}
