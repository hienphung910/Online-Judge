// V112 - Mang hieu (difference array) 1 chieu: cong v vao doan [l, r] trong O(1)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<long long> a(n + 1), d(n + 2, 0);
    for (int i = 1; i <= n; i++) cin >> a[i];
    while (m--) {
        int l, r;
        long long v;
        cin >> l >> r >> v;
        d[l] += v;        // tu l tro di cao them v
        d[r + 1] -= v;    // tu r+1 tro di bo phan cao them do
    }
    long long them = 0;
    for (int i = 1; i <= n; i++) {
        them += d[i];
        cout << a[i] + them << (i < n ? ' ' : '\n');
    }
    return 0;
}
