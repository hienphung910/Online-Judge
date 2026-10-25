// V014 - Bao loi Andrew monotone chain, O(n log n)
// In ra 2 lan dien tich bao loi (cong thuc shoelace), dung so nguyen 64 bit.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct P { ll x, y; };

// tich co huong (b - a) x (c - a): > 0 neu a -> b -> c re trai
ll cross(P a, P b, P c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<P> p(n);
    for (auto &q : p) cin >> q.x >> q.y;
    sort(p.begin(), p.end(), [](P a, P b) { return a.x < b.x || (a.x == b.x && a.y < b.y); });

    // dung nua duoi roi nua tren; bo diem thang hang (cross <= 0)
    vector<P> h(2 * n + 1);
    int k = 0;
    for (int i = 0; i < n; i++) {
        while (k >= 2 && cross(h[k - 2], h[k - 1], p[i]) <= 0) k--;
        h[k++] = p[i];
    }
    for (int i = n - 2, t = k + 1; i >= 0; i--) {
        while (k >= t && cross(h[k - 2], h[k - 1], p[i]) <= 0) k--;
        h[k++] = p[i];
    }
    // h[0..k-1] la bao loi, h[k-1] trung h[0]
    ll area2 = 0;
    for (int i = 0; i + 1 < k; i++) area2 += h[i].x * h[i + 1].y - h[i + 1].x * h[i].y;
    cout << llabs(area2) << "\n";
    return 0;
}
