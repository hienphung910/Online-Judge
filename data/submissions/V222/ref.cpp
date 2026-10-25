// V222 - Phan tich thua so nguyen to bang chia thu den can bac hai, in dang p1^e1 * p2^e2 * ...
// Chia het cho d bao nhieu lan thi chia bay nhieu lan; phan con lai > 1 sau vong lap la mot so nguyen to.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int q;
    cin >> q;
    while (q--) {
        ll n;
        cin >> n;
        vector<pair<ll, int>> f;               // (thua so nguyen to, so mu)
        for (ll d = 2; d * d <= n; d++) {
            if (n % d != 0) continue;
            int e = 0;
            while (n % d == 0) { n /= d; e++; }
            f.push_back({d, e});
        }
        if (n > 1) f.push_back({n, 1});
        for (size_t i = 0; i < f.size(); i++) {
            if (i > 0) cout << " * ";
            cout << f[i].first;
            if (f[i].second > 1) cout << "^" << f[i].second;
        }
        cout << "\n";
    }
    return 0;
}
