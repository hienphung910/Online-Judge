// V056 - Phep chia lay du voi so am: vi tri kim tren vong tron m cabin
#include <bits/stdc++.h>
using namespace std;

int main() {
    long long m, n, p;
    cin >> m >> n >> p;
    for (int i = 0; i < n; i++) {
        long long d;
        cin >> d;
        p = ((p + d % m) % m + m) % m;   // d % m co the am nen cong them m
    }
    cout << p << "\n";
    return 0;
}
