// V178 - Di xuong cay phan doan: tim vi tri so 1 thu k, O(log n) moi truy van
// cnt[node] = so ghe trong trong doan cua node. Tim ghe trong thu k: neu con trai
// co it nhat k ghe trong thi di sang trai, nguoc lai tru k di cnt(trai) roi sang phai.
#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> cnt;

void update(int node, int l, int r, int pos, int val) {
    if (l == r) { cnt[node] = val; return; }
    int mid = (l + r) / 2;
    if (pos <= mid) update(2 * node, l, mid, pos, val);
    else update(2 * node + 1, mid + 1, r, pos, val);
    cnt[node] = cnt[2 * node] + cnt[2 * node + 1];
}

int kth(int node, int l, int r, int k) {   // goi khi chac chan cnt[node] >= k
    if (l == r) return l;
    int mid = (l + r) / 2;
    if (cnt[2 * node] >= k) return kth(2 * node, l, mid, k);
    return kth(2 * node + 1, mid + 1, r, k - cnt[2 * node]);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    string s;
    cin >> n >> q >> s;
    cnt.assign(4 * n, 0);
    for (int i = 1; i <= n; i++) update(1, 1, n, i, s[i - 1] - '0');
    while (q--) {
        int type, x;
        cin >> type >> x;
        if (type == 1) {
            s[x - 1] = (s[x - 1] == '1') ? '0' : '1';
            update(1, 1, n, x, s[x - 1] - '0');
        } else {
            if (cnt[1] < x) cout << -1 << '\n';
            else cout << kth(1, 1, n, x) << '\n';
        }
    }
    return 0;
}
