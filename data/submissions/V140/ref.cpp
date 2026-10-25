// V140 - DFS ba mau tim chu trinh tren do thi co huong
// Robot chay mai mai tu u <=> tu u di toi duoc mot chu trinh.
// mau 0 = chua tham, 1 = dang tham (tren stack DFS), 2 = da xong.
// Gap dinh mau 1 la gap chu trinh; inf[u] = co the chay mai tu u.
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> adj;
vector<int> color;
vector<bool> inf;

void dfs(int u) {
    color[u] = 1;
    for (int v : adj[u]) {
        if (color[v] == 0) dfs(v);
        if (color[v] == 1 || inf[v]) inf[u] = true;  // canh quay lui hoac di toi dinh chay mai
    }
    color[u] = 2;
}

int main() {
    int n, m;
    cin >> n >> m;
    adj.assign(n + 1, {});
    color.assign(n + 1, 0);
    inf.assign(n + 1, false);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }
    for (int u = 1; u <= n; u++)
        if (color[u] == 0) dfs(u);  // do sau toi da n <= 2000, de quy an toan
    for (int u = 1; u <= n; u++) cout << (inf[u] ? '1' : '0');
    cout << '\n';
    return 0;
}
