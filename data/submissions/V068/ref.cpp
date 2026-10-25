// V068 - Dinh ly Lucas: C(n, k) mod p voi p nguyen to nho, n, k toi 10^18
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll p;
vector<ll> fact, invFact;

ll power(ll a, ll b) {
    ll r = 1;
    a %= p;
    while (b > 0) {
        if (b & 1) r = r * a % p;
        a = a * a % p;
        b >>= 1;
    }
    return r;
}

ll smallC(ll a, ll b) {   // a, b < p
    if (b > a) return 0;
    return fact[a] * invFact[b] % p * invFact[a - b] % p;
}

int main() {
    int q;
    scanf("%lld %d", &p, &q);
    fact.assign(p, 1);
    invFact.assign(p, 1);
    for (ll i = 1; i < p; i++) fact[i] = fact[i - 1] * i % p;
    invFact[p - 1] = power(fact[p - 1], p - 2);
    for (ll i = p - 1; i > 0; i--) invFact[i - 1] = invFact[i] * i % p;

    while (q--) {
        ll n, k;
        scanf("%lld %lld", &n, &k);
        ll res = 1;
        if (k > n) res = 0;
        while (res != 0 && (n > 0 || k > 0)) {   // xet tung chu so co so p
            res = res * smallC(n % p, k % p) % p;
            n /= p;
            k /= p;
        }
        printf("%lld\n", res);
    }
    return 0;
}
