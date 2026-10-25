// V282 - Logarit roi rac voi modulo bat ky (baby-step giant-step mo rong)
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// tim x >= 0 nho nhat voi a^x = b (mod m), khong co thi tra -1
ll exLog(ll a, ll b, ll m) {
    a %= m; b %= m;
    if (1 % m == b) return 0;
    // buoc 1: khu dan uoc chung cua a va m
    // sau k buoc: t * a^(x-k) = b (mod m) voi gcd(a, m) = 1
    ll t = 1, k = 0, g;
    while ((g = __gcd(a, m)) > 1) {
        if (b == t) return k;
        if (b % g != 0) return -1;
        b /= g; m /= g;
        t = t * (a / g) % m;
        k++;
    }
    if (b == t % m) return k;
    // buoc 2: BSGS cho t * a^y = b, y >= 1; x = y + k
    ll s = (ll)sqrt((double)m) + 1;
    unordered_map<ll, ll> baby;  // b * a^j -> j lon nhat
    baby.reserve(2 * s);
    ll cur = b % m;
    for (ll j = 0; j < s; j++) {
        baby[cur] = j;
        cur = cur * a % m;
    }
    ll as = 1;
    for (ll j = 0; j < s; j++) as = as * a % m;  // a^s
    ll gnt = t % m;
    for (ll i = 1; i <= s; i++) {
        gnt = gnt * as % m;  // t * a^(i*s)
        auto it = baby.find(gnt);
        if (it != baby.end()) return i * s - it->second + k;  // y = i*s - j
    }
    return -1;
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        ll a, b, m;
        scanf("%lld %lld %lld", &a, &b, &m);
        printf("%lld\n", exLog(a, b, m));
    }
    return 0;
}
