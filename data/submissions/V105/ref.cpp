// V105 - Hop long nhau: sap xep (w tang, h giam) roi tim LIS chat tren h
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<long long, long long>> box(n);
    for (auto &b : box) cin >> b.first >> b.second;
    sort(box.begin(), box.end(), [](const pair<long long, long long> &a, const pair<long long, long long> &b) {
        if (a.first != b.first) return a.first < b.first;
        return a.second > b.second;   // cung w thi h giam dan
    });
    vector<long long> d;   // d[k] = h cuoi nho nhat cua chuoi do dai k + 1
    for (auto &b : box) {
        auto it = lower_bound(d.begin(), d.end(), b.second);
        if (it == d.end()) d.push_back(b.second);
        else *it = b.second;
    }
    cout << d.size() << "\n";
    return 0;
}
