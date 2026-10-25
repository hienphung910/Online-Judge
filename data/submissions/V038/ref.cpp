// V038 - Bang diem ICPC: cap nhat so bai giai va thoi gian phat sau moi lan nop,
// moi cau hoi thi duyet N doi de dem so doi xep tren
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, e;
    cin >> n >> m >> e;
    vector<int> giai(n + 1, 0), phat(n + 1, 0);
    vector<vector<int>> sai(n + 1, vector<int>(m, 0));          // so lan WA truoc khi AC
    vector<vector<bool>> xong(n + 1, vector<bool>(m, false));
    // a xep tren b?
    auto tren = [&](int a, int b) {
        return giai[a] > giai[b] || (giai[a] == giai[b] && phat[a] < phat[b]);
    };
    while (e--) {
        string loai;
        cin >> loai;
        if (loai == "NOP") {
            int t, d; string p, v;
            cin >> t >> d >> p >> v;
            int b = p[0] - 'A';
            if (xong[d][b]) continue;                 // da giai: bo qua
            if (v == "WA") sai[d][b]++;
            else {
                xong[d][b] = true;
                giai[d]++;
                phat[d] += t + 20 * sai[d][b];
            }
        } else if (loai == "HANG") {
            int d;
            cin >> d;
            int hang = 1;
            for (int x = 1; x <= n; x++) if (tren(x, d)) hang++;
            cout << hang << "\n";
        } else {
            int best = 1;
            for (int x = 2; x <= n; x++) if (tren(x, best)) best = x;   // chi doi khi tot hon han
            cout << best << "\n";
        }
    }
    return 0;
}
