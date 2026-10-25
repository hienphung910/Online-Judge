// V224 - Tinh a^b mod m voi b rat lon (chuoi chu so) bang dinh ly Euler mo rong
// Neu b >= phi(m): a^b = a^(b mod phi + phi) (mod m), dung ca khi gcd(a, m) > 1.
// Neu b < phi(m): tinh thang a^b. Khong duoc cong phi khi b nho (vi du 2^1 mod 8).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll phi(ll n) {
    ll res = n;
    for (ll p = 2; p * p <= n; p++) {
        if (n % p != 0) continue;
        while (n % p == 0) n /= p;
        res = res / p * (p - 1);
    }
    if (n > 1) res = res / n * (n - 1);
    return res;
}

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

int main() {
    int q;
    cin >> q;
    while (q--) {
        ll a, m;
        string b;
        cin >> a >> b >> m;
        ll f = phi(m);
        ll bmod = 0;            // b mod phi(m)
        bool lon = false;       // b >= phi(m) ?
        ll gt = 0;              // gia tri that cua b, chi theo doi khi b con nho
        for (char c : b) {
            bmod = (bmod * 10 + (c - '0')) % f;
            gt = gt * 10 + (c - '0');
            if (gt >= f) { lon = true; gt = f; }   // chan lai de khong tran
        }
        ll e = lon ? bmod + f : gt;
        cout << power(a, e, m) << "\n";
    }
    return 0;
}
