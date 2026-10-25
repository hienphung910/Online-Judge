// V300 - Slope trick voi rang buoc |b_i - b_(i+1)| <= D
// F_i(x) = |x - a_i| + min{ F_(i-1)(y) : |x - y| <= D }, ham loi gay khuc.
// L (max-heap) luu diem gay ben trai doan day, R (min-heap) luu ben phai.
// Lay min trong cua so: dich L sang trai D, R sang phai D (dung bien dich addL, addR).
// Cong |x - a|: neu a nam ngoai doan day [top L, top R] thi gia tri day tang them khoang cach.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int n;
    ll D;
    scanf("%d %lld", &n, &D);
    priority_queue<ll> L;                              // gia tri that = phan tu + addL
    priority_queue<ll, vector<ll>, greater<ll>> R;     // gia tri that = phan tu + addR
    ll addL = 0, addR = 0, ans = 0;
    for (int i = 0; i < n; i++) {
        ll a;
        scanf("%lld", &a);
        if (i > 0) addL -= D, addR += D;
        if (!L.empty() && a < L.top() + addL) {        // a nam ben trai doan day
            ll l = L.top() + addL;
            ans += l - a;
            L.pop();
            L.push(a - addL);
            L.push(a - addL);
            R.push(l - addR);
        } else if (!R.empty() && a > R.top() + addR) { // a nam ben phai doan day
            ll r = R.top() + addR;
            ans += a - r;
            R.pop();
            R.push(a - addR);
            R.push(a - addR);
            L.push(r - addL);
        } else {                                       // a nam trong doan day
            L.push(a - addL);
            R.push(a - addR);
        }
    }
    printf("%lld\n", ans);
    return 0;
}
