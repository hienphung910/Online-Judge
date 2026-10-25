// V073 - Sap xep theo tan suat giam dan, cung tan suat thi gia tri tang dan
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    map<int, int> dem;                  // dem[x] = so lan xuat hien cua x
    for (auto &x : a) { cin >> x; dem[x]++; }
    sort(a.begin(), a.end(), [&](int x, int y) {
        if (dem[x] != dem[y]) return dem[x] > dem[y];
        return x < y;
    });
    for (int i = 0; i < n; i++) cout << a[i] << (i + 1 < n ? ' ' : '\n');
    return 0;
}
