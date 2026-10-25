// V189 - Xau con chung dai nhat cua hai xau: chat nhi phan do dai + bam xau 2 modulo
// Neu co xau con chung do dai L thi cung co do dai L-1 -> tinh chat don dieu.
// Kiem tra L: lay ma bam moi doan do dai L cua A, sap xep, roi tim tung doan cua B.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll M1 = 1000000007, M2 = 998244353, B = 131;
vector<ll> p1, p2;

struct Hash {
    vector<ll> h1, h2;
    Hash(const string& s) {
        int n = s.size();
        h1.assign(n + 1, 0); h2.assign(n + 1, 0);
        for (int i = 0; i < n; i++) {
            h1[i + 1] = (h1[i] * B + s[i]) % M1;
            h2[i + 1] = (h2[i] * B + s[i]) % M2;
        }
    }
    ll get(int i, int len) {             // ma bam cua doan bat dau tai i (0-based), dai len
        ll a = ((h1[i + len] - h1[i] * p1[len]) % M1 + M1) % M1;
        ll b = ((h2[i + len] - h2[i] * p2[len]) % M2 + M2) % M2;
        return a * M2 + b;               // gop 2 ma bam thanh 1 so (< 10^18)
    }
};

int main() {
    string a, b;
    cin >> a >> b;
    int n = a.size(), m = b.size();
    p1.assign(max(n, m) + 1, 1); p2.assign(max(n, m) + 1, 1);
    for (int i = 1; i <= max(n, m); i++) { p1[i] = p1[i - 1] * B % M1; p2[i] = p2[i - 1] * B % M2; }
    Hash ha(a), hb(b);
    auto coChung = [&](int L) {
        vector<ll> v;
        for (int i = 0; i + L <= n; i++) v.push_back(ha.get(i, L));
        sort(v.begin(), v.end());
        for (int j = 0; j + L <= m; j++)
            if (binary_search(v.begin(), v.end(), hb.get(j, L))) return true;
        return false;
    };
    int lo = 0, hi = min(n, m);
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (coChung(mid)) lo = mid; else hi = mid - 1;
    }
    cout << lo << '\n';
    return 0;
}
