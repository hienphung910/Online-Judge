// V229 - Chia keo chia n vat giong nhau vao k ngan, moi ngan toi da c vat (bao ham - loai tru)
// Khong gioi han: C(n + k - 1, k - 1). Ep j ngan "tran" (>= c + 1 vat): bot di j*(c+1) vat.
// Dap an = tong_j (-1)^j * C(k, j) * C(n - j*(c+1) + k - 1, k - 1), voi j*(c+1) <= n.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
const int MAXF = 200000;

ll fact[MAXF + 1], inv[MAXF + 1];

ll power(ll a, ll e) {
    ll r = 1;
    a %= MOD;
    while (e > 0) {
        if (e & 1) r = r * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return r;
}

ll C(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
}

int main() {
    fact[0] = 1;
    for (int i = 1; i <= MAXF; i++) fact[i] = fact[i - 1] * i % MOD;
    inv[MAXF] = power(fact[MAXF], MOD - 2);
    for (int i = MAXF; i > 0; i--) inv[i - 1] = inv[i] * i % MOD;

    int q;
    cin >> q;
    while (q--) {
        ll n, k, c;
        cin >> n >> k >> c;
        ll ans = 0;
        for (ll j = 0; j <= k && j * (c + 1) <= n; j++) {
            ll term = C(k, j) * C(n - j * (c + 1) + k - 1, k - 1) % MOD;
            if (j % 2 == 0) ans = (ans + term) % MOD;
            else ans = (ans - term + MOD) % MOD;
        }
        cout << ans << "\n";
    }
    return 0;
}
