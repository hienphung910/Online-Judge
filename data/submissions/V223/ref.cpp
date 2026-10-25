// V223 - Dem k trong [1, n] nguyen to cung nhau voi n = phi(n), phan tich n bang chia thu
// phi(n) = n * tich (1 - 1/p) qua cac uoc nguyen to p cua n; lam phep chia truoc roi moi nhan de khong tran.
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
    if (n > 1) res = res / n * (n - 1);   // con lai mot uoc nguyen to lon hon can bac hai
    return res;
}

int main() {
    int q;
    cin >> q;
    while (q--) {
        ll n;
        cin >> n;
        cout << phi(n) << "\n";
    }
    return 0;
}
