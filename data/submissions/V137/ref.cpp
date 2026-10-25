// V137 - BFS to hai mau (kiem tra do thi hai phia) va dem so cach chia doi
// Moi thanh phan lien thong to duoc 2 cach (doi mau) neu khong co chu trinh le.
// Dap an = 2^(so thanh phan) mod 1e9+7, hoac 0 neu co canh noi hai dinh cung mau.
#include <bits/stdc++.h>
using namespace std;

int main() {
    const long long MOD = 1000000007;
    int n, m;
    cin >> n >> m;
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<int> color(n + 1, -1);
    long long ways = 1;
    for (int s = 1; s <= n; s++) {
        if (color[s] != -1) continue;
        ways = ways * 2 % MOD;
        color[s] = 0;
        queue<int> q;
        q.push(s);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (color[v] == -1) {
                    color[v] = 1 - color[u];
                    q.push(v);
                } else if (color[v] == color[u]) {
                    cout << 0 << '\n';
                    return 0;
                }
            }
        }
    }
    cout << ways << '\n';
    return 0;
}
