// V077 - Sap xep voi phep so sanh tu dinh nghia: x truoc y neu x+y > y+x
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> a(n);
    for (auto &s : a) cin >> s;
    sort(a.begin(), a.end(), [](const string &x, const string &y) {
        return x + y > y + x;
    });
    string kq;
    for (auto &s : a) kq += s;
    cout << kq << "\n";
    return 0;
}
