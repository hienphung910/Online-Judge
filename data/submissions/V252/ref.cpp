// V252 - DSU co hoan tac (rollback): hop theo kich thuoc, khong nen duong di
#include <bits/stdc++.h>
using namespace std;

vector<int> par, sz;

// khong nen duong di nen do sau cay DSU chi O(log n)
int findRoot(int u) {
    while (par[u] != u) u = par[u];
    return u;
}

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    par.resize(n + 1); sz.assign(n + 1, 1);
    for (int i = 1; i <= n; i++) par[i] = i;
    vector<int> st;  // moi cay cau da dung: goc bi gan vao goc khac, -1 neu cau thua
    while (q--) {
        int t, u, v;
        scanf("%d", &t);
        if (t == 1) {
            scanf("%d %d", &u, &v);
            int a = findRoot(u), b = findRoot(v);
            if (a == b) { st.push_back(-1); continue; }
            if (sz[a] < sz[b]) swap(a, b);  // gan cay nho vao cay lon
            par[b] = a; sz[a] += sz[b];
            st.push_back(b);
        } else if (t == 2) {
            int b = st.back(); st.pop_back();
            if (b != -1) { sz[par[b]] -= sz[b]; par[b] = b; }  // tach b ra lai
        } else {
            scanf("%d %d", &u, &v);
            puts(findRoot(u) == findRoot(v) ? "CO" : "KHONG");
        }
    }
    return 0;
}
