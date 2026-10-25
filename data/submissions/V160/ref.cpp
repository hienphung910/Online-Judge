// V160 - DSU theo kich thuoc: dem so nhom va nhom lon nhat sau moi lan gop
#include <bits/stdc++.h>
using namespace std;

vector<int> par, sz;

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
    par.resize(n + 1);
    sz.assign(n + 1, 1);
    iota(par.begin(), par.end(), 0);
    int groups = n, best = 1;
    while (m--) {
        int u, v;
        cin >> u >> v;
        int a = findRoot(u), b = findRoot(v);
        if (a != b) {
            if (sz[a] < sz[b]) swap(a, b);   // gop nhom nho vao nhom lon
            par[b] = a;
            sz[a] += sz[b];
            groups--;
            best = max(best, sz[a]);
        }
        cout << groups << ' ' << best << '\n';
    }
    return 0;
}
