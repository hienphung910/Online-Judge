// V231 - C(n, k) mod m voi m khong chinh phuong: Lucas cho tung uoc nguyen to p cua m, roi ghep bang CRT
// Lucas: C(n, k) = tich C(n_i, k_i) (mod p) voi n_i, k_i la cac chu so trong he co so p.
// CRT: cac p doi mot nguyen to cung nhau nen ghep lan luot x = r_p (mod p).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll power(ll a, ll e, ll m) {
    ll r = 1 % m;
    a %= m;
    while (e > 0) {
        if (e & 1) r = r * a % m;
        a = a * a % m;
        e >>= 1;
    }
    return r;
}

struct Prime {
    ll p;
    vector<ll> fact;       // fact[i] = i! mod p, 0 <= i < p
    ll smallC(ll n, ll k) {        // n, k < p
        if (k > n) return 0;
        return fact[n] * power(fact[k] * fact[n - k] % p, p - 2, p) % p;
    }
    ll lucas(ll n, ll k) {
        ll r = 1;
        while ((n > 0 || k > 0) && r > 0) {
            r = r * smallC(n % p, k % p) % p;
            n /= p;
            k /= p;
        }
        return r;
    }
};

int main() {
    ll m;
    int q;
    cin >> m >> q;
    vector<Prime> ps;
    ll t = m;
    for (ll p = 2; p * p <= t; p++) {
        if (t % p == 0) { ps.push_back({p, {}}); t /= p; }
    }
    if (t > 1) ps.push_back({t, {}});
    for (auto &P : ps) {
        P.fact.assign(P.p, 1);
        for (ll i = 1; i < P.p; i++) P.fact[i] = P.fact[i - 1] * i % P.p;
    }
    while (q--) {
        ll n, k;
        cin >> n >> k;
        ll x = 0, M = 1;                    // x = C(n, k) mod M
        if (k <= n) {
            for (auto &P : ps) {
                ll r = P.lucas(n, k);
                // tim t: x + M*t = r (mod p)
                ll tt = ((r - x % P.p) % P.p + P.p) % P.p * power(M % P.p, P.p - 2, P.p) % P.p;
                x += M * tt;
                M *= P.p;
            }
        }
        cout << x % m << "\n";
    }
    return 0;
}
