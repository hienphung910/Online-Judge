// V001 - Phan loai tam giac: xet lan luot tung truong hop, binh phuong dung long long
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    string res;
    while (t--) {
        long long s[3];
        cin >> s[0] >> s[1] >> s[2];
        sort(s, s + 3);                       // s[2] la canh lon nhat
        long long a = s[0], b = s[1], c = s[2];
        if (c >= a + b) res += "KHONG HOP LE\n";
        else if (a == c) res += "DEU\n";      // da sap xep nen a == c thi ca 3 bang nhau
        else if (a * a + b * b == c * c) res += "VUONG\n";
        else if (a == b || b == c) res += "CAN\n";
        else res += "THUONG\n";
    }
    cout << res;
    return 0;
}
