// V298 - Slope trick: chi phi nho nhat de day tang chat
// Dat c_i = a_i - i, can day d khong giam va toi thieu tong |c_i - d_i|.
// Ham chi phi la loi, gay khuc; hang doi uu tien max luu cac diem gay ben trai.
// Them c: neu dinh hang doi > c thi phai tra (dinh - c), thay dinh bang c.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    priority_queue<long long> pq;
    long long ans = 0;
    for (int i = 1; i <= n; i++) {
        long long a;
        scanf("%lld", &a);
        long long c = a - i;
        pq.push(c);
        if (pq.top() > c) {
            ans += pq.top() - c;
            pq.pop();
            pq.push(c);
        }
    }
    printf("%lld\n", ans);
    return 0;
}
