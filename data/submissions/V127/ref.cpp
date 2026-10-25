// V127 - Bang bam theo khoa chuan hoa: moi diem -> huong (x/g, y/g) voi dau co dinh, dem nhom
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    map<pair<long long, long long>, int> cnt;   // so nha tren moi duong thang qua goc
    long long pairs = 0;
    int best = 0;
    for (int i = 0; i < n; i++) {
        long long x, y;
        cin >> x >> y;
        long long g = __gcd(llabs(x), llabs(y));
        x /= g;
        y /= g;
        if (x < 0 || (x == 0 && y < 0)) {      // (x, y) va (-x, -y) cung mot duong -> chon mot dau
            x = -x;
            y = -y;
        }
        int &c = cnt[{x, y}];
        pairs += c;                            // nha moi ghep cap voi moi nha cu cung duong
        c++;
        best = max(best, c);
    }
    cout << pairs << ' ' << best << '\n';
    return 0;
}
