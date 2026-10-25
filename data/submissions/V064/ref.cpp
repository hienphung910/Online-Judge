// V064 - Nghich dao modulo bang thuat toan Euclid mo rong (m khong can nguyen to)
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// tra ve g = UCLN(a, b) va tim x, y sao cho a*x + b*y = g
ll extGcd(ll a, ll b, ll &x, ll &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    ll x1, y1;
    ll g = extGcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    int q;
    cin >> q;
    while (q--) {
        ll a, m;
        cin >> a >> m;
        ll x, y;
        ll g = extGcd(a % m, m, x, y);
        if (g != 1) cout << -1 << "\n";
        else cout << ((x % m) + m) % m << "\n";
    }
    return 0;
}
