// V101 - Tong XOR moi cap: dem rieng tung bit
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (auto &x : a) cin >> x;
    long long total = 0;
    for (int b = 0; b < 30; b++) {
        long long cnt = 0;   // so phan tu co bit b bang 1
        for (long long x : a)
            if (x >> b & 1) cnt++;
        total += cnt * (n - cnt) * (1LL << b);
    }
    cout << total << "\n";
    return 0;
}
