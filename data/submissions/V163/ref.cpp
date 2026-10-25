// V163 - Kruskal voi dinh ao 0: gieng tai xom i = canh (0, i, a_i)
#include <bits/stdc++.h>
using namespace std;

vector<int> par;

int findRoot(int x) {
    while (par[x] != x) {
        par[x] = par[par[x]];
        x = par[x];
    }
    return x;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<array<long long, 3>> e;   // {w, u, v}
    for (int i = 1; i <= n; i++) {
        long long a;
        cin >> a;
        e.push_back({a, 0, i});       // khoan gieng = noi voi dinh ao 0
    }
    for (int j = 0; j < m; j++) {
        long long u, v, w;
        cin >> u >> v >> w;
        e.push_back({w, u, v});
    }
    sort(e.begin(), e.end());
    par.resize(n + 1);
    iota(par.begin(), par.end(), 0);
    long long total = 0;
    for (auto &x : e) {
        int a = findRoot(x[1]), b = findRoot(x[2]);
        if (a == b) continue;
        par[a] = b;
        total += x[0];
    }
    cout << total << '\n';
    return 0;
}
