// V093 - Mua re ban dat (moi phien 1 bao): tham lam co hoi han bang hang doi uu tien
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    priority_queue<long long, vector<long long>, greater<long long>> pq;
    long long profit = 0;
    for (int i = 0; i < n; i++) {
        long long p;
        cin >> p;
        if (!pq.empty() && pq.top() < p) {
            profit += p - pq.top();   // ban bao mua re nhat
            pq.pop();
            pq.push(p);               // de "hoi han": sau nay co the ban o gia cao hon
        }
        pq.push(p);                   // gia p cung la mot lua chon mua
    }
    cout << profit << "\n";
    return 0;
}
