// V170 - Cay Fenwick: cong doan, hoi gia tri mot diem, O((n + q) log n)
// Luu mang hieu d[i] = a[i] - a[i-1] trong BIT: cong x vao [l, r] la d[l] += x, d[r+1] -= x;
// gia tri a[i] chinh la tong tien to d[1] + ... + d[i].
#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> bit;

void add(int i, long long v) {
    for (; i <= n; i += i & -i) bit[i] += v;
}

long long prefixSum(int i) {
    long long s = 0;
    for (; i > 0; i -= i & -i) s += bit[i];
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    bit.assign(n + 2, 0);
    long long prev = 0;
    for (int i = 1; i <= n; i++) {
        long long a;
        cin >> a;
        add(i, a - prev);
        prev = a;
    }
    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            long long x;
            cin >> l >> r >> x;
            add(l, x);
            if (r + 1 <= n) add(r + 1, -x);
        } else {
            int i;
            cin >> i;
            cout << prefixSum(i) << '\n';
        }
    }
    return 0;
}
