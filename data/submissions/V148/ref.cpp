// V148 - Floyd-Warshall tinh khoang cach moi cap dinh, O(n^3 + q)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, q;
    cin >> n >> m >> q;
    const long long INF = 1e18;
    vector<vector<long long>> d(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; i++) d[i][i] = 0;
    for (int i = 0; i < m; i++) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        d[u][v] = min(d[u][v], w);            // giu canh re nhat
        d[v][u] = min(d[v][u], w);
    }
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                if (d[i][k] < INF && d[k][j] < INF)
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
    while (q--) {
        int a, b;
        cin >> a >> b;
        cout << (d[a][b] == INF ? -1 : d[a][b]) << '\n';
    }
    return 0;
}
