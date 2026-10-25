// V116 - Hang doi uu tien (heap) voi thu tu so sanh tu dinh nghia
#include <bits/stdc++.h>
using namespace std;

int main() {
    int q;
    cin >> q;
    vector<string> ten;
    // priority_queue lay phan tu LON nhat: (p, -thu tu den) -> p lon truoc, cung p thi den som truoc
    priority_queue<pair<int, int>> pq;
    while (q--) {
        int loai;
        cin >> loai;
        if (loai == 1) {
            string s;
            int p;
            cin >> s >> p;
            ten.push_back(s);
            pq.push({p, -(int)(ten.size() - 1)});
        } else if (pq.empty()) {
            cout << "TRONG\n";
        } else {
            cout << ten[-pq.top().second] << "\n";
            pq.pop();
        }
    }
    return 0;
}
