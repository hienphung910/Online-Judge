// V129 - Tap hop co thu tu (std::set) cac cho trong: lower_bound tim cho trong dau tien >= p
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    set<int> trong;
    for (int i = 1; i <= n; i++) trong.insert(i);
    while (q--) {
        char t;
        int v;
        cin >> t >> v;
        if (t == '-') {
            trong.insert(v);
            continue;
        }
        if (trong.empty()) {
            cout << -1 << '\n';
            continue;
        }
        auto it = trong.lower_bound(v);         // cho trong nho nhat >= v
        if (it == trong.end()) it = trong.begin();  // het cho phia sau -> vong lai tu cho 1
        cout << *it << '\n';
        trong.erase(it);
    }
    return 0;
}
