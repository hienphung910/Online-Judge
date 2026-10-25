// V152 - Phat hien chu trinh am bang Bellman-Ford voi nguon ao (d = 0 cho moi dinh)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        vector<array<int, 3>> e(m);
        for (auto& x : e) cin >> x[0] >> x[1] >> x[2];
        vector<long long> d(n + 1, 0);       // nhu co dinh nguon ao noi toi moi dinh
        bool changed = false;
        for (int it = 1; it <= n; it++) {     // vong thu n van giam duoc => co chu trinh am
            changed = false;
            for (auto [u, v, w] : e)
                if (d[u] + w < d[v]) {
                    d[v] = d[u] + w;
                    changed = true;
                }
            if (!changed) break;
        }
        cout << (changed ? "YES" : "NO") << '\n';
    }
    return 0;
}
