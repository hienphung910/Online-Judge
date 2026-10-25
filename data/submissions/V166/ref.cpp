// V166 - Cay khung lon nhat (Kruskal) + nhay nhi phan lay canh nho nhat tren duong di
#include <bits/stdc++.h>
using namespace std;

const int LOG = 10;   // 2^10 > n
vector<int> par;

int findRoot(int x) {
    while (par[x] != x) {
        par[x] = par[par[x]];
        x = par[x];
    }
    return x;
}

int main() {
    int n, m, q;
    scanf("%d %d %d", &n, &m, &q);
    vector<array<int, 3>> e(m);   // {c, u, v}
    for (auto &x : e) scanf("%d %d %d", &x[1], &x[2], &x[0]);
    sort(e.rbegin(), e.rend());    // tai trong giam dan

    // 1) Kruskal lay rung khung lon nhat
    par.resize(n + 1);
    iota(par.begin(), par.end(), 0);
    vector<vector<pair<int, int>>> adj(n + 1);
    for (auto &x : e) {
        int a = findRoot(x[1]), b = findRoot(x[2]);
        if (a == b) continue;
        par[a] = b;
        adj[x[1]].push_back({x[2], x[0]});
        adj[x[2]].push_back({x[1], x[0]});
    }

    // 2) BFS tung cay: do sau, cha, canh len cha
    vector<int> dep(n + 1, -1), comp(n + 1);
    vector<array<int, LOG>> up(n + 1), mn(n + 1);   // mn[v][j] = canh nho nhat tren 2^j buoc nhay
    for (int r = 1; r <= n; r++) {
        if (dep[r] >= 0) continue;
        vector<int> order = {r};
        dep[r] = 0;
        up[r][0] = r;
        mn[r][0] = INT_MAX;
        for (int i = 0; i < (int)order.size(); i++) {
            int u = order[i];
            comp[u] = r;
            for (auto [v, c] : adj[u])
                if (dep[v] < 0) {
                    dep[v] = dep[u] + 1;
                    up[v][0] = u;
                    mn[v][0] = c;
                    order.push_back(v);
                }
        }
        for (int u : order)
            for (int j = 1; j < LOG; j++) {
                up[u][j] = up[up[u][j - 1]][j - 1];
                mn[u][j] = min(mn[u][j - 1], mn[up[u][j - 1]][j - 1]);
            }
    }

    // 3) Tra loi: nhay u, v len LCA, gom canh nho nhat
    while (q--) {
        int u, v;
        scanf("%d %d", &u, &v);
        if (comp[u] != comp[v]) { puts("-1"); continue; }
        int best = INT_MAX;
        if (dep[u] < dep[v]) swap(u, v);
        for (int j = LOG - 1; j >= 0; j--)
            if (dep[u] - (1 << j) >= dep[v]) {
                best = min(best, mn[u][j]);
                u = up[u][j];
            }
        if (u != v) {
            for (int j = LOG - 1; j >= 0; j--)
                if (up[u][j] != up[v][j]) {
                    best = min(best, min(mn[u][j], mn[v][j]));
                    u = up[u][j];
                    v = up[v][j];
                }
            best = min(best, min(mn[u][0], mn[v][0]));
        }
        printf("%d\n", best);
    }
    return 0;
}
