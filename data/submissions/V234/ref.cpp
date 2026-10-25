// V234 - Trinh cham cho bai "thu tu topo": kiem tra thu tu hoc cac hoc phan
// Tra loi 0 dung khi do thi co chu trinh (Kahn khong lay het dinh); tra loi thu tu thi kiem tra truc tiep.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        vector<int> eu(m), ev(m), indeg(n + 1, 0);
        vector<vector<int>> adj(n + 1);
        for (int i = 0; i < m; i++) {
            cin >> eu[i] >> ev[i];
            adj[eu[i]].push_back(ev[i]);
            indeg[ev[i]]++;
        }
        int flag;
        cin >> flag;
        bool ok;
        if (flag == 0) {
            // Kahn: lay dan cac dinh co ban bac vao 0; neu khong lay het thi co chu trinh
            queue<int> qu;
            for (int v = 1; v <= n; v++) if (indeg[v] == 0) qu.push(v);
            int taken = 0;
            while (!qu.empty()) {
                int u = qu.front(); qu.pop();
                taken++;
                for (int v : adj[u]) if (--indeg[v] == 0) qu.push(v);
            }
            ok = (taken < n);
        } else {
            vector<ll> p(n);
            for (auto &x : p) cin >> x;
            vector<int> pos(n + 1, -1);      // pos[v] = vi tri cua v trong thu tu, -1 neu chua gap
            ok = true;
            for (int i = 0; i < n; i++) {
                if (p[i] < 1 || p[i] > n || pos[p[i]] != -1) { ok = false; break; }
                pos[p[i]] = i;
            }
            for (int i = 0; ok && i < m; i++)
                if (pos[eu[i]] > pos[ev[i]]) ok = false;   // u phai dung truoc v
        }
        cout << (ok ? "DUNG" : "SAI") << "\n";
    }
    return 0;
}
