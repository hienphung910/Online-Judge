// V187 - XOR lon nhat cua doan con: XOR tien to + trie nhi phan, O(n * 30)
// xor(l..r) = p[r] ^ p[l-1]. Voi moi p[r], tim p[j] (j < r) trong trie de XOR lon nhat:
// di tu bit cao xuong, uu tien nhanh co bit nguoc voi bit cua p[r].
#include <bits/stdc++.h>
using namespace std;

const int BITS = 30;
vector<array<int, 2>> ch(1, {0, 0});    // nut 0 la goc

void them(int x) {
    int u = 0;
    for (int b = BITS - 1; b >= 0; b--) {
        int c = (x >> b) & 1;
        if (!ch[u][c]) { ch[u][c] = ch.size(); ch.push_back({0, 0}); }
        u = ch[u][c];
    }
}

int timMax(int x) {                      // max (x ^ y) voi y da co trong trie
    int u = 0, res = 0;
    for (int b = BITS - 1; b >= 0; b--) {
        int c = (x >> b) & 1;
        if (ch[u][c ^ 1]) { res |= 1 << b; u = ch[u][c ^ 1]; }
        else u = ch[u][c];
    }
    return res;
}

int main() {
    int n;
    cin >> n;
    int p = 0, best = 0;
    them(0);                             // p[0] = 0
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        p ^= a;
        best = max(best, timMax(p));
        them(p);
    }
    cout << best << '\n';
    return 0;
}
