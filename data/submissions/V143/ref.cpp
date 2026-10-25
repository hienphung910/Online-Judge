// V143 - Tim khop (dinh cat) bang thuat toan Tarjan
// num[u] = thu tu tham, low[u] = num nho nhat di toi duoc tu cay con cua u qua toi da mot canh nguoc.
// u (khong phai goc) la khop neu co con v voi low[v] >= num[u]; goc la khop neu co >= 2 con.
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> adj;
vector<int> num, low;
vector<bool> isCut;
int timer_ = 0;

void dfs(int u, int parent) {
    num[u] = low[u] = ++timer_;
    int children = 0;
    for (int v : adj[u]) {
        if (v == parent) continue;
        if (num[v]) {
            low[u] = min(low[u], num[v]);  // canh nguoc
        } else {
            dfs(v, u);
            children++;
            low[u] = min(low[u], low[v]);
            if (parent != 0 && low[v] >= num[u]) isCut[u] = true;
        }
    }
    if (parent == 0 && children >= 2) isCut[u] = true;
}

int main() {
    int n, m;
    cin >> n >> m;
    adj.assign(n + 1, {});
    num.assign(n + 1, 0);
    low.assign(n + 1, 0);
    isCut.assign(n + 1, false);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    for (int u = 1; u <= n; u++)
        if (!num[u]) dfs(u, 0);  // do sau toi da n <= 2000
    vector<int> res;
    for (int u = 1; u <= n; u++)
        if (isCut[u]) res.push_back(u);
    cout << res.size() << '\n';
    for (int i = 0; i < (int)res.size(); i++) cout << res[i] << (i + 1 == (int)res.size() ? '\n' : ' ');
    return 0;
}
