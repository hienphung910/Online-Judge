// V135 - BFS tren do thi vo huong: ngay nghe tin don cua moi nguoi
// d[u] = so canh it nhat tu s den u = ngay u nghe tin; -1 neu khong bao gio nghe.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, s;
    cin >> n >> m >> s;
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<int> d(n + 1, -1);
    queue<int> q;
    d[s] = 0;
    q.push(s);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u])
            if (d[v] == -1) {
                d[v] = d[u] + 1;
                q.push(v);
            }
    }
    for (int u = 1; u <= n; u++) cout << d[u] << (u == n ? '\n' : ' ');
    return 0;
}
