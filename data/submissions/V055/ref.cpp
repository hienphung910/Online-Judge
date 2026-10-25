// V055 - Nhom ban than lon nhat (clique lon nhat): nhanh can, can tren bang to mau tham lam
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

int n, best = 0;
ull ke[64];

// To mau tham lam cac dinh trong tap s: hai dinh cung mau thi khong quen nhau,
// nen mot nhom ban than lay toi da 1 dinh moi mau -> so mau la can tren.
int soMau(ull s) {
    int mau = 0;
    while (s) {
        mau++;
        ull q = s;                         // cac dinh con co the to mau hien tai
        while (q) {
            int v = __builtin_ctzll(q);
            s &= ~(1ULL << v);
            q &= ~(1ULL << v) & ~ke[v];    // bo v va ban cua v
        }
    }
    return mau;
}

void tim(int dem, ull ungVien) {
    if (ungVien == 0) { best = max(best, dem); return; }
    if (dem + soMau(ungVien) <= best) return;                 // nhanh can
    int v = __builtin_ctzll(ungVien);
    tim(dem + 1, ungVien & ke[v]);                              // chon v: chi giu ban cua v
    tim(dem, ungVien & ~(1ULL << v));                           // bo v
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < n; j++)
            if (s[j] == '1') ke[i] |= 1ULL << j;
    }
    tim(0, n == 64 ? ~0ULL : (1ULL << n) - 1);
    cout << best << "\n";
    return 0;
}
