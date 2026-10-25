// V042 - Dem bo ba que ghep duoc tam giac bang cach duyet moi bo ba
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (auto &x : a) cin >> x;
    long long dem = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            for (int k = j + 1; k < n; k++) {
                long long x = a[i], y = a[j], z = a[k];
                if (x + y > z && y + z > x && x + z > y) dem++;   // dung long long tranh tran so
            }
    cout << dem << "\n";
    return 0;
}
