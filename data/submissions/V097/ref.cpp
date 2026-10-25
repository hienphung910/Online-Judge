// V097 - Quy hoach dong dem so cach leo cau thang tranh bac gay
#include <bits/stdc++.h>
using namespace std;

int main() {
    const long long MOD = 1000000007;
    int n, m;
    cin >> n >> m;
    vector<bool> broken(n + 1, false);
    for (int i = 0; i < m; i++) {
        int b;
        cin >> b;
        broken[b] = true;
    }
    vector<long long> f(n + 1, 0);
    f[0] = 1;
    for (int i = 1; i <= n; i++) {
        if (broken[i]) continue;   // f[i] = 0
        for (int k = 1; k <= 3; k++)
            if (i - k >= 0) f[i] = (f[i] + f[i - k]) % MOD;
    }
    cout << f[n] << "\n";
    return 0;
}
