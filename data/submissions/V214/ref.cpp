// V214 - Chia can: cong mot gia tri vao doan, hoi tong doan
// Moi khoi luu tong that sum[] va gia tri "cong cho" lazy[] ap dung cho ca khoi.
#include <bits/stdc++.h>
using namespace std;

int n, B;
vector<long long> a, sum_, lazy_;

void addOne(int i, long long x) { a[i] += x; sum_[i / B] += x; }

int main() {
    int q;
    cin >> n >> q;
    B = max(1, (int)sqrt((double)n));
    a.assign(n, 0); sum_.assign(n / B + 1, 0); lazy_.assign(n / B + 1, 0);
    for (int i = 0; i < n; i++) { cin >> a[i]; sum_[i / B] += a[i]; }
    while (q--) {
        int t, l, r;
        cin >> t >> l >> r;
        l--, r--;
        if (t == 1) {
            long long x;
            cin >> x;
            while (l <= r && l % B != 0) addOne(l++, x);
            while (l + B - 1 <= r) { lazy_[l / B] += x; l += B; }   // ca khoi: chi ghi cho
            while (l <= r) addOne(l++, x);
        } else {
            long long s = 0;
            // phan tu le: gia tri that = a[i] + lazy cua khoi chua no
            while (l <= r && l % B != 0) { s += a[l] + lazy_[l / B]; l++; }
            while (l + B - 1 <= r) { s += sum_[l / B] + lazy_[l / B] * B; l += B; }
            while (l <= r) { s += a[l] + lazy_[l / B]; l++; }
            cout << s << '\n';
        }
    }
    return 0;
}
