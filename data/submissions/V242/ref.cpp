// V242 - Minimax tren trang thai bitmask (QHD tren tap con)
// f[mask] = chenh lech (nguoi sap di - nguoi kia) toi uu khi cac vien con lai la mask.
// f[mask] = max over i in mask cua v[i] - f[mask bo i va cac vien ky voi i]; f[0] = 0.
// Mask moi luon nho hon mask cu nen duyet mask tang dan.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        vector<long long> v(n);
        for (auto &x : v) cin >> x;
        vector<int> adj(n, 0);
        for (int j = 0; j < m; j++) {
            int a, b;
            cin >> a >> b;
            a--; b--;
            adj[a] |= 1 << b;
            adj[b] |= 1 << a;
        }
        int full = (1 << n) - 1;
        vector<long long> f(full + 1, 0);
        for (int mask = 1; mask <= full; mask++) {
            long long best = LLONG_MIN;
            for (int i = 0; i < n; i++)
                if (mask >> i & 1) {
                    int rest = mask & ~(1 << i) & ~adj[i];
                    best = max(best, v[i] - f[rest]);
                }
            f[mask] = best;
        }
        cout << f[full] << "\n";
    }
    return 0;
}
