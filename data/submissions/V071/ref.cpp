// V071 - Sap xep dem (counting sort): dem so thi sinh moi muc diem roi cong don
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    int cnt[102] = {0};                 // cnt[d] = so thi sinh dat d diem
    for (auto &x : a) { cin >> x; cnt[x]++; }
    int hang[102];                      // hang[d] = 1 + so thi sinh co diem > d
    int caoHon = 0;
    for (int d = 100; d >= 0; d--) {
        hang[d] = caoHon + 1;
        caoHon += cnt[d];
    }
    for (int i = 0; i < n; i++) cout << hang[a[i]] << (i + 1 < n ? ' ' : '\n');
    return 0;
}
