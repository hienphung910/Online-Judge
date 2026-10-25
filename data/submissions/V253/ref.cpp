// V253 - 2-SAT: tim nhi phan tien to dai nhat thoa man duoc (Kosaraju khu de quy)
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> U, A, V, B;

// dinh 2(u-1)+a nghia la "den u o trang thai a"; phu dinh cua dinh x la x^1
bool satisfiable(int k) {
    int N = 2 * n;
    vector<vector<int>> g(N), rg(N);
    for (int i = 0; i < k; i++) {
        int x = 2 * (U[i] - 1) + A[i], y = 2 * (V[i] - 1) + B[i];
        // (x hoac y)  <=>  (!x -> y) va (!y -> x)
        g[x ^ 1].push_back(y); rg[y].push_back(x ^ 1);
        g[y ^ 1].push_back(x); rg[x].push_back(y ^ 1);
    }
    // luot 1: DFS bang ngan xep, ghi thu tu hoan thanh
    vector<int> order, it(N, 0), st;
    vector<char> seen(N, 0);
    for (int s = 0; s < N; s++) {
        if (seen[s]) continue;
        seen[s] = 1; st.push_back(s);
        while (!st.empty()) {
            int u = st.back();
            if (it[u] < (int)g[u].size()) {
                int v = g[u][it[u]++];
                if (!seen[v]) { seen[v] = 1; st.push_back(v); }
            } else { order.push_back(u); st.pop_back(); }
        }
    }
    // luot 2: loang tren do thi nguoc theo thu tu hoan thanh giam dan
    vector<int> comp(N, -1);
    int c = 0;
    for (int i = N - 1; i >= 0; i--) {
        int s = order[i];
        if (comp[s] >= 0) continue;
        comp[s] = c; st.push_back(s);
        while (!st.empty()) {
            int u = st.back(); st.pop_back();
            for (int v : rg[u]) if (comp[v] < 0) { comp[v] = c; st.push_back(v); }
        }
        c++;
    }
    for (int i = 0; i < N; i += 2)
        if (comp[i] == comp[i + 1]) return false;
    return true;
}

int main() {
    scanf("%d %d", &n, &m);
    U.resize(m); A.resize(m); V.resize(m); B.resize(m);
    for (int i = 0; i < m; i++) scanf("%d %d %d %d", &U[i], &A[i], &V[i], &B[i]);
    // them yeu cau chi lam kho hon => tinh thoa man don dieu theo k
    int lo = 1, hi = m;  // tien to do dai 1 luon thoa man
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (satisfiable(mid)) lo = mid; else hi = mid - 1;
    }
    printf("%d\n", lo);
    return 0;
}
