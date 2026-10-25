// V284 - Khop mau co ky tu dai dien '?' o ca hai xau bang NTT
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll MOD = 998244353, G = 3;

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

void ntt(vector<ll> &f, bool invert) {
    int n = f.size();
    for (int i = 1, j = 0; i < n; i++) {
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

int main() {
    static char bufT[20005], bufP[20005];
    scanf("%s %s", bufT, bufP);
    string t = bufT, p = bufP;
    int n = t.size(), m = p.size();
    int sz = 1;
    while (sz < n + m) sz <<= 1;
    // ma hoa: '?' = 0, 'a'..'z' = 1..26; dao nguoc mau
    vector<ll> T1(sz), T2(sz), T3(sz), P1(sz), P2(sz), P3(sz);
    for (int i = 0; i < n; i++) {
        ll x = t[i] == '?' ? 0 : t[i] - 'a' + 1;
        T1[i] = x; T2[i] = x * x; T3[i] = x * x * x;
    }
    for (int j = 0; j < m; j++) {
        ll y = p[m - 1 - j] == '?' ? 0 : p[m - 1 - j] - 'a' + 1;
        P1[j] = y; P2[j] = y * y; P3[j] = y * y * y;
    }
    for (auto *v : {&T1, &T2, &T3, &P1, &P2, &P3}) ntt(*v, false);
    // tong y*x*(y-x)^2 = y^3*x - 2*y^2*x^2 + y*x^3, bang 0 khi va chi khi moi cap khop
    vector<ll> S(sz);
    for (int i = 0; i < sz; i++)
        S[i] = (P3[i] * T1[i] % MOD - 2 * P2[i] % MOD * T2[i] % MOD + 2 * MOD + P1[i] * T3[i] % MOD) % MOD;
    ntt(S, true);
    int cnt = 0, first = -1;
    for (int i = 0; i + m <= n; i++)
        if (S[i + m - 1] == 0) {
            cnt++;
            if (first == -1) first = i + 1;
        }
    printf("%d\n%d\n", cnt, first);
    return 0;
}
