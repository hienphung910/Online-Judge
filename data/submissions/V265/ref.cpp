// V265 - Con tro nhay (jump pointer) O(n) bo nho: them la truc tuyen, to tien thu k, LCA
#include <bits/stdc++.h>
using namespace std;

vector<int> par, jmp, dep;  // cha, con tro nhay, do sau; nut 1 la goc

void addLeaf(int p) {
    par.push_back(p);
    dep.push_back(dep[p] + 1);
    int j = jmp[p];
    // neu hai buoc nhay lien tiep tu p dai bang nhau thi gop lai thanh mot buoc dai gap doi
    if (dep[p] - dep[j] == dep[j] - dep[jmp[j]]) jmp.push_back(jmp[j]);
    else jmp.push_back(p);
}

int ancestorAtDepth(int v, int d) {  // to tien cua v co do sau d (d <= dep[v])
    while (dep[v] > d) {
        if (dep[jmp[v]] >= d) v = jmp[v];
        else v = par[v];
    }
    return v;
}

int lca(int u, int v) {
    if (dep[u] < dep[v]) swap(u, v);
    u = ancestorAtDepth(u, dep[v]);
    while (u != v) {  // cung do sau thi con tro nhay cung do dai
        if (jmp[u] != jmp[v]) { u = jmp[u]; v = jmp[v]; }
        else { u = par[u]; v = par[v]; }
    }
    return u;
}

int main() {
    par = {0, 1}; jmp = {0, 1}; dep = {0, 0};  // chi so 0 bo trong
    int q;
    scanf("%d", &q);
    while (q--) {
        char op[3];
        scanf("%s", op);
        if (op[0] == '+') {
            int p; scanf("%d", &p);
            addLeaf(p);
        } else if (op[0] == 'A') {
            int v, k; scanf("%d %d", &v, &k);
            printf("%d\n", k > dep[v] ? -1 : ancestorAtDepth(v, dep[v] - k));
        } else {
            int u, v; scanf("%d %d", &u, &v);
            printf("%d\n", lca(u, v));
        }
    }
    return 0;
}
