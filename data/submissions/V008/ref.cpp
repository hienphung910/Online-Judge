// V008 - Dem cap co tong bang K bang bang bam, O(n)
// Duyet tu trai sang phai: voi moi a[j], so cap (i, j) moi la so lan K - a[j] da xuat hien truoc do.
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long k;
    cin >> n >> k;
    unordered_map<long long, int> cnt;   // cnt[v] = so phan tu bang v da gap
    cnt.reserve(2 * n + 1);
    long long ans = 0;                   // dap an co the toi ~2e10, can 64-bit
    for (int j = 0; j < n; j++) {
        long long a;
        cin >> a;
        auto it = cnt.find(k - a);       // k - a co the toi 2e9, can 64-bit
        if (it != cnt.end()) ans += it->second;
        cnt[a]++;
    }
    cout << ans << '\n';
    return 0;
}
