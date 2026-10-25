// V299 - Aliens trick (WQS binary search): dung k doan con roi nhau co tong lon nhat
// f(k) lom theo k. Phat moi doan lam: g(lam) = max (tong - lam * so doan), khong gioi han so doan,
// tinh bang QHD O(n). Khi hoa thi uu tien nhieu doan hon.
// lam lon nhat ma so doan toi uu >= k chinh la f(k) - f(k-1), va f(k) = g(lam) + lam * k.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> P;   // (gia tri, so doan); so sanh theo gia tri roi so doan

int n, k;
vector<ll> a;

P solve(ll lam) {
    P out = {0, 0};              // phan tu hien tai khong thuoc doan nao
    P in = {LLONG_MIN / 4, 0};   // phan tu hien tai thuoc mot doan
    for (int i = 0; i < n; i++) {
        P start = max(out, in);              // mo doan moi tai i (sau 1 khoang trong hoac sat doan truoc)
        start.first -= lam, start.second++;
        P ni = max(in, start);               // keo dai doan cu hoac mo doan moi
        ni.first += a[i];
        out = max(out, in);
        in = ni;
    }
    return max(out, in);
}

int main() {
    scanf("%d %d", &n, &k);
    a.resize(n);
    for (auto &x : a) scanf("%lld", &x);
    ll lo = -100000000, hi = 100000000;      // |f(k) - f(k-1)| <= 2 * n * max|a_i| < 10^8
    while (lo < hi) {                        // tim lam lon nhat co so doan >= k
        ll mid = lo + (hi - lo + 1) / 2;
        if (solve(mid).second >= k) lo = mid;
        else hi = mid - 1;
    }
    printf("%lld\n", solve(lo).first + lo * k);
    return 0;
}
