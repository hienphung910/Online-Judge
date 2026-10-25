// V237 - Tro choi Nim: XOR cac dong va dem so nuoc di thang
// Nguoi di truoc thang khi X = a_1 ^ ... ^ a_n khac 0.
// Nuoc thang o dong i: dua a_i ve a_i ^ X, chi lam duoc khi (a_i ^ X) < a_i.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> a(n);
    long long X = 0;
    for (auto &x : a) {
        cin >> x;
        X ^= x;
    }
    int cnt = 0;
    for (long long x : a)
        if ((x ^ X) < x) cnt++;      // khi X = 0 dieu kien nay luon sai nen cnt = 0
    cout << (X ? "AN" : "BINH") << "\n" << cnt << "\n";
    return 0;
}
