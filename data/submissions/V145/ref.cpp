// V145 - Thanh phan lien thong manh (Tarjan) va do thi nen
// Sau khi gop moi TPLT manh thanh mot dinh, ta duoc mot DAG.
// So nguoi it nhat can bao tin = so TPLT manh khong co canh nao di vao tu TPLT khac.
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> adj;
vector<int> num, low, comp, st;
vector<bool> onStack;
int timer_ = 0, compCnt = 0;

void dfs(int u) {
    num[u] = low[u] = ++timer_;
    st.push_back(u);
    onStack[u] = true;
    for (int v : adj[u]) {
        if (!num[v]) {
            dfs(v);
            low[u] = min(low[u], low[v]);
        } else if (onStack[v]) {
            low[u] = min(low[u], num[v]);
        }
    }
    if (low[u] == num[u]) {  // u la goc cua mot TPLT manh
        compCnt++;
        while (true) {
            int v = st.back();
            st.pop_back();
            onStack[v] = false;
            comp[v] = compCnt;
            if (v == u) break;
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    adj.assign(n + 1, {});
    num.assign(n + 1, 0);
    low.assign(n + 1, 0);
    comp.assign(n + 1, 0);
    onStack.assign(n + 1, false);
    vector<pair<int, int>> edges(m);
    for (auto &[u, v] : edges) {
        cin >> u >> v;
        adj[u].push_back(v);
    }
    for (int u = 1; u <= n; u++)
        if (!num[u]) dfs(u);  // do sau toi da n <= 2000
    vector<int> sz(compCnt + 1, 0);
    vector<bool> hasIn(compCnt + 1, false);
    for (int u = 1; u <= n; u++) sz[comp[u]]++;
    for (auto [u, v] : edges)
        if (comp[u] != comp[v]) hasIn[comp[v]] = true;
    int largest = *max_element(sz.begin() + 1, sz.end());
    int seeds = 0;
    for (int c = 1; c <= compCnt; c++)
        if (!hasIn[c]) seeds++;
    cout << compCnt << ' ' << largest << ' ' << seeds << '\n';
    return 0;
}
