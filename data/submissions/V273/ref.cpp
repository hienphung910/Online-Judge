// V273 - Lat gach 1x2: cap ghep cuc dai tren luoi to mau ban co (Hopcroft-Karp)
#include <bits/stdc++.h>
using namespace std;

int R, C;
vector<string> g;
vector<vector<int>> adj;      // adj[o trang] = cac o den ke ben con trong
vector<int> matchL, matchR, dist;
int nL;                       // so dinh ben trai (o trang, (r + c) chan)

// BFS chia tang tu cac dinh trai chua ghep
bool bfs() {
    queue<int> q;
    bool found = false;
    for (int u = 0; u < nL; u++) {
        if (matchL[u] < 0) { dist[u] = 0; q.push(u); }
        else dist[u] = -1;
    }
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {
            int w = matchR[v];
            if (w < 0) found = true;
            else if (dist[w] < 0) { dist[w] = dist[u] + 1; q.push(w); }
        }
    }
    return found;
}

// DFS tim duong tang di dung theo tang
bool dfs(int u) {
    for (int v : adj[u]) {
        int w = matchR[v];
        if (w < 0 || (dist[w] == dist[u] + 1 && dfs(w))) {
            matchL[u] = v; matchR[v] = u;
            return true;
        }
    }
    dist[u] = -1;   // dinh nay khong con dung duoc trong pha nay
    return false;
}

int main() {
    cin >> R >> C;
    g.resize(R);
    for (auto &row : g) cin >> row;
    // danh so rieng o trang (trai) va o den (phai)
    vector<vector<int>> id(R, vector<int>(C, -1));
    int nR = 0;
    nL = 0;
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++)
            if (g[r][c] == '.') id[r][c] = ((r + c) % 2 == 0) ? nL++ : nR++;
    adj.assign(nL, {});
    int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};
    for (int r = 0; r < R; r++)
        for (int c = 0; c < C; c++) {
            if (g[r][c] != '.' || (r + c) % 2 != 0) continue;
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d], nc = c + dc[d];
                if (nr >= 0 && nr < R && nc >= 0 && nc < C && g[nr][nc] == '.')
                    adj[id[r][c]].push_back(id[nr][nc]);
            }
        }
    matchL.assign(nL, -1);
    matchR.assign(nR, -1);
    dist.assign(nL, -1);
    int ans = 0;
    while (bfs())
        for (int u = 0; u < nL; u++)
            if (matchL[u] < 0 && dfs(u)) ans++;
    printf("%d\n", ans);
    return 0;
}
