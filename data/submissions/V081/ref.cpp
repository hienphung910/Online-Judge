// V081 - Doi tien it to nhat voi he menh gia chuan: tham lam lay to lon nhat
#include <bits/stdc++.h>
using namespace std;

int main() {
    int coin[] = {500, 200, 100, 50, 20, 10, 5, 2, 1};
    int t;
    cin >> t;
    while (t--) {
        long long n, cnt = 0;
        cin >> n;
        for (int c : coin) {
            cnt += n / c;   // dung toi da to menh gia c
            n %= c;
        }
        cout << cnt << "\n";
    }
    return 0;
}
