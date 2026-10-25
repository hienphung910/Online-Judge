// V094 - Tim so xuat hien le lan bang phep XOR
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    long long x = 0;
    for (int i = 0; i < n; i++) {
        long long a;
        cin >> a;
        x ^= a;   // cac so giong nhau tu triet tieu
    }
    cout << x << "\n";
    return 0;
}
