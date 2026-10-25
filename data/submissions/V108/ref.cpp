// V108 - Dem tap con co tong bang S bang chia doi (meet in the middle)
#include <bits/stdc++.h>
using namespace std;

vector<long long> allSums(const vector<long long> &v) {   // tong cua moi tap con
    vector<long long> s = {0};
    for (long long x : v) {
        int sz = s.size();
        for (int i = 0; i < sz; i++) s.push_back(s[i] + x);
    }
    return s;
}

int main() {
    int n;
    long long S;
    cin >> n >> S;
    vector<long long> a(n);
    for (auto &x : a) cin >> x;
    int h = n / 2;
    vector<long long> L = allSums(vector<long long>(a.begin(), a.begin() + h));
    vector<long long> R = allSums(vector<long long>(a.begin() + h, a.end()));
    sort(R.begin(), R.end());
    long long cnt = 0;
    for (long long x : L) {
        auto range = equal_range(R.begin(), R.end(), S - x);
        cnt += range.second - range.first;
    }
    cout << cnt << "\n";
    return 0;
}
