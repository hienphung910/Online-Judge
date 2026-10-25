// V208 - Luy thua ma tran ke: dem so hanh trinh tu 1 den n dai tu 1 den K buoc
// Them dinh "kho" n+1: canh n -> n+1 va khuyen n+1 -> n+1.
// So duong di dai K+1 tu 1 den n+1 = tong so duong di dai 0..K tu 1 den n (dai 0 bang 0 vi n >= 2).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<vector<ll>> Mat;
const ll MOD = 1000000007;

Mat mul(const Mat &A, const Mat &B) {
    int k = A.size();
    Mat C(k, vector<ll>(k, 0));
    for (int i = 0; i < k; i++)
        for (int t = 0; t < k; t++) {
            if (A[i][t] == 0) continue;
            for (int j = 0; j < k; j++)
                C[i][j] = (C[i][j] + A[i][t] * B[t][j]) % MOD;
        }
    return C;
}

int main() {
    int n, m;
    ll K;
    cin >> n >> m >> K;
    int s = n + 1;                      // dinh 0..n-1 la ben xe, dinh n la kho
    Mat A(s, vector<ll>(s, 0));
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        A[u - 1][v - 1] = 1;
    }
    A[n - 1][n] = 1;
    A[n][n] = 1;
    Mat R(s, vector<ll>(s, 0));
    for (int i = 0; i < s; i++) R[i][i] = 1;
    for (ll e = K + 1; e > 0; e >>= 1) {
        if (e & 1) R = mul(R, A);
        A = mul(A, A);
    }
    cout << R[0][n] << "\n";
    return 0;
}
