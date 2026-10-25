// V171 - Dem so cap nghich the bang cay Fenwick (nen toa do), O(n log n)
// So lan doi cho hai ban canh nhau it nhat = so cap i < j co h[i] > h[j].
// Duyet tu trai sang phai, BIT dem so ban da gap theo hang chieu cao.
#include <bits/stdc++.h>
using namespace std;

int m;
vector<int> bit;

void add(int i) {
    for (; i <= m; i += i & -i) bit[i]++;
}

int countUpTo(int i) {   // so ban da gap co hang <= i
    int s = 0;
    for (; i > 0; i -= i & -i) s += bit[i];
    return s;
}

int main() {
    int n;
    cin >> n;
    vector<int> h(n);
    for (int &x : h) cin >> x;
    vector<int> vals = h;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    m = vals.size();
    bit.assign(m + 1, 0);
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        int r = lower_bound(vals.begin(), vals.end(), h[i]) - vals.begin() + 1;
        ans += i - countUpTo(r);   // so ban dung truoc cao hon han ban i
        add(r);
    }
    cout << ans << '\n';
    return 0;
}
