// V089 - Toi thieu tong w*c (luat Smith): lap luan doi cho, sap xep theo t_i*w_j < t_j*w_i
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<long long, long long>> a(n);   // (t, w)
    for (auto &x : a) cin >> x.first >> x.second;
    sort(a.begin(), a.end(), [](const pair<long long, long long> &p, const pair<long long, long long> &q) {
        return p.first * q.second < q.first * p.second;   // so sanh t/w khong dung so thuc
    });
    long long now = 0, total = 0;
    for (auto &x : a) {
        now += x.first;
        total += x.second * now;
    }
    cout << total << "\n";
    return 0;
}
