// V268 - Dem so gia tri khac nhau tren doan, tra loi truc tuyen bang cay phan doan luu vet
#include <bits/stdc++.h>
using namespace std;

const int MAXNODE = 1 << 17;  // moi phien ban them toi da 2 duong, moi duong ~log2(n) + 1 nut
int lc[MAXNODE], rc[MAXNODE], cnt[MAXNODE], nodes = 1;  // nut 0 la cay rong

int add(int old, int lo, int hi, int pos, int delta) {
    int u = nodes++;
    lc[u] = lc[old]; rc[u] = rc[old]; cnt[u] = cnt[old] + delta;
    if (lo < hi) {
        int mid = (lo + hi) / 2;
        if (pos <= mid) lc[u] = add(lc[old], lo, mid, pos, delta);
        else rc[u] = add(rc[old], mid + 1, hi, pos, delta);
    }
    return u;
}

int query(int u, int lo, int hi, int l, int r) {
    if (u == 0 || r < lo || hi < l) return 0;
    if (l <= lo && hi <= r) return cnt[u];
    int mid = (lo + hi) / 2;
    return query(lc[u], lo, mid, l, r) + query(rc[u], mid + 1, hi, l, r);
}

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    // phien ban r: danh dau 1 tai lan xuat hien cuoi cung (trong a_1..a_r) cua moi gia tri
    vector<int> root(n + 1, 0);
    map<int, int> lastPos;
    for (int i = 1; i <= n; i++) {
        int x;
        scanf("%d", &x);
        int cur = root[i - 1];
        if (lastPos.count(x)) cur = add(cur, 1, n, lastPos[x], -1);  // bo dau o lan xuat hien truoc
        root[i] = add(cur, 1, n, i, +1);
        lastPos[x] = i;
    }
    long long last = 0;
    while (q--) {
        long long a, b;
        scanf("%lld %lld", &a, &b);
        int l = (a + last) % n + 1, r = (b + last) % n + 1;
        if (l > r) swap(l, r);
        last = query(root[r], 1, n, l, r);
        printf("%lld\n", last);
    }
    return 0;
}
