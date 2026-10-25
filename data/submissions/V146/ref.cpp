// V146 - Euler tour tren cay + tim kiem nhi phan: dem hau due o dung k doi sau
// Cac dinh trong cay con cua u co tin nam trong doan [tin[u], tout[u]].
// Gom tin cua cac dinh theo do sau (theo thu tu tang dan vi DFS tham theo thu tu thoi gian),
// dap an = so phan tu cua danh sach do sau depth[u] + k nam trong doan tren.
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> child, byDepth;
vector<int> tin, tout, dep;
int timer_ = 0;

void dfs(int u, int d) {
    tin[u] = ++timer_;
    dep[u] = d;
    byDepth[d].push_back(tin[u]);  // tu dong tang dan
    for (int v : child[u]) dfs(v, d + 1);
    tout[u] = timer_;
}

int main() {
    int n;
    cin >> n;
    child.assign(n + 1, {});
    byDepth.assign(n + 1, {});
    tin.assign(n + 1, 0);
    tout.assign(n + 1, 0);
    dep.assign(n + 1, 0);
    for (int i = 2; i <= n; i++) {
        int p;
        cin >> p;
        child[p].push_back(i);
    }
    dfs(1, 0);  // do sau toi da n <= 2000
    int q;
    cin >> q;
    while (q--) {
        int u, k;
        cin >> u >> k;
        int d = dep[u] + k;
        if (d > n - 1) {
            cout << 0 << '\n';
            continue;
        }
        const vector<int> &L = byDepth[d];
        int cnt = upper_bound(L.begin(), L.end(), tout[u]) - lower_bound(L.begin(), L.end(), tin[u]);
        cout << cnt << '\n';
    }
    return 0;
}
