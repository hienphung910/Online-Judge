// V221 - Tim so nguyen to nho nhat >= n bang kiem tra chia thu den can bac hai
// Khoang cach giua hai so nguyen to lien tiep duoi 10^12 chi vai tram, nen thu lan luot n, n+1, ...
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool laNguyenTo(ll x) {
    if (x < 2) return false;
    if (x < 4) return true;               // 2, 3
    if (x % 2 == 0 || x % 3 == 0) return false;
    for (ll d = 5; d * d <= x; d += 6)    // chi thu d = 6k-1 va 6k+1
        if (x % d == 0 || x % (d + 2) == 0) return false;
    return true;
}

int main() {
    int q;
    cin >> q;
    while (q--) {
        ll n;
        cin >> n;
        while (!laNguyenTo(n)) n++;
        cout << n << "\n";
    }
    return 0;
}
