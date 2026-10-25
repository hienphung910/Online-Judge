// V155 - Dijkstra tren trang thai (dinh, so phieu mien phi da dung)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, K;
    cin >> n >> m >> K;
    vector<vector<pair<int, int>>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }
    const long long INF = LLONG_MAX;
    vector<vector<long long>> d(n + 1, vector<long long>(K + 1, INF));   // d[v][j]
    priority_queue<tuple<long long, int, int>, vector<tuple<long long, int, int>>, greater<>> pq;
    d[1][0] = 0;
    pq.push({0, 1, 0});
    while (!pq.empty()) {
        auto [du, u, j] = pq.top();
        pq.pop();
        if (du != d[u][j]) continue;
        for (auto [v, w] : adj[u]) {
            if (du + w < d[v][j]) {                      // tra tien
                d[v][j] = du + w;
                pq.push({d[v][j], v, j});
            }
            if (j < K && du < d[v][j + 1]) {             // dung mot phieu
                d[v][j + 1] = du;
                pq.push({du, v, j + 1});
            }
        }
    }
    long long ans = *min_element(d[n].begin(), d[n].end());
    cout << (ans == INF ? -1 : ans) << '\n';
    return 0;
}
