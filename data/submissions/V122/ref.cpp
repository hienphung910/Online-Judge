// V122 - Mo phong may in: sap xep theo thoi diem gui + hang doi uu tien (d, r, chi so)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> r(n), d(n);
    vector<int> id(n);
    for (int i = 0; i < n; i++) {
        cin >> r[i] >> d[i];
        id[i] = i;
    }
    sort(id.begin(), id.end(), [&](int a, int b) { return r[a] < r[b]; });
    // min-heap theo bo ba (d, r, chi so)
    priority_queue<tuple<long long, long long, int>, vector<tuple<long long, long long, int>>, greater<>> pq;
    long long t = 0;
    int k = 0;   // id[k] la yeu cau tiep theo chua duoc dua vao hang doi
    vector<int> thuTu;
    while ((int)thuTu.size() < n) {
        if (pq.empty() && r[id[k]] > t) t = r[id[k]];   // may ranh, khong ai cho: nhay toi yeu cau ke tiep
        while (k < n && r[id[k]] <= t) {
            pq.push({d[id[k]], r[id[k]], id[k]});
            k++;
        }
        auto [dd, rr, i] = pq.top();
        pq.pop();
        thuTu.push_back(i + 1);
        t += dd;
    }
    for (int i = 0; i < n; i++) cout << thuTu[i] << (i + 1 < n ? ' ' : '\n');
    return 0;
}
