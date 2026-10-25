// V027 - Tinh tien ve: xet lan luot tung buoc theo dung thu tu cua de
#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int a, d, h, m;
        cin >> a >> d >> h >> m;
        if (h < 8 || h >= 22) { cout << "DONG CUA\n"; continue; }
        if (a < 3) { cout << 0 << "\n"; continue; }
        int gia;
        if (d == 2) gia = 30000;                  // ngay hoi
        else {
            gia = (d >= 6) ? 70000 : 50000;       // cuoi tuan dat hon
            if (a <= 12 || a >= 65) gia /= 2;     // tre em, nguoi gia
            if (h >= 18) gia -= 10000;            // buoi toi
        }
        if (m == 1) gia = gia * 8 / 10;           // hoi vien tra 80%
        cout << gia << "\n";
    }
    return 0;
}
