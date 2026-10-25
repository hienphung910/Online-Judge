// V091 - Lam nhieu bai kip han nhat (Moore-Hodgson): duyet theo han, bo bai ton thoi gian nhat khi tre
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<long long, long long>> job(n);   // (han d, thoi gian t)
    for (auto &j : job) cin >> j.second >> j.first;
    sort(job.begin(), job.end());
    priority_queue<long long> chosen;   // dinh la bai ton nhieu gio nhat
    long long now = 0;
    for (auto &j : job) {
        chosen.push(j.second);
        now += j.second;
        if (now > j.first) {   // tre han: bo bai dai nhat
            now -= chosen.top();
            chosen.pop();
        }
    }
    cout << chosen.size() << "\n";
    return 0;
}
