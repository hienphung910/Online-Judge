// V084 - Toi thieu tong thoi gian cho: phuc vu khach nhanh truoc (lap luan doi cho)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> t(n);
    for (auto &x : t) cin >> x;
    sort(t.begin(), t.end());
    long long now = 0, total = 0;
    for (long long x : t) {
        total += now;   // khach nay da cho 'now' phut
        now += x;
    }
    cout << total << "\n";
    return 0;
}
