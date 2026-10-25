// V182 - Chu ky nho nhat va so vien cua xau bang ham tien to (KMP), O(n)
// pi[i] = do dai vien dai nhat cua S[0..i]. Chu ky nho nhat = n - pi[n-1].
// Cac vien cua S la pi[n-1], pi[pi[n-1]-1], ... (nhay dan den 0).
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.size();
    vector<int> pi(n, 0);
    for (int i = 1; i < n; i++) {
        int k = pi[i - 1];
        while (k > 0 && s[i] != s[k]) k = pi[k - 1];
        if (s[i] == s[k]) k++;
        pi[i] = k;
    }
    int soVien = 0;
    for (int k = pi[n - 1]; k > 0; k = pi[k - 1]) soVien++;
    cout << n - pi[n - 1] << ' ' << soVien << '\n';
    return 0;
}
