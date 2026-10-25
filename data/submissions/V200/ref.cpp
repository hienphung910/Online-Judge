// V200 - Dien tich hop cac hinh chu nhat: duong quet theo x + cay phan doan tren y da nen
// cnt[v] = so hinh dang phu tron nut v, len[v] = do dai phan bi phu trong nut v.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<int> ys;
vector<int> cnt, len_;

void update(int v, int l, int r, int ql, int qr, int d) {   // nut v quan ly [ys[l], ys[r]]
    if (qr <= l || r <= ql) return;
    if (ql <= l && r <= qr) cnt[v] += d;
    else {
        int m = (l + r) / 2;
        update(2 * v, l, m, ql, qr, d);
        update(2 * v + 1, m, r, ql, qr, d);
    }
    if (cnt[v] > 0) len_[v] = ys[r] - ys[l];
    else if (r - l == 1) len_[v] = 0;
    else len_[v] = len_[2 * v] + len_[2 * v + 1];
}

int main() {
    int n;
    scanf("%d", &n);
    vector<array<int, 4>> ev;   // {x, +1/-1, y1, y2}
    for (int i = 0; i < n; i++) {
        int x1, y1, x2, y2;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        ev.push_back({x1, 1, y1, y2});
        ev.push_back({x2, -1, y1, y2});
        ys.push_back(y1);
        ys.push_back(y2);
    }
    sort(ys.begin(), ys.end());
    ys.erase(unique(ys.begin(), ys.end()), ys.end());
    int m = ys.size();
    cnt.assign(8 * m, 0);
    len_.assign(8 * m, 0);
    sort(ev.begin(), ev.end());
    ll area = 0;
    for (size_t i = 0; i < ev.size(); i++) {
        if (i > 0) area += (ll)len_[1] * (ev[i][0] - ev[i - 1][0]);
        int a = lower_bound(ys.begin(), ys.end(), ev[i][2]) - ys.begin();
        int b = lower_bound(ys.begin(), ys.end(), ev[i][3]) - ys.begin();
        update(1, 0, m - 1, a, b, ev[i][1]);
    }
    printf("%lld\n", area);
    return 0;
}
