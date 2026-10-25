// V022 - Phan tu nho thu k tren doan bang cay phan doan luu vet (persistent)
#include <bits/stdc++.h>
using namespace std;

const int MAXNODE = 100000 * 20;
int lc[MAXNODE], rc[MAXNODE], cnt[MAXNODE], nodes = 1;  // nut 0 la cay rong

// tao phien ban moi tu cay cu, them 1 vao vi tri pos
int insert(int old, int lo, int hi, int pos) {
    int cur = nodes++;
    lc[cur] = lc[old]; rc[cur] = rc[old]; cnt[cur] = cnt[old] + 1;
    if (lo < hi) {
        int mid = (lo + hi) / 2;
        if (pos <= mid) lc[cur] = insert(lc[old], lo, mid, pos);
        else rc[cur] = insert(rc[old], mid + 1, hi, pos);
    }
    return cur;
}

// cay (u - v) chua dung cac phan tu a_l..a_r; tim vi tri nho thu k
int kth(int u, int v, int lo, int hi, int k) {
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        int leftCount = cnt[lc[u]] - cnt[lc[v]];
        if (k <= leftCount) { u = lc[u]; v = lc[v]; hi = mid; }
        else { k -= leftCount; u = rc[u]; v = rc[v]; lo = mid + 1; }
    }
    return lo;
}

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
    vector<int> vals(a.begin() + 1, a.end());  // nen gia tri
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    int sz = vals.size();
    vector<int> root(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        int pos = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin();
        root[i] = insert(root[i - 1], 0, sz - 1, pos);
    }
    string out;
    while (q--) {
        int l, r, k;
        scanf("%d %d %d", &l, &r, &k);
        out += to_string(vals[kth(root[r], root[l - 1], 0, sz - 1, k)]);
        out += '\n';
    }
    fputs(out.c_str(), stdout);
    return 0;
}
