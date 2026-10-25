// V009 - BFS tren luoi tu o S, O(R * C)
// d[x][y] = so buoc it nhat de di tu S den o (x, y), -1 neu chua toi duoc.
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int r, c;
    cin >> r >> c;
    vector<string> g(r);
    for (auto &row : g) cin >> row;

    vector<vector<int>> d(r, vector<int>(c, -1));
    queue<pair<int, int>> q;
    int tx = 0, ty = 0;
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++) {
            if (g[i][j] == 'S') { d[i][j] = 0; q.push({i, j}); }
            if (g[i][j] == 'T') { tx = i; ty = j; }
        }

    int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();
        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k], ny = y + dy[k];
            if (nx < 0 || nx >= r || ny < 0 || ny >= c) continue;
            if (g[nx][ny] == '#' || d[nx][ny] != -1) continue;
            d[nx][ny] = d[x][y] + 1;
            q.push({nx, ny});
        }
    }
    cout << d[tx][ty] << '\n';
    return 0;
}
