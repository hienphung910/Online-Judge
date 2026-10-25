// V115 - Max tren cua so truot do dai k bang deque, O(n)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (auto& x : a) cin >> x;
    deque<int> dq;   // chi so, gia tri giam dan tu dau den cuoi
    vector<int> res;
    for (int i = 0; i < n; i++) {
        while (!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();
        dq.push_back(i);
        if (dq.front() <= i - k) dq.pop_front();   // gio da roi khoi cua so
        if (i >= k - 1) res.push_back(a[dq.front()]);
    }
    for (size_t i = 0; i < res.size(); i++) cout << res[i] << (i + 1 < res.size() ? ' ' : '\n');
    return 0;
}
