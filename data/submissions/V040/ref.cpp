// V040 - Mo phong tro 2048: lay tung hang/cot theo thu tu tu mep huong di,
// don cac o khac 0, nhap cap bang nhau, ghi nguoc lai; them o 2 neu bang co thay doi
#include <bits/stdc++.h>
using namespace std;

int n;
long long a[10][10];
long long diem = 0;

// o thu k (k = 0 la sat mep) cua duong thu i theo huong h
long long &oThu(char h, int i, int k) {
    if (h == 'L') return a[i][k];
    if (h == 'R') return a[i][n - 1 - k];
    if (h == 'U') return a[k][i];
    return a[n - 1 - k][i];
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cin >> a[i][j];
    string luot;
    cin >> luot;
    int voHieu = 0;
    for (char h : luot) {
        bool doi = false;
        for (int i = 0; i < n; i++) {
            vector<long long> v, kq;
            for (int k = 0; k < n; k++) if (oThu(h, i, k) != 0) v.push_back(oThu(h, i, k));
            for (int k = 0; k < (int)v.size(); k++) {
                if (k + 1 < (int)v.size() && v[k] == v[k + 1]) {
                    kq.push_back(2 * v[k]);
                    diem += 2 * v[k];
                    k++;                       // vien moi khong nhap tiep
                } else kq.push_back(v[k]);
            }
            kq.resize(n, 0);
            for (int k = 0; k < n; k++) {
                if (oThu(h, i, k) != kq[k]) doi = true;
                oThu(h, i, k) = kq[k];
            }
        }
        if (!doi) { voHieu++; continue; }
        bool datRoi = false;
        for (int i = 0; i < n && !datRoi; i++)
            for (int j = 0; j < n && !datRoi; j++)
                if (a[i][j] == 0) { a[i][j] = 2; datRoi = true; }
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cout << a[i][j] << (j + 1 < n ? " " : "\n");
    cout << diem << " " << voHieu << "\n";
    return 0;
}
