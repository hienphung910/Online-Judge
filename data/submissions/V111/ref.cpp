// V111 - Mo phong xep hang mua ve bang hang doi (queue)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> t(n), xong(n);
    queue<int> q;
    for (int i = 0; i < n; i++) {
        cin >> t[i];
        q.push(i);
    }
    int phut = 0;
    while (!q.empty()) {
        int i = q.front();
        q.pop();
        phut++;           // nguoi i mua 1 ve trong phut nay
        t[i]--;
        if (t[i] > 0) q.push(i);   // con thieu ve: quay lai cuoi hang
        else xong[i] = phut;
    }
    for (int i = 0; i < n; i++) cout << xong[i] << (i + 1 < n ? ' ' : '\n');
    return 0;
}
