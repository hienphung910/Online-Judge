// V180 - Cay phan doan lazy hai loai nhan: gan doan + cong doan, hoi tong va max doan
// Moi nut co hai nhan cho day xuong: hasAsg/asg (gan) va add (cong them).
// Quy uoc: neu co ca hai thi hieu la "gan asg truoc, roi cong add".
//  - Nhan gan x moi den: xoa nhan cong cu, dat asg = x.
//  - Nhan cong x moi den: chi cong vao add (gan cu van giu nguyen).
#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> sum, mx, asg, add;
vector<bool> hasAsg;

void applyAssign(int node, int l, int r, long long x) {
    sum[node] = x * (r - l + 1);
    mx[node] = x;
    hasAsg[node] = true;
    asg[node] = x;
    add[node] = 0;
}

void applyAdd(int node, int l, int r, long long x) {
    sum[node] += x * (r - l + 1);
    mx[node] += x;
    add[node] += x;
}

void push(int node, int l, int r) {
    int mid = (l + r) / 2;
    if (hasAsg[node]) {
        applyAssign(2 * node, l, mid, asg[node]);
        applyAssign(2 * node + 1, mid + 1, r, asg[node]);
        hasAsg[node] = false;
    }
    if (add[node] != 0) {
        applyAdd(2 * node, l, mid, add[node]);
        applyAdd(2 * node + 1, mid + 1, r, add[node]);
        add[node] = 0;
    }
}

void pull(int node) {
    sum[node] = sum[2 * node] + sum[2 * node + 1];
    mx[node] = max(mx[2 * node], mx[2 * node + 1]);
}

void build(int node, int l, int r, const vector<long long> &a) {
    if (l == r) { sum[node] = mx[node] = a[l]; return; }
    int mid = (l + r) / 2;
    build(2 * node, l, mid, a);
    build(2 * node + 1, mid + 1, r, a);
    pull(node);
}

// type = 1: cong x, type = 2: gan x
void update(int node, int l, int r, int u, int v, int type, long long x) {
    if (v < l || r < u) return;
    if (u <= l && r <= v) {
        if (type == 1) applyAdd(node, l, r, x);
        else applyAssign(node, l, r, x);
        return;
    }
    push(node, l, r);
    int mid = (l + r) / 2;
    update(2 * node, l, mid, u, v, type, x);
    update(2 * node + 1, mid + 1, r, u, v, type, x);
    pull(node);
}

pair<long long, long long> query(int node, int l, int r, int u, int v) {   // (tong, max)
    if (v < l || r < u) return {0, LLONG_MIN};
    if (u <= l && r <= v) return {sum[node], mx[node]};
    push(node, l, r);
    int mid = (l + r) / 2;
    auto a = query(2 * node, l, mid, u, v);
    auto b = query(2 * node + 1, mid + 1, r, u, v);
    return {a.first + b.first, max(a.second, b.second)};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    sum.assign(4 * n, 0);
    mx.assign(4 * n, 0);
    asg.assign(4 * n, 0);
    add.assign(4 * n, 0);
    hasAsg.assign(4 * n, false);
    build(1, 1, n, a);
    while (q--) {
        int type, l, r;
        cin >> type >> l >> r;
        if (type == 3) {
            auto res = query(1, 1, n, l, r);
            cout << res.first << ' ' << res.second << '\n';
        } else {
            long long x;
            cin >> x;
            update(1, 1, n, l, r, type, x);
        }
    }
    return 0;
}
