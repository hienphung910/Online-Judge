// V173 - Cay Fenwick cong doan, tong doan (hai BIT), O((n + q) log n)
// Goi d la mang hieu cua a. Tong tien to:
//   a[1] + ... + a[p] = (p + 1) * sum(d[i]) - sum(i * d[i])   voi i = 1..p
// nen ta giu hai BIT: b1 cho d[i], b2 cho i * d[i].
#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> b1, b2;

void add(vector<long long> &b, int i, long long v) {
    for (; i <= n; i += i & -i) b[i] += v;
}

long long get(const vector<long long> &b, int i) {
    long long s = 0;
    for (; i > 0; i -= i & -i) s += b[i];
    return s;
}

void rangeAdd(int l, int r, long long x) {   // cong x vao a[l..r]
    add(b1, l, x);
    add(b2, l, x * l);
    if (r + 1 <= n) {
        add(b1, r + 1, -x);
        add(b2, r + 1, -x * (r + 1));
    }
}

long long prefixSum(int p) {
    return (p + 1) * get(b1, p) - get(b2, p);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    b1.assign(n + 1, 0);
    b2.assign(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        long long a;
        cin >> a;
        rangeAdd(i, i, a);
    }
    while (q--) {
        int type, l, r;
        cin >> type >> l >> r;
        if (type == 1) {
            long long x;
            cin >> x;
            rangeAdd(l, r, x);
        } else {
            cout << prefixSum(r) - prefixSum(l - 1) << '\n';
        }
    }
    return 0;
}
