// V164 - LCA bang Euler tour + sparse table (RMQ), tong khoang cach tren cay
#include <bits/stdc++.h>
using namespace std;

int n, k;
vector<vector<pair<int, int>>> adj;
vector<int> euler, first, dep;
vector<long long> dist;           // do dai duong tu goc 1
vector<vector<int>> sp;           // sp[j][i] = dinh nong nhat trong euler[i .. i + 2^j - 1]

int shallower(int a, int b) { return dep[a] < dep[b] ? a : b; }

int lca(int u, int v) {
    int l = first[u], r = first[v];
    if (l > r) swap(l, r);
    int j = __lg(r - l + 1);
    return shallower(sp[j][l], sp[j][r - (1 << j) + 1]);
}

int main() {
    scanf("%d %d", &n, &k);
    adj.assign(n + 1, {});
    for (int i = 0; i < n - 1; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }
    // DFS khu de quy: ngan xep chua dinh, idx[u] = chi so canh ke tiep cua u
    first.assign(n + 1, -1);
    dep.assign(n + 1, 0);
    dist.assign(n + 1, 0);
    vector<int> parent(n + 1, 0), idx(n + 1, 0);
    vector<int> st = {1};
    first[1] = 0;
    euler.push_back(1);
    while (!st.empty()) {
        int u = st.back();
        if (idx[u] < (int)adj[u].size()) {
            auto [v, w] = adj[u][idx[u]++];
            if (v == parent[u]) continue;
            parent[v] = u;
            dep[v] = dep[u] + 1;
            dist[v] = dist[u] + w;
            first[v] = euler.size();
            euler.push_back(v);
            st.push_back(v);
        } else {
            st.pop_back();
            if (!st.empty()) euler.push_back(st.back());   // quay ve cha
        }
    }
    int m = euler.size();
    int LOG = __lg(m) + 1;
    sp.assign(LOG, vector<int>(m));
    sp[0] = euler;
    for (int j = 1; j < LOG; j++)
        for (int i = 0; i + (1 << j) <= m; i++)
            sp[j][i] = shallower(sp[j - 1][i], sp[j - 1][i + (1 << (j - 1))]);

    vector<int> c(k);
    for (auto &x : c) scanf("%d", &x);
    long long total = 0;
    for (int i = 0; i + 1 < k; i++) {
        int a = c[i], b = c[i + 1];
        total += dist[a] + dist[b] - 2 * dist[lca(a, b)];
    }
    printf("%lld\n", total);
    return 0;
}
