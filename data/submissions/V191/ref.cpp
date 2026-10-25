// V191 - Dem xau khong chua P: QHD tren otomat KMP, O(N * |P| * A)
// Trang thai j = do dai tien to dai nhat cua P dang khop o cuoi xau da sinh (0 <= j < |P|).
// go[j][c] = trang thai moi khi them ky tu c (tinh bang ham tien to). Khong duoc den trang thai |P|.
#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;

int main() {
    int n, A;
    string p;
    cin >> n >> A >> p;
    int m = p.size();
    vector<int> pi(m, 0);
    for (int i = 1; i < m; i++) {
        int k = pi[i - 1];
        while (k > 0 && p[i] != p[k]) k = pi[k - 1];
        if (p[i] == p[k]) k++;
        pi[i] = k;
    }
    vector<vector<int>> go(m, vector<int>(A));
    for (int j = 0; j < m; j++)
        for (int c = 0; c < A; c++) {
            if (p[j] - 'a' == c) go[j][c] = j + 1;
            else go[j][c] = (j == 0) ? 0 : go[pi[j - 1]][c];   // pi[j-1] < j nen da tinh xong
        }
    vector<long long> dp(m, 0), nd(m);
    dp[0] = 1;
    for (int step = 0; step < n; step++) {
        fill(nd.begin(), nd.end(), 0);
        for (int j = 0; j < m; j++) {
            if (dp[j] == 0) continue;
            for (int c = 0; c < A; c++) {
                int t = go[j][c];
                if (t < m) nd[t] = (nd[t] + dp[j]) % MOD;   // t == m nghia la vua chua P -> bo
            }
        }
        swap(dp, nd);
    }
    long long ans = 0;
    for (int j = 0; j < m; j++) ans = (ans + dp[j]) % MOD;
    cout << ans << '\n';
    return 0;
}
