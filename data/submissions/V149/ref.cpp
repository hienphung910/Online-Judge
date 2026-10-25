// V149 - Duong di dai nhat tren DAG: sap xep topo Kahn + quy hoach dong
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<pair<int, int>>> adj(n + 1);
    vector<int> indeg(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        indeg[v]++;
    }
    // Kahn: lay dan cac dinh khong con canh di vao
    vector<int> order;
    queue<int> q;
    for (int i = 1; i <= n; i++)
        if (indeg[i] == 0) q.push(i);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        order.push_back(u);
        for (auto [v, w] : adj[u])
            if (--indeg[v] == 0) q.push(v);
    }
    vector<long long> dp(n + 1, -1);       // -1 = chua toi duoc
    dp[1] = 0;
    for (int u : order) {
        if (dp[u] < 0) continue;
        for (auto [v, w] : adj[u]) dp[v] = max(dp[v], dp[u] + w);
    }
    for (int i = 1; i <= n; i++) cout << dp[i] << (i == n ? '\n' : ' ');
    return 0;
}
