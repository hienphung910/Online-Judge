// V142 - Duong di Euler tren cay (tin/tout): kiem tra to tien va tong cay con
// DFS danh so tin[u] khi vao, tout[u] khi ra. Cay con cua u = cac dinh co tin trong [tin[u], tout[u]].
// u la to tien cua v <=> tin[u] < tin[v] va tout[v] <= tout[u].
// Tong cay con = tong doan lien tiep tren mang theo thu tu tin -> dung tong tien to.
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> child;
vector<int> tin, tout;
int timer_ = 0;

void dfs(int u) {
    tin[u] = ++timer_;
    for (int v : child[u]) dfs(v);
    tout[u] = timer_;  // tin lon nhat trong cay con cua u
}

int main() {
    int n;
    cin >> n;
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    child.assign(n + 1, {});
    tin.assign(n + 1, 0);
    tout.assign(n + 1, 0);
    for (int i = 2; i <= n; i++) {
        int p;
        cin >> p;
        child[p].push_back(i);
    }
    dfs(1);  // do sau toi da n <= 1000
    vector<long long> pre(n + 1, 0);  // pre[k] = tong a cua cac dinh co tin <= k
    vector<long long> byTin(n + 1);
    for (int u = 1; u <= n; u++) byTin[tin[u]] = a[u];
    for (int k = 1; k <= n; k++) pre[k] = pre[k - 1] + byTin[k];
    int q;
    cin >> q;
    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int u, v;
            cin >> u >> v;
            bool anc = tin[u] < tin[v] && tout[v] <= tout[u];
            cout << (anc ? "CO" : "KHONG") << '\n';
        } else {
            int u;
            cin >> u;
            cout << pre[tout[u]] - pre[tin[u] - 1] << '\n';
        }
    }
    return 0;
}
