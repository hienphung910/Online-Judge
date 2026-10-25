// V162 - DSU co chan le (parity): kiem tra loi khai cung doi / khac doi
#include <bits/stdc++.h>
using namespace std;

vector<int> par, rel, sz;   // rel[x] = 0 neu x cung doi voi par[x], 1 neu khac doi

// tra ve goc cua x, dong thoi tinh p = quan he giua x va goc
int findRoot(int x, int &p) {
    p = 0;
    while (par[x] != x) {
        p ^= rel[x];
        x = par[x];
    }
    return x;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    par.resize(n + 1);
    iota(par.begin(), par.end(), 0);
    rel.assign(n + 1, 0);
    sz.assign(n + 1, 1);
    while (k--) {
        int u, v, d, pu, pv;
        cin >> u >> v >> d;
        int a = findRoot(u, pu), b = findRoot(v, pv);
        bool ok;
        if (a == b) {
            ok = ((pu ^ pv) == d);          // da cung nhom: kiem tra co khop khong
        } else {
            ok = true;                       // khac nhom: gop lai, luon hop le
            if (sz[a] < sz[b]) swap(a, b);
            par[b] = a;
            rel[b] = pu ^ pv ^ d;
            sz[a] += sz[b];
        }
        cout << (ok ? "DUNG" : "SAI") << '\n';
    }
    return 0;
}
