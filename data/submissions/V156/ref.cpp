// V156 - Floyd-Warshall them dinh theo thu tu nguoc, O(n^3)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<vector<long long>> d(n + 1, vector<long long>(n + 1));
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) cin >> d[i][j];
    vector<int> p(n + 1);
    for (int i = 1; i <= n; i++) cin >> p[i];

    vector<bool> open(n + 1, false);
    vector<long long> ans(n + 1);
    for (int t = n; t >= 1; t--) {            // them kho p[t] vao (nguoc thu tu dong cua)
        int k = p[t];
        open[k] = true;
        for (int i = 1; i <= n; i++)          // k lam dinh trung gian cho MOI cap
            for (int j = 1; j <= n; j++)
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
        long long s = 0;
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                if (open[i] && open[j]) s += d[i][j];
        ans[t] = s;
    }
    for (int i = 1; i <= n; i++) cout << ans[i] << (i == n ? '\n' : ' ');
    return 0;
}
