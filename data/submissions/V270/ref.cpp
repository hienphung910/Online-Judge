// V270 - So duong di khong chung canh (dinh ly Menger, luong cuc dai voi suc chua 1)
#include <bits/stdc++.h>
using namespace std;

struct Edge { int to, cap; };

int n, m;
vector<Edge> edges;          // canh 2k va 2k+1 la mot cap nguoc nhau
vector<vector<int>> adj;
vector<int> level, ptr;

// duong hai chieu: moi chieu suc chua 1, chung mot cap canh nen di nguoc se "huy" luong
void addRoad(int u, int v) {
    adj[u].push_back(edges.size()); edges.push_back({v, 1});
    adj[v].push_back(edges.size()); edges.push_back({u, 1});
}

bool bfs() {
    level.assign(n + 1, -1);
    level[1] = 0;
    queue<int> q;
    q.push(1);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int id : adj[u])
            if (edges[id].cap > 0 && level[edges[id].to] < 0) {
                level[edges[id].to] = level[u] + 1;
                q.push(edges[id].to);
            }
    }
    return level[n] >= 0;
}

int dfs(int u, int pushed) {
    if (u == n) return pushed;
    for (int &i = ptr[u]; i < (int)adj[u].size(); i++) {
        int id = adj[u][i], v = edges[id].to;
        if (edges[id].cap > 0 && level[v] == level[u] + 1) {
            int got = dfs(v, min(pushed, edges[id].cap));
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
        scanf("%d %d", &u, &v);
        addRoad(u, v);
    }
    int flow = 0;
    while (bfs()) {
        ptr.assign(n + 1, 0);
        while (int f = dfs(1, INT_MAX)) flow += f;
    }
    printf("%d\n", flow);
    return 0;
}
