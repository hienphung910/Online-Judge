// V161 - Cay khung nho nhat tren do thi day du bang Prim O(n^2)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<long long> x(n), y(n);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &x[i], &y[i]);

    const long long INF = LLONG_MAX;
    vector<long long> d(n, INF);   // d[i] = chi phi nho nhat noi i vao cay hien tai
    vector<bool> inTree(n, false);
    d[0] = 0;
    long long total = 0;
    for (int it = 0; it < n; it++) {
        int u = -1;                     // dinh ngoai cay gan cay nhat
        for (int i = 0; i < n; i++)
            if (!inTree[i] && (u == -1 || d[i] < d[u])) u = i;
        inTree[u] = true;
        total += d[u];
        for (int v = 0; v < n; v++) {   // cap nhat khoang cach tu u
            long long w = llabs(x[u] - x[v]) + llabs(y[u] - y[v]);
            if (!inTree[v] && w < d[v]) d[v] = w;
        }
    }
    printf("%lld\n", total);
    return 0;
}
