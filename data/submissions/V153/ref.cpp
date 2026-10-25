// V153 - Dijkstra dem so duong di ngan nhat, so canh it nhat va nhieu nhat
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1e9 + 7;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<pair<int, int>>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }
    const long long INF = LLONG_MAX;
    vector<long long> d(n + 1, INF), cnt(n + 1, 0);
    vector<int> mn(n + 1, 0), mx(n + 1, 0);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    d[1] = 0;
    cnt[1] = 1;
    pq.push({0, 1});
    while (!pq.empty()) {
        auto [du, u] = pq.top();
        pq.pop();
        if (du != d[u]) continue;
        for (auto [v, w] : adj[u]) {
            long long nd = du + w;
            if (nd < d[v]) {                       // duong moi tot hon han
                d[v] = nd;
                cnt[v] = cnt[u];
                mn[v] = mn[u] + 1;
                mx[v] = mx[u] + 1;
                pq.push({nd, v});
            } else if (nd == d[v]) {               // them mot nhom duong bang nhau
                cnt[v] = (cnt[v] + cnt[u]) % MOD;
                mn[v] = min(mn[v], mn[u] + 1);
                mx[v] = max(mx[v], mx[u] + 1);
            }
        }
    }
    cout << d[n] << ' ' << cnt[n] << ' ' << mn[n] << ' ' << mx[n] << '\n';
    return 0;
}
