// V147 - Duong di Euler co huong nho nhat theo thu tu tu dien (Hierholzer)
// Dieu kien: moi dinh co ban bac ra = ban bac vao, tru toi da mot dinh ra - vao = 1 (diem dau)
// va mot dinh vao - ra = 1 (diem cuoi); moi canh phai di toi duoc tu diem dau.
// Sap xep danh sach ke tang dan, Hierholzer luon di canh co dinh dich nho nhat truoc;
// ket qua (dao nguoc thu tu roi khoi dinh) la hanh trinh nho nhat theo tu dien.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> adj(n + 1);
    vector<int> outd(n + 1, 0), ind(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        outd[u]++;
        ind[v]++;
    }
    int start = 0, plus = 0, minus = 0;
    for (int u = 1; u <= n; u++) {
        int d = outd[u] - ind[u];
        if (d == 1) { plus++; start = u; }
        else if (d == -1) minus++;
        else if (d != 0) { cout << -1 << '\n'; return 0; }
    }
    if (plus > 1 || minus > 1 || plus != minus) { cout << -1 << '\n'; return 0; }
    if (start == 0)  // chu trinh Euler: bat dau tu dinh nho nhat co canh ra
        for (int u = n; u >= 1; u--)
            if (outd[u] > 0) start = u;
    for (auto &l : adj) sort(l.begin(), l.end());

    vector<int> ptr(n + 1, 0), path, st = {start};
    while (!st.empty()) {
        int u = st.back();
        if (ptr[u] < (int)adj[u].size()) {
            st.push_back(adj[u][ptr[u]++]);
        } else {
            path.push_back(u);
            st.pop_back();
        }
    }
    if ((int)path.size() != m + 1) { cout << -1 << '\n'; return 0; }  // co canh khong toi duoc
    reverse(path.begin(), path.end());
    for (int i = 0; i <= m; i++) cout << path[i] << (i == m ? '\n' : ' ');
    return 0;
}
