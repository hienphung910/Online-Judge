// V002 - Dem so cach dat n quan hau bang quay lui, danh dau cot va hai duong cheo
#include <bits/stdc++.h>
using namespace std;

int n;
long long cnt = 0;
bool cot[20], cheo1[40], cheo2[40];   // cheo1: r + c, cheo2: r - c + n

void datHau(int r) {
    if (r == n) { cnt++; return; }
    for (int c = 0; c < n; c++) {
        if (cot[c] || cheo1[r + c] || cheo2[r - c + n]) continue;
        cot[c] = cheo1[r + c] = cheo2[r - c + n] = true;
        datHau(r + 1);
        cot[c] = cheo1[r + c] = cheo2[r - c + n] = false;   // quay lui
    }
}

int main() {
    cin >> n;
    datHau(0);
    cout << cnt << "\n";
    return 0;
}
