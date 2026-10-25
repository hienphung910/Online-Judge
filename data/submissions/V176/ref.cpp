// V176 - Cay phan doan lazy: gan doan, tong doan, O((n + q) log n)
// asg[node] = gia tri dang cho gan xuong ca doan cua node, -1 neu khong co
// (dung -1 vi gia tri gan hop le luon >= 0, ke ca gan bang 0).
#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> sum, asg;

void apply(int node, int l, int r, long long x) {   // gan x cho ca doan [l, r]
    sum[node] = x * (r - l + 1);
    asg[node] = x;
}

void push(int node, int l, int r) {
    if (asg[node] != -1) {
        int mid = (l + r) / 2;
        apply(2 * node, l, mid, asg[node]);
        apply(2 * node + 1, mid + 1, r, asg[node]);
        asg[node] = -1;
    }
}

void build(int node, int l, int r, const vector<long long> &a) {
    if (l == r) { sum[node] = a[l]; return; }
    int mid = (l + r) / 2;
    build(2 * node, l, mid, a);
    build(2 * node + 1, mid + 1, r, a);
    sum[node] = sum[2 * node] + sum[2 * node + 1];
}

void update(int node, int l, int r, int u, int v, long long x) {
    if (v < l || r < u) return;
    if (u <= l && r <= v) { apply(node, l, r, x); return; }
    push(node, l, r);
    int mid = (l + r) / 2;
    update(2 * node, l, mid, u, v, x);
    update(2 * node + 1, mid + 1, r, u, v, x);
    sum[node] = sum[2 * node] + sum[2 * node + 1];
}

long long query(int node, int l, int r, int u, int v) {
    if (v < l || r < u) return 0;
    if (u <= l && r <= v) return sum[node];
    push(node, l, r);
    int mid = (l + r) / 2;
    return query(2 * node, l, mid, u, v) + query(2 * node + 1, mid + 1, r, u, v);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    sum.assign(4 * n, 0);
    asg.assign(4 * n, -1);
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
