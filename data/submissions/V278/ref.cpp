// V278 - Tham lam tren matroid tuyen tinh: co so XOR co tong trong so lon nhat
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int basis[30];  // basis[b] = vector co bit cao nhat la b (0 neu chua co)

// thu chen x vao co so; tra ve true neu x doc lap voi cac vector da chon
bool insertVec(int x) {
    for (int b = 29; b >= 0; b--) {
        if (!(x >> b & 1)) continue;
        if (basis[b] == 0) { basis[b] = x; return true; }
        x ^= basis[b];
    }
    return false;  // x bi khu ve 0: phu thuoc tuyen tinh
}

int main() {
    int n;
    scanf("%d", &n);
    vector<pair<ll, int>> items(n);  // (gia tri, ma)
    for (auto &it : items) scanf("%d %lld", &it.second, &it.first);
    sort(items.rbegin(), items.rend());  // gia tri giam dan
    ll total = 0;
    for (auto &it : items)
        if (insertVec(it.second)) total += it.first;
    printf("%lld\n", total);
    return 0;
}
