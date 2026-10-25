// V095 - Dem cap co tong <= X bang hai con tro
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    long long X;
    cin >> n >> X;
    vector<long long> a(n);
    for (auto &x : a) cin >> x;
    sort(a.begin(), a.end());
    long long cnt = 0;
    int i = 0, j = n - 1;
    while (i < j) {
        if (a[i] + a[j] <= X) {
            cnt += j - i;   // a[i] ghep duoc voi a[i+1..j]
            i++;
        } else {
            j--;
        }
    }
    cout << cnt << "\n";
    return 0;
}
