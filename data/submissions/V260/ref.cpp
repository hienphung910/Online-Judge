// V260 - Cay phan doan khong de quy (iterative, 2n o nho): gan mot diem, hoi UCLN doan
#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> t;  // la o t[n..2n-1], nut i co hai con 2i va 2i+1

void update(int p, long long x) {  // p tinh tu 0
    for (t[p += n] = x; p > 1; p >>= 1) t[p >> 1] = __gcd(t[p], t[p ^ 1]);
}

long long query(int l, int r) {  // doan nua mo [l, r)
    long long g = 0;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l & 1) g = __gcd(g, t[l++]);
        if (r & 1) g = __gcd(g, t[--r]);
    }
    return g;
}

int main() {
    int q;
    scanf("%d %d", &n, &q);
    t.assign(2 * n, 0);
    for (int i = 0; i < n; i++) scanf("%lld", &t[n + i]);
    for (int i = n - 1; i >= 1; i--) t[i] = __gcd(t[2 * i], t[2 * i + 1]);
    while (q--) {
        int type, a, b;
        scanf("%d %d %d", &type, &a, &b);
        if (type == 1) update(a - 1, b);
        else printf("%lld\n", query(a - 1, b));
    }
    return 0;
}
