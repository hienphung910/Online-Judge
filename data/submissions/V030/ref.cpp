// V030 - Mo phong thang may: di den a, mo cua, di den b, mo cua; tong dung long long
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    long long f;
    cin >> n >> f;
    long long cur = 1, tang = 0, mocua = 0;
    for (int i = 0; i < n; i++) {
        long long a, b;
        cin >> a >> b;
        tang += llabs(a - cur); cur = a; mocua++;   // den don khach
        tang += llabs(b - cur); cur = b; mocua++;   // dua khach den noi
    }
    cout << tang << " " << tang * 2 + mocua * 5 << "\n";
    return 0;
}
