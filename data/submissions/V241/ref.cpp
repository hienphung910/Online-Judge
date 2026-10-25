// V241 - Tro choi tach dong (Kayles): thoi 1 hoac 2 nen lien ke, doan nen bi tach doi
// g[len] = mex{ g[a] ^ g[b] : a + b = len - 1 (thoi 1 nen) hoac a + b = len - 2 (thoi 2 nen) }
// Moi doan '1' lien tiep la mot tro choi doc lap; Nhi thang khi XOR cac g[do dai doan] khac 0.
#include <bits/stdc++.h>
using namespace std;

const int MAXL = 3000;
int g[MAXL + 1];

int main() {
    g[0] = 0;
    for (int len = 1; len <= MAXL; len++) {
        vector<bool> seen(2 * MAXL + 2, false);   // g[len] <= so nuoc di nen nho hon 2*len + 2
        for (int a = 0; a <= len - 1; a++) seen[g[a] ^ g[len - 1 - a]] = true;
        for (int a = 0; a <= len - 2; a++) seen[g[a] ^ g[len - 2 - a]] = true;
        int v = 0;
        while (seen[v]) v++;
        g[len] = v;
    }
    int T;
    cin >> T;
    while (T--) {
        int r, X = 0;
        cin >> r;
        for (int i = 0; i < r; i++) {
            string s;
            cin >> s;
            int run = 0;                         // do dai doan '1' dang dem
            for (char c : s) {
                if (c == '1') run++;
                else { X ^= g[run]; run = 0; }
            }
            X ^= g[run];
        }
        cout << (X ? "NHI" : "TU") << "\n";
    }
    return 0;
}
