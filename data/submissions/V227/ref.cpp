// V227 - Dem toan anh (moi mon xuat hien it nhat mot lan) bang bao ham - loai tru
// So cach = tong_{j=0..k} (-1)^j * C(k, j) * (k - j)^n  (j la so mon bi bo qua bat buoc).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
const int MAXK = 1000000;

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

ll fact[MAXK + 1], inv[MAXK + 1];

ll C(int n, int r) {
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
}

int main() {
    fact[0] = 1;
    for (int i = 1; i <= MAXK; i++) fact[i] = fact[i - 1] * i % MOD;
    inv[MAXK] = power(fact[MAXK], MOD - 2);
    for (int i = MAXK; i > 0; i--) inv[i - 1] = inv[i] * i % MOD;

    int q;
    cin >> q;
    while (q--) {
        ll n;
        int k;
        cin >> n >> k;
        ll ans = 0;
        for (int j = 0; j <= k; j++) {
            ll term = C(k, j) * power(k - j, n) % MOD;
            if (j % 2 == 0) ans = (ans + term) % MOD;
            else ans = (ans - term + MOD) % MOD;
        }
        cout << ans << "\n";
    }
    return 0;
}
