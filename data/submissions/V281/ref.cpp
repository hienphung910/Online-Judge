// V281 - Dem cap (x, y) co gcd = k bang nghich dao Mobius va chia khoi floor
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int V = 1000000;
int mu[V + 1], smu[V + 1];  // smu = tong tien to cua mu
bool comp[V + 1];
vector<int> primes;

int main() {
    mu[1] = 1;
    for (int i = 2; i <= V; i++) {
        if (!comp[i]) { primes.push_back(i); mu[i] = -1; }
        for (int p : primes) {
            if ((ll)i * p > V) break;
            comp[i * p] = true;
            if (i % p == 0) { mu[i * p] = 0; break; }
            mu[i * p] = -mu[i];
        }
    }
    for (int i = 1; i <= V; i++) smu[i] = smu[i - 1] + mu[i];

    int q;
    scanf("%d", &q);
    while (q--) {
        int a, b, k;
        scanf("%d %d %d", &a, &b, &k);
        // gcd(x, y) = k  <=>  x = k*x', y = k*y', gcd(x', y') = 1
        int A = a / k, B = b / k;
        if (A > B) swap(A, B);
        // dem cap nguyen to cung nhau = tong mu(d) * (A/d) * (B/d); gom cac d cung gia tri A/d, B/d
        ll ans = 0;
        for (int d = 1, nd; d <= A; d = nd + 1) {
            nd = min(A / (A / d), B / (B / d));
            ans += (ll)(smu[nd] - smu[d - 1]) * (A / d) * (B / d);
        }
        printf("%lld\n", ans);
    }
    return 0;
}
