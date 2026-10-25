// V118 - Mang hieu 2 chieu: cong 1 vao ca hinh chu nhat trong O(1), cong don O(R*C)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int R, C, K, T;
    cin >> R >> C >> K >> T;
    vector<vector<int>> d(R + 2, vector<int>(C + 2, 0));
    for (int k = 0; k < K; k++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        d[x1][y1]++;
        d[x1][y2 + 1]--;
        d[x2 + 1][y1]--;
        d[x2 + 1][y2 + 1]++;
    }
    long long dem = 0;
    for (int i = 1; i <= R; i++)
        for (int j = 1; j <= C; j++) {
            // sau buoc nay d[i][j] = so tam tham phu o (i, j)
            d[i][j] += d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1];
            if (d[i][j] >= T) dem++;
        }
    cout << dem << "\n";
    return 0;
}
