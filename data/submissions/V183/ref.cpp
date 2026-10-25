// V183 - Dem so tu co tien to cho truoc bang cay tien to (trie)
// cnt[u] = so tu di qua nut u, tuc so tu nhan xau ung voi nut u lam tien to.
#include <bits/stdc++.h>
using namespace std;

vector<array<int, 26>> nxt(1);   // nut 0 la goc
vector<int> cnt(1, 0);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    for (int i = 0; i < n; i++) {
        string w;
        cin >> w;
        int u = 0;
        for (char ch : w) {
            int c = ch - 'a';
            if (nxt[u][c] == 0) {            // chua co canh -> tao nut moi
                nxt[u][c] = nxt.size();
                nxt.push_back({});
                cnt.push_back(0);
            }
            u = nxt[u][c];
            cnt[u]++;
        }
    }
    while (q--) {
        string p;
        cin >> p;
        int u = 0;
        for (char ch : p) {
            u = nxt[u][ch - 'a'];
            if (u == 0) break;               // khong co tu nao di theo duong nay
        }
        cout << (u == 0 ? 0 : cnt[u]) << '\n';
    }
    return 0;
}
