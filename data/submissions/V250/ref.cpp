// V250 - Chat nhi phan song song: dot tuoi dau tien moi ho du nuoc
// Moi ho chat nhi phan dap an trong [1, k+1] (k+1 = khong bao gio du).
// Moi vong: xoa cay Fenwick, lan luot ap dung dot tuoi 1..k (cong doan, hoi diem),
// sau dot t thi kiem tra moi ho dang co mid = t. Khoang log k vong.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, m, k;
vector<ll> fw;
void add(int i, ll v) { for (; i <= m; i += i & -i) fw[i] += v; }
ll get(int i) { ll s = 0; for (; i > 0; i -= i & -i) s += fw[i]; return s; }

int main() {
    cin >> n >> m >> k;
    vector<vector<int>> cells(n + 1);           // cac thua cua moi ho
    for (int j = 1; j <= m; j++) { int o; cin >> o; cells[o].push_back(j); }
    vector<ll> need(n + 1);
    for (int i = 1; i <= n; i++) cin >> need[i];
    vector<int> L(k + 1), R(k + 1), W(k + 1);
    for (int t = 1; t <= k; t++) cin >> L[t] >> R[t] >> W[t];

    vector<int> lo(n + 1, 1), hi(n + 1, k + 1);
    while (true) {
        vector<vector<int>> at(k + 1);          // at[t] = cac ho can kiem tra sau dot t
        bool any = false;
        for (int i = 1; i <= n; i++)
            if (lo[i] < hi[i]) { at[(lo[i] + hi[i]) / 2].push_back(i); any = true; }
        if (!any) break;
        fw.assign(m + 1, 0);
        for (int t = 1; t <= k; t++) {
            add(L[t], W[t]);                     // cong W[t] cho doan [L, R]
            if (R[t] + 1 <= m) add(R[t] + 1, -W[t]);
            for (int i : at[t]) {
                ll s = 0;
                for (int c : cells[i]) s += get(c);
                if (s >= need[i]) hi[i] = t; else lo[i] = t + 1;
            }
        }
    }
    for (int i = 1; i <= n; i++) cout << (lo[i] == k + 1 ? -1 : lo[i]) << "\n";
    return 0;
}
