// V054 - Chia viec cho k tho, toi thieu thoi diem xong: quay lui + nhanh can
#include <bits/stdc++.h>
using namespace std;

int n, k;
long long t[20], tai[20], best, canDuoi;

void giao(int i) {
    if (best == canDuoi) return;                        // da dat can duoi, khong the tot hon
    if (i == n) {
        best = *max_element(tai, tai + k);
        return;
    }
    for (int w = 0; w < k; w++) {
        if (tai[w] + t[i] >= best) continue;            // nhanh can: khong tot hon ket qua hien co
        bool trung = false;                             // tho co cung tai voi tho truoc: thu lai la thua
        for (int u = 0; u < w; u++) if (tai[u] == tai[w]) trung = true;
        if (trung) continue;
        tai[w] += t[i];
        giao(i + 1);
        tai[w] -= t[i];
    }
}

int main() {
    cin >> n >> k;
    long long tong = 0;
    for (int i = 0; i < n; i++) { cin >> t[i]; tong += t[i]; }
    sort(t, t + n, greater<long long>());               // viec lon xep truoc de cat nhanh som
    canDuoi = max(t[0], (tong + k - 1) / k);
    // ket qua ban dau: giao lan luot moi viec cho tho dang ranh nhat (tham lam)
    for (int i = 0; i < n; i++) *min_element(tai, tai + k) += t[i];
    best = *max_element(tai, tai + k);
    fill(tai, tai + k, 0);
    giao(0);
    cout << best << "\n";
    return 0;
}
