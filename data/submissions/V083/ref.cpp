// V083 - Dong thung moi thung toi da 2 mon: hai con tro, mon nang nhat ghep voi mon nhe nhat neu duoc
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    long long W;
    cin >> n >> W;
    vector<long long> w(n);
    for (auto &x : w) cin >> x;
    sort(w.begin(), w.end());
    int i = 0, j = n - 1, boxes = 0;
    while (i <= j) {
        if (i < j && w[i] + w[j] <= W) i++;   // mon nhe nhat bo chung thung
        j--;                                  // mon nang nhat luon vao thung nay
        boxes++;
    }
    cout << boxes << "\n";
    return 0;
}
