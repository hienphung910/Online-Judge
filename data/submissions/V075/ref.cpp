// V075 - Mo phong sap xep nhanh voi chot la phan tu dau, dem so phep so sanh
#include <bits/stdc++.h>
using namespace std;

long long soSanh = 0;

void quickSort(const vector<int> &a) {
    if (a.size() <= 1) return;
    int chot = a[0];
    vector<int> trai, phai;
    for (size_t i = 1; i < a.size(); i++) {
        soSanh++;
        if (a[i] < chot) trai.push_back(a[i]);
        else phai.push_back(a[i]);
    }
    quickSort(trai);
    quickSort(phai);
}

int main() {
    int n;
    cin >> n;
    vector<int> p(n);
    for (auto &x : p) cin >> x;
    quickSort(p);
    cout << soSanh << "\n";
    return 0;
}
