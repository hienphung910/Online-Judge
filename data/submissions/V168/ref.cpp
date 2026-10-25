// V168 - DSU tren cay (small-to-large): dem so mau khac nhau trong moi cay con
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> c(n + 1), p(n + 1, 0);
    for (int i = 1; i <= n; i++) scanf("%d", &c[i]);
    vector<vector<int>> child(n + 1);
    for (int i = 2; i <= n; i++) {
        scanf("%d", &p[i]);
        child[p[i]].push_back(i);
    }
    // thu tu BFS tu goc: cha luon dung truoc con
    vector<int> order = {1};
    for (int i = 0; i < (int)order.size(); i++)
        for (int v : child[order[i]]) order.push_back(v);

    vector<set<int>> S(n + 1);
    vector<int> id(n + 1), ans(n + 1);   // id[v] = chi so tap mau dang dai dien cay con v
    for (int v = 1; v <= n; v++) {
        id[v] = v;
        S[v].insert(c[v]);
    }
    // duyet nguoc: moi con da gop xong truoc khi xu ly cha
    for (int i = n - 1; i >= 0; i--) {
        int v = order[i];
        ans[v] = S[id[v]].size();
        if (v == 1) continue;
        int u = p[v];
        if (S[id[u]].size() < S[id[v]].size()) swap(id[u], id[v]);   // u giu tap lon hon
        for (int x : S[id[v]]) S[id[u]].insert(x);
        S[id[v]].clear();
    }
    for (int v = 1; v <= n; v++) printf("%d%c", ans[v], v == n ? '\n' : ' ');
    return 0;
}
