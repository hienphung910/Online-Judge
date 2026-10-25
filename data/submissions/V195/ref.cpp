// V195 - Kiem tra hai doan thang co diem chung (ke ca cham, chong len nhau, doan suy bien)
// Dung dau tich co huong: cat nhau that su khi moi doan tach hai dau mut doan kia ve hai phia;
// con lai chi gap nhau khi co mot dau mut nam tren doan kia.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct P { ll x, y; };

ll cross(P o, P a, P b) { return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x); }
int sgn(ll v) { return (v > 0) - (v < 0); }

// p nam tren doan [a, b]: thang hang va nam trong hinh chu nhat bao
bool onSeg(P p, P a, P b) {
    return cross(a, b, p) == 0 && min(a.x, b.x) <= p.x && p.x <= max(a.x, b.x)
        && min(a.y, b.y) <= p.y && p.y <= max(a.y, b.y);
}

bool meet(P a, P b, P c, P d) {
    int d1 = sgn(cross(a, b, c)), d2 = sgn(cross(a, b, d));
    int d3 = sgn(cross(c, d, a)), d4 = sgn(cross(c, d, b));
    if (d1 * d2 < 0 && d3 * d4 < 0) return true;
    return onSeg(c, a, b) || onSeg(d, a, b) || onSeg(a, c, d) || onSeg(b, c, d);
}

int main() {
    int q;
    scanf("%d", &q);
    while (q--) {
        P a, b, c, d;
        scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &a.x, &a.y, &b.x, &b.y, &c.x, &c.y, &d.x, &d.y);
        puts(meet(a, b, c, d) ? "CO" : "KHONG");
    }
    return 0;
}
