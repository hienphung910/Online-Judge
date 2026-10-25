// V021 - 2-SAT: do thi keo theo + thanh phan lien thong manh Kosaraju (khu de quy)
#include <bits/stdc++.h>
using namespace std;

// doc so nguyen nhanh (co the am)
int readInt() {
    int c = getchar(), s = 1, x = 0;
    while (c != '-' && (c < '0' || c > '9')) c = getchar();
    if (c == '-') { s = -1; c = getchar(); }
    while (c >= '0' && c <= '9') { x = x * 10 + (c - '0'); c = getchar(); }
    return x * s;
}

// dinh 2i: bien i+1 dung, dinh 2i+1: bien i+1 sai
int lit(int v) { return v > 0 ? 2 * (v - 1) : 2 * (-v - 1) + 1; }

// luu do thi dang mang lien tiep (CSR): canh cua u la adj[start[u] .. start[u+1]-1]
struct Graph {
    vector<int> start, adj;
    void build(int N, const vector<int>& from, const vector<int>& to) {
        start.assign(N + 1, 0);
        for (int u : from) start[u + 1]++;
        for (int i = 0; i < N; i++) start[i + 1] += start[i];
        adj.resize(from.size());
        vector<int> pos(start.begin(), start.end() - 1);
        for (size_t i = 0; i < from.size(); i++) adj[pos[from[i]]++] = to[i];
    }
};

bool solve(int n, const vector<int>& xs, const vector<int>& ys) {
    int N = 2 * n;
    vector<int> from, to;  // (x OR y)  <=>  (!x -> y) va (!y -> x)
    for (size_t i = 0; i < xs.size(); i++) {
        int a = lit(xs[i]), b = lit(ys[i]);
        from.push_back(a ^ 1); to.push_back(b);
        from.push_back(b ^ 1); to.push_back(a);
    }
    Graph g, rg;
    g.build(N, from, to);
    rg.build(N, to, from);  // do thi nguoc
    // luot 1: DFS khu de quy tren g, ghi thu tu hoan thanh
    vector<int> order, it(g.start.begin(), g.start.end() - 1), st;
    vector<char> seen(N, 0);
    for (int s = 0; s < N; s++) {
        if (seen[s]) continue;
        seen[s] = 1;
        st.push_back(s);
        while (!st.empty()) {
            int u = st.back();
            if (it[u] < g.start[u + 1]) {
                int v = g.adj[it[u]++];
                if (!seen[v]) { seen[v] = 1; st.push_back(v); }
            } else {
                order.push_back(u);
                st.pop_back();
            }
        }
    }
    // luot 2: duyet rg theo thu tu hoan thanh giam dan, moi lan loang la mot TPLT manh
    vector<int> comp(N, -1);
    int c = 0;
    for (int i = N - 1; i >= 0; i--) {
        int s = order[i];
        if (comp[s] >= 0) continue;
        comp[s] = c;
        st.push_back(s);
        while (!st.empty()) {
            int u = st.back(); st.pop_back();
            for (int k = rg.start[u]; k < rg.start[u + 1]; k++) {
                int v = rg.adj[k];
                if (comp[v] < 0) { comp[v] = c; st.push_back(v); }
            }
        }
        c++;
    }
    for (int i = 0; i < N; i += 2)
        if (comp[i] == comp[i + 1]) return false;  // x va !x cung TPLT manh
    return true;
}

int main() {
    int T = readInt();
    while (T--) {
        int n = readInt(), m = readInt();
        vector<int> xs(m), ys(m);
        for (int i = 0; i < m; i++) { xs[i] = readInt(); ys[i] = readInt(); }
        puts(solve(n, xs, ys) ? "CO" : "KHONG");
    }
    return 0;
}
