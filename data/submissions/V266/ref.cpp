// V266 - Cay wavelet (wavelet tree): dem so phan tu co gia tri trong [x, y] tren doan [l, r]
#include <bits/stdc++.h>
using namespace std;

struct Wavelet {
    int lo, hi;                 // nut quan ly cac gia tri (da nen) trong [lo, hi]
    Wavelet *L = nullptr, *R = nullptr;
    vector<int> b;              // b[i] = so phan tu trong i phan tu dau di sang con trai

    Wavelet(int* from, int* to, int x, int y) : lo(x), hi(y) {
        if (lo == hi || from >= to) return;
        int mid = (lo + hi) / 2;
        auto goLeft = [mid](int v) { return v <= mid; };
        b.reserve(to - from + 1);
        b.push_back(0);
        for (int* it = from; it != to; it++) b.push_back(b.back() + goLeft(*it));
        int* pivot = stable_partition(from, to, goLeft);
        L = new Wavelet(from, pivot, lo, mid);
        R = new Wavelet(pivot, to, mid + 1, hi);
    }

    // so phan tu co gia tri <= k trong cac vi tri [l, r] (tinh tu 1) cua nut nay
    int countLE(int l, int r, int k) {
        if (l > r || k < lo) return 0;
        if (hi <= k) return r - l + 1;
        int lb = b[l - 1], rb = b[r];
        return L->countLE(lb + 1, rb, k) + R->countLE(l - lb, r - rb, k);
    }
};

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    vector<int> a(n);
    for (auto& v : a) scanf("%d", &v);
    vector<int> vals = a;  // nen gia tri ve 0..sz-1
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    for (auto& v : a) v = lower_bound(vals.begin(), vals.end(), v) - vals.begin();
    Wavelet wt(a.data(), a.data() + n, 0, (int)vals.size() - 1);
    while (q--) {
        int l, r, x, y;
        scanf("%d %d %d %d", &l, &r, &x, &y);
        int kHi = upper_bound(vals.begin(), vals.end(), y) - vals.begin() - 1;  // gia tri nen lon nhat <= y
        int kLo = lower_bound(vals.begin(), vals.end(), x) - vals.begin() - 1;  // gia tri nen lon nhat < x
        printf("%d\n", wt.countLE(l, r, kHi) - wt.countLE(l, r, kLo));
    }
    return 0;
}
