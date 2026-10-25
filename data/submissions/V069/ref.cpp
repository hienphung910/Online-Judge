// V069 - Dem duong di tren luoi tranh o cam: to hop + nghich dao giai thua, tru dan theo o cam dau tien
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll MOD = 1000000007LL;
const int MAXF = 2000000;
ll fact[MAXF + 1], invFact[MAXF + 1];

ll power(ll a, ll b) {
    ll r = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) r = r * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return r;
}

ll ways(int down, int right) {   // so duong di xuong 'down' buoc, sang phai 'right' buoc
    return fact[down + right] * invFact[down] % MOD * invFact[right] % MOD;
}

int main() {
    fact[0] = 1;
    for (int i = 1; i <= MAXF; i++) fact[i] = fact[i - 1] * i % MOD;
    invFact[MAXF] = power(fact[MAXF], MOD - 2);
    for (int i = MAXF; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;

    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);
    vector<pair<int, int>> p(k);
    for (auto &x : p) scanf("%d %d", &x.first, &x.second);
    sort(p.begin(), p.end());          // theo hang, roi theo cot
    p.push_back({n, m});               // dich den luon dung sau cung

    vector<ll> f(p.size());            // f[i] = so duong toi o i khong qua o cam nao khac
    for (size_t i = 0; i < p.size(); i++) {
        f[i] = ways(p[i].first - 1, p[i].second - 1);
        for (size_t j = 0; j < i; j++)
            if (p[j].first <= p[i].first && p[j].second <= p[i].second)
                f[i] = (f[i] - f[j] * ways(p[i].first - p[j].first, p[i].second - p[j].second)) % MOD;
        f[i] = (f[i] + MOD) % MOD;
    }
    printf("%lld\n", f.back());
    return 0;
}
