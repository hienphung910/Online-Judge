// V017 - Dem so chia het cho it nhat mot a_i bang bao ham - loai tru, O(2^k * log)
// Moi tap con S (khac rong) dong gop (-1)^(|S|+1) * floor(N / lcm(S)).
// Khi lcm > N thi dong gop bang 0 va moi tap lon hon cung vay -> cat nhanh.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef __int128 i128;

int k;
ll N, a[15];
i128 total = 0;   // tong co dau co the vuot 2^63 giua chung nen dung __int128

// da chon xong cac phan tu truoc idx, lcm hien tai la cur, so phan tu da chon la cnt
void dfs(int idx, ll cur, int cnt) {
    for (int i = idx; i < k; i++) {
        i128 l = (i128)(cur / __gcd(cur, a[i])) * a[i];
        if (l > N) continue;                          // vuot N: dong gop 0, bo ca nhanh
        if ((cnt + 1) % 2 == 1) total += N / (ll)l;
        else total -= N / (ll)l;
        dfs(i + 1, (ll)l, cnt + 1);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> N >> k;
    for (int i = 0; i < k; i++) cin >> a[i];
    dfs(0, 1, 0);
    cout << (ll)total << "\n";
    return 0;
}
