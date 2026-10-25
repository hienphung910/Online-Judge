// V279 - Dem cap nguyen to cung nhau trong mang bang ham Mobius
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int V = 1000000;
int mu[V + 1], cnt[V + 1];
bool comp[V + 1];
vector<int> primes;

int main() {
    // sang tuyen tinh tinh mu
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
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int a;
        scanf("%d", &a);
        cnt[a]++;
    }
    // so cap (i<j) nguyen to cung nhau = tong mu(d) * C(c_d, 2), c_d = so phan tu chia het cho d
    ll ans = 0;
    for (int d = 1; d <= V; d++) {
        if (mu[d] == 0) continue;
        ll c = 0;
        for (int m = d; m <= V; m += d) c += cnt[m];
        ans += mu[d] * (c * (c - 1) / 2);
    }
    printf("%lld\n", ans);
    return 0;
}
