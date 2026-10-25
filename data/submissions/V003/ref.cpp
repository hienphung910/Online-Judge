// V003 - To hop C(n, k) mod 1e9+7: tinh truoc giai thua va nghich dao bang luy thua nhanh
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;
const int MAXN = 1000000;
long long fact[MAXN + 1], inv[MAXN + 1];   // inv[i] = (i!)^-1 mod MOD

long long power(long long a, long long b) {
    long long r = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) r = r * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    fact[0] = 1;
    for (int i = 1; i <= MAXN; i++) fact[i] = fact[i - 1] * i % MOD;
    inv[MAXN] = power(fact[MAXN], MOD - 2);              // dinh ly Fermat nho
    for (int i = MAXN; i > 0; i--) inv[i - 1] = inv[i] * i % MOD;

    int q;
    cin >> q;
    string res;
    while (q--) {
        int n, k;
        cin >> n >> k;
        long long ans = 0;
        if (k <= n) ans = fact[n] * inv[k] % MOD * inv[n - k] % MOD;
        res += to_string(ans);
        res += '\n';
    }
    cout << res;
    return 0;
}
