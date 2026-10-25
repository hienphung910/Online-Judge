// V036 - So La Ma: bang 13 cap (gia tri, ky hieu), doi so -> chu bang tham lam;
// doi chu -> so: cong/tru theo ky hieu ke tiep, roi doi nguoc lai de kiem tra cach viet chuan
#include <bits/stdc++.h>
using namespace std;

int giaTri[13] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
string kyHieu[13] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

string sangLaMa(int n) {
    string s;
    for (int i = 0; i < 13; i++)
        while (n >= giaTri[i]) { s += kyHieu[i]; n -= giaTri[i]; }
    return s;
}

int mot(char c) {
    switch (c) {
        case 'I': return 1;    case 'V': return 5;   case 'X': return 10;
        case 'L': return 50;   case 'C': return 100; case 'D': return 500;
        default: return 1000;
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        if (isdigit(s[0])) { cout << sangLaMa(stoi(s)) << "\n"; continue; }
        int n = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            if (i + 1 < (int)s.size() && mot(s[i]) < mot(s[i + 1])) n -= mot(s[i]);
            else n += mot(s[i]);
        }
        if (n >= 1 && n <= 3999 && sangLaMa(n) == s) cout << n << "\n";
        else cout << "KHONG HOP LE\n";
    }
    return 0;
}
