// V256 - 2-SAT: nghiem nho nhat theo thu tu tu dien bang tham lam + lan truyen keo theo
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<int>> g;  // dinh 2(v-1)+b nghia la "nguoi v truc ca b"; phu dinh la x^1
vector<int> val;        // val[v] = -1 (chua gan), 0 hoac 1

// menh de (p hoac q)  <=>  (!p -> q) va (!q -> p)
void clause(int p, int q) { g[p ^ 1].push_back(q); g[q ^ 1].push_back(p); }
int lit(int v, int b) { return 2 * (v - 1) + b; }

// gan literal x = dung roi lan truyen moi he qua; mau thuan thi hoan tac va tra ve false
bool tryAssign(int x) {
    vector<int> q = {x}, touched = {x / 2 + 1};
    val[x / 2 + 1] = x & 1;
    for (size_t i = 0; i < q.size(); i++) {
        for (int y : g[q[i]]) {
            int v = y / 2 + 1, b = y & 1;
            if (val[v] == b) continue;
            if (val[v] == -1) { val[v] = b; touched.push_back(v); q.push_back(y); continue; }
            for (int t : touched) val[t] = -1;  // mau thuan: hoan tac
            return false;
        }
    }
    return true;
}

int main() {
    scanf("%d %d", &n, &m);
    g.assign(2 * n, {});
    for (int i = 0; i < m; i++) {
        int t, u, v;
        scanf("%d %d %d", &t, &u, &v);
        if (t == 1) { clause(lit(u, 0), lit(v, 1)); clause(lit(u, 1), lit(v, 0)); }       // cung ca
        else if (t == 2) { clause(lit(u, 0), lit(v, 0)); clause(lit(u, 1), lit(v, 1)); }  // khac ca
        else if (t == 3) clause(lit(u, 0), lit(v, 0));  // khong ca hai cung ca toi
        else clause(lit(u, 1), lit(v, 1));              // it nhat mot nguoi ca toi
    }
    val.assign(n + 1, -1);
    // uu tien ca sang (0) cho nguoi co so nho; neu lan truyen khong mau thuan thi phan con lai
    // van giai duoc khi va chi khi cong thuc ban dau giai duoc
    for (int v = 1; v <= n; v++) {
        if (val[v] != -1) continue;
        if (!tryAssign(lit(v, 0)) && !tryAssign(lit(v, 1))) { puts("KHONG"); return 0; }
    }
    for (int v = 1; v <= n; v++) putchar('0' + val[v]);
    putchar('\n');
    return 0;
}
