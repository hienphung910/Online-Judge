// V263 - Cay phan doan khong de quy voi phep ghep khong giao hoan (hop cac ham bac nhat)
#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;
struct F { long long a, b; };  // ham x -> a*x + b (mod MOD)
const F ID = {1, 0};

// lam f truoc, roi lam g: x -> g.a*(f.a*x + f.b) + g.b
F then(F f, F g) { return {g.a * f.a % MOD, (g.a * f.b + g.b) % MOD}; }

int n;
vector<F> t;

void update(int p, F v) {
    // nut cha = (con trai lam truoc) roi (con phai)
    for (t[p += n] = v; p > 1; p >>= 1) {
        int par = p >> 1;
        t[par] = then(t[2 * par], t[2 * par + 1]);
    }
}

F query(int l, int r) {  // doan nua mo [l, r), giu dung thu tu trai -> phai
    F left = ID, right = ID;
    for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
        if (l & 1) left = then(left, t[l++]);
        if (r & 1) right = then(t[--r], right);
    }
    return then(left, right);
}

int main() {
    int q;
    scanf("%d %d", &n, &q);
    t.assign(2 * n, ID);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &t[n + i].a, &t[n + i].b);
    for (int i = n - 1; i >= 1; i--) t[i] = then(t[2 * i], t[2 * i + 1]);
    while (q--) {
        int type;
        scanf("%d", &type);
        if (type == 1) {
            int i; long long a, b;
            scanf("%d %lld %lld", &i, &a, &b);
            update(i - 1, {a, b});
        } else {
            int l, r; long long x;
            scanf("%d %d %lld", &l, &r, &x);
            F f = query(l - 1, r);
            printf("%lld\n", (f.a * x + f.b) % MOD);
        }
    }
    return 0;
}
