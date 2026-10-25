// V004 - Dem nghich the bang sap xep tron, O(n log n)
#include <bits/stdc++.h>
using namespace std;

vector<long long> a, tmp;

long long demNghichThe(int l, int r) {          // dem tren doan [l, r) va sap xep doan do
    if (r - l <= 1) return 0;
    int m = (l + r) / 2;
    long long res = demNghichThe(l, m) + demNghichThe(m, r);
    int i = l, j = m, k = l;
    while (i < m && j < r) {
        if (a[i] <= a[j]) tmp[k++] = a[i++];   // bang nhau khong tinh la nghich the
        else {
            res += m - i;                       // a[i..m-1] deu lon hon a[j]
            tmp[k++] = a[j++];
        }
    }
    while (i < m) tmp[k++] = a[i++];
    while (j < r) tmp[k++] = a[j++];
    for (int t = l; t < r; t++) a[t] = tmp[t];
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    a.resize(n);
    tmp.resize(n);
    for (auto &x : a) cin >> x;
    cout << demNghichThe(0, n) << "\n";
    return 0;
}
