// V138 - BFS tren khong gian trang thai: bai toan hai binh nuoc
// Trang thai (x, y) = luong nuoc trong binh 1 va binh 2. Moi thao tac la mot canh.
// BFS tu (0, 0), dung khi gap trang thai co x == c hoac y == c.
#include <bits/stdc++.h>
using namespace std;

int solve(int a, int b, int c) {
    vector<vector<int>> d(a + 1, vector<int>(b + 1, -1));
    queue<pair<int, int>> q;
    d[0][0] = 0;
    q.push({0, 0});
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();
        if (x == c || y == c) return d[x][y];
        int p1 = min(x, b - y), p2 = min(y, a - x);  // luong do tu binh 1 sang 2, tu 2 sang 1
        pair<int, int> nxt[6] = {{a, y}, {x, b}, {0, y}, {x, 0}, {x - p1, y + p1}, {x + p2, y - p2}};
        for (auto [nx, ny] : nxt)
            if (d[nx][ny] == -1) {
                d[nx][ny] = d[x][y] + 1;
                q.push({nx, ny});
            }
    }
    return -1;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int a, b, c;
        cin >> a >> b >> c;
        cout << solve(a, b, c) << '\n';
    }
    return 0;
}
