// V257 - Lien thong dong offline: cay phan doan theo thoi gian + DSU co hoan tac
#include <bits/stdc++.h>
using namespace std;

int n, q, comps;
vector<int> par, sz, hist;  // hist: cac goc bi gan (de hoan tac)
vector<int> T, X, Y;
vector<vector<pair<int, int>>> seg;  // seg[node] = cac con duong mo suot doan thoi gian cua node

int findRoot(int u) { while (par[u] != u) u = par[u]; return u; }
void unite(int u, int v) {
    u = findRoot(u); v = findRoot(v);
    if (u == v) return;
    if (sz[u] < sz[v]) swap(u, v);
    par[v] = u; sz[u] += sz[v]; comps--;
    hist.push_back(v);
}
void rollback(size_t keep) {
    while (hist.size() > keep) {
        int v = hist.back(); hist.pop_back();
        sz[par[v]] -= sz[v]; par[v] = v; comps++;
    }
}

// gan con duong (u, v) vao moi node phu doan thoi gian [l, r)
void addEdge(int node, int nl, int nr, int l, int r, pair<int, int> e) {
    if (r <= nl || nr <= l) return;
    if (l <= nl && nr <= r) { seg[node].push_back(e); return; }
    int mid = (nl + nr) / 2;
    addEdge(2 * node, nl, mid, l, r, e);
    addEdge(2 * node + 1, mid, nr, l, r, e);
}

// duyet cay phan doan, do sau O(log q); ra khoi node thi hoan tac cac phep hop
void dfs(int node, int nl, int nr) {
    size_t keep = hist.size();
    for (auto& e : seg[node]) unite(e.first, e.second);
    if (nr - nl == 1) {
        if (T[nl] == 3) puts(findRoot(X[nl]) == findRoot(Y[nl]) ? "CO" : "KHONG");
        if (T[nl] == 4) printf("%d\n", comps);
    } else {
        int mid = (nl + nr) / 2;
        dfs(2 * node, nl, mid);
        dfs(2 * node + 1, mid, nr);
    }
    rollback(keep);
}

int main() {
    scanf("%d %d", &n, &q);
    T.resize(q); X.assign(q, 0); Y.assign(q, 0);
    seg.resize(4 * q);
    map<pair<int, int>, int> openAt;  // con duong dang mo -> thoi diem mo
    for (int i = 0; i < q; i++) {
        scanf("%d", &T[i]);
        if (T[i] == 4) continue;
        scanf("%d %d", &X[i], &Y[i]);
        pair<int, int> e = {min(X[i], Y[i]), max(X[i], Y[i])};
        if (T[i] == 1) openAt[e] = i;
        if (T[i] == 2) { addEdge(1, 0, q, openAt[e], i, e); openAt.erase(e); }
    }
    for (auto& [e, s] : openAt) addEdge(1, 0, q, s, q, e);  // mo den het
    par.resize(n + 1); sz.assign(n + 1, 1);
    for (int i = 1; i <= n; i++) par[i] = i;
    comps = n;
    dfs(1, 0, q);
    return 0;
}
