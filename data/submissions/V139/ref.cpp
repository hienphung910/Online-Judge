// V139 - BFS 0-1: so lan di nguoc chieu it nhat
// Canh u -> v tao hai canh: u -> v trong so 0 (di dung chieu), v -> u trong so 1 (di nguoc).
// Deque: canh trong so 0 day vao dau, canh trong so 1 day vao cuoi.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<pair<int, int>>> adj(n + 1);  // (dinh ke, trong so)
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back({v, 0});
        adj[v].push_back({u, 1});
    }
    const int INF = INT_MAX;
    vector<int> d(n + 1, INF);
    deque<int> dq;
    d[1] = 0;
    dq.push_back(1);
    while (!dq.empty()) {
        int u = dq.front();
        dq.pop_front();
        for (auto [v, w] : adj[u])
            if (d[u] + w < d[v]) {
                d[v] = d[u] + w;
                if (w == 0) dq.push_front(v);
                else dq.push_back(v);
            }
    }
    for (int u = 1; u <= n; u++) cout << (d[u] == INF ? -1 : d[u]) << (u == n ? '\n' : ' ');
    return 0;
}
