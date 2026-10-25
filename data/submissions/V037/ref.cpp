// V037 - Mo phong hang cho: voi moi khach, tim quay trong so nho nhat,
// neu khong co thi lay quay giai phong som nhat (hoa thi so nho nhat)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<long long> ranh(k + 1, 0);   // ranh[j] = thoi diem quay j trong tro lai
    for (int i = 0; i < n; i++) {
        long long t, d;
        cin >> t >> d;
        int chon = -1;
        for (int j = 1; j <= k; j++)
            if (ranh[j] <= t) { chon = j; break; }      // co quay trong ngay
        long long batDau = t;
        if (chon == -1) {                               // phai cho
            chon = 1;
            for (int j = 2; j <= k; j++)
                if (ranh[j] < ranh[chon]) chon = j;
            batDau = ranh[chon];
        }
        ranh[chon] = batDau + d;
        cout << chon << " " << ranh[chon] << "\n";
    }
    return 0;
}
