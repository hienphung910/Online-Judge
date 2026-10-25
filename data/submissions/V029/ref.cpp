// V029 - Ngay ke tiep: kiem tra ngay hop le (nam nhuan), roi xu ly sang thang / sang nam
#include <bits/stdc++.h>
using namespace std;

bool nhuan(int y) { return y % 400 == 0 || (y % 4 == 0 && y % 100 != 0); }

int soNgay(int m, int y) {
    if (m == 2) return nhuan(y) ? 29 : 28;
    if (m == 4 || m == 6 || m == 9 || m == 11) return 30;
    return 31;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int d, m, y;
        cin >> d >> m >> y;
        if (m < 1 || m > 12 || d < 1 || d > soNgay(m, y)) {
            cout << "KHONG HOP LE\n";
            continue;
        }
        d++;
        if (d > soNgay(m, y)) { d = 1; m++; }   // sang thang moi
        if (m > 12) { m = 1; y++; }             // sang nam moi
        cout << d << " " << m << " " << y << "\n";
    }
    return 0;
}
