// V269 - Cap ghep cuc dai tren do thi hai phia (thuat toan Kuhn)
#include <bits/stdc++.h>
using namespace std;

int n, m, k;
vector<vector<int>> adj;   // adj[a] = cac ca ma ban a ranh
vector<int> matchCa;       // matchCa[b] = ban dang nhan ca b (0 neu chua co)
vector<int> seen;          // seen[b] = lan tim thu may da di qua ca b

// thu tim cho ban a mot ca; neu ca da co nguoi thi thu doi nguoi do sang ca khac
bool tryKuhn(int a, int stamp) {
    for (int b : adj[a]) {
        if (seen[b] == stamp) continue;
        seen[b] = stamp;
        if (matchCa[b] == 0 || tryKuhn(matchCa[b], stamp)) {
            matchCa[b] = a;
            return true;
        }
    }
    return false;
}

int main() {
    scanf("%d %d %d", &n, &m, &k);
    adj.assign(n + 1, {});
    for (int i = 0; i < k; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        adj[a].push_back(b);
    }
    matchCa.assign(m + 1, 0);
    seen.assign(m + 1, 0);
    int ans = 0;
    for (int a = 1; a <= n; a++)
        if (tryKuhn(a, a)) ans++;
    printf("%d\n", ans);
    return 0;
}
