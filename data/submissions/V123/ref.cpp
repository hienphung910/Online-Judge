// V123 - Dem tan suat bang map: so ten khac nhau va ten nhieu phieu nhat
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    map<string, int> cnt;              // map duyet theo thu tu tu dien
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        cnt[s]++;
    }
    string best;
    int most = 0;
    for (auto &p : cnt)
        if (p.second > most) {         // chi doi khi lon hon han -> giu ten nho nhat khi hoa
            most = p.second;
            best = p.first;
        }
    cout << cnt.size() << '\n' << best << ' ' << most << '\n';
    return 0;
}
