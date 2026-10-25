// V202 - Luy thua ma tran 3x3 cho cong thuc truy hoi f(n) = a*f(n-1) + b*f(n-2) + c
// Vector trang thai (f(i), f(i-1), 1) nhan voi ma tran M thi duoc (f(i+1), f(i), 1).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<vector<ll>> Mat;
const ll MOD = 1000000007;

Mat mul(const Mat &A, const Mat &B) {
    int k = A.size();
    Mat C(k, vector<ll>(k, 0));
    for (int i = 0; i < k; i++)
        for (int t = 0; t < k; t++)
            for (int j = 0; j < k; j++)
                C[i][j] = (C[i][j] + A[i][t] * B[t][j]) % MOD;
    return C;
}

int main() {
    ll a, b, c, f0, f1;
    int T;
    cin >> a >> b >> c >> f0 >> f1 >> T;
    Mat M = {{a % MOD, b % MOD, c % MOD}, {1, 0, 0}, {0, 0, 1}};
    while (T--) {
        ll n;
        cin >> n;
        if (n == 0) { cout << f0 % MOD << "\n"; continue; }
        // tinh M^(n-1)
        Mat R = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}, P = M;
        for (ll e = n - 1; e > 0; e >>= 1) {
            if (e & 1) R = mul(R, P);
            P = mul(P, P);
        }
        // f(n) = R[0][0]*f(1) + R[0][1]*f(0) + R[0][2]*1
        ll ans = (R[0][0] * (f1 % MOD) + R[0][1] * (f0 % MOD) + R[0][2]) % MOD;
        cout << ans << "\n";
    }
    return 0;
}
