// V020 - Diem hen gap nhau nhanh nhat: chat nhi phan theo thoi gian T, O(n * 100)
// Sau T giay ban i co the o bat ky dau trong doan [x_i - v_i*T, x_i + v_i*T].
// Moi nguoi gap duoc nhau <=> cac doan co diem chung <=> max(trai) <= min(phai).
#include <bits/stdc++.h>
using namespace std;
typedef long double ld;

int n;
vector<ld> x, v;

bool ok(ld T) {
    ld L = -1e30L, R = 1e30L;
    for (int i = 0; i < n; i++) {
        L = max(L, x[i] - v[i] * T);
        R = min(R, x[i] + v[i] * T);
    }
    return L <= R;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    x.resize(n), v.resize(n);
    for (int i = 0; i < n; i++) {
        long long a, b;
        cin >> a >> b;
        x[i] = a, v[i] = b;
    }
    ld lo = 0, hi = 2e9L;          // T = 2e9 luon du (khoang cach <= 2e9, toc do >= 1)
    for (int it = 0; it < 100; it++) {
        ld mid = (lo + hi) / 2;
        if (ok(mid)) hi = mid; else lo = mid;
    }
    cout << fixed << setprecision(9) << (double)hi << "\n";
    return 0;
}
