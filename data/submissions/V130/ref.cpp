// V130 - multiset: lower_bound cho phan tu >= x va phan tu dung truoc no (< x), so sanh hai ung vien
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    multiset<long long> ke;
    while (q--) {
        char t;
        long long x;
        cin >> t >> x;
        if (t == '+') {
            ke.insert(x);
        } else if (t == '-') {
            ke.erase(ke.find(x));             // chi xoa MOT ban sao
        } else if (ke.empty()) {
            cout << "KHONG\n";
        } else {
            auto it = ke.lower_bound(x);      // phan tu nho nhat >= x
            long long best;
            if (it == ke.end()) best = *prev(it);
            else {
                best = *it;
                if (it != ke.begin() && x - *prev(it) <= *it - x)   // hoa thi chon so nho hon
                    best = *prev(it);
            }
            cout << best << '\n';
        }
    }
    return 0;
}
