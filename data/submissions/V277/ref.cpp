// V277 - Tong cac uoc sigma(i) bang sang tuyen tinh, tra loi doan bang tong tien to
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int N = 1000000;
int lp[N + 1];        // uoc nguyen to nho nhat
int pw[N + 1];        // luy thua lon nhat cua lp[i] chia het i
ll sig[N + 1];        // sigma(i) = tong cac uoc cua i
ll pre[N + 1];        // pre[i] = sig[1] + ... + sig[i]
vector<int> primes;

int main() {
    sig[1] = 1;
    for (int i = 2; i <= N; i++) {
        if (lp[i] == 0) {  // i nguyen to
            lp[i] = i; pw[i] = i; sig[i] = i + 1;
            primes.push_back(i);
        }
        for (int p : primes) {
            if (p > lp[i] || (ll)i * p > N) break;
            int x = i * p;
            lp[x] = p;
            if (p < lp[i]) {           // p moi xuat hien: nhan tinh voi i
                pw[x] = p;
                sig[x] = sig[i] * (p + 1);
            } else {                   // p == lp[i]: tang so mu cua p
                pw[x] = pw[i] * p;
                int rest = i / pw[i];  // phan con lai, nguyen to cung nhau voi p
                if (rest == 1) sig[x] = sig[i] * p + 1;          // x = p^k
                else sig[x] = sig[rest] * sig[pw[x]];
            }
        }
    }
    for (int i = 1; i <= N; i++) pre[i] = pre[i - 1] + sig[i];

    int q;
    scanf("%d", &q);
    while (q--) {
        int l, r;
        scanf("%d %d", &l, &r);
        printf("%lld\n", pre[r] - pre[l - 1]);
    }
    return 0;
}
