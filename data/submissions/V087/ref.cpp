// V087 - Phu doan [0, L] bang it doan nhat: tham lam chon doan vuon xa nhat
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, L;
    cin >> n >> L;
    vector<pair<int, int>> a(n);
    for (auto &x : a) cin >> x.first >> x.second;
    sort(a.begin(), a.end());
    int reach = 0, cnt = 0, i = 0;
    while (reach < L) {
        int best = reach;
        while (i < n && a[i].first <= reach) {   // cac den bat dau trong vung da sang
            best = max(best, a[i].second);
            i++;
        }
        if (best == reach) { cout << -1 << "\n"; return 0; }   // bi ho
        reach = best;
        cnt++;
    }
    cout << cnt << "\n";
    return 0;
}
