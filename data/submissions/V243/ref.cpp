// V243 - Green Hackenbush tren rung: nguyen ly "cot co" (colon principle)
// G[u] = XOR qua cac con c cua (G[c] + 1); dat dinh 0 la mat dat, ca rung co gia tri G[0].
// Dem nuoc thang: cat canh (p_c, c) thi G[p_c] mat di (G[c] + 1); cap nhat nguoc len den dinh 0,
// nuoc thang khi gia tri moi cua dinh 0 bang 0. Do phuc tap O(n * do sau) <= O(n^2).
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> p(n + 1, -1);
    for (int i = 1; i <= n; i++) cin >> p[i];
    vector<long long> G(n + 1, 0);
    for (int i = n; i >= 1; i--) G[p[i]] ^= G[i] + 1;   // p[i] < i nen G[i] da xong

    int cnt = 0;
    for (int c = 1; c <= n; c++) {
        int u = p[c];
        long long nu = G[u] ^ (G[c] + 1);                // gia tri moi cua u sau khi cat
        while (u != 0) {
            int w = p[u];
            long long nw = G[w] ^ (G[u] + 1) ^ (nu + 1);
            u = w;
            nu = nw;
        }
        if (nu == 0) cnt++;
    }
    cout << (G[0] ? "DUC" : "MAI") << "\n" << cnt << "\n";
    return 0;
}
