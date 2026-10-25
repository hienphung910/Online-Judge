// V285 - Aho-Corasick: kiem tra moi tin nhan co chua tu cam nao khong
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int k;
    cin >> k;
    vector<array<int, 26>> go(1);
    go[0].fill(0);
    vector<char> bad(1, 0); // bad[u] = 1 neu co tu cam la hau to cua xau ung voi dinh u
    for (int i = 0; i < k; i++) {
        string p;
        cin >> p;
        int u = 0;
        for (char ch : p) {
            int c = ch - 'a';
            if (!go[u][c]) {
                go[u][c] = go.size();
                go.push_back({});
                go.back().fill(0);
                bad.push_back(0);
            }
            u = go[u][c];
        }
        bad[u] = 1;
    }
    // BFS: dung lien ket that bai, dien bang chuyen, lan truyen co "bad" theo lien ket that bai
    vector<int> fail(go.size(), 0);
    queue<int> q;
    for (int c = 0; c < 26; c++)
        if (go[0][c]) q.push(go[0][c]);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        bad[u] |= bad[fail[u]];
        for (int c = 0; c < 26; c++) {
            int v = go[u][c];
            if (v) {
                fail[v] = go[fail[u]][c];
                q.push(v);
            } else {
                go[u][c] = go[fail[u]][c];
            }
        }
    }
    // dung automat mot lan, chay tung tin nhan
    int m;
    cin >> m;
    while (m--) {
        string t;
        cin >> t;
        int u = 0;
        bool found = false;
        for (char ch : t) {
            u = go[u][ch - 'a'];
            if (bad[u]) { found = true; break; }
        }
        cout << (found ? "CO" : "KHONG") << '\n';
    }
    return 0;
}
