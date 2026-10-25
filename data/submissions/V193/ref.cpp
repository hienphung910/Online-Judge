// V193 - Phan loai tam giac bang tich vo huong tai tung dinh
// Tich co huong = 0 -> suy bien; tich vo huong < 0 -> goc tu, = 0 -> goc vuong.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// tich vo huong cua hai vecto (b - a) va (c - a): dau cho biet goc tai a
ll dotAt(ll ax, ll ay, ll bx, ll by, ll cx, ll cy) {
    return (bx - ax) * (cx - ax) + (by - ay) * (cy - ay);
}

int main() {
    int q;
    scanf("%d", &q);
    while (q--) {
        ll x1, y1, x2, y2, x3, y3;
        scanf("%lld %lld %lld %lld %lld %lld", &x1, &y1, &x2, &y2, &x3, &y3);
        ll cr = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
        if (cr == 0) { puts("SUYBIEN"); continue; }
        ll d[3] = {dotAt(x1, y1, x2, y2, x3, y3), dotAt(x2, y2, x1, y1, x3, y3), dotAt(x3, y3, x1, y1, x2, y2)};
        ll mn = min({d[0], d[1], d[2]});
        if (mn < 0) puts("TU");
        else if (mn == 0) puts("VUONG");
        else puts("NHON");
    }
    return 0;
}
