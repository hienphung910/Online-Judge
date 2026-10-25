// V128 - Bang bam luu lan xuat hien dau tien cua moi so du tong tien to
// Doan (l, r] co tong chia het cho K <=> pre[l] va pre[r] cung so du khi chia K.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    long long k;
    cin >> n >> k;
    unordered_map<long long, int> first;   // first[du] = chi so tien to nho nhat co so du nay
    first[0] = 0;                          // tien to rong
    long long pre = 0;
    int bestLen = 0, bestL = 0;
    for (int r = 1; r <= n; r++) {
        long long a;
        cin >> a;
        pre += a;                          // co the toi 2e12, can 64-bit
        long long du = ((pre % k) + k) % k;   // so du khong am ke ca khi pre < 0
        auto it = first.find(du);
        if (it == first.end()) {
            first[du] = r;
        } else if (r - it->second > bestLen) {   // chi doi khi dai hon han -> giu doan bat dau som nhat
            bestLen = r - it->second;
            bestL = it->second + 1;
        }
    }
    cout << bestLen << ' ' << bestL << '\n';
    return 0;
}
