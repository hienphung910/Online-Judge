// V031 - Truy van don gian tren mang: duyet thang doan [l, r] cho moi cau hoi
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    while (q--) {
        int loai;
        cin >> loai;
        if (loai == 1) {
            int i; long long x;
            cin >> i >> x;
            a[i] = x;
        } else if (loai == 2 || loai == 3) {
            int l, r;
            cin >> l >> r;
            long long tong = 0, lon = a[l];
            for (int i = l; i <= r; i++) { tong += a[i]; lon = max(lon, a[i]); }
            cout << (loai == 2 ? tong : lon) << "\n";
        } else {
            long long x;
            cin >> x;
            int dem = 0;
            for (int i = 1; i <= n; i++) if (a[i] >= x) dem++;
            cout << dem << "\n";
        }
    }
    return 0;
}
