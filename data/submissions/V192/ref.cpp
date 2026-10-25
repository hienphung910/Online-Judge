// V192 - Huong re: dau cua tich co huong (B - A) x (C - A)
// > 0: C ben trai, < 0: ben phai, = 0: thang hang. Moi gia tri <= 8e18 vua kieu long long.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int q;
    scanf("%d", &q);
    while (q--) {
        ll xa, ya, xb, yb, xc, yc;
        scanf("%lld %lld %lld %lld %lld %lld", &xa, &ya, &xb, &yb, &xc, &yc);
        ll cr = (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa);
        if (cr > 0) puts("TRAI");
        else if (cr < 0) puts("PHAI");
        else puts("THANG");
    }
    return 0;
}
