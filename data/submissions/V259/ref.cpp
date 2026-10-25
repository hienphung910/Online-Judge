// V259 - Cay trong tam (centroid tree): mo tram, hoi khoang cach toi tram gan nhat
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
int n, q;
vector<vector<int>> adj;
vector<char> removed;
vector<int> sz, par, dist, best;
vector<vector<pair<int, int>>> anc;  // anc[v] = cac (trong tam to tien c, khoang cach v -> c)

vector<int> bfs(int s) {  // BFS trong thanh phan hien tai, tinh par va dist tu s
    vector<int> order = {s};
    par[s] = 0; dist[s] = 0;
    for (size_t i = 0; i < order.size(); i++) {
        int u = order[i];
        for (int v : adj[u])
            if (!removed[v] && v != par[u]) { par[v] = u; dist[v] = dist[u] + 1; order.push_back(v); }
    }
    return order;
}

void build(int s) {
    vector<int> order = bfs(s);
    int total = order.size(), c = s;
    for (int i = total - 1; i >= 0; i--) {  // kich thuoc cay con tu la len
        int u = order[i];
        sz[u] = 1;
        for (int v : adj[u]) if (!removed[v] && v != par[u]) sz[u] += sz[v];
    }
    for (int u : order) {  // trong tam: xoa u thi moi phan con lai <= total/2
        int big = total - sz[u];
        for (int v : adj[u]) if (!removed[v] && v != par[u]) big = max(big, sz[v]);
        if (big * 2 <= total) { c = u; break; }
    }
    for (int u : bfs(c)) anc[u].push_back({c, dist[u]});  // ghi khoang cach toi trong tam c
    removed[c] = 1;
    for (int v : adj[c]) if (!removed[v]) build(v);  // do sau de quy O(log n)
}

int main() {
    scanf("%d %d", &n, &q);
    adj.resize(n + 1);
    for (int i = 1; i < n; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        adj[u].push_back(v); adj[v].push_back(u);
    }
    removed.assign(n + 1, 0); sz.assign(n + 1, 0); par.assign(n + 1, 0); dist.assign(n + 1, 0);
    anc.resize(n + 1);
    build(1);
    best.assign(n + 1, INF);  // best[c] = khoang cach nho nhat tu c toi tram trong thanh phan cua c
    // duong di u -> v luon di qua trong tam to tien chung, nen chi can xet cac to tien cua v
    while (q--) {
        int t, v;
        scanf("%d %d", &t, &v);
        if (t == 1) {
            for (auto [c, d] : anc[v]) best[c] = min(best[c], d);
        } else {
            int ans = INF;
            for (auto [c, d] : anc[v]) ans = min(ans, best[c] + d);
            printf("%d\n", ans >= INF ? -1 : ans);
        }
    }
    return 0;
}
