// V248 - Cap diem gan nhat bang chia de tri, in binh phuong khoang cach
// Sap xep theo x, chia doi; d = min hai nua. Chi can xet cac diem cach duong chia
// nho hon d theo x, sap theo y; moi diem chi so voi vai diem ke tiep co |dy| < d.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<pair<ll, ll>> p, buf;         // (x, y)
ll best = LLONG_MAX;

ll sq(ll v) { return v * v; }
bool byY(const pair<ll, ll>& a, const pair<ll, ll>& b) { return a.second < b.second; }

void rec(int l, int r) {             // xet p[l..r), ket thuc thi doan nay da sap theo y
    if (r - l <= 3) {
        for (int i = l; i < r; i++)
            for (int j = i + 1; j < r; j++)
                best = min(best, sq(p[i].first - p[j].first) + sq(p[i].second - p[j].second));
        sort(p.begin() + l, p.begin() + r, byY);
        return;
    }
    int m = (l + r) / 2;
    ll midx = p[m].first;
    rec(l, m);
    rec(m, r);
    inplace_merge(p.begin() + l, p.begin() + m, p.begin() + r, byY);
    int k = 0;                       // dai giua: cac diem co (x - midx)^2 < best
    for (int i = l; i < r; i++) {
        if (sq(p[i].first - midx) >= best) continue;
        for (int j = k - 1; j >= 0 && sq(p[i].second - buf[j].second) < best; j--)
            best = min(best, sq(p[i].first - buf[j].first) + sq(p[i].second - buf[j].second));
        buf[k++] = p[i];
    }
}

int main() {
    int n;
    cin >> n;
    p.resize(n);
    buf.resize(n);
    for (auto& q : p) cin >> q.first >> q.second;
    sort(p.begin(), p.end());
    rec(0, n);
    cout << best << "\n";
    return 0;
}
