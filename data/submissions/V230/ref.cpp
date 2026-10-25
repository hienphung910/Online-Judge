// V230 - Phan tich so 64 bit bang Pollard rho (Brent) + Miller-Rabin
// Tu phan tich suy ra uoc nguyen to lon nhat va so uoc d(n) = tich (e_i + 1).
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;

ull mulmod(ull a, ull b, ull m) { return (ull)((unsigned __int128)a * b % m); }

ull power(ull a, ull e, ull m) {
    ull r = 1;
    a %= m;
    while (e > 0) {
        if (e & 1) r = mulmod(r, a, m);
        a = mulmod(a, a, m);
        e >>= 1;
    }
    return r;
}

bool isPrime(ull n) {
    if (n < 2) return false;
    ull bases[12] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (ull p : bases)
        if (n % p == 0) return n == p;
    ull d = n - 1;
    int s = 0;
    while (d % 2 == 0) { d /= 2; s++; }
    for (ull a : bases) {
        ull x = power(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool composite = true;
        for (int i = 1; i < s; i++) {
            x = mulmod(x, x, n);
            if (x == n - 1) { composite = false; break; }
        }
        if (composite) return false;
    }
    return true;
}

mt19937_64 rng(20261025);

// tra ve mot uoc thuc su cua hop so n (n le, khong phai so nguyen to)
ull rho(ull n) {
    while (true) {
        ull c = rng() % (n - 1) + 1;
        ull x = rng() % n, y = x, g = 1, q = 1, xs = x;
        auto f = [&](ull v) { return (mulmod(v, v, n) + c) % n; };
        for (ull r = 1; g == 1; r <<= 1) {
            x = y;
            for (ull i = 0; i < r; i++) y = f(y);
            for (ull k = 0; k < r && g == 1; k += 128) {
                xs = y;
                for (ull i = 0; i < 128 && i < r - k; i++) {
                    y = f(y);
                    q = mulmod(q, x > y ? x - y : y - x, n);
                }
                g = __gcd(q, n);
            }
        }
        if (g == n) {                         // gop qua nhieu, lui lai tung buoc
            g = 1;
            while (g == 1) {
                xs = f(xs);
                g = __gcd(x > xs ? x - xs : xs - x, n);
            }
        }
        if (g != n) return g;
    }
}

void factor(ull n, map<ull, int> &f) {
    if (n == 1) return;
    if (isPrime(n)) { f[n]++; return; }
    ull d = (n % 2 == 0) ? 2 : rho(n);
    factor(d, f);
    factor(n / d, f);
}

int main() {
    int q;
    cin >> q;
    while (q--) {
        ull n;
        cin >> n;
        map<ull, int> f;
        for (ull p = 2; p < 1000; p++)        // chia thu cac uoc nho truoc cho nhanh
            while (n % p == 0) { f[p]++; n /= p; }
        factor(n, f);
        ull largest = f.rbegin()->first;
        ull d = 1;
        for (auto &pe : f) d *= pe.second + 1;
        cout << largest << " " << d << "\n";
    }
    return 0;
}
