// V159 - DSU tra loi truy van lien thong truc tuyen
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
    int n, q;
    cin >> n >> q;
    par.resize(n + 1);
    iota(par.begin(), par.end(), 0);
    while (q--) {
        int t, u, v;
        cin >> t >> u >> v;
        int a = findRoot(u), b = findRoot(v);
        if (t == 1) par[a] = b;                       // gop hai nhom
        else cout << (a == b ? "CO" : "KHONG") << '\n';
    }
    return 0;
}
