// V286 - Mang hau to + LCP (Kasai): dem so xau con phan biet
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.size();
    // mang hau to bang nhan doi do dai: sap theo cap (hang[i], hang[i+k])
    vector<int> sa(n), rk(n), tmp(n);
    for (int i = 0; i < n; i++) { sa[i] = i; rk[i] = s[i]; }
    for (int k = 1;; k <<= 1) {
        auto cmp = [&](int a, int b) {
            if (rk[a] != rk[b]) return rk[a] < rk[b];
            int ra = a + k < n ? rk[a + k] : -1;
            int rb = b + k < n ? rk[b + k] : -1;
            return ra < rb;
        };
        sort(sa.begin(), sa.end(), cmp);
        tmp[sa[0]] = 0;
        for (int i = 1; i < n; i++) tmp[sa[i]] = tmp[sa[i - 1]] + cmp(sa[i - 1], sa[i]);
        rk = tmp;
        if (rk[sa[n - 1]] == n - 1) break;
    }
    // Kasai: h = tien to chung dai nhat cua hau to i va hau to dung ngay truoc no
    long long total = 1LL * n * (n + 1) / 2;
    int h = 0;
    for (int i = 0; i < n; i++) {
        if (rk[i] == 0) { h = 0; continue; }
        int j = sa[rk[i] - 1];
        while (i + h < n && j + h < n && s[i + h] == s[j + h]) h++;
        total -= h; // h tien to dau cua hau to i da duoc dem o hau to dung truoc
        if (h > 0) h--;
    }
    cout << total << '\n';
    return 0;
}
