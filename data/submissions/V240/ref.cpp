// V240 - Tro choi tren DAG: so Grundy cua dinh tinh theo thu tu topo nguoc
// g[u] = mex{ g[v] : co canh u -> v }; mot van thang khi XOR g cua cac vi tri bi khac 0.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> adj(n + 1);
    vector<int> indeg(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        indeg[v]++;
    }
    // Kahn: lay thu tu topo
    vector<int> order;
    queue<int> q;
    for (int u = 1; u <= n; u++)
        if (indeg[u] == 0) q.push(u);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        order.push_back(u);
        for (int v : adj[u])
            if (--indeg[v] == 0) q.push(v);
    }
    // duyet nguoc: moi dinh ke cua u da co so Grundy
    vector<int> g(n + 1, 0);
    for (int i = n - 1; i >= 0; i--) {
        int u = order[i];
        vector<bool> seen(adj[u].size() + 1, false);
        for (int v : adj[u])
            if (g[v] < (int)seen.size()) seen[g[v]] = true;
        int x = 0;
        while (seen[x]) x++;
        g[u] = x;
    }
    int Q;
    cin >> Q;
    while (Q--) {
        int k, X = 0;
        cin >> k;
        for (int i = 0; i < k; i++) {
            int c;
            cin >> c;
            X ^= g[c];
        }
        cout << (X ? "KHOA" : "VY") << "\n";
    }
    return 0;
}
