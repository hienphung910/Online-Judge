// V070 - Sap xep theo nhieu tieu chi: tong giam dan, Toan giam dan, ten tang dan
#include <bits/stdc++.h>
using namespace std;

struct HocSinh {
    string ten;
    int toan, van, anh;
    int tong() const { return toan + van + anh; }
};

int main() {
    int n;
    cin >> n;
    vector<HocSinh> a(n);
    for (auto &h : a) cin >> h.ten >> h.toan >> h.van >> h.anh;
    sort(a.begin(), a.end(), [](const HocSinh &x, const HocSinh &y) {
        if (x.tong() != y.tong()) return x.tong() > y.tong();
        if (x.toan != y.toan) return x.toan > y.toan;
        return x.ten < y.ten;
    });
    for (auto &h : a) cout << h.ten << "\n";
    return 0;
}
