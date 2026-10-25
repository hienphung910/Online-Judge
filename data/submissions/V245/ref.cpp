// V245 - Chat tam phan tren so thuc: chon diem xuong nuoc de cuu ho nhanh nhat
// Diem xuong nuoc (x, 0) voi 0 <= x <= d. Thoi gian
//   f(x) = sqrt(x^2 + a^2) / v1 + sqrt((d - x)^2 + b^2) / v2
// la tong hai ham loi nen loi -> chat tam phan 100 lan.
#include <bits/stdc++.h>
using namespace std;

double a, b, d, v1, v2;

double f(double x) {
    return sqrt(x * x + a * a) / v1 + sqrt((d - x) * (d - x) + b * b) / v2;
}

int main() {
    int q;
    cin >> q;
    while (q--) {
        cin >> a >> b >> d >> v1 >> v2;
        double lo = 0, hi = d;
        for (int it = 0; it < 100; it++) {
            double m1 = lo + (hi - lo) / 3, m2 = hi - (hi - lo) / 3;
            if (f(m1) < f(m2)) hi = m2;   // cuc tieu khong nam ben phai m2
            else lo = m1;                 // cuc tieu khong nam ben trai m1
        }
        printf("%.9f\n", f((lo + hi) / 2));
    }
    return 0;
}
