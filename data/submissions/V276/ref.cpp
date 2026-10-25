// V276 - Chon du an (bao dong co trong so lon nhat) bang lat cat hep nhat
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
    int P, Q;
    scanf("%d %d", &P, &Q);
    // dinh: 0 = nguon, 1..P = du an, P+1..P+Q = thiet bi, P+Q+1 = dich
    V = P + Q + 2;
    S = 0; T = P + Q + 1;
    adj.assign(V, {});
    ll sumProfit = 0;
    for (int i = 1; i <= P; i++) {
        ll p;
        scanf("%lld", &p);
        sumProfit += p;
        addEdge(S, i, p);            // bo du an i = cat canh nay, mat p
    }
    for (int j = 1; j <= Q; j++) {
        ll q;
        scanf("%lld", &q);
        addEdge(P + j, T, q);        // thue thiet bi j = cat canh nay, ton q
    }
    for (int i = 1; i <= P; i++) {
        int k;
        scanf("%d", &k);
        while (k--) {
            int j;
            scanf("%d", &j);
            addEdge(i, P + j, INF);  // da lam du an i thi bat buoc thue thiet bi j
        }
    }
    ll flow = 0;
    while (bfs()) {
        ptr.assign(V, 0);
        while (ll f = dfs(S, INF)) flow += f;
    }
    // loi nhuan lon nhat = tong loi nhuan - lat cat hep nhat
    printf("%lld\n", sumProfit - flow);
    return 0;
}
