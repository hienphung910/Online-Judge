// V090 - Viec mot ngay co han chot va tien cong: duyet theo han, hang doi uu tien bo viec re nhat
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<int, long long>> job(n);   // (han d, tien p)
    for (auto &j : job) cin >> j.first >> j.second;
    sort(job.begin(), job.end());
    priority_queue<long long, vector<long long>, greater<long long>> taken;
    long long total = 0;
    for (auto &j : job) {
        taken.push(j.second);
        total += j.second;
        if ((int)taken.size() > j.first) {   // qua so ngay cho phep: bo viec it tien nhat
            total -= taken.top();
            taken.pop();
        }
    }
    cout << total << "\n";
    return 0;
}
