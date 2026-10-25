// V267 - Cay phan doan luu vet (persistent): sua mot o tao phien ban moi, hoi tong doan o phien ban bat ky
#include <bits/stdc++.h>
using namespace std;

const int MAXNODE = 1 << 16;  // cay ban dau 2n nut + moi lan sua tao them khoang log2(n) + 1 nut
int lc[MAXNODE], rc[MAXNODE], nodes = 0;
long long sum[MAXNODE];
int n;
vector<long long> a;

int build(int lo, int hi) {
    int u = nodes++;
    if (lo == hi) { sum[u] = a[lo]; return u; }
    int mid = (lo + hi) / 2;
    lc[u] = build(lo, mid);
    rc[u] = build(mid + 1, hi);
    sum[u] = sum[lc[u]] + sum[rc[u]];
    return u;
}

// tra ve goc moi; chi sao chep cac nut tren duong tu goc xuong la pos
int setValue(int old, int lo, int hi, int pos, long long x) {
    int u = nodes++;
    lc[u] = lc[old]; rc[u] = rc[old];
    if (lo == hi) { sum[u] = x; return u; }
    int mid = (lo + hi) / 2;
    if (pos <= mid) lc[u] = setValue(lc[old], lo, mid, pos, x);
    else rc[u] = setValue(rc[old], mid + 1, hi, pos, x);
    sum[u] = sum[lc[u]] + sum[rc[u]];
    return u;
}

long long query(int u, int lo, int hi, int l, int r) {
    if (r < lo || hi < l) return 0;
    if (l <= lo && hi <= r) return sum[u];
    int mid = (lo + hi) / 2;
    return query(lc[u], lo, mid, l, r) + query(rc[u], mid + 1, hi, l, r);
}

int main() {
    int q;
    scanf("%d %d", &n, &q);
    a.resize(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &a[i]);
    vector<int> root = {build(1, n)};  // root[v] = goc cua phien ban v
    while (q--) {
        int type, v, x, y;
        scanf("%d %d %d %d", &type, &v, &x, &y);
        if (type == 1) root.push_back(setValue(root[v], 1, n, x, y));
        else printf("%lld\n", query(root[v], 1, n, x, y));
    }
    return 0;
}
