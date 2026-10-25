// V249 - Chia de tri CDQ: dem cap i < j co a_i < a_j va b_i < b_j
// Chia doi theo chi so. Cap cheo (i o nua trai, j o nua phai) tu dong thoa i < j,
// chi con dieu kien a, b: duyet hai nua da sap theo a, them b_i cua ben trai vao
// cay Fenwick roi hoi so b_i < b_j. Tong O(n log^2 n).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MAXV = 100000;
int fw[MAXV + 1];
void add(int i, int v) { for (; i <= MAXV; i += i & -i) fw[i] += v; }
int sum(int i) { int s = 0; for (; i > 0; i -= i & -i) s += fw[i]; return s; }

vector<pair<int, int>> p, tmp;       // (a, b), ban dau theo thu tu chi so
ll ans = 0;

void cdq(int l, int r) {             // xong thi p[l..r) sap theo a tang dan
    if (r - l <= 1) return;
    int m = (l + r) / 2;
    cdq(l, m);
    cdq(m, r);
    int i = l;
    for (int j = m; j < r; j++) {
        while (i < m && p[i].first < p[j].first) add(p[i++].second, 1);  // a_i < a_j (nghiem ngat)
        ans += sum(p[j].second - 1);                                     // b_i < b_j
    }
    for (int k = l; k < i; k++) add(p[k].second, -1);                    // xoa cay
    merge(p.begin() + l, p.begin() + m, p.begin() + m, p.begin() + r, tmp.begin() + l);
    copy(tmp.begin() + l, tmp.begin() + r, p.begin() + l);
}

int main() {
    int n;
    cin >> n;
    p.resize(n);
    tmp.resize(n);
    for (auto& q : p) cin >> q.first >> q.second;
    cdq(0, n);
    cout << ans << "\n";
    return 0;
}
