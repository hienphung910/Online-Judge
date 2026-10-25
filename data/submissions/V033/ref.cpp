// V033 - Co ca-ro 3x3: dem quan, kiem tra ai thang, roi xet lan luot cac truong hop
#include <bits/stdc++.h>
using namespace std;

string b;

bool thang(char p) {
    int L[8][3] = {{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}};
    for (auto &l : L)
        if (b[l[0]] == p && b[l[1]] == p && b[l[2]] == p) return true;
    return false;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        string r1, r2, r3;
        cin >> r1 >> r2 >> r3;
        b = r1 + r2 + r3;
        int x = count(b.begin(), b.end(), 'X');
        int o = count(b.begin(), b.end(), 'O');
        bool xt = thang('X'), ot = thang('O');
        string kq;
        if (x != o && x != o + 1) kq = "KHONG HOP LE";      // X di truoc nen x = o hoac o + 1
        else if (xt && ot) kq = "KHONG HOP LE";             // van dung ngay khi co nguoi thang
        else if (xt) kq = (x == o + 1) ? "X THANG" : "KHONG HOP LE";   // X vua di nuoc cuoi
        else if (ot) kq = (x == o) ? "O THANG" : "KHONG HOP LE";       // O vua di nuoc cuoi
        else if (x + o == 9) kq = "HOA";
        else kq = (x == o) ? "LUOT X" : "LUOT O";
        cout << kq << "\n";
    }
    return 0;
}
