// V165 - Nhay nhi phan (binary lifting): LCA va dinh thu k tren duong di u -> v
#include <bits/stdc++.h>
using namespace std;

const int LOG = 10;   // 2^10 = 1024 > n
int n, q;
vector<int> dep;
vector<array<int, LOG>> up;   // up[v][j] = to tien thu 2^j cua v (goc 1 co cha la chinh no)

int ancestor(int v, int t) {   // to tien thu t cua v
    for (int j = 0; j < LOG; j++)
        if (t >> j & 1) v = up[v][j];
    return v;
}

int lca(int u, int v) {
    if (dep[u] < dep[v]) swap(u, v);
    u = ancestor(u, dep[u] - dep[v]);
    if (u == v) return u;
    for (int j = LOG - 1; j >= 0; j--)
        if (up[u][j] != up[v][j]) {
            u = up[u][j];
            v = up[v][j];
        }
    return up[u][0];
}

int main() {
    scanf("%d %d", &n, &q);
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    // BFS tu goc 1 de lay cha va do sau (khong de quy)
    dep.assign(n + 1, -1);
    up.assign(n + 1, {});
    vector<int> order = {1};
    dep[1] = 0;
    up[1][0] = 1;
    for (int i = 0; i < (int)order.size(); i++) {
        int u = order[i];
        for (int v : adj[u])
            if (dep[v] < 0) {
                dep[v] = dep[u] + 1;
                up[v][0] = u;
                order.push_back(v);
            }
    }
    for (int u : order)               // cha da duoc tinh truoc con
        for (int j = 1; j < LOG; j++) up[u][j] = up[up[u][j - 1]][j - 1];

    while (q--) {
        int u, v, k;
        scanf("%d %d %d", &u, &v, &k);
        int w = lca(u, v);
        int du = dep[u] - dep[w], dv = dep[v] - dep[w];
        int t = k - 1;                // so buoc tu u
        int ans;
        if (t <= du) ans = ancestor(u, t);
        else if (t <= du + dv) ans = ancestor(v, du + dv - t);
        else ans = -1;
        printf("%d\n", ans);
    }
    return 0;
}
