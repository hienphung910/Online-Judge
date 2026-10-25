// V275 - Luong chi phi cuc tieu: chuyen toi da K don vi voi chi phi nho nhat (SPFA + tang luong)
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct Edge { int to; ll cap, cost; };

int n, m;
vector<Edge> edges;          // canh 2k va 2k+1 la mot cap nguoc nhau (canh nguoc chi phi am)
vector<vector<int>> adj;

void addEdge(int u, int v, ll cap, ll cost) {
    adj[u].push_back(edges.size()); edges.push_back({v, cap, cost});
    adj[v].push_back(edges.size()); edges.push_back({u, 0, -cost});
}

int main() {
    ll K;
    scanf("%d %d %lld", &n, &m, &K);
    adj.assign(n + 1, {});
    for (int i = 0; i < m; i++) {
        int u, v;
        ll c, d;
        scanf("%d %d %lld %lld", &u, &v, &c, &d);
        addEdge(u, v, c, d);
    }
    ll flow = 0, cost = 0;
    while (flow < K) {
        // SPFA tim duong re nhat tu 1 toi n tren do thi du
        vector<ll> dist(n + 1, LLONG_MAX);
        vector<int> prevEdge(n + 1, -1), inQueue(n + 1, 0);
        queue<int> q;
        dist[1] = 0; q.push(1); inQueue[1] = 1;
        while (!q.empty()) {
            int u = q.front(); q.pop(); inQueue[u] = 0;
            for (int id : adj[u]) {
                Edge &e = edges[id];
                if (e.cap > 0 && dist[u] + e.cost < dist[e.to]) {
                    dist[e.to] = dist[u] + e.cost;
                    prevEdge[e.to] = id;
                    if (!inQueue[e.to]) { inQueue[e.to] = 1; q.push(e.to); }
                }
            }
        }
        if (dist[n] == LLONG_MAX) break;   // khong con duong tang
        // luong tang = suc chua nho nhat tren duong, nhung khong vuot qua phan con thieu
        ll push = K - flow;
        for (int v = n; v != 1; v = edges[prevEdge[v] ^ 1].to)
            push = min(push, edges[prevEdge[v]].cap);
        for (int v = n; v != 1; v = edges[prevEdge[v] ^ 1].to) {
            edges[prevEdge[v]].cap -= push;
            edges[prevEdge[v] ^ 1].cap += push;
        }
        flow += push;
        cost += push * dist[n];
    }
    printf("%lld %lld\n", flow, cost);
    return 0;
}
