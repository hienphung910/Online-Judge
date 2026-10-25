// V028 - Bang tra so doan LED cua tung chu so, tinh truoc diem sang cua 1440 phut
#include <bits/stdc++.h>
using namespace std;

int main() {
    int seg[10] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
    int sang[1440];
    for (int x = 0; x < 1440; x++) {
        int h = x / 60, m = x % 60;
        sang[x] = seg[h / 10] + seg[h % 10] + seg[m / 10] + seg[m % 10];
    }
    int t;
    scanf("%d", &t);
    while (t--) {
        int h1, m1, h2, m2;
        scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
        long long tong = 0;
        for (int x = h1 * 60 + m1; x <= h2 * 60 + m2; x++) tong += sang[x];
        printf("%lld\n", tong);
    }
    return 0;
}
