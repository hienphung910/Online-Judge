// V102 - Day con chung dai nhat (LCS), quy hoach dong hai dong
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s, t;
    cin >> s >> t;
    int n = s.size(), m = t.size();
    vector<int> prv(m + 1, 0), cur(m + 1, 0);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (s[i - 1] == t[j - 1]) cur[j] = prv[j - 1] + 1;
            else cur[j] = max(prv[j], cur[j - 1]);
        }
        swap(prv, cur);
    }
    cout << prv[m] << "\n";
    return 0;
}
