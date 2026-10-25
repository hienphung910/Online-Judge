// V207 - QHD tren cay doi goc (rerooting): chon dinh hop mat co tong quang duong nho nhat
// S(v) = tong c[i] * dist(i, v). Tinh S(1) roi doi goc: S(con) = S(cha) + w * (tong - 2 * sub[con]).
// Duyet BFS (khong de quy) de an toan voi cay dang duong thang.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int n;
    cin >> n;
    vector<ll> c(n + 1);
    for (int i = 1; i <= n; i++) cin >> c[i];
    vector<vector<pair<int, ll>>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        ll w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }
    vector<int> order = {1}, par(n + 1, 0);
    vector<ll> pw(n + 1, 0);              // do dai canh noi voi cha
    par[1] = -1;
    for (int k = 0; k < (int)order.size(); k++) {
        int u = order[k];
        for (auto [v, w] : adj[u])
            if (v != par[u]) { par[v] = u; pw[v] = w; order.push_back(v); }
    }
    vector<ll> sub(c), S(n + 1, 0);
    ll root = 0;
    for (int k = n - 1; k > 0; k--) {     // con truoc cha
        int u = order[k];
        sub[par[u]] += sub[u];
        root += sub[u] * pw[u];           // sub[u] nguoi phai di qua canh (u, cha)
    }
    ll total = sub[1];
    S[1] = root;
    for (int k = 1; k < n; k++) {         // cha truoc con
        int u = order[k];
        S[u] = S[par[u]] + pw[u] * (total - 2 * sub[u]);
    }
    int best = 1;
    for (int v = 2; v <= n; v++)
        if (S[v] < S[best]) best = v;
    cout << S[best] << " " << best << "\n";
    return 0;
}
