// V271 - Phu dinh nho nhat tren do thi hai phia (dinh ly Konig): so lan phun = cap ghep cuc dai
#include <bits/stdc++.h>
using namespace std;

int R, C;
vector<string> g;
vector<int> matchCol;   // matchCol[c] = hang dang ghep voi cot c (-1 neu chua)
vector<int> seen;

// moi o co sau (r, c) la mot canh noi hang r voi cot c
bool tryKuhn(int r, int stamp) {
    for (int c = 0; c < C; c++) {
        if (g[r][c] != '#' || seen[c] == stamp) continue;
        seen[c] = stamp;
        if (matchCol[c] < 0 || tryKuhn(matchCol[c], stamp)) {
            matchCol[c] = r;
            return true;
        }
    }
    return false;
}

int main() {
    cin >> R >> C;
    g.resize(R);
    for (auto &row : g) cin >> row;
    matchCol.assign(C, -1);
    seen.assign(C, -1);
    int ans = 0;
    for (int r = 0; r < R; r++)
        if (tryKuhn(r, r)) ans++;
    printf("%d\n", ans);
    return 0;
}
