// V190 - Dem cap doan doi xung khong giao nhau: Manacher + mang hieu, O(n)
// Tam le i ban kinh k: cac doan [i-j, i+j], j = 0..k-1 -> bat dau trong [i-k+1, i], ket thuc trong [i, i+k-1].
// Tam chan (giua i-1 va i) ban kinh k: bat dau trong [i-k, i-1], ket thuc trong [i, i+k-1].
// batDau[x], ketThuc[x] = so doan doi xung bat dau / ket thuc tai x (cong theo doan bang mang hieu).
// Dap an = tong batDau[c] * (so doan ket thuc truoc c).
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
vector<ll> dBd, dKt;                     // mang hieu cho batDau, ketThuc (kich thuoc n + 1)

void congDoan(vector<ll>& d, int l, int r) { d[l]++; d[r + 1]--; }

int main() {
    string s;
    cin >> s;
    n = s.size();
    dBd.assign(n + 1, 0); dKt.assign(n + 1, 0);
    // Manacher tam le: d1[i] = so doan doi xung le co tam i
    vector<int> d1(n), d2(n);
    for (int i = 0, l = 0, r = -1; i < n; i++) {
        int k = (i > r) ? 1 : min(d1[l + r - i], r - i + 1);
        while (i - k >= 0 && i + k < n && s[i - k] == s[i + k]) k++;
        d1[i] = k;
        if (i + k - 1 > r) { l = i - k + 1; r = i + k - 1; }
    }
    // Manacher tam chan: d2[i] = so doan doi xung chan co tam giua i-1 va i
    for (int i = 0, l = 0, r = -1; i < n; i++) {
        int k = (i > r) ? 0 : min(d2[l + r - i + 1], r - i + 1);
        while (i - k - 1 >= 0 && i + k < n && s[i - k - 1] == s[i + k]) k++;
        d2[i] = k;
        if (i + k - 1 > r) { l = i - k; r = i + k - 1; }
    }
    for (int i = 0; i < n; i++) {
        congDoan(dBd, i - d1[i] + 1, i);
        congDoan(dKt, i, i + d1[i] - 1);
        if (d2[i] > 0) {
            congDoan(dBd, i - d2[i], i - 1);
            congDoan(dKt, i, i + d2[i] - 1);
        }
    }
    ll bd = 0, kt = 0, ketTruoc = 0, ans = 0;
    for (int x = 0; x < n; x++) {
        bd += dBd[x];                    // so doan bat dau tai x
        ans += bd * ketTruoc;            // ghep voi moi doan ket thuc tai vi tri < x
        kt += dKt[x];                    // so doan ket thuc tai x
        ketTruoc += kt;
    }
    cout << ans << '\n';
    return 0;
}
