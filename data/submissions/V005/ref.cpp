// V005 - Chon nhieu doan khong giao nhau nhat: tham lam theo dau mut phai nho nhat
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<long long, long long>> seg(n);   // luu (r, l) de sort theo r
    for (auto &s : seg) cin >> s.second >> s.first;
    sort(seg.begin(), seg.end());
    long long lastEnd = LLONG_MIN;
    int cnt = 0;
    for (auto &s : seg) {
        if (s.second >= lastEnd) {   // cham dau mut van duoc chon
            cnt++;
            lastEnd = s.first;
        }
    }
    cout << cnt << "\n";
    return 0;
}
