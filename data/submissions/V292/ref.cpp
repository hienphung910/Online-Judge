// V292 - Cay palindrome: max (do dai x so lan xuat hien) cua mot xau doi xung
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.size();
    vector<int> len(n + 2), link(n + 2);
    vector<long long> occ(n + 2, 0);
    vector<array<int, 26>> nxt(n + 2);
    for (auto &a : nxt) a.fill(0);
    len[0] = -1; link[0] = 0;
    len[1] = 0;  link[1] = 0;
    int sz = 2, last = 1;
    for (int i = 0; i < n; i++) {
        int c = s[i] - 'a';
        auto getLink = [&](int v) {
            while (i - len[v] - 1 < 0 || s[i - len[v] - 1] != s[i]) v = link[v];
            return v;
        };
        int cur = getLink(last);
        if (!nxt[cur][c]) {
            int v = sz++;
            len[v] = len[cur] + 2;
            link[v] = (len[v] == 1) ? 1 : nxt[getLink(link[cur])][c];
            nxt[cur][c] = v;
        }
        last = nxt[cur][c];
        occ[last]++; // chi ghi cho palindrome hau to dai nhat ket thuc tai i
    }
    // moi lan xuat hien cua v cung la mot lan xuat hien cua link[v] (palindrome hau to cua v).
    // link[v] luon duoc tao truoc v (chi so nho hon), nen duyet nguoc chi so de cong don.
    long long ans = 0;
    for (int v = sz - 1; v >= 2; v--) {
        ans = max(ans, occ[v] * len[v]);
        occ[link[v]] += occ[v];
    }
    cout << ans << '\n';
    return 0;
}
