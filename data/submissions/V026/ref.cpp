// V026 - Dem so tap con bang QHD tong tren tap con (SOS DP)
#include <bits/stdc++.h>
using namespace std;

const int B = 20;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> f(1 << B, 0);
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        f[a]++;
    }
    // sau vong bit b: f[mask] = so a_i la tap con cua mask, chi khac mask o cac bit < b+1
    for (int b = 0; b < B; b++)
        for (int mask = 0; mask < (1 << B); mask++)
            if (mask >> b & 1) f[mask] += f[mask ^ (1 << b)];
    string out;
    for (int j = 0; j < q; j++) {
        int x;
        cin >> x;
        out += to_string(f[x]);
        out += '\n';
    }
    cout << out;
    return 0;
}
