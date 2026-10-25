// V205 - QHD chu so: dem so trong [L, R] co tong chu so chia het cho D
// dem(X) = so luong so trong [0, X] thoa man; dap an = dem(R) - dem(L - 1).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int D;
ll f[19][200];   // f[len][r] = so xau len chu so (tu do) co tong chu so chia D du r

ll dem(ll X) {
    if (X < 0) return 0;
    string s = to_string(X);
    int n = s.size();
    ll res = 0;
    int pre = 0;                        // tong chu so cua phan tien to da co dinh (mod D)
    for (int i = 0; i < n; i++) {
        int d = s[i] - '0';
        for (int c = 0; c < d; c++) {   // dat chu so c < d tai vi tri i, phan sau tu do
            int need = ((-(pre + c)) % D + D) % D;
            res += f[n - 1 - i][need];
        }
        pre = (pre + d) % D;
    }
    if (pre == 0) res++;                // chinh X
    return res;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        ll L, R;
        cin >> L >> R >> D;
        memset(f, 0, sizeof f);
        f[0][0] = 1;
        for (int len = 1; len < 19; len++)   // X <= 10^18 co toi da 19 chu so
            for (int r = 0; r < D; r++)
                for (int c = 0; c <= 9; c++)
                    f[len][(r + c) % D] += f[len - 1][r];
        cout << dem(R) - dem(L - 1) << "\n";
    }
    return 0;
}
