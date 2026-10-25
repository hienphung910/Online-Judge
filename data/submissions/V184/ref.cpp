// V184 - So sanh tu dien hai doan con bang bam xau (2 modulo) + chat nhi phan tim LCP
// get(l, r) = ma bam cua S[l..r]; LCP cua hai doan tim bang chat nhi phan tren do dai.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll M1 = 1000000007, M2 = 998244353, B = 131;
int n;
string s;
vector<ll> h1, h2, p1, p2;

pair<ll, ll> get(int l, int r) {     // 1-based, doan [l, r]
    ll a = (h1[r] - h1[l - 1] * p1[r - l + 1]) % M1;
    ll b = (h2[r] - h2[l - 1] * p2[r - l + 1]) % M2;
    if (a < 0) a += M1;
    if (b < 0) b += M2;
    return {a, b};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> s;
    n = s.size();
    h1.assign(n + 1, 0); h2.assign(n + 1, 0); p1.assign(n + 1, 1); p2.assign(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        h1[i] = (h1[i - 1] * B + s[i - 1]) % M1;
        h2[i] = (h2[i - 1] * B + s[i - 1]) % M2;
        p1[i] = p1[i - 1] * B % M1;
        p2[i] = p2[i - 1] * B % M2;
    }
    int q;
    cin >> q;
    while (q--) {
        int l1, r1, l2, r2;
        cin >> l1 >> r1 >> l2 >> r2;
        int len1 = r1 - l1 + 1, len2 = r2 - l2 + 1;
        int lo = 0, hi = min(len1, len2);    // LCP nam trong [lo, hi]
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (get(l1, l1 + mid - 1) == get(l2, l2 + mid - 1)) lo = mid;
            else hi = mid - 1;
        }
        char kq;
        if (lo == min(len1, len2)) kq = (len1 < len2 ? '<' : (len1 == len2 ? '=' : '>'));
        else kq = (s[l1 - 1 + lo] < s[l2 - 1 + lo] ? '<' : '>');
        cout << kq << '\n';
    }
    return 0;
}
