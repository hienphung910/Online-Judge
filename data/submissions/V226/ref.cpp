// V226 - Ky vong so loai the khac nhau sau k goi, tinh theo modulo 10^9 + 7
// Tuyen tinh cua ky vong: moi loai the vang mat voi xac suat ((n-1)/n)^k.
// E = n * (1 - ((n-1)/n)^k); chia cho n bang nhan nghich dao (Fermat: n^(p-2)).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;

ll power(ll a, ll e) {
    ll r = 1;
    a %= MOD;
    while (e > 0) {
        if (e & 1) r = r * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return r;
}

int main() {
    int q;
    cin >> q;
    while (q--) {
        ll n, k;
        cin >> n >> k;
        ll pMiss = power((n - 1) % MOD * power(n, MOD - 2) % MOD, k);   // xac suat mot loai khong xuat hien
        ll ans = n % MOD * ((1 - pMiss + MOD) % MOD) % MOD;
        cout << ans << "\n";
    }
    return 0;
}
