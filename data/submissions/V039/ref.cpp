// V039 - Doc so thanh chu: tach nhom 3 chu so, xet tung truong hop linh / muoi / mot / tu / lam
#include <bits/stdc++.h>
using namespace std;

const string so[10] = {"khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"};
const string tenNhom[4] = {"", "nghin", "trieu", "ty"};

// doc phan chuc - don vi; coTram = co hang tram dung truoc
string chucDonVi(int b, int c, bool coTram) {
    string s;
    if (b == 0) {
        if (c != 0 && coTram) s = " linh " + so[c];
    } else if (b == 1) {
        s = " muoi";
        if (c == 5) s += " lam";
        else if (c != 0) s += " " + so[c];
    } else {
        s = " " + so[b] + " muoi";
        if (c == 4) s += " tu";
        else if (c == 5) s += " lam";
        else if (c != 0) s += " " + so[c];
    }
    return s;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        long long n;
        cin >> n;
        if (n == 0) { cout << "khong\n"; continue; }
        int nhom[4];
        for (int i = 0; i < 4; i++) { nhom[i] = n % 1000; n /= 1000; }
        int dau = 3;
        while (nhom[dau] == 0) dau--;            // nhom dau = nhom khac 0 cao nhat
        string kq;
        for (int i = dau; i >= 0; i--) {
            int g = nhom[i], a = g / 100, b = g / 10 % 10, c = g % 10;
            if (i == dau) {
                if (g >= 100) kq += " " + so[a] + " tram" + chucDonVi(b, c, true);
                else if (g >= 10) kq += chucDonVi(b, c, false);
                else kq += " " + so[c];
            } else {
                if (g == 0) continue;            // nhom 000 bo qua ca ten nhom
                kq += " " + so[a] + " tram" + chucDonVi(b, c, true);
            }
            if (i > 0) kq += " " + tenNhom[i];
        }
        cout << kq.substr(1) << "\n";
    }
    return 0;
}
