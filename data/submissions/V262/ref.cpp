// V262 - Danh sach nhay (skip list) co do dai buoc nhay: them, xoa, phan tu thu k, dem so nho hon
#include <bits/stdc++.h>
using namespace std;

const int L = 18;              // so tang toi da
vector<long long> val;         // nut 0 la dau danh sach (head)
vector<array<int, L>> nxt;     // nxt[u][i]: nut ke tiep o tang i (-1 neu het)
vector<array<int, L>> width;    // width[u][i]: so buoc o tang 0 tu u den nxt[u][i]
mt19937 rng(2024);

int newNode(long long v) {
    val.push_back(v);
    array<int, L> a; a.fill(-1); nxt.push_back(a);
    a.fill(0); width.push_back(a);
    return val.size() - 1;
}

void insert(long long x) {
    int upd[L], rk[L], cur = 0;
    for (int i = L - 1; i >= 0; i--) {   // tim vi tri dung truoc moi so >= x
        rk[i] = (i == L - 1) ? 0 : rk[i + 1];
        while (nxt[cur][i] != -1 && val[nxt[cur][i]] < x) { rk[i] += width[cur][i]; cur = nxt[cur][i]; }
        upd[i] = cur;
    }
    int lv = 1;
    while (lv < L && rng() % 2) lv++;      // tung dong xu chon so tang
    int u = newNode(x);
    for (int i = 0; i < L; i++) {
        if (i < lv) {
            nxt[u][i] = nxt[upd[i]][i];
            width[u][i] = width[upd[i]][i] - (rk[0] - rk[i]);
            nxt[upd[i]][i] = u;
            width[upd[i]][i] = rk[0] - rk[i] + 1;
        } else width[upd[i]][i]++;          // buoc nhay o tang cao bay qua them 1 nut
    }
}

void erase(long long x) {
    int upd[L], cur = 0;
    for (int i = L - 1; i >= 0; i--) {
        while (nxt[cur][i] != -1 && val[nxt[cur][i]] < x) cur = nxt[cur][i];
        upd[i] = cur;
    }
    int u = nxt[cur][0];                    // de bai dam bao val[u] == x
    for (int i = 0; i < L; i++) {
        if (nxt[upd[i]][i] == u) {
            width[upd[i]][i] += width[u][i] - 1;
            nxt[upd[i]][i] = nxt[u][i];
        } else width[upd[i]][i]--;
    }
}

long long kth(int k) {
    int cur = 0, passed = 0;
    for (int i = L - 1; i >= 0; i--)
        while (nxt[cur][i] != -1 && passed + width[cur][i] <= k) { passed += width[cur][i]; cur = nxt[cur][i]; }
    return val[cur];
}

int countLess(long long x) {
    int cur = 0, passed = 0;
    for (int i = L - 1; i >= 0; i--)
        while (nxt[cur][i] != -1 && val[nxt[cur][i]] < x) { passed += width[cur][i]; cur = nxt[cur][i]; }
    return passed;
}

int main() {
    newNode(LLONG_MIN);  // head
    int q;
    scanf("%d", &q);
    while (q--) {
        char op[3]; long long x;
        scanf("%s %lld", op, &x);
        if (op[0] == '+') insert(x);
        else if (op[0] == '-') erase(x);
        else if (op[0] == 'K') printf("%lld\n", kth((int)x));
        else printf("%d\n", countLess(x));
    }
    return 0;
}
