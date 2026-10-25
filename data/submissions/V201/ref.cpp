// V201 - Duong kinh tap diem: bao loi (Andrew) + xoay compa (rotating calipers), O(n log n)
// Voi moi canh (h[i], h[i+1]), dich con tro j toi dinh xa canh nhat (dien tich tam giac lon nhat),
// cap (h[i], h[j]) va (h[i+1], h[j]) la ung vien.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> P;

ll cross(P o, P a, P b) {
    return (a.first - o.first) * (b.second - o.second) - (a.second - o.second) * (b.first - o.first);
}
ll d2(P a, P b) {
    ll dx = a.first - b.first, dy = a.second - b.second;
    return dx * dx + dy * dy;
}

int main() {
    int n;
    scanf("%d", &n);
    vector<P> p(n);
    for (auto &q : p) scanf("%lld %lld", &q.first, &q.second);
    sort(p.begin(), p.end());
    p.erase(unique(p.begin(), p.end()), p.end());
    n = p.size();
    if (n == 1) { puts("0"); return 0; }

    vector<P> h(2 * n);
    int k = 0;
    for (int i = 0; i < n; i++) {
        while (k >= 2 && cross(h[k - 2], h[k - 1], p[i]) <= 0) k--;
        h[k++] = p[i];
    }
    for (int i = n - 2, t = k + 1; i >= 0; i--) {
        while (k >= t && cross(h[k - 2], h[k - 1], p[i]) <= 0) k--;
        h[k++] = p[i];
    }
    k--;                                   // h[0..k-1] nguoc chieu kim dong ho
    if (k == 2) { printf("%lld\n", d2(h[0], h[1])); return 0; }

    ll best = 0;
    for (int i = 0, j = 1; i < k; i++) {
        P a = h[i], b = h[(i + 1) % k];
        // tang j khi dinh tiep theo xa canh (a, b) hon
        while (cross(a, b, h[(j + 1) % k]) > cross(a, b, h[j])) j = (j + 1) % k;
        best = max({best, d2(a, h[j]), d2(b, h[j])});
    }
    printf("%lld\n", best);
    return 0;
}
