// V006 - Day con tang dan dai nhat, O(n log n) bang lower_bound
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> d;   // d[i] = phan tu cuoi nho nhat cua day tang do dai i + 1
    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        auto it = lower_bound(d.begin(), d.end(), x);   // tang chat nen dung lower_bound
        if (it == d.end()) d.push_back(x);
        else *it = x;
    }
    cout << d.size() << "\n";
    return 0;
}
