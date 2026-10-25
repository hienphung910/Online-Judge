// V072 - Sap xep voi khoa tu dinh nghia: (tong chu so, gia tri)
#include <bits/stdc++.h>
using namespace std;

int tongChuSo(int x) {
    int s = 0;
    while (x > 0) { s += x % 10; x /= 10; }
    return s;
}

int main() {
    int n;
    cin >> n;
    vector<pair<int, int>> a(n);        // (tong chu so, gia tri)
    for (auto &p : a) { cin >> p.second; p.first = tongChuSo(p.second); }
    sort(a.begin(), a.end());           // pair so sanh first truoc roi den second
    for (int i = 0; i < n; i++) cout << a[i].second << (i + 1 < n ? ' ' : '\n');
    return 0;
}
