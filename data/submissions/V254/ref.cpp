// V254 - Phan ra nhe-nang (HLD) + cay Fenwick: gan gia tri dinh, tong tren duong di
#include <bits/stdc++.h>
using namespace std;

int n, q;
vector<long long> bit;
void add(int i, long long d) { for (i++; i <= n; i += i & -i) bit[i] += d; }
long long pref(int i) { long long s = 0; for (i++; i > 0; i -= i & -i) s += bit[i]; return s; }
long long rangeSum(int l, int r) { return pref(r) - pref(l - 1); }

int main() {
    scanf("%d %d", &n, &q);
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &a[i]);
    vector<int> par(n + 1, 0), dep(n + 1, 0), sz(n + 1, 1), heavy(n + 1, 0), head(n + 1), pos(n + 1);
    vector<vector<int>> ch(n + 1);
    for (int i = 2; i <= n; i++) { scanf("%d", &par[i]); ch[par[i]].push_back(i); }
    // cha luon co so nho hon con: duyet nguoc de tinh kich thuoc cay con, duyet xuoi de tinh do sau
    for (int i = n; i >= 2; i--) sz[par[i]] += sz[i];
    for (int i = 2; i <= n; i++) dep[i] = dep[par[i]] + 1;
    for (int u = 1; u <= n; u++)
        for (int c : ch[u]) if (!heavy[u] || sz[c] > sz[heavy[u]]) heavy[u] = c;
    // DFS bang ngan xep, con nang duoc tham ngay sau cha => moi chuoi nang lien tiep trong pos
    vector<int> st = {1};
    head[1] = 1;
    int cur = 0;
    while (!st.empty()) {
        int u = st.back(); st.pop_back();
        pos[u] = cur++;
        for (int c : ch[u]) if (c != heavy[u]) { head[c] = c; st.push_back(c); }
        if (heavy[u]) { head[heavy[u]] = head[u]; st.push_back(heavy[u]); }
    }
    bit.assign(n + 1, 0);
    for (int i = 1; i <= n; i++) add(pos[i], a[i]);
    while (q--) {
        int t, u, v;
        scanf("%d %d %d", &t, &u, &v);
        if (t == 1) {  // gan a[u] = v
            add(pos[u], v - a[u]); a[u] = v;
        } else {       // tong tren duong u - v: nhay tung chuoi nang
            long long res = 0;
            while (head[u] != head[v]) {
                if (dep[head[u]] < dep[head[v]]) swap(u, v);
                res += rangeSum(pos[head[u]], pos[u]);
                u = par[head[u]];
            }
            if (dep[u] > dep[v]) swap(u, v);
            res += rangeSum(pos[u], pos[v]);
            printf("%lld\n", res);
        }
    }
    return 0;
}
