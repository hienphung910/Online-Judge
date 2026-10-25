// V011 - Cay khung nho nhat bang Kruskal + DSU, O(m log m)
#include <bits/stdc++.h>
using namespace std;

vector<int> par;

int findRoot(int x) {
    while (par[x] != x) {
        par[x] = par[par[x]];   // nen duong di
        x = par[x];
    }
    return x;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<array<long long, 3>> e(m);   // {w, u, v}
    for (auto &x : e) cin >> x[1] >> x[2] >> x[0];
    sort(e.begin(), e.end());

    par.resize(n + 1);
    iota(par.begin(), par.end(), 0);
    long long total = 0;
    int used = 0;                        // so canh da chon
    for (auto &x : e) {
        int a = findRoot(x[1]), b = findRoot(x[2]);
        if (a == b) continue;            // tao chu trinh, bo qua
        par[a] = b;
        total += x[0];
        used++;
    }
    cout << (used == n - 1 ? total : -1) << '\n';
    return 0;
}
