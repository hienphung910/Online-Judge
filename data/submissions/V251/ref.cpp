// V251 - Chat nhi phan song song + DSU: thoi diem som nhat u, v chung mot vung du lon
// Dieu kien "sau t cau, u va v cung thanh phan co it nhat s dao" don dieu theo t.
// Moi vong: dung lai DSU tu dau, them lan luot cau 1..m, sau cau t kiem tra cac
// truy van co mid = t. Dap an nam trong [0, m+1] (m+1 = khong bao gio).
#include <bits/stdc++.h>
using namespace std;

vector<int> par, sz;
int root(int x) { return par[x] == x ? x : par[x] = root(par[x]); }
void unite(int a, int b) {
    a = root(a), b = root(b);
    if (a == b) return;
    if (sz[a] < sz[b]) swap(a, b);
    par[b] = a;
    sz[a] += sz[b];
}

int main() {
    int n, m, q;
    cin >> n >> m >> q;
    vector<int> eu(m + 1), ev(m + 1);
    for (int t = 1; t <= m; t++) cin >> eu[t] >> ev[t];
    vector<int> U(q), V(q), S(q), lo(q, 0), hi(q, m + 1);
    for (int i = 0; i < q; i++) cin >> U[i] >> V[i] >> S[i];

    while (true) {
        vector<vector<int>> at(m + 1);
        bool any = false;
        for (int i = 0; i < q; i++)
            if (lo[i] < hi[i]) { at[(lo[i] + hi[i]) / 2].push_back(i); any = true; }
        if (!any) break;
        par.resize(n + 1);
        sz.assign(n + 1, 1);
        iota(par.begin(), par.end(), 0);
        for (int t = 0; t <= m; t++) {
            if (t > 0) unite(eu[t], ev[t]);
            for (int i : at[t]) {
                int r = root(U[i]);
                if (r == root(V[i]) && sz[r] >= S[i]) hi[i] = t; else lo[i] = t + 1;
            }
        }
    }
    for (int i = 0; i < q; i++) cout << (lo[i] == m + 1 ? -1 : lo[i]) << "\n";
    return 0;
}
