// V199 - Dem cap doan ngang/doc giao nhau bang duong quet + cay Fenwick, O(n log C)
// Su kien theo x: bat doan ngang (loai 0) truoc, roi hoi doan doc (loai 1), roi tat doan ngang (loai 2)
// de cac truong hop cham dau mut deu duoc dem.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int M = 100002;
int bit[M + 1];
void upd(int i, int v) { for (i++; i <= M; i += i & -i) bit[i] += v; }
int qry(int i) { int s = 0; for (i++; i > 0; i -= i & -i) s += bit[i]; return s; }  // tong [0, i]

int main() {
    int n;
    scanf("%d", &n);
    vector<array<int, 4>> ev;   // {x, loai, a, b}
    for (int i = 0; i < n; i++) {
        int x1, y1, x2, y2;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        if (y1 == y2) {
            ev.push_back({x1, 0, y1, 0});
            ev.push_back({x2, 2, y1, 0});
        } else {
            ev.push_back({x1, 1, y1, y2});
        }
    }
    sort(ev.begin(), ev.end());
    ll ans = 0;
    for (auto &e : ev) {
        if (e[1] == 0) upd(e[2], 1);
        else if (e[1] == 2) upd(e[2], -1);
        else ans += qry(e[3]) - qry(e[2] - 1);
    }
    printf("%lld\n", ans);
    return 0;
}
