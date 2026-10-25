// V045 - Dem cach viet n = a^2 + b^2: chi duyet a den sqrt(n/2)
#include <bits/stdc++.h>
using namespace std;

long long canNguyen(long long x) {          // phan nguyen cua can bac hai
    long long r = sqrtl((long double)x);
    while (r * r > x) r--;
    while ((r + 1) * (r + 1) <= x) r++;
    return r;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        long long n;
        cin >> n;
        int dem = 0;
        for (long long a = 1; 2 * a * a <= n; a++) {
            long long r = n - a * a;
            long long b = canNguyen(r);
            if (b * b == r) dem++;               // b >= a vi 2a^2 <= n
        }
        cout << dem << "\n";
    }
    return 0;
}
