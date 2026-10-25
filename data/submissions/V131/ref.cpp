// V131 - Nen toa do + mang hieu: chi xet cac diem dau mut, dem so den phu tung khoang giua hai diem ke nhau
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<long long> l(n), r(n), xs;
    for (int i = 0; i < n; i++) {
        cin >> l[i] >> r[i];
        xs.push_back(l[i]);
        xs.push_back(r[i]);
    }
    sort(xs.begin(), xs.end());
    xs.erase(unique(xs.begin(), xs.end()), xs.end());      // xs[j] = toa do thu j sau khi nen
    int m = xs.size();
    vector<int> diff(m + 1, 0);
    for (int i = 0; i < n; i++) {
        int a = lower_bound(xs.begin(), xs.end(), l[i]) - xs.begin();
        int b = lower_bound(xs.begin(), xs.end(), r[i]) - xs.begin();
        diff[a]++;          // den i phu cac khoang a, a+1, ..., b-1
        diff[b]--;
    }
    long long total = 0;    // co the toi 2e9, vuot int
    int cover = 0;
    for (int j = 0; j + 1 < m; j++) {
        cover += diff[j];   // so den phu khoang [xs[j], xs[j+1]]
        if (cover >= k) total += xs[j + 1] - xs[j];
    }
    cout << total << '\n';
    return 0;
}
