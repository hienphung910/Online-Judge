// V067 - Tong sigma(1) + ... + sigma(n) = tong d * (n / d), gom cac d cung thuong n / d (n toi 10^12)
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll MOD = 1000000007LL;
const ll INV2 = 500000004LL;   // nghich dao cua 2 theo modulo MOD

int main() {
    int q;
    cin >> q;
    while (q--) {
        ll n;
        cin >> n;
        ll ans = 0;
        for (ll l = 1; l <= n;) {
            ll v = n / l;          // moi d trong [l, r] deu co n / d = v
            ll r = n / v;
            ll sumLR = (l + r) % MOD * ((r - l + 1) % MOD) % MOD * INV2 % MOD;   // l + ... + r
            ans = (ans + v % MOD * sumLR) % MOD;
            l = r + 1;
        }
        cout << ans << "\n";
    }
    return 0;
}
