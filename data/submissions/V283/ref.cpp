// V283 - Nhan hai da thuc bang NTT modulo 998244353
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll MOD = 998244353, G = 3;  // 998244353 = 119 * 2^23 + 1, 3 la can nguyen thuy

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

// bien doi NTT tai cho; invert = true la bien doi nguoc
void ntt(vector<ll> &f, bool invert) {
    int n = f.size();
    for (int i = 1, j = 0; i < n; i++) {  // dao bit
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(f[i], f[j]);
    }
    for (int len = 2; len <= n; len <<= 1) {
        ll w = power(G, (MOD - 1) / len);
        if (invert) w = power(w, MOD - 2);
        for (int i = 0; i < n; i += len) {
            ll wk = 1;
            for (int k = 0; k < len / 2; k++) {
                ll u = f[i + k], v = f[i + k + len / 2] * wk % MOD;
                f[i + k] = (u + v) % MOD;
                f[i + k + len / 2] = (u - v + MOD) % MOD;
                wk = wk * w % MOD;
            }
        }
    }
    if (invert) {
        ll inv = power(n, MOD - 2);
        for (ll &x : f) x = x * inv % MOD;
    }
}

vector<ll> gen(int n, ll s, ll u, ll w) {
    vector<ll> a(n);
    a[0] = s;
    for (int i = 1; i < n; i++) a[i] = (a[i - 1] * u + w) % MOD;
    return a;
}

int main() {
    int n, m;
    ll s1, u1, w1, s2, u2, w2;
    scanf("%d %lld %lld %lld", &n, &s1, &u1, &w1);
    scanf("%d %lld %lld %lld", &m, &s2, &u2, &w2);
    vector<ll> a = gen(n, s1, u1, w1), b = gen(m, s2, u2, w2);
    int sz = 1;
    while (sz < n + m - 1) sz <<= 1;
    a.resize(sz); b.resize(sz);
    ntt(a, false); ntt(b, false);
    for (int i = 0; i < sz; i++) a[i] = a[i] * b[i] % MOD;
    ntt(a, true);
    ll x = 0;
    for (int k = 0; k < n + m - 1; k++) x ^= a[k];
    printf("%lld\n", x);
    return 0;
}
