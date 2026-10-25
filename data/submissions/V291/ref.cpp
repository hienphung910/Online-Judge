// V291 - Automat hau to: xau ngan nhat (nho nhat theo tu dien) khong phai xau con
#include <bits/stdc++.h>
using namespace std;

int main() {
    int A;
    string s;
    cin >> A >> s;
    int n = s.size();
    int cap = 2 * n + 1;
    vector<int> len(cap, 0), link(cap, -1);
    vector<array<int, 26>> nxt(cap);
    for (auto &a : nxt) a.fill(-1);
    int sz = 1, last = 0;
    for (char ch : s) {
        int c = ch - 'a';
        int cur = sz++;
        len[cur] = len[last] + 1;
        int p = last;
        while (p != -1 && nxt[p][c] == -1) { nxt[p][c] = cur; p = link[p]; }
        if (p == -1) link[cur] = 0;
        else {
            int q = nxt[p][c];
            if (len[p] + 1 == len[q]) link[cur] = q;
            else {
                int cl = sz++;
                len[cl] = len[p] + 1;
                nxt[cl] = nxt[q];
                link[cl] = link[q];
                while (p != -1 && nxt[p][c] == q) { nxt[p][c] = cl; p = link[p]; }
                link[q] = link[cur] = cl;
            }
        }
        last = cur;
    }
    // dp[v] = do dai ngan nhat cua xau w sao cho doc w tu trang thai v thi bi roi khoi automat.
    // Canh chuyen luon di toi trang thai co len lon hon, nen tinh theo len giam dan.
    vector<int> order(sz);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int a, int b) { return len[a] > len[b]; });
    vector<int> dp(sz);
    for (int v : order) {
        dp[v] = INT_MAX;
        for (int c = 0; c < A; c++) {
            int w = nxt[v][c] == -1 ? 1 : 1 + dp[nxt[v][c]];
            dp[v] = min(dp[v], w);
        }
    }
    // dung lai dap an tu goc: moi buoc chon chu cai nho nhat ma van dat do dai toi uu
    string ans;
    int v = 0;
    while (true) {
        int c = 0;
        while (nxt[v][c] != -1 && 1 + dp[nxt[v][c]] != dp[v]) c++;
        ans += char('a' + c);
        if (nxt[v][c] == -1) break; // chu cai nay khong doc duoc nua: xong
        v = nxt[v][c];
    }
    cout << ans << '\n';
    return 0;
}
