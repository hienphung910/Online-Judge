// V023 - Luong cuc dai bang Dinic
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct Edge {
    int to;
    ll cap;
};

int n, m;
vector<Edge> edges;          // canh 2k la canh xuoi, 2k+1 la canh nguoc cua no
vector<vector<int>> adj;     // adj[u] = danh sach chi so canh di ra tu u
vector<int> level, ptr;

void addEdge(int u, int v, ll c) {
    adj[u].push_back(edges.size()); edges.push_back({v, c});
    adj[v].push_back(edges.size()); edges.push_back({u, 0});
}

bool bfs(int s, int t) {
    level.assign(n + 1, -1);
    level[s] = 0;
    queue<int> q;
    q.push(s);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int id : adj[u])
            if (edges[id].cap > 0 && level[edges[id].to] < 0) {
                level[edges[id].to] = level[u] + 1;
                q.push(edges[id].to);
            }
    }
    return level[t] >= 0;
}

// tim luong tang tren do thi phan tang (do sau toi da n nen de quy an toan)
ll dfs(int u, int t, ll pushed) {
    if (u == t) return pushed;
    for (int &i = ptr[u]; i < (int)adj[u].size(); i++) {
        int id = adj[u][i];
        int v = edges[id].to;
        if (edges[id].cap > 0 && level[v] == level[u] + 1) {
            ll got = dfs(v, t, min(pushed, edges[id].cap));
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
    scanf("%d %d", &n, &m);
    adj.assign(n + 1, {});
    for (int i = 0; i < m; i++) {
        int u, v;
        ll c;
        scanf("%d %d %lld", &u, &v, &c);
        if (u != v) addEdge(u, v, c);  // khuyen u -> u khong giup gi
    }
    ll flow = 0;
    while (bfs(1, n)) {
        ptr.assign(n + 1, 0);
        while (ll f = dfs(1, n, LLONG_MAX)) flow += f;
    }
    printf("%lld\n", flow);
    return 0;
}
