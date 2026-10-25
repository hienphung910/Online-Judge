// V106 - Dem so day con tang dai nhat (quy hoach dong O(n^2))
#include <bits/stdc++.h>
using namespace std;

int main() {
    const long long MOD = 1000000007;
    int n;
    cin >> n;
    vector<long long> a(n);
    for (auto &x : a) cin >> x;
    vector<int> len(n, 1);
    vector<long long> cnt(n, 1);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < i; j++) {
            if (a[j] >= a[i]) continue;
            if (len[j] + 1 > len[i]) {
                len[i] = len[j] + 1;
                cnt[i] = cnt[j];
            } else if (len[j] + 1 == len[i]) {
                cnt[i] = (cnt[i] + cnt[j]) % MOD;
            }
        }
    int best = *max_element(len.begin(), len.end());
    long long total = 0;
    for (int i = 0; i < n; i++)
        if (len[i] == best) total = (total + cnt[i]) % MOD;
    cout << best << " " << total << "\n";
    return 0;
}
