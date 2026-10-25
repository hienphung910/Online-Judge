// V287 - Mang hau to + LCP: xau dai nhat xuat hien it nhat K lan
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    int K;
    cin >> s >> K;
    int n = s.size();
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
    vector<int> lcp(n, 0); // lcp[r] = tien to chung cua hau to sa[r-1] va sa[r]
    for (int i = 0, h = 0; i < n; i++) {
        if (rk[i] == 0) { h = 0; continue; }
        int j = sa[rk[i] - 1];
        while (i + h < n && j + h < n && s[i + h] == s[j + h]) h++;
        lcp[rk[i]] = h;
        if (h > 0) h--;
    }
    // K hau to lien tiep sa[r-K+1..r] co chung tien to dai min(lcp[r-K+2..r]).
    // Cua so dau tien (theo thu tu hau to) dat max cho xau nho nhat theo tu dien.
    int best = 0, pos = -1;
    if (K == 1) {
        best = n; pos = 0; // ca xau S xuat hien 1 lan
    } else {
        deque<int> dq; // chi so lcp trong cua so, gia tri tang dan -> dau deque la min
        for (int r = 1; r < n; r++) {
            while (!dq.empty() && lcp[dq.back()] >= lcp[r]) dq.pop_back();
            dq.push_back(r);
            int l = r - K + 2; // cua so lcp[l..r] gom K-1 phan tu
            if (l < 1) continue;
            while (dq.front() < l) dq.pop_front();
            if (lcp[dq.front()] > best) { best = lcp[dq.front()]; pos = sa[r]; }
        }
    }
    cout << best << '\n';
    if (best > 0) cout << s.substr(pos, best) << '\n';
    return 0;
}
