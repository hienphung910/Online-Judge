// V025 - Aho-Corasick, cong don so lan xuat hien tren cay lien ket that bai
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
    vector<int> endNode(k);
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
            }
            u = go[u][c];
        }
        endNode[i] = u;
    }
    // BFS dung lien ket that bai va dien day du bang chuyen trang thai
    int sz = go.size();
    vector<int> fail(sz, 0), order;
    order.reserve(sz);
    queue<int> q;
    for (int c = 0; c < 26; c++)
        if (go[0][c]) q.push(go[0][c]);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        order.push_back(u);
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
    // chay van ban: moi vi tri chi tang dem tai dung mot dinh
    vector<long long> cnt(sz, 0);
    int u = 0;
    for (char ch : t) {
        u = go[u][ch - 'a'];
        cnt[u]++;
    }
    // day so dem tu dinh sau len dinh that bai (thu tu BFS nguoc)
    for (int i = (int)order.size() - 1; i >= 0; i--) {
        int v = order[i];
        cnt[fail[v]] += cnt[v];
    }
    string out;
    for (int i = 0; i < k; i++) {
        out += to_string(cnt[endNode[i]]);
        out += '\n';
    }
    cout << out;
    return 0;
}
