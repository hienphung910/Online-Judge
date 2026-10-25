// V280 - Can bac hai modulo so nguyen to bang thuat toan Tonelli-Shanks
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll power(ll a, ll e, ll p) {
    ll r = 1;
    a %= p;
    while (e > 0) {
        if (e & 1) r = r * a % p;
        a = a * a % p;
        e >>= 1;
    }
    return r;
}

// tra ve mot x voi x*x = a (mod p), hoac -1 neu khong co
ll sqrtMod(ll a, ll p) {
    if (a == 0 || p == 2) return a;
    if (power(a, (p - 1) / 2, p) != 1) return -1;  // tieu chuan Euler
    ll q = p - 1;
    int s = 0;
    while (q % 2 == 0) { q /= 2; s++; }           // p - 1 = q * 2^s, q le
    ll z = 2;
    while (power(z, (p - 1) / 2, p) != p - 1) z++; // z khong chinh phuong
    ll c = power(z, q, p), x = power(a, (q + 1) / 2, p), t = power(a, q, p);
    int m = s;
    while (t != 1) {
        // tim i nho nhat de t^(2^i) = 1
        int i = 0;
        ll u = t;
        while (u != 1) { u = u * u % p; i++; }
        ll b = c;
        for (int j = 0; j < m - i - 1; j++) b = b * b % p;
        x = x * b % p;
        c = b * b % p;
        t = t * c % p;
        m = i;
    }
    return x;
}

int main() {
    int q;
    scanf("%d", &q);
    while (q--) {
        ll p, a;
        scanf("%lld %lld", &p, &a);
        ll x = sqrtMod(a, p);
        if (x != -1) x = min(x, p - x);
        printf("%lld\n", x);
    }
    return 0;
}
