// V060 - Luy thua nhanh a^b mod m voi m toi 10^18 (nhan qua __int128)
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

ull mulmod(ull a, ull b, ull m) {
    return (unsigned __int128)a * b % m;
}

ull power(ull a, ull b, ull m) {
    ull r = 1 % m;          // a^0 = 1, nhung neu m = 1 thi ket qua la 0
    a %= m;
    while (b > 0) {
        if (b & 1) r = mulmod(r, a, m);
        a = mulmod(a, a, m);
        b >>= 1;
    }
    return r;
}

int main() {
    int q;
    cin >> q;
    while (q--) {
        ull a, b, m;
        cin >> a >> b >> m;
        cout << power(a, b, m) << "\n";
    }
    return 0;
}
