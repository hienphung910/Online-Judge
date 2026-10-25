// V289 - Cay palindrome (eertree): dem so xau doi xung khac nhau
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.size();
    // dinh 0: goc do dai -1, dinh 1: goc do dai 0; moi dinh con lai la mot palindrome khac nhau
    vector<int> len(n + 2), link(n + 2);
    vector<array<int, 26>> nxt(n + 2);
    for (auto &a : nxt) a.fill(0);
    len[0] = -1; link[0] = 0;
    len[1] = 0;  link[1] = 0;
    int sz = 2, last = 1;
    for (int i = 0; i < n; i++) {
        int c = s[i] - 'a';
        // nhay theo link toi palindrome hau to X dau tien co s[i-len(X)-1] == s[i]
        auto getLink = [&](int v) {
            while (i - len[v] - 1 < 0 || s[i - len[v] - 1] != s[i]) v = link[v];
            return v;
        };
        int cur = getLink(last);
        if (!nxt[cur][c]) { // c + X + c la palindrome moi
            int v = sz++;
            len[v] = len[cur] + 2;
            link[v] = (len[v] == 1) ? 1 : nxt[getLink(link[cur])][c];
            nxt[cur][c] = v;
        }
        last = nxt[cur][c];
    }
    cout << sz - 2 << '\n';
    return 0;
}
