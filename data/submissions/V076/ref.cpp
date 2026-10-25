// V076 - Phan tu nho thu k bang chon nhanh (nth_element), trung binh O(n)
#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n, k, x, A, B, M;
    cin >> n >> k >> x >> A >> B >> M;
    vector<int> a(n);
    a[0] = x;
    for (int i = 1; i < n; i++) {
        x = (A * x + B) % M;
        a[i] = x;
    }
    nth_element(a.begin(), a.begin() + (k - 1), a.end());
    cout << a[k - 1] << "\n";
    return 0;
}
