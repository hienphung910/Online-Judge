// V218 - Thuat toan Mo tren mang tien to XOR: dem doan con [i, j] trong [l, r] co XOR = k
// Doan [i, j] co XOR = k <=> p[i-1] ^ p[j] = k; cau hoi (l, r) -> dem cap trong chi so [l-1, r].
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q, k;
    cin >> n >> q >> k;
    vector<int> p(n + 1, 0);
    for (int i = 1; i <= n; i++) { int x; cin >> x; p[i] = p[i - 1] ^ x; }

    vector<int> L(q), R(q), id(q);
    for (int i = 0; i < q; i++) {
        cin >> L[i] >> R[i];
        L[i]--;                    // xet cac chi so tien to L..R
        id[i] = i;
    }
    int B = max(1, (int)sqrt((double)(n + 1)));
    sort(id.begin(), id.end(), [&](int x, int y) {
        if (L[x] / B != L[y] / B) return L[x] / B < L[y] / B;
        return R[x] < R[y];
    });

    vector<int> cnt(1 << 21, 0);   // gia tri XOR < 2^20
    vector<long long> ans(q);
    long long cur = 0;
    int curL = 0, curR = -1;
    auto add = [&](int i) { cur += cnt[p[i] ^ k]; cnt[p[i]]++; };
    auto del = [&](int i) { cnt[p[i]]--; cur -= cnt[p[i] ^ k]; };
    for (int t : id) {
        while (curR < R[t]) add(++curR);
        while (curL > L[t]) add(--curL);
        while (curR > R[t]) del(curR--);
        while (curL < L[t]) del(curL++);
        ans[t] = cur;
    }
    for (int i = 0; i < q; i++) cout << ans[i] << '\n';
    return 0;
}
