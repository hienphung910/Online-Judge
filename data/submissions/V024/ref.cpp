// V024 - Logarit roi rac nho nhat bang baby-step giant-step
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll power(ll a, ll e, ll p) {
    ll r = 1 % p;
    a %= p;
    while (e > 0) {
        if (e & 1) r = r * a % p;
        a = a * a % p;
        e >>= 1;
    }
    return r;
}

// bang bam dia chi mo don gian: khoa = a^j mod p, gia tri = j
const int H = 1 << 17;
ll keyOf[H];
int valOf[H];

int slot(ll k) {
    int h = (int)((unsigned long long)k * 0x9E3779B97F4A7C15ULL >> 47);  // 17 bit cao
    while (keyOf[h] != -1 && keyOf[h] != k) h = (h + 1) & (H - 1);
    return h;
}

// tim x nho nhat voi a^x = b (mod p), p nguyen to; khong co thi tra -1
ll discreteLog(ll a, ll b, ll p) {
    ll m = (ll)ceil(sqrt((double)p));
    fill(keyOf, keyOf + H, -1);
    ll cur = 1;
    for (ll j = 0; j < m; j++) {
        int h = slot(cur);
        if (keyOf[h] == -1) { keyOf[h] = cur; valOf[h] = j; }  // chi giu j nho nhat
        cur = cur * a % p;
    }
    ll step = power(a, p - 1 - m % (p - 1), p);  // a^(-m) theo dinh ly Fermat nho
    ll g = b % p;
    for (ll i = 0; i <= m; i++) {  // x = i*m + j, duyet i tang dan
        int h = slot(g);
        if (keyOf[h] == g) return i * m + valOf[h];
        g = g * step % p;
    }
    return -1;
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        ll a, b, p;
        scanf("%lld %lld %lld", &a, &b, &p);
        printf("%lld\n", discreteLog(a, b, p));
    }
    return 0;
}
