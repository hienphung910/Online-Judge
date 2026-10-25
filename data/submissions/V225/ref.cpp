// V225 - Dinh ly thang du Trung Hoa tong quat (modulo khong nhat thiet nguyen to cung nhau)
// Gop lan luot: x = r1 (mod m1), x = r2 (mod m2). Dat g = gcd(m1, m2).
// Co nghiem khi (r2 - r1) chia het cho g; khi do x = r1 + m1 * t voi t = (r2 - r1)/g * nghich dao(m1/g) (mod m2/g).
// Cac tich co the toi 10^36 nen dung __int128.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 i128;

// tra ve g = gcd(a, b) va x, y voi a*x + b*y = g
ll extgcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) { x = 1; y = 0; return a; }
    ll x1, y1;
    ll g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int k;
        cin >> k;
        ll r = 0, m = 1;            // nghiem hien tai: x = r (mod m)
        bool ok = true;
        for (int i = 0; i < k; i++) {
            ll r2, m2;
            cin >> r2 >> m2;
            if (!ok) continue;
            ll p, q;
            ll g = extgcd(m, m2, p, q);     // m*p + m2*q = g
            if ((r2 - r) % g != 0) { ok = false; continue; }
            ll mg = m2 / g;
            i128 t = (i128)((r2 - r) / g) % mg * (p % mg) % mg;
            if (t < 0) t += mg;
            i128 x = (i128)r + (i128)m * t;
            m = m / g * m2;             // lcm, de bai dam bao <= 10^18
            r = (ll)(x % m);
        }
        cout << (ok ? r : -1) << "\n";
    }
    return 0;
}
