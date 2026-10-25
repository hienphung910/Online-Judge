// V150 - Dijkstra nhieu nguon: moi tram cuu hoa vao hang doi voi khoang cach 0
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    vector<long long> d(n + 1, -1);              // -1 = chua toi duoc
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    for (int i = 0; i < k; i++) {
        int s;
        cin >> s;
        d[s] = 0;
        pq.push({0, s});
    }
    vector<vector<pair<int, int>>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }
    while (!pq.empty()) {
        auto [du, u] = pq.top();
        pq.pop();
        if (du != d[u]) continue;                  // ban ghi cu
        for (auto [v, w] : adj[u])
            if (d[v] == -1 || du + w < d[v]) {
                d[v] = du + w;
                pq.push({d[v], v});
            }
    }
    for (int i = 1; i <= n; i++) cout << d[i] << (i == n ? '\n' : ' ');
    return 0;
}
