// V238 - Minimax tren cay tro choi cho san
// Dinh o do sau chan la luot Minh (lay max), do sau le la luot Ha (lay min).
// Vi p_i < i nen duyet i tu n ve 2 la moi dinh con da co gia tri truoc dinh cha.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> p(n + 1, 0), depth(n + 1, 0), childCnt(n + 1, 0);
    for (int i = 2; i <= n; i++) {
        cin >> p[i];
        depth[i] = depth[p[i]] + 1;
        childCnt[p[i]]++;
    }
    vector<long long> val(n + 1);
    vector<bool> has(n + 1, false);          // dinh trong da nhan duoc gia tri tu con nao chua
    for (int i = 1; i <= n; i++)
        if (childCnt[i] == 0) { cin >> val[i]; has[i] = true; }

    for (int i = n; i >= 2; i--) {
        int u = p[i];
        bool maxTurn = (depth[u] % 2 == 0);
        if (!has[u]) { val[u] = val[i]; has[u] = true; }
        else if (maxTurn) val[u] = max(val[u], val[i]);
        else val[u] = min(val[u], val[i]);
    }
    cout << val[1] << "\n";
    return 0;
}
