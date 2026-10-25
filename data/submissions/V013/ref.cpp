// V013 - Dem so lan xuat hien cua P trong T bang KMP (ham tien to), O(|T| + |P|)
// pi[i] = do dai tien to dai nhat cua P (khac P[0..i]) cung la hau to cua P[0..i].
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string t, p;
    cin >> t >> p;
    int m = p.size();
    vector<int> pi(m, 0);
    for (int i = 1; i < m; i++) {
        int k = pi[i - 1];
        while (k > 0 && p[i] != p[k]) k = pi[k - 1];
        if (p[i] == p[k]) k++;
        pi[i] = k;
    }

    long long cnt = 0;
    int k = 0;                       // so ky tu cua P dang khop
    for (char ch : t) {
        while (k > 0 && ch != p[k]) k = pi[k - 1];
        if (ch == p[k]) k++;
        if (k == m) {                // khop tron P, lui ve de dem ca lan chong nhau
            cnt++;
            k = pi[k - 1];
        }
    }
    cout << cnt << '\n';
    return 0;
}
