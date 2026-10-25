// V144 - Tim cau tren do thi co canh lap bang Tarjan
// Canh (u, v) voi v la con cua u trong cay DFS la cau <=> low[v] > num[u].
// Vi co the co nhieu canh noi cung cap dinh, ta chi bo qua dung CANH vua di xuong (theo chi so),
// khong bo qua ca dinh cha: canh lap thu hai toi cha van la canh nguoc hop le.
#include <bits/stdc++.h>
using namespace std;

vector<vector<pair<int, int>>> adj;  // (dinh ke, chi so canh)
vector<int> num, low;
vector<bool> isBridge;
int timer_ = 0;

void dfs(int u, int parentEdge) {
    num[u] = low[u] = ++timer_;
    for (auto [v, id] : adj[u]) {
        if (id == parentEdge) continue;
        if (num[v]) {
            low[u] = min(low[u], num[v]);
        } else {
            dfs(v, id);
            low[u] = min(low[u], low[v]);
            if (low[v] > num[u]) isBridge[id] = true;
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    adj.assign(n + 1, {});
    num.assign(n + 1, 0);
    low.assign(n + 1, 0);
    isBridge.assign(m + 1, false);
    for (int i = 1; i <= m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back({v, i});
        adj[v].push_back({u, i});
    }
    for (int u = 1; u <= n; u++)
        if (!num[u]) dfs(u, 0);  // do sau toi da n <= 2000
    vector<int> res;
    for (int i = 1; i <= m; i++)
        if (isBridge[i]) res.push_back(i);
    cout << res.size() << '\n';
    for (int i = 0; i < (int)res.size(); i++) cout << res[i] << (i + 1 == (int)res.size() ? '\n' : ' ');
    return 0;
}
