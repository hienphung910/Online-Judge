// V198 - Liet ke dinh bao loi (Andrew monotone chain), bo diem trung va diem nam tren canh
// Sap xep theo (x, y); dung nua duoi roi nua tren, pop khi cross <= 0 de bo diem thang hang.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> P;

ll cross(P o, P a, P b) {
    return (a.first - o.first) * (b.second - o.second) - (a.second - o.second) * (b.first - o.first);
}

int main() {
    int n;
    scanf("%d", &n);
    vector<P> p(n);
    for (auto &q : p) scanf("%lld %lld", &q.first, &q.second);
    sort(p.begin(), p.end());
    p.erase(unique(p.begin(), p.end()), p.end());
    n = p.size();
    if (n == 1) {
        printf("1\n%lld %lld\n", p[0].first, p[0].second);
        return 0;
    }
    vector<P> h(2 * n);
    int k = 0;
    for (int i = 0; i < n; i++) {                       // nua duoi
        while (k >= 2 && cross(h[k - 2], h[k - 1], p[i]) <= 0) k--;
        h[k++] = p[i];
    }
    for (int i = n - 2, t = k + 1; i >= 0; i--) {       // nua tren
        while (k >= t && cross(h[k - 2], h[k - 1], p[i]) <= 0) k--;
        h[k++] = p[i];
    }
    k--;                                                // h[k] trung h[0]
    printf("%d\n", k);                                  // thang hang -> k = 2 tu nhien
    for (int i = 0; i < k; i++) printf("%lld %lld\n", h[i].first, h[i].second);
    return 0;
}
