// V109 - Mang cong don (prefix sum) 1 chieu, moi truy van O(1)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<long long> s(n + 1, 0);   // s[i] = a[1] + ... + a[i]
    for (int i = 1; i <= n; i++) {
        long long a;
        cin >> a;
        s[i] = s[i - 1] + a;
    }
    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << s[r] - s[l - 1] << "\n";
    }
    return 0;
}
