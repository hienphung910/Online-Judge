// V272 - Bai toan phan cong: luong cuc dai chi phi cuc tieu (SPFA tim duong tang re nhat)
#include <bits/stdc++.h>
using namespace std;

struct Edge { int to, cap, cost; };

int V;                        // so dinh cua mang
vector<Edge> edges;           // canh 2k va 2k+1 la mot cap nguoc nhau
vector<vector<int>> adj;

void addEdge(int u, int v, int cap, int cost) {
    adj[u].push_back(edges.size()); edges.push_back({v, cap, cost});
    adj[v].push_back(edges.size()); edges.push_back({u, 0, -cost});
}

int main() {
    int n;
    scanf("%d", &n);
    // dinh: 0 = nguon, 1..n = doi, n+1..2n = cong trinh, 2n+1 = dich
    V = 2 * n + 2;
    int s = 0, t = 2 * n + 1;
    adj.assign(V, {});
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) {
            int c;
            scanf("%d", &c);
            addEdge(i, n + j, 1, c);
        }
    for (int i = 1; i <= n; i++) {
        addEdge(s, i, 1, 0);
        addEdge(n + i, t, 1, 0);
    }
    long long total = 0;
    for (int step = 0; step < n; step++) {
        // SPFA: duong di re nhat tu s toi t tren do thi du
        vector<long long> dist(V, LLONG_MAX);
        vector<int> prevEdge(V, -1), inQueue(V, 0);
        queue<int> q;
        dist[s] = 0; q.push(s); inQueue[s] = 1;
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
        // tang 1 don vi luong doc theo duong vua tim
        for (int v = t; v != s; v = edges[prevEdge[v] ^ 1].to) {
            edges[prevEdge[v]].cap -= 1;
            edges[prevEdge[v] ^ 1].cap += 1;
        }
        total += dist[t];
    }
    printf("%lld\n", total);
    return 0;
}
