// V185 - Dem so lan xuat hien cua moi tien to bang ham tien to, O(n)
// Moi vi tri i ket thuc mot lan xuat hien cua tien to do dai pi[i], pi[pi[i]-1], ...
// Dem cnt[pi[i]]++, roi day so dem tu do dai lon ve do dai nho theo chuoi pi.
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.size();
    vector<int> pi(n, 0);
    for (int i = 1; i < n; i++) {
        int k = pi[i - 1];
        while (k > 0 && s[i] != s[k]) k = pi[k - 1];
        if (s[i] == s[k]) k++;
        pi[i] = k;
    }
    vector<long long> cnt(n + 1, 0);
    for (int i = 0; i < n; i++) cnt[pi[i]]++;
    for (int k = n; k >= 1; k--) cnt[pi[k - 1]] += cnt[k];   // tien to k xuat hien thi vien cua no cung xuat hien
    long long best = 0;
    for (int k = 1; k <= n; k++) best = max(best, (long long)k * (cnt[k] + 1));  // +1: chinh tien to o vi tri 1
    cout << best << '\n';
    return 0;
}
