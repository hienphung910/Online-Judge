// V274 - Lat cat dinh co trong so: tach moi dinh thanh hai dinh (vao, ra) roi tinh luong cuc dai
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF = (ll)4e18;

struct Edge { int to; ll cap; };

int V, S, T;
vector<Edge> edges;
vector<vector<int>> adj;
vector<int> level, ptr;

void addEdge(int u, int v, ll c) {
    adj[u].push_back(edges.size()); edges.push_back({v, c});
    adj[v].push_back(edges.size()); edges.push_back({u, 0});
}

bool bfs() {
    level.assign(V, -1);
    level[S] = 0;
    queue<int> q;
    q.push(S);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int id : adj[u])
            if (edges[id].cap > 0 && level[edges[id].to] < 0) {
                level[edges[id].to] = level[u] + 1;
                q.push(edges[id].to);
            }
    }
    return level[T] >= 0;
}

ll dfs(int u, ll pushed) {
    if (u == T) return pushed;
    for (int &i = ptr[u]; i < (int)adj[u].size(); i++) {
        int id = adj[u][i], v = edges[id].to;
        if (edges[id].cap > 0 && level[v] == level[u] + 1) {
            ll got = dfs(v, min(pushed, edges[id].cap));
            if (got > 0) {
                edges[id].cap -= got;
                edges[id ^ 1].cap += got;
                return got;
            }
        }
    }
    return 0;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    // thanh i: dinh "vao" la i, dinh "ra" la i + n
    V = 2 * n + 1;
    adj.assign(V, {});
    for (int i = 1; i <= n; i++) {
        ll w;
        scanf("%lld", &w);
        // lap chot o thanh i ton w <=> cat canh i -> i + n (thanh 1 va n khong duoc cat)
        if (i != 1 && i != n) addEdge(i, i + n, w);
    }
    bool direct = false;
    for (int k = 0; k < m; k++) {
        int u, v;
        scanf("%d %d", &u, &v);
        if ((u == 1 && v == n) || (u == n && v == 1)) direct = true;
        addEdge(u + n, v, INF);   // con duong hai chieu: khong bao gio bi cat
        addEdge(v + n, u, INF);
    }
    if (direct) { printf("-1\n"); return 0; }
    S = 1 + n;   // nguon: dinh "ra" cua thanh 1
    T = n;       // dich: dinh "vao" cua thanh n
    ll flow = 0;
    while (bfs()) {
        ptr.assign(V, 0);
        while (ll f = dfs(S, INF)) flow += f;
    }
    printf("%lld\n", flow);
    return 0;
}
