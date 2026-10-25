// V046 - Quay lui sinh xau nhi phan khong co hai so 1 ke nhau, toi da k so 1
#include <bits/stdc++.h>
using namespace std;

int n, k;
string s;
vector<string> kq;

void thu(int i, int soMot) {
    if (i == n) { kq.push_back(s); return; }
    s[i] = '0';
    thu(i + 1, soMot);
    if ((i == 0 || s[i - 1] == '0') && soMot < k) {
        s[i] = '1';
        thu(i + 1, soMot + 1);
        s[i] = '0';                        // tra lai trang thai cu
    }
}

int main() {
    cin >> n >> k;
    s = string(n, '0');
    thu(0, 0);
    cout << kq.size() << "\n";
    for (auto &x : kq) cout << x << "\n";
    return 0;
}
