// V043 - Thu lan luot n, n+1, ... cho den khi gap so co cac chu so doi mot khac nhau
#include <bits/stdc++.h>
using namespace std;

bool khacNhau(long long x) {
    bool daCo[10] = {false};
    while (x > 0) {
        int d = x % 10;
        if (daCo[d]) return false;
        daCo[d] = true;
        x /= 10;
    }
    return true;
}

int main() {
    long long n;
    cin >> n;
    long long x = n;
    while (!khacNhau(x)) x++;
    cout << x << "\n";
    return 0;
}
