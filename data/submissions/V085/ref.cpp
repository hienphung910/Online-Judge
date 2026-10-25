// V085 - Toi thieu do tre lon nhat: may theo han chot tang dan (EDD)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<long long, long long>> job(n);   // (han e, thoi gian d)
    for (auto &j : job) cin >> j.second >> j.first;
    sort(job.begin(), job.end());
    long long now = 0, worst = 0;
    for (auto &j : job) {
        now += j.second;
        worst = max(worst, now - j.first);
    }
    cout << worst << "\n";
    return 0;
}
