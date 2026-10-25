// V034 - Mo phong robot tren luoi: huong 0..3 theo chieu kim dong ho, danh dau o da den
#include <bits/stdc++.h>
using namespace std;

int main() {
    int r, c;
    cin >> r >> c;
    vector<string> g(r);
    int x = 0, y = 0;
    for (int i = 0; i < r; i++) {
        cin >> g[i];
        for (int j = 0; j < c; j++) if (g[i][j] == 'S') { x = i; y = j; }
    }
    string lenh;
    cin >> lenh;
    int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};   // Bac, Dong, Nam, Tay
    string ten[4] = {"BAC", "DONG", "NAM", "TAY"};
    vector<vector<bool>> den(r, vector<bool>(c, false));
    den[x][y] = true;
    int huong = 0, vacham = 0, soO = 1;
    for (char ch : lenh) {
        if (ch == 'L') huong = (huong + 3) % 4;
        else if (ch == 'R') huong = (huong + 1) % 4;
        else {
            int nx = x + dx[huong], ny = y + dy[huong];
            if (nx < 0 || nx >= r || ny < 0 || ny >= c || g[nx][ny] == '#') { vacham++; continue; }
            x = nx; y = ny;
            if (!den[x][y]) { den[x][y] = true; soO++; }
        }
    }
    cout << x + 1 << " " << y + 1 << " " << ten[huong] << " " << vacham << " " << soO << "\n";
    return 0;
}
