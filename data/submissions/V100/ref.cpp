// V100 - Tim kiem nhi phan tren dap an: dat c tram xa nhau nhat
#include <bits/stdc++.h>
using namespace std;

int n, c;
vector<long long> x;

bool ok(long long d) {   // dat tham lam, xem co du c tram khong
    int placed = 1;
    long long last = x[0];
    for (int i = 1; i < n; i++)
        if (x[i] - last >= d) {
            placed++;
            last = x[i];
        }
    return placed >= c;
}

int main() {
    cin >> n >> c;
    x.resize(n);
    for (auto &v : x) cin >> v;
    sort(x.begin(), x.end());
    long long lo = 1, hi = x[n - 1] - x[0];   // ok(lo) luon dung vi cac vi tri khac nhau
    while (lo < hi) {
        long long mid = (lo + hi + 1) / 2;
        if (ok(mid)) lo = mid;
        else hi = mid - 1;
    }
    cout << lo << "\n";
    return 0;
}
