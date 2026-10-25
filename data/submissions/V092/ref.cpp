// V092 - Hai may noi tiep (quy tac Johnson): nhom a<=b theo a tang, nhom a>b theo b giam
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<long long, long long>> first, second;
    for (int i = 0; i < n; i++) {
        long long a, b;
        cin >> a >> b;
        if (a <= b) first.push_back({a, b});
        else second.push_back({a, b});
    }
    sort(first.begin(), first.end());   // a tang dan
    sort(second.begin(), second.end(), [](auto &p, auto &q) { return p.second > q.second; });   // b giam dan
    first.insert(first.end(), second.begin(), second.end());
    long long endA = 0, endB = 0;
    for (auto &x : first) {
        endA += x.first;                          // may nhao lam lien tuc
        endB = max(endB, endA) + x.second;        // lo nuong cho bot nhao xong
    }
    cout << endB << "\n";
    return 0;
}
