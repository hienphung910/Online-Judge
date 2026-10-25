// V121 - Doan dai nhat co max - min <= D: hai con tro + hai deque, O(n)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, D;
    cin >> n >> D;
    vector<int> a(n);
    for (auto& x : a) cin >> x;
    deque<int> mx, mn;   // mx: gia tri giam dan, mn: gia tri tang dan (luu chi so)
    int l = 0, best = 0, start = 0;
    for (int r = 0; r < n; r++) {
        while (!mx.empty() && a[mx.back()] <= a[r]) mx.pop_back();
        while (!mn.empty() && a[mn.back()] >= a[r]) mn.pop_back();
        mx.push_back(r);
        mn.push_back(r);
        while (a[mx.front()] - a[mn.front()] > D) {   // cua so [l, r] chua hop le: day l len
            l++;
            if (mx.front() < l) mx.pop_front();
            if (mn.front() < l) mn.pop_front();
        }
        if (r - l + 1 > best) {   // chi cap nhat khi dai hon han -> giu doan bat dau som nhat
            best = r - l + 1;
            start = l + 1;
        }
    }
    cout << best << " " << start << "\n";
    return 0;
}
