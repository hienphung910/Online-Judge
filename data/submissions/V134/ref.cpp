// V134 - Bieu dien do thi: dem bac va kiem tra hai dinh co ke nhau
// Luu danh sach ke dang set de tra loi "u, v co duong noi truc tiep khong" nhanh.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<set<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].insert(v);
        adj[v].insert(u);
    }
    for (int u = 1; u <= n; u++) cout << adj[u].size() << (u == n ? '\n' : ' ');
    int q;
    cin >> q;
    while (q--) {
        int u, v;
        cin >> u >> v;
        cout << (adj[u].count(v) ? "CO" : "KHONG") << '\n';
    }
    return 0;
}
