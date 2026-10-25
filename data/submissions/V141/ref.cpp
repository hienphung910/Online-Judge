// V141 - Sap xep topo nho nhat theo thu tu tu dien (Kahn + hang doi uu tien)
// Luon lay mon co so hieu nho nhat trong cac mon da hoc du mon tien quyet.
// Neu lay ra it hon n mon thi do thi co chu trinh -> in -1.
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
    priority_queue<int, vector<int>, greater<int>> pq;  // min-heap
    for (int u = 1; u <= n; u++)
        if (indeg[u] == 0) pq.push(u);
    vector<int> order;
    while (!pq.empty()) {
        int u = pq.top();
        pq.pop();
        order.push_back(u);
        for (int v : adj[u])
            if (--indeg[v] == 0) pq.push(v);
    }
    if ((int)order.size() < n) {
        cout << -1 << '\n';
        return 0;
    }
    for (int i = 0; i < n; i++) cout << order[i] << (i + 1 == n ? '\n' : ' ');
    return 0;
}
