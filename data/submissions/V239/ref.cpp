// V239 - Tro choi tru chu so: so Grundy voi tap nuoc di phu thuoc trang thai
// g[x] = mex{ g[x - d] : d la mot chu so khac 0 cua x }; Lan thang khi XOR cac g[a_i] khac 0.
#include <bits/stdc++.h>
using namespace std;

const int MAXA = 1000000;
int g[MAXA + 1];

int main() {
    g[0] = 0;
    for (int x = 1; x <= MAXA; x++) {
        int seen = 0;                       // bit v bat neu da gap gia tri Grundy v
        for (int y = x; y > 0; y /= 10) {
            int d = y % 10;
            if (d > 0) seen |= 1 << g[x - d];
        }
        int v = 0;
        while (seen >> v & 1) v++;          // mex (toi da 9 gia tri nen v <= 9)
        g[x] = v;
    }
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        int X = 0;
        for (int i = 0; i < n; i++) {
            int a;
            cin >> a;
            X ^= g[a];
        }
        cout << (X ? "LAN" : "HUY") << "\n";
    }
    return 0;
}
