// V062 - Sang dem so uoc d[x] cho moi x <= 10^6, roi luu so tot nhat tren tien to
#include <bits/stdc++.h>
using namespace std;

const int N = 1000000;
int d[N + 1];      // d[x] = so uoc duong cua x
int best[N + 1];   // best[n] = x nho nhat trong [1, n] co d[x] lon nhat

int main() {
    for (int i = 1; i <= N; i++)
        for (int j = i; j <= N; j += i) d[j]++;
    best[1] = 1;
    for (int x = 2; x <= N; x++)
        best[x] = (d[x] > d[best[x - 1]]) ? x : best[x - 1];   // chi doi khi lon hon han

    int q;
    scanf("%d", &q);
    while (q--) {
        int n;
        scanf("%d", &n);
        printf("%d %d\n", best[n], d[best[n]]);
    }
    return 0;
}
