// V196 - Diem trong da giac don: kiem tra bien truoc, sau do ban tia sang phai dem so lan cat
// Quy uoc nua mo (a.y > p.y) != (b.y > p.y) giup tia di qua dung mot dinh chi duoc dem dung mot lan.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct P { ll x, y; };

ll cross(P o, P a, P b) { return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x); }

bool onSeg(P p, P a, P b) {
    return cross(a, b, p) == 0 && min(a.x, b.x) <= p.x && p.x <= max(a.x, b.x)
        && min(a.y, b.y) <= p.y && p.y <= max(a.y, b.y);
}

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    vector<P> v(n);
    for (auto &p : v) scanf("%lld %lld", &p.x, &p.y);
    while (q--) {
        P p;
        scanf("%lld %lld", &p.x, &p.y);
        bool border = false, inside = false;
        for (int i = 0; i < n && !border; i++) {
            P a = v[i], b = v[(i + 1) % n];
            if (onSeg(p, a, b)) { border = true; break; }
            if ((a.y > p.y) != (b.y > p.y)) {
                // giao diem cua canh voi duong ngang y = p.y nam ben phai p ?
                // tuong duong: p nam ben trai canh khi di tu duoi len tren
                ll c = cross(a, b, p);
                if ((b.y > a.y) ? (c > 0) : (c < 0)) inside = !inside;
            }
        }
        puts(border ? "BIEN" : inside ? "TRONG" : "NGOAI");
    }
    return 0;
}
