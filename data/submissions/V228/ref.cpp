// V228 - Kiem tra nguyen to Miller-Rabin tat dinh cho so 64 bit
// Viet n - 1 = d * 2^s (d le). Voi moi co so a: x = a^d mod n; neu x = 1 hoac x = n - 1 thi qua;
// neu binh phuong toi da s - 1 lan ma khong gap n - 1 thi n chac chan la hop so.
// 12 co so nguyen to dau tien (2..37) du de dung cho moi n < 3 * 10^23 (moi so 64 bit).
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef __int128 i128;

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
    for (ull p : bases) {
        if (n % p == 0) return n == p;
    }
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

int main() {
    int q;
    cin >> q;
    while (q--) {
        ull n;
        cin >> n;
        cout << (isPrime(n) ? "CO" : "KHONG") << "\n";
    }
    return 0;
}
