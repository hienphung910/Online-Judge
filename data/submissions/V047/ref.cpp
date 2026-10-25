// V047 - Dem bo x <= y <= z co tich <= n: duyet x den can bac ba, y den can bac hai, z tinh bang phep chia
#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n;
    cin >> n;
    long long dem = 0;
    for (long long x = 1; x * x * x <= n; x++)
        for (long long y = x; x * y * y <= n; y++)
            dem += n / (x * y) - y + 1;      // z chay tu y den n / (x*y)
    cout << dem << "\n";
    return 0;
}
