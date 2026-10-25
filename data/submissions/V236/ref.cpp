// V236 - Trinh cham cho bai "duong di ngan nhat": kiem tra duong di hoc sinh dua ra
// Dijkstra tinh dist(s, t), roi kiem tra tung buoc cua duong di (dinh hop le, co canh, tong trong so).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF = LLONG_MAX;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) {
        int n, m, s, t;
        cin >> n >> m >> s >> t;
        vector<vector<pair<int, ll>>> adj(n + 1);
        map<pair<int, int>, ll> w;              // trong so con duong noi (u, v), luu ca hai chieu
        for (int i = 0; i < m; i++) {
            int u, v; ll c;
            cin >> u >> v >> c;
            adj[u].push_back({v, c});
            adj[v].push_back({u, c});
            w[{u, v}] = c;
            w[{v, u}] = c;
        }

        // Dijkstra tu s
        vector<ll> dist(n + 1, INF);
        priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<>> pq;
        dist[s] = 0;
        pq.push({0, s});
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d > dist[u]) continue;
            for (auto [v, c] : adj[u])
                if (d + c < dist[v]) { dist[v] = d + c; pq.push({dist[v], v}); }
        }

        int flag;
        cin >> flag;
        bool ok;
        if (flag == 0) {
            ok = (dist[t] == INF);                       // khang dinh khong toi duoc t
        } else {
            ll D; int k;
            cin >> D >> k;
            vector<ll> p(k);
            for (auto &x : p) cin >> x;
            ok = dist[t] != INF && D == dist[t] && p[0] == s && p[k - 1] == t;
            for (int i = 0; ok && i < k; i++)
                if (p[i] < 1 || p[i] > n) ok = false;    // dinh ngoai [1, n]
            ll sum = 0;
            for (int i = 0; ok && i + 1 < k; i++) {
                auto it = w.find({(int)p[i], (int)p[i + 1]});
                if (it == w.end()) ok = false;           // hai dinh lien tiep khong co duong noi
                else sum += it->second;
            }
            if (ok && sum != D) ok = false;              // tong do dai phai dung bang D
        }
        cout << (ok ? "DUNG" : "SAI") << "\n";
    }
    return 0;
}
