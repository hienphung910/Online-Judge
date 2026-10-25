// V209 - QHD chu so: dem so trong [L, R] chia het cho M va khong co hai chu so ke nhau bang nhau
// cnt[len][r][last] = so cach viet them len chu so (chu so dau khac last) de so chia het cho M,
// biet phan da viet co so du r. last = 10 nghia la khong rang buoc.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int M;
ll cnt[19][200][11];

ll dem(ll X) {                          // so luong so thoa man trong [1, X]
    if (X <= 0) return 0;
    string s = to_string(X);
    int n = s.size();
    ll res = 0;
    for (int l = 1; l < n; l++)         // cac so it chu so hon X
        for (int d = 1; d <= 9; d++) res += cnt[l - 1][d % M][d];
    int r = 0, prev = 10;
    for (int i = 0; i < n; i++) {       // cac so cung do dai, nho hon X
        int x = s[i] - '0';
        for (int d = (i == 0 ? 1 : 0); d < x; d++)
            if (d != prev) res += cnt[n - 1 - i][(r * 10 + d) % M][d];
        if (x == prev) return res;      // tien to cua X da hong
        r = (r * 10 + x) % M;
        prev = x;
    }
    if (r == 0) res++;                  // chinh X
    return res;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        ll L, R;
        cin >> L >> R >> M;
        for (int r = 0; r < M; r++)
            for (int last = 0; last <= 10; last++) cnt[0][r][last] = (r == 0);
        for (int len = 1; len < 19; len++)
            for (int r = 0; r < M; r++)
                for (int last = 0; last <= 10; last++) {
                    ll s = 0;
                    for (int d = 0; d <= 9; d++)
                        if (d != last) s += cnt[len - 1][(r * 10 + d) % M][d];
                    cnt[len][r][last] = s;
                }
        cout << dem(R) - dem(L - 1) << "\n";
    }
    return 0;
}
