// V194 - Dien tich da giac don bang cong thuc shoelace (so nguyen 64 bit)
// S2 = |tong x_i*y_{i+1} - x_{i+1}*y_i| la 2 lan dien tich; in S2/2 va them ".5" neu S2 le.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int n;
    scanf("%d", &n);
    vector<ll> x(n), y(n);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &x[i], &y[i]);
    ll s2 = 0;
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        s2 += x[i] * y[j] - x[j] * y[i];
    }
    s2 = llabs(s2);
    if (s2 % 2 == 0) printf("%lld\n", s2 / 2);
    else printf("%lld.5\n", s2 / 2);
    return 0;
}
