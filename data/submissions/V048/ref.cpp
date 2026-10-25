// V048 - De quy co nho: f(L) = f(L/p) + f(L/q), luu ket qua vao map
#include <bits/stdc++.h>
using namespace std;

long long p, q;
map<long long, long long> nho;

long long f(long long L) {
    if (L == 0) return 1;
    auto it = nho.find(L);
    if (it != nho.end()) return it->second;   // da tinh roi thi dung lai
    long long kq = f(L / p) + f(L / q);
    nho[L] = kq;
    return kq;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        long long n;
        cin >> n >> p >> q;
        nho.clear();                            // moi cau hoi co p, q khac nhau
        cout << f(n) << "\n";
    }
    return 0;
}
