// V151 - Bellman-Ford gioi han toi da K canh, trong so co the am
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, s, t, K;
    cin >> n >> m >> s >> t >> K;
    vector<array<int, 3>> e(m);
    for (auto& x : e) cin >> x[0] >> x[1] >> x[2];

    const long long INF = LLONG_MAX;
    vector<long long> d(n + 1, INF);       // d[v] = re nhat toi v voi <= j chang
    d[s] = 0;
    for (int j = 1; j <= K; j++) {
        vector<long long> nd = d;          // dung gia tri cua vong truoc
        for (auto [u, v, w] : e)
            if (d[u] != INF && d[u] + w < nd[v]) nd[v] = d[u] + w;
        d = nd;
    }
    if (d[t] == INF) cout << "KHONG\n";
    else cout << d[t] << '\n';
    return 0;
}
