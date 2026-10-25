// V078 - Sap xep dem (counting sort) tren gia tri nho, O(n + M)
#include <bits/stdc++.h>
using namespace std;

int main() {
    const long long MOD = 1000000007;
    long long n, x, A, B, M;
    cin >> n >> x >> A >> B >> M;
    vector<int> cnt(M, 0);              // cnt[v] = so kien nang v gam
    cnt[x]++;
    for (int i = 2; i <= n; i++) {
        x = (A * x + B) % M;
        cnt[x]++;
    }
    long long S = 0, viTri = 0;         // viTri = chi so cua phan tu dang xet trong day da sap xep
    for (long long v = 0; v < M; v++) {
        for (int t = 0; t < cnt[v]; t++) {
            viTri++;
            S = (S + viTri % MOD * v) % MOD;
        }
    }
    cout << S << "\n";
    return 0;
}
