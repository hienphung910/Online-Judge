// V050 - Quay lui liet ke cach phan tich n thanh tong cac so khong tang, moi so <= m
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> cur;
vector<vector<int>> kq;

void chia(int conLai, int lonNhat) {
    if (conLai == 0) { kq.push_back(cur); return; }
    for (int x = min(conLai, lonNhat); x >= 1; x--) {   // thu tu lon xuong nho
        cur.push_back(x);
        chia(conLai - x, x);
        cur.pop_back();
    }
}

int main() {
    cin >> n >> m;
    chia(n, m);
    cout << kq.size() << "\n";
    for (auto &p : kq) {
        for (int i = 0; i < (int)p.size(); i++) cout << p[i] << (i + 1 < (int)p.size() ? " " : "\n");
    }
    return 0;
}
