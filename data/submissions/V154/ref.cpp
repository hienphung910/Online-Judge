// V154 - He rang buoc hieu giai bang SPFA (kiem tra chu trinh am bang nguon ao)
#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<pair<int, int>>> adj;   // canh u -> v trong so w: x_v <= x_u + w
const long long INF = LLONG_MAX / 4;

// SPFA tu cac dinh trong 'src' (khoang cach 0). Tra ve false neu gap chu trinh am.
bool spfa(const vector<int>& src, vector<long long>& d) {
    d.assign(n + 1, INF);
    vector<int> len(n + 1, 0);        // so canh tren duong di hien tai
    vector<bool> inq(n + 1, false);
    queue<int> q;
    for (int s : src) {
        d[s] = 0;
        q.push(s);
        inq[s] = true;
    }
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        inq[u] = false;
        for (auto [v, w] : adj[u]) {
            if (d[u] + w < d[v]) {
                d[v] = d[u] + w;
                len[v] = len[u] + 1;
                if (len[v] >= n) return false;   // duong di qua >= n canh => co chu trinh am
                if (!inq[v]) {
                    q.push(v);
                    inq[v] = true;
                }
            }
        }
    }
    return true;
}

int main() {
    int p, q;
    cin >> n >> p >> q;
    adj.assign(n + 1, {});
    for (int i = 1; i < n; i++) adj[i + 1].push_back({i, 0});       // x_i <= x_(i+1)
    for (int i = 0; i < p; i++) {
        int a, b, d;
        cin >> a >> b >> d;
        adj[a].push_back({b, d});                                    // x_b <= x_a + d
    }
    for (int i = 0; i < q; i++) {
        int a, b, d;
        cin >> a >> b >> d;
        adj[b].push_back({a, -d});                                   // x_a <= x_b - d
    }
    vector<long long> d;
    vector<int> all;
    for (int i = 1; i <= n; i++) all.push_back(i);
    if (!spfa(all, d)) {              // nguon ao: moi dinh bat dau voi khoang cach 0
        cout << -1 << '\n';
        return 0;
    }
    spfa({1}, d);
    cout << (d[n] >= INF ? -2 : d[n]) << '\n';
    return 0;
}
