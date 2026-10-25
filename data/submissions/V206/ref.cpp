// V206 - QHD tren cay: tap doc lap co tong trong so lon nhat
// dp[u][1] = w[u] + tong dp[con][0]; dp[u][0] = tong max(dp[con][0], dp[con][1]).
// Duyet BFS tu goc 1 roi xu ly nguoc thu tu BFS (con truoc cha), khong de quy.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int n;
    cin >> n;
    vector<ll> w(n + 1);
    for (int i = 1; i <= n; i++) cin >> w[i];
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<int> order, par(n + 1, 0);
    order.push_back(1);
    par[1] = -1;
    for (int k = 0; k < (int)order.size(); k++) {
        int u = order[k];
        for (int v : adj[u])
            if (v != par[u]) { par[v] = u; order.push_back(v); }
    }
    vector<ll> take(n + 1), skip(n + 1);   // take = chon u, skip = khong chon u
    for (int k = n - 1; k >= 0; k--) {
        int u = order[k];
        take[u] += w[u];
        if (par[u] > 0) {
            take[par[u]] += skip[u];
            skip[par[u]] += max(take[u], skip[u]);
        }
    }
    cout << max(take[1], skip[1]) << "\n";
    return 0;
}
