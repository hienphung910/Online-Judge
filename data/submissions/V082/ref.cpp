// V082 - Mua nhieu mon nhat voi so tien co han: sap xep tang dan, mua mon re truoc
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    long long m;
    cin >> n >> m;
    vector<long long> p(n);
    for (auto &x : p) cin >> x;
    sort(p.begin(), p.end());
    int cnt = 0;
    for (long long x : p) {
        if (x > m) break;   // mon re nhat con lai cung khong mua noi
        m -= x;
        cnt++;
    }
    cout << cnt << "\n";
    return 0;
}
