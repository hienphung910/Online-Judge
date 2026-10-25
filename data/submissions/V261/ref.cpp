// V261 - Cay Fenwick hai chieu: cong vao mot o, hoi tong hinh chu nhat
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<long long>> bit;  // bit[i][j], chi so tu 1

void add(int x, int y, long long v) {
    for (int i = x; i <= n; i += i & -i)
        for (int j = y; j <= m; j += j & -j) bit[i][j] += v;
}

long long sum(int x, int y) {  // tong hinh chu nhat (1,1)..(x,y)
    long long s = 0;
    for (int i = x; i > 0; i -= i & -i)
        for (int j = y; j > 0; j -= j & -j) s += bit[i][j];
    return s;
}

int main() {
    int q;
    scanf("%d %d %d", &n, &m, &q);
    bit.assign(n + 1, vector<long long>(m + 1, 0));
    while (q--) {
        int type;
        scanf("%d", &type);
        if (type == 1) {
            int x, y; long long v;
            scanf("%d %d %lld", &x, &y, &v);
            add(x, y, v);
        } else {
            int x1, y1, x2, y2;
            scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
            // bao ham - loai tru tren 4 goc
            long long s = sum(x2, y2) - sum(x1 - 1, y2) - sum(x2, y1 - 1) + sum(x1 - 1, y1 - 1);
            printf("%lld\n", s);
        }
    }
    return 0;
}
