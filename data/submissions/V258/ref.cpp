// V258 - HLD + cay phan doan lazy: cong tren duong di, tong cay con, max tren duong di
#include <bits/stdc++.h>
using namespace std;

int n, q;
vector<long long> sum_, mx, lz;

// cay phan doan tren thu tu pos: cong doan [l, r], hoi tong va max
void apply(int node, int len, long long x) { sum_[node] += x * len; mx[node] += x; lz[node] += x; }
void push(int node, int nl, int nr) {
    if (!lz[node]) return;
    int mid = (nl + nr) / 2;
    apply(2 * node, mid - nl + 1, lz[node]);
    apply(2 * node + 1, nr - mid, lz[node]);
    lz[node] = 0;
}
void update(int node, int nl, int nr, int l, int r, long long x) {
    if (r < nl || nr < l) return;
    if (l <= nl && nr <= r) { apply(node, nr - nl + 1, x); return; }
    push(node, nl, nr);
    int mid = (nl + nr) / 2;
    update(2 * node, nl, mid, l, r, x);
    update(2 * node + 1, mid + 1, nr, l, r, x);
    sum_[node] = sum_[2 * node] + sum_[2 * node + 1];
    mx[node] = max(mx[2 * node], mx[2 * node + 1]);
}
long long qSum(int node, int nl, int nr, int l, int r) {
    if (r < nl || nr < l) return 0;
    if (l <= nl && nr <= r) return sum_[node];
    push(node, nl, nr);
    int mid = (nl + nr) / 2;
    return qSum(2 * node, nl, mid, l, r) + qSum(2 * node + 1, mid + 1, nr, l, r);
}
long long qMax(int node, int nl, int nr, int l, int r) {
    if (r < nl || nr < l) return LLONG_MIN;
    if (l <= nl && nr <= r) return mx[node];
    push(node, nl, nr);
    int mid = (nl + nr) / 2;
    return max(qMax(2 * node, nl, mid, l, r), qMax(2 * node + 1, mid + 1, nr, l, r));
}

int main() {
    scanf("%d %d", &n, &q);
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &a[i]);
    vector<int> par(n + 1, 0), dep(n + 1, 0), sz(n + 1, 1), heavy(n + 1, 0), head(n + 1), pos(n + 1);
    vector<vector<int>> ch(n + 1);
    for (int i = 2; i <= n; i++) { scanf("%d", &par[i]); ch[par[i]].push_back(i); }
    for (int i = n; i >= 2; i--) sz[par[i]] += sz[i];        // p_i < i: duyet nguoc
    for (int i = 2; i <= n; i++) dep[i] = dep[par[i]] + 1;
    for (int u = 1; u <= n; u++)
        for (int c : ch[u]) if (!heavy[u] || sz[c] > sz[heavy[u]]) heavy[u] = c;
    // DFS tien thu tu bang ngan xep, con nang tham ngay sau cha:
    // chuoi nang lien tiep, cay con cua u la doan [pos[u], pos[u] + sz[u] - 1]
    vector<int> st = {1};
    head[1] = 1;
    int cur = 0;
    while (!st.empty()) {
        int u = st.back(); st.pop_back();
        pos[u] = cur++;
        for (int c : ch[u]) if (c != heavy[u]) { head[c] = c; st.push_back(c); }
        if (heavy[u]) { head[heavy[u]] = head[u]; st.push_back(heavy[u]); }
    }
    sum_.assign(4 * n, 0); mx.assign(4 * n, 0); lz.assign(4 * n, 0);
    for (int i = 1; i <= n; i++) update(1, 0, n - 1, pos[i], pos[i], a[i]);
    while (q--) {
        int t, u, v;
        scanf("%d %d", &t, &u);
        if (t == 2) { printf("%lld\n", qSum(1, 0, n - 1, pos[u], pos[u] + sz[u] - 1)); continue; }
        scanf("%d", &v);
        long long x = 0, best = LLONG_MIN;
        if (t == 1) scanf("%lld", &x);
        // nhay tung chuoi nang cho toi khi u, v cung chuoi
        while (true) {
            if (head[u] == head[v]) {
                if (dep[u] > dep[v]) swap(u, v);
                if (t == 1) update(1, 0, n - 1, pos[u], pos[v], x);
                else best = max(best, qMax(1, 0, n - 1, pos[u], pos[v]));
                break;
            }
            if (dep[head[u]] < dep[head[v]]) swap(u, v);
            if (t == 1) update(1, 0, n - 1, pos[head[u]], pos[u], x);
            else best = max(best, qMax(1, 0, n - 1, pos[head[u]], pos[u]));
            u = par[head[u]];
        }
        if (t == 3) printf("%lld\n", best);
    }
    return 0;
}
