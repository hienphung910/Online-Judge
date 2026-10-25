// V157 - k lo trinh re nhat: Dijkstra cho moi dinh duoc lay ra toi da k lan
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<pair<int, int>>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }
    vector<int> popped(n + 1, 0);              // so lan moi dinh da duoc lay ra
    vector<long long> ans;
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    pq.push({0, 1});
    while (!pq.empty() && (int)ans.size() < k) {
        auto [c, u] = pq.top();
        pq.pop();
        if (popped[u] == k) continue;          // da co du k lo trinh toi u
        popped[u]++;
        if (u == n) ans.push_back(c);
        for (auto [v, w] : adj[u])
            if (popped[v] < k) pq.push({c + w, v});
    }
    while ((int)ans.size() < k) ans.push_back(-1);
    for (int i = 0; i < k; i++) cout << ans[i] << (i == k - 1 ? '\n' : ' ');
    return 0;
}
