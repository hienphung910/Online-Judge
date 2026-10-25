// V288 - Aho-Corasick: che cac ky tu nam trong mot lan xuat hien cua tu cam
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string t;
    int k;
    cin >> t >> k;
    vector<array<int, 26>> go(1);
    go[0].fill(0);
    vector<int> best(1, 0); // best[u] = do dai tu cam dai nhat la hau to cua xau ung voi u
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
                best.push_back(0);
            }
            u = go[u][c];
        }
        best[u] = p.size();
    }
    vector<int> fail(go.size(), 0);
    queue<int> q;
    for (int c = 0; c < 26; c++)
        if (go[0][c]) q.push(go[0][c]);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        best[u] = max(best[u], best[fail[u]]); // fail[u] o tang nong hon nen da xong
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
    // tai vi tri i, tu cam dai nhat ket thuc o i phu doan [i-L+1, i] (cac tu ngan hon nam gon trong do)
    int n = t.size();
    vector<int> d(n + 1, 0); // mang hieu danh dau doan bi che
    int u = 0;
    for (int i = 0; i < n; i++) {
        u = go[u][t[i] - 'a'];
        int L = best[u];
        if (L > 0) { d[i - L + 1]++; d[i + 1]--; }
    }
    int cur = 0;
    for (int i = 0; i < n; i++) {
        cur += d[i];
        if (cur > 0) t[i] = '#';
    }
    cout << t << '\n';
    return 0;
}
