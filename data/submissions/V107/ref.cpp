// V107 - Tong a_i + b_j nho thu k: tim kiem nhi phan tren dap an + hai con tro
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<long long> a, b;

long long countLE(long long v) {   // so cap (i, j) co a[i] + b[j] <= v
    long long cnt = 0;
    int j = m - 1;
    for (int i = 0; i < n; i++) {
        while (j >= 0 && a[i] + b[j] > v) j--;
        cnt += j + 1;
    }
    return cnt;
}

int main() {
    long long k;
    cin >> n >> m >> k;
    a.resize(n);
    b.resize(m);
    for (auto &x : a) cin >> x;
    for (auto &x : b) cin >> x;
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    long long lo = a[0] + b[0], hi = a[n - 1] + b[m - 1];
    while (lo < hi) {
        long long mid = (lo + hi) / 2;
        if (countLE(mid) >= k) hi = mid;
        else lo = mid + 1;
    }
    cout << lo << "\n";
    return 0;
}
