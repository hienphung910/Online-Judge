// V233 - Trinh kiem tra du lieu vao (validator) cho bai "Truy van doan"
// Doc lan luot cac so theo dung thu tu cua de goc, dung lai o loi dau tien.
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll NMAX = 1000, AMAX = 1000000, QMAX = 1000;

string check(const vector<ll> &b) {
    size_t pos = 0;                         // so luong so da doc
    string loi = "LOI ";                    // in kem vi tri cua so vua doc (bang pos)
    if (pos == b.size()) return "THIEU";
    ll n = b[pos++];
    if (n < 1 || n > NMAX) return loi + to_string(pos);
    set<ll> used;
    for (ll i = 0; i < n; i++) {
        if (pos == b.size()) return "THIEU";
        ll a = b[pos++];
        if (a < 1 || a > AMAX || used.count(a)) return loi + to_string(pos);
        used.insert(a);
    }
    if (pos == b.size()) return "THIEU";
    ll q = b[pos++];
    if (q < 1 || q > QMAX) return loi + to_string(pos);
    for (ll j = 0; j < q; j++) {
        if (pos == b.size()) return "THIEU";
        ll l = b[pos++];
        if (l < 1 || l > n) return loi + to_string(pos);
        if (pos == b.size()) return "THIEU";
        ll r = b[pos++];
        if (r < l || r > n) return loi + to_string(pos);
    }
    if (pos < b.size()) return "THUA";      // doc xong ma van con so
    return "HOP_LE";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) {
        int c;
        cin >> c;
        vector<ll> b(c);
        for (auto &x : b) cin >> x;
        cout << check(b) << "\n";
    }
    return 0;
}
