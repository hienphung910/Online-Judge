// V010 - Dijkstra voi hang doi uu tien, O((n + m) log n)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<pair<int, long long>>> adj(n + 1);   // adj[u] = {v, w}
    for (int i = 0; i < m; i++) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    vector<long long> d(n + 1, -1);                   // -1 = chua toi duoc
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    d[1] = 0;
    pq.push({0, 1});
    while (!pq.empty()) {
        auto [du, u] = pq.top();
        pq.pop();
        if (du != d[u]) continue;                     // ban ghi cu, bo qua
        for (auto [v, w] : adj[u]) {
            if (d[v] == -1 || du + w < d[v]) {
                d[v] = du + w;
                pq.push({d[v], v});
            }
        }
    }

    for (int i = 1; i <= n; i++) cout << d[i] << (i == n ? '\n' : ' ');
    return 0;
}
