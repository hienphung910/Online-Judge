// V177 - Di xuong cay phan doan max: tim j nho nhat, j >= l, a[j] >= x, O(log n) moi truy van
// Cay luu max tung doan. Khi tim: bo qua doan nam hoan toan ben trai l hoac co max < x;
// trong cac doan con lai, uu tien con trai truoc nen gap duoc j nho nhat.
#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> mx;

void update(int node, int l, int r, int pos, long long val) {
    if (l == r) { mx[node] = val; return; }
    int mid = (l + r) / 2;
    if (pos <= mid) update(2 * node, l, mid, pos, val);
    else update(2 * node + 1, mid + 1, r, pos, val);
    mx[node] = max(mx[2 * node], mx[2 * node + 1]);
}

int findFirst(int node, int l, int r, int from, long long x) {
    if (r < from || mx[node] < x) return -1;   // khong co ben hop le trong doan nay
    if (l == r) return l;
    int mid = (l + r) / 2;
    int res = findFirst(2 * node, l, mid, from, x);
    if (res == -1) res = findFirst(2 * node + 1, mid + 1, r, from, x);
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> n >> q;
    mx.assign(4 * n, 0);
    for (int i = 1; i <= n; i++) {
        long long a;
        cin >> a;
        update(1, 1, n, i, a);
    }
    while (q--) {
        int type, p;
        long long x;
        cin >> type >> p >> x;
        if (type == 1) update(1, 1, n, p, x);
        else cout << findFirst(1, 1, n, p, x) << '\n';
    }
    return 0;
}
