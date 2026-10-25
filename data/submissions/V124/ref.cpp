// V124 - Nen toa do: hang cua moi diem = vi tri trong mang gia tri khac nhau sap giam dan
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (auto &x : a) cin >> x;
    vector<long long> v = a;
    sort(v.begin(), v.end(), greater<long long>());   // sap giam dan
    v.erase(unique(v.begin(), v.end()), v.end());     // bo trung -> cac muc diem khac nhau
    cout << v.size() << '\n';
    for (int i = 0; i < n; i++) {
        // vi tri dau tien co gia tri <= a[i] trong mang giam dan, chinh la so muc lon hon a[i]
        int pos = lower_bound(v.begin(), v.end(), a[i], greater<long long>()) - v.begin();
        cout << pos + 1 << (i + 1 < n ? ' ' : '\n');
    }
    return 0;
}
