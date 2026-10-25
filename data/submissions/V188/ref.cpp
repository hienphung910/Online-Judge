// V188 - Dem vi tri khop P voi T sai toi da 1 ky tu, dung ham Z hai chieu, O(|T| + |P|)
// pre[i] = so ky tu dau cua T[i..] khop voi dau P   (Z cua P + '#' + T)
// suf[j] = so ky tu cuoi cua T[..j] khop voi cuoi P (Z cua rev(P) + '#' + rev(T))
// Vi tri i hop le khi pre[i] + suf[i+m-1] >= m - 1.
#include <bits/stdc++.h>
using namespace std;

vector<int> zfunc(const string& s) {
    int n = s.size();
    vector<int> z(n, 0);
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i < r) z[i] = min(r - i, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
        if (i + z[i] > r) { l = i; r = i + z[i]; }
    }
    return z;
}

int main() {
    string t, p;
    cin >> t >> p;
    int n = t.size(), m = p.size();
    if (m > n) { cout << 0 << '\n'; return 0; }
    vector<int> z1 = zfunc(p + "#" + t);
    string rt(t.rbegin(), t.rend()), rp(p.rbegin(), p.rend());
    vector<int> z2 = zfunc(rp + "#" + rt);
    int dem = 0;
    for (int i = 0; i + m <= n; i++) {
        int pre = z1[m + 1 + i];                 // khop tu dau tai T[i]
        int j = i + m - 1;                       // vi tri cuoi cua cua so
        int suf = z2[m + 1 + (n - 1 - j)];       // khop tu cuoi tai T[j]
        if (pre + suf >= m - 1) dem++;
    }
    cout << dem << '\n';
    return 0;
}
