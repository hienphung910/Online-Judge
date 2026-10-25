// V212 - QHD bitmask theo duong vien (broken profile): dem so cach lat domino 1x2
// Duyet tung o theo hang. Bit j cua mask = o (i, j) da bi lap boi domino dung tu o phia tren.
// Sau khi xu ly o (i, j), bit j chuyen thanh trang thai cua o (i + 1, j).
#include <bits/stdc++.h>
using namespace std;
const int MOD = 1000000007;

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> g(n);
    for (auto &s : g) cin >> s;
    auto freeCell = [&](int i, int j) { return i < n && j < m && g[i][j] == '.'; };
    vector<int> dp(1 << m, 0), nd(1 << m);
    dp[0] = 1;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            fill(nd.begin(), nd.end(), 0);
            for (int mask = 0; mask < (1 << m); mask++) {
                int ways = dp[mask];
                if (!ways) continue;
                bool filled = mask >> j & 1;
                int base = mask & ~(1 << j);              // bit j cua o (i + 1, j) mac dinh = 0
                auto add = [&](int nm) { nd[nm] = (nd[nm] + ways) % MOD; };
                if (g[i][j] == '#' || filled) {           // o bi chan (khi do filled luon = 0) hoac da lap
                    add(base);
                    continue;
                }
                if (freeCell(i + 1, j)) add(base | (1 << j));                     // domino dung
                if (freeCell(i, j + 1) && !(mask >> (j + 1) & 1)) add(base | (1 << (j + 1)));   // domino nam
            }
            swap(dp, nd);
        }
    cout << dp[0] << "\n";
    return 0;
}
