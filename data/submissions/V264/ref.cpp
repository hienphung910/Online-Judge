// V264 - Cay Li Chao: them duong thang, hoi gia tri nho nhat tai mot diem
#include <bits/stdc++.h>
using namespace std;

struct Line {
    long long a, b;
    long long at(long long x) const { return a * x + b; }
};

const long long LO = -1000000000, HI = 1000000000;
vector<Line> ln;                 // duong thang luu o moi nut
vector<int> lc, rc;              // con trai, con phai (-1 neu chua co)

int newNode(Line f) { ln.push_back(f); lc.push_back(-1); rc.push_back(-1); return ln.size() - 1; }

// nut u quan ly doan [lo, hi]; giu o u duong thang tot hon tai diem giua
void add(int u, long long lo, long long hi, Line f) {
    long long mid = lo + (hi - lo) / 2;
    bool betterLo = f.at(lo) < ln[u].at(lo);
    bool betterMid = f.at(mid) < ln[u].at(mid);
    if (betterMid) swap(f, ln[u]);
    if (lo == hi) return;
    if (betterLo != betterMid) {        // hai duong cat nhau o nua trai
        if (lc[u] == -1) { int v = newNode(f); lc[u] = v; }
        else add(lc[u], lo, mid, f);
    } else {                            // cat nhau o nua phai (hoac khong cat)
        if (rc[u] == -1) { int v = newNode(f); rc[u] = v; }
        else add(rc[u], mid + 1, hi, f);
    }
}

long long query(int u, long long lo, long long hi, long long x) {
    long long res = LLONG_MAX;
    while (u != -1) {
        res = min(res, ln[u].at(x));
        long long mid = lo + (hi - lo) / 2;
        if (x <= mid) { u = lc[u]; hi = mid; }
        else { u = rc[u]; lo = mid + 1; }
    }
    return res;
}

int main() {
    int q;
    scanf("%d", &q);
    int root = -1;
    while (q--) {
        char op[3];
        scanf("%s", op);
        if (op[0] == '+') {
            long long a, b;
            scanf("%lld %lld", &a, &b);
            if (root == -1) root = newNode({a, b});
            else add(root, LO, HI, {a, b});
        } else {
            long long x;
            scanf("%lld", &x);
            printf("%lld\n", query(root, LO, HI, x));
        }
    }
    return 0;
}
