// V074 - Chi so anh huong (h-index) bang sap xep dem, O(n)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> cnt(n + 1, 0);          // cnt[v] = so bai co min(c, n) = v
    for (int i = 0; i < n; i++) {
        long long c;
        cin >> c;
        cnt[min<long long>(c, n)]++;
    }
    int atLeast = 0;                    // so bai co it nhat h trich dan
    for (int h = n; h >= 0; h--) {
        atLeast += cnt[h];
        if (atLeast >= h) { cout << h << "\n"; return 0; }
    }
    return 0;
}
