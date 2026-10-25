// V232 - Trinh cham cho bai "xao tron qua" (hoan vi khong co diem bat dong)
// Moi bo: kiem tra day p co phai hoan vi 1..n va p_i != i khong; tra loi 0 chi dung khi n = 1.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) {
        int n, flag;
        cin >> n >> flag;
        bool ok;
        if (flag == 0) {
            ok = (n == 1);                 // chi khi n = 1 moi khong co cach xao tron
        } else {
            vector<ll> p(n + 1);
            for (int i = 1; i <= n; i++) cin >> p[i];
            vector<bool> seen(n + 1, false);
            ok = true;
            for (int i = 1; i <= n; i++) {
                if (p[i] < 1 || p[i] > n || seen[p[i]] || p[i] == i) { ok = false; break; }
                seen[p[i]] = true;
            }
        }
        cout << (ok ? "DUNG" : "SAI") << "\n";
    }
    return 0;
}
