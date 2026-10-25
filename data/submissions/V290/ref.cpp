// V290 - Automat hau to: dem xau con phan biet xuat hien dung K lan
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    int K;
    cin >> s >> K;
    int n = s.size();
    int cap = 2 * n + 1;
    vector<int> len(cap, 0), link(cap, -1);
    vector<long long> cnt(cap, 0);
    vector<array<int, 26>> nxt(cap);
    for (auto &a : nxt) a.fill(-1);
    int sz = 1, last = 0;
    for (char ch : s) {
        int c = ch - 'a';
        int cur = sz++;
        len[cur] = len[last] + 1;
        cnt[cur] = 1; // trang thai moi ung voi mot vi tri ket thuc moi
        int p = last;
        while (p != -1 && nxt[p][c] == -1) { nxt[p][c] = cur; p = link[p]; }
        if (p == -1) link[cur] = 0;
        else {
            int q = nxt[p][c];
            if (len[p] + 1 == len[q]) link[cur] = q;
            else {
                int cl = sz++; // ban sao: khong co vi tri ket thuc rieng nen cnt = 0
                len[cl] = len[p] + 1;
                nxt[cl] = nxt[q];
                link[cl] = link[q];
                while (p != -1 && nxt[p][c] == q) { nxt[p][c] = cl; p = link[p]; }
                link[q] = link[cur] = cl;
            }
        }
        last = cur;
    }
    // sap trang thai theo len tang dan (dem phan phoi), cong don cnt tu duoi len theo link
    vector<int> bucket(n + 1, 0), order(sz);
    for (int v = 0; v < sz; v++) bucket[len[v]]++;
    for (int i = 1; i <= n; i++) bucket[i] += bucket[i - 1];
    for (int v = sz - 1; v >= 0; v--) order[--bucket[len[v]]] = v;
    for (int i = sz - 1; i > 0; i--) {
        int v = order[i];
        cnt[link[v]] += cnt[v];
    }
    // trang thai v chua (len[v] - len[link[v]]) xau con khac nhau, cung xuat hien cnt[v] lan
    long long ans = 0;
    for (int v = 1; v < sz; v++)
        if (cnt[v] == K) ans += len[v] - len[link[v]];
    cout << ans << '\n';
    return 0;
}
