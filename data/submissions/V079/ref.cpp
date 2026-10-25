// V079 - Dem cap (i < j, a_i > 2*a_j) bang sap xep tron, O(n log n)
#include <bits/stdc++.h>
using namespace std;

vector<long long> a, tmp;

long long dem(int l, int r) {                   // dem tren doan [l, r) roi sap xep doan do
    if (r - l <= 1) return 0;
    int m = (l + r) / 2;
    long long res = dem(l, m) + dem(m, r);
    int j = m;                                  // a[m..j-1] la cac phan tu nua phai co 2*a < a[i]
    for (int i = l; i < m; i++) {               // nua trai tang dan nen j chi tien len
        while (j < r && a[i] > 2 * a[j]) j++;
        res += j - m;
    }
    merge(a.begin() + l, a.begin() + m, a.begin() + m, a.begin() + r, tmp.begin() + l);
    copy(tmp.begin() + l, tmp.begin() + r, a.begin() + l);
    return res;
}

int main() {
    int n;
    cin >> n;
    a.resize(n);
    tmp.resize(n);
    for (auto &x : a) cin >> x;
    cout << dem(0, n) << "\n";
    return 0;
}
