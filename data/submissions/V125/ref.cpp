// V125 - Danh sach lien ket doi: rut mot nut ra va chen lai truoc/sau nut khac trong O(1)
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> L, R;   // L[i], R[i]: nguoi dung truoc / sau hoc sinh i; 0 la nut gia dau hang, n+1 la nut gia cuoi hang

void rut(int x) {           // bo x ra khoi hang
    R[L[x]] = R[x];
    L[R[x]] = L[x];
}
void chenSau(int x, int y) { // dat x ngay sau y
    L[x] = y;
    R[x] = R[y];
    L[R[y]] = x;
    R[y] = x;
}

int main() {
    cin >> n >> m;
    L.resize(n + 2);
    R.resize(n + 2);
    for (int i = 0; i <= n + 1; i++) {
        L[i] = i - 1;
        R[i] = i + 1;
    }
    while (m--) {
        char t;
        int x, y;
        cin >> t >> x >> y;
        rut(x);
        if (t == 'A') chenSau(x, y);
        else chenSau(x, L[y]);   // dung truoc y = dung sau nguoi dang dung truoc y
    }
    for (int i = R[0]; i != n + 1; i = R[i]) cout << i << (R[i] == n + 1 ? '\n' : ' ');
    return 0;
}
