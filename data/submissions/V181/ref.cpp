// V181 - Tong do dai tien to chung cua S voi moi hau to, dung ham Z, O(n)
// z[i] = do dai tien to chung dai nhat cua S va S[i..n-1]; z[0] = n.
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.size();
    vector<int> z(n, 0);
    z[0] = n;
    int l = 0, r = 0;                      // [l, r) la doan khop xa nhat ve ben phai
    for (int i = 1; i < n; i++) {
        if (i < r) z[i] = min(r - i, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
        if (i + z[i] > r) { l = i; r = i + z[i]; }
    }
    long long tong = 0;
    for (int i = 0; i < n; i++) tong += z[i];
    cout << tong << '\n';
    return 0;
}
