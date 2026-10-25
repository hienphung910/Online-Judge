// V066 - Sang tren doan [L, R] voi R toi 10^12: dung cac so nguyen to <= 10^6 de gach hop so
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int S = 1000000;   // sqrt(10^12)
bool notPrime[S + 1];

int main() {
    ll L, R;
    cin >> L >> R;
    vector<int> primes;
    for (int i = 2; i <= S; i++) {
        if (notPrime[i]) continue;
        primes.push_back(i);
        for (ll j = (ll)i * i; j <= S; j += i) notPrime[j] = true;
    }
    vector<bool> composite(R - L + 1, false);   // composite[x - L]
    for (int p : primes) {
        if ((ll)p * p > R) break;
        ll start = max((ll)p * p, (L + p - 1) / p * p);   // boi dau tien >= L, khong gach chinh p
        for (ll x = start; x <= R; x += p) composite[x - L] = true;
    }
    if (L == 1) composite[0] = true;   // 1 khong phai so nguyen to
    ll cnt = 0;
    for (ll x = L; x <= R; x++)
        if (!composite[x - L]) cnt++;
    cout << cnt << "\n";
    return 0;
}
