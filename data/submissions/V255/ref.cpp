// V255 - Phan ra trong tam (centroid): dem cap dinh cach nhau dung k canh
#include <bits/stdc++.h>
using namespace std;

int n, k;
vector<vector<int>> adj;
vector<char> removed;
vector<int> sz, par, cnt;  // cnt[d] = so dinh da xet co khoang cach d toi trong tam
long long answer = 0;

// BFS trong thanh phan chua s (bo qua dinh da xoa), tra ve thu tu tham
vector<int> bfs(int s, vector<int>& dist) {
    vector<int> order = {s};
    par[s] = 0; dist[s] = 0;
    for (size_t i = 0; i < order.size(); i++) {
        int u = order[i];
        for (int v : adj[u])
            if (!removed[v] && v != par[u]) { par[v] = u; dist[v] = dist[u] + 1; order.push_back(v); }
    }
    return order;
}

vector<int> dist;

int findCentroid(int s) {
    vector<int> order = bfs(s, dist);
    int total = order.size();
    for (int i = total - 1; i >= 0; i--) {  // tinh kich thuoc cay con tu la len
        int u = order[i];
        sz[u] = 1;
        for (int v : adj[u]) if (!removed[v] && v != par[u]) sz[u] += sz[v];
    }
    for (int u : order) {  // trong tam: moi phan con lai sau khi xoa u deu <= total/2
        int big = total - sz[u];
        for (int v : adj[u]) if (!removed[v] && v != par[u]) big = max(big, sz[v]);
        if (big * 2 <= total) return u;
    }
    return s;
}

void solve(int s) {
    int c = findCentroid(s);
    removed[c] = 1;
    vector<int> used = {0};
    cnt[0] = 1;
    for (int v : adj[c]) {
        if (removed[v]) continue;
        vector<int> order = bfs(v, dist);  // dist tinh tu v, khoang cach toi c la dist + 1
        for (int u : order) {
            int d = dist[u] + 1;
            if (d <= k) answer += cnt[k - d];  // ghep voi cac nhanh truoc
        }
        for (int u : order) {
            int d = dist[u] + 1;
            if (d <= k) { cnt[d]++; used.push_back(d); }
        }
    }
    for (int d : used) cnt[d] = 0;
    for (int v : adj[c]) if (!removed[v]) solve(v);  // do sau de quy chi O(log n)
}

int main() {
    scanf("%d %d", &n, &k);
    adj.resize(n + 1);
    for (int i = 1; i < n; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        adj[u].push_back(v); adj[v].push_back(u);
    }
    removed.assign(n + 1, 0); sz.assign(n + 1, 0); par.assign(n + 1, 0);
    dist.assign(n + 1, 0); cnt.assign(n + 1, 0);
    if (k <= n) solve(1);  // k > n - 1 thi khong co cap nao
    printf("%lld\n", answer);
    return 0;
}
