// V012 - Cay Fenwick (BIT): gan gia tri tai mot vi tri va tinh tong doan, O((n + q) log n)
// Gan a[i] = x tuong duong cong them (x - a[i]) vao vi tri i.
#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> bit;

void add(int i, long long v) {
    for (; i <= n; i += i & -i) bit[i] += v;
}

long long prefixSum(int i) {   // a[1] + ... + a[i]
    long long s = 0;
    for (; i > 0; i -= i & -i) s += bit[i];
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    vector<long long> a(n + 1);
    bit.assign(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        add(i, a[i]);
    }
    while (q--) {
        int type;
        long long x, y;
        cin >> type >> x >> y;
        if (type == 1) {
            add(x, y - a[x]);
            a[x] = y;
        } else {
            cout << prefixSum(y) - prefixSum(x - 1) << '\n';
        }
    }
    return 0;
}
