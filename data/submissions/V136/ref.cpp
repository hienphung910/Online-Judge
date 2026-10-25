// V136 - DFS dem thanh phan lien thong va so thanh phan co chu trinh
// Mot thanh phan co k dinh la cay neu co dung k - 1 canh; nhieu canh hon thi co chu trinh.
// DFS viet bang stack de khong lo tran stack khi do thi la duong thang dai.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<bool> seen(n + 1, false);
    int groups = 0, cyclic = 0;
    for (int s = 1; s <= n; s++) {
        if (seen[s]) continue;
        groups++;
        long long verts = 0, degSum = 0;
        stack<int> st;
        st.push(s);
        seen[s] = true;
        while (!st.empty()) {
            int u = st.top();
            st.pop();
            verts++;
            degSum += adj[u].size();
            for (int v : adj[u])
                if (!seen[v]) { seen[v] = true; st.push(v); }
        }
        if (degSum / 2 >= verts) cyclic++;  // so canh = tong bac / 2
    }
    cout << groups << ' ' << cyclic << '\n';
    return 0;
}
