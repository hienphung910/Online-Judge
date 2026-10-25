// V296 - Dem so cach cai tui gioi han so luong bang cua so truot theo so du
// g[s] = f[s] + f[s-w] + ... + f[s-c*w]  (lay 0..c dong xu menh gia w).
// Cac chi so cung du khi chia w, cua so dai c+1 truot dan:
//     g[s] = f[s] + g[s-w] - f[s-(c+1)*w]
// Moi loai xu ton O(S), tong O(n*S).
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;

int main() {
    int n, S;
    cin >> n >> S;
    vector<long long> f(S + 1, 0), g(S + 1);
    f[0] = 1;
    for (int i = 0; i < n; i++) {
        long long w, c;
        cin >> w >> c;
        for (long long s = 0; s <= S; s++) {
            g[s] = f[s];
            if (s >= w) g[s] += g[s - w];
            if (s >= (c + 1) * w) g[s] -= f[s - (c + 1) * w];
            g[s] = ((g[s] % MOD) + MOD) % MOD;
        }
        f = g;
    }
    cout << f[S] << "\n";
    return 0;
}
