// V058 - Boi chung nho nhat cua day, phat hien vuot 10^18 (tranh tran so)
#include <bits/stdc++.h>
using namespace std;

int main() {
    const long long LIMIT = 1000000000000000000LL;   // 10^18
    int n;
    cin >> n;
    long long L = 1;
    bool tooBig = false;
    for (int i = 0; i < n; i++) {
        long long t;
        cin >> t;
        if (tooBig) continue;
        long long a = L / __gcd(L, t);        // chia truoc
        if (a > LIMIT / t) tooBig = true;     // a * t > 10^18 ?
        else L = a * t;
    }
    if (tooBig) cout << -1 << "\n";
    else cout << L << "\n";
    return 0;
}
