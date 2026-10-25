// V086 - So phong it nhat: duyet theo gio bat dau, hang doi uu tien giu gio ket thuc cac phong
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<pair<int, int>> a(n);
    for (auto &x : a) cin >> x.first >> x.second;
    sort(a.begin(), a.end());
    priority_queue<int, vector<int>, greater<int>> rooms;   // gio phong trong lai
    for (auto &x : a) {
        if (!rooms.empty() && rooms.top() <= x.first) rooms.pop();   // dung lai phong da trong
        rooms.push(x.second);
    }
    cout << rooms.size() << "\n";
    return 0;
}
