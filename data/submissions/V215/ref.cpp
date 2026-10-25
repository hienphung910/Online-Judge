// V215 - Chia can theo buoc nhay: tong a[s] + a[s+d] + a[s+2d] + ...
// d <= B ~ sqrt(n): tra bang tong hau to f[d][i] da tinh truoc. d > B: cong truc tiep (< sqrt(n) so hang).
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    vector<long long> a(n);
    for (auto &x : a) cin >> x;
    int B = max(1, (int)sqrt((double)n));
    // f[d][i] = a[i] + f[d][i + d]
    vector<vector<long long>> f(B + 1, vector<long long>(n, 0));
    for (int d = 1; d <= B; d++)
        for (int i = n - 1; i >= 0; i--)
            f[d][i] = a[i] + (i + d < n ? f[d][i + d] : 0);
    while (q--) {
        int s, d;
        cin >> s >> d;
        s--;
        long long ans = 0;
        if (d <= B) ans = f[d][s];
        else for (int i = s; i < n; i += d) ans += a[i];
        cout << ans << '\n';
    }
    return 0;
}
