// V167 - DSU + gop tap nho vao tap lon (small-to-large) dem so loai hang
#include <bits/stdc++.h>
using namespace std;

vector<int> par;
vector<set<int>> types;   // types[r] = cac ma hang cua khu co goc r

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
    int n, q;
    cin >> n >> q;
    par.resize(n + 1);
    iota(par.begin(), par.end(), 0);
    types.resize(n + 1);
    for (int i = 1; i <= n; i++) {
        int t;
        cin >> t;
        types[i].insert(t);
    }
    while (q--) {
        int op, u;
        cin >> op >> u;
        if (op == 1) {
            int v;
            cin >> v;
            int a = findRoot(u), b = findRoot(v);
            if (a == b) continue;
            if (types[a].size() < types[b].size()) swap(a, b);   // a giu tap lon hon
            for (int t : types[b]) types[a].insert(t);           // do tap nho vao tap lon
            types[b].clear();
            par[b] = a;
        } else {
            cout << types[findRoot(u)].size() << '\n';
        }
    }
    return 0;
}
