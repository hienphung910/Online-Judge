// V244 - Chat tam phan tren so nguyen: f(t) = tong |a_i + b_i * t| la ham loi
// Ham loi => hieu f(t+1) - f(t) khong giam, nen chat nhi phan tim t dau tien
// ma f(t+1) >= f(t); do chinh la diem cuc tieu.
#include <bits/stdc++.h>
using namespace std;

int n;
long long T;
vector<long long> a, b;

long long f(long long t) {
    long long s = 0;
    for (int i = 0; i < n; i++) s += llabs(a[i] + b[i] * t);
    return s;
}

int main() {
    cin >> n >> T;
    a.resize(n), b.resize(n);
    for (int i = 0; i < n; i++) cin >> a[i] >> b[i];
    long long lo = 0, hi = T;          // dap an nam trong [0, T]
    while (lo < hi) {
        long long mid = (lo + hi) / 2;
        if (f(mid + 1) >= f(mid)) hi = mid;   // di sang phai khong tot hon -> cuc tieu o ben trai
        else lo = mid + 1;
    }
    cout << f(lo) << "\n";
    return 0;
}
