// V057 - Uoc chung lon nhat (Euclid): canh gach vuong lon nhat va so vien gach
#include <bits/stdc++.h>
using namespace std;

long long gcdEuclid(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    int q;
    cin >> q;
    while (q--) {
        long long a, b;
        cin >> a >> b;
        long long g = gcdEuclid(a, b);
        cout << g << " " << (a / g) * (b / g) << "\n";
    }
    return 0;
}
