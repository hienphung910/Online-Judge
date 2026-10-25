// V099 - Doan dai nhat co khong qua K gia tri phan biet (hai con tro)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> c(n);
    for (auto &x : c) cin >> x;
    map<int, int> cnt;   // so lan xuat hien cua moi mau trong cua so [l, r]
    int best = 0, l = 0;
    for (int r = 0; r < n; r++) {
        cnt[c[r]]++;
        while ((int)cnt.size() > k) {
            if (--cnt[c[l]] == 0) cnt.erase(c[l]);
            l++;
        }
        best = max(best, r - l + 1);
    }
    cout << best << "\n";
    return 0;
}
