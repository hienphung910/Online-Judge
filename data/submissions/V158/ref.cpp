// V158 - Bellman-Ford: khoang cach, khong toi duoc, va -INF do chu trinh am
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<array<int, 3>> e(m);
    vector<vector<int>> adj(n + 1);
    for (auto& x : e) {
        cin >> x[0] >> x[1] >> x[2];
        adj[x[0]].push_back(x[1]);
    }
    const long long INF = LLONG_MAX;
    vector<long long> d(n + 1, INF);
    d[1] = 0;
    for (int it = 1; it < n; it++)             // n - 1 vong Bellman-Ford
        for (auto [u, v, w] : e)
            if (d[u] != INF && d[u] + w < d[v]) d[v] = d[u] + w;

    // vong thu n: dinh nao con giam duoc thi di duoc tu chu trinh am
    vector<bool> neg(n + 1, false);
    queue<int> q;
    for (auto [u, v, w] : e)
        if (d[u] != INF && d[u] + w < d[v] && !neg[v]) {
            neg[v] = true;
            q.push(v);
        }
    while (!q.empty()) {                       // loang -INF sang moi dinh di duoc tu do
        int u = q.front();
        q.pop();
        for (int v : adj[u])
            if (!neg[v]) {
                neg[v] = true;
                q.push(v);
            }
    }
    for (int v = 1; v <= n; v++) {
        if (neg[v]) cout << "-INF\n";
        else if (d[v] == INF) cout << "KHONG\n";
        else cout << d[v] << '\n';
    }
    return 0;
}
