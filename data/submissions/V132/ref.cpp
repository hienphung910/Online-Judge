// V132 - set luu cac coc hong (tim hang xom bang upper_bound), multiset luu do dai cac doan lanh
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    int m;
    cin >> n >> m;
    set<long long> hong = {0, n + 1};     // hai coc gia o hai dau cho de xu ly bien
    multiset<long long> doan = {n};       // do dai cac doan coc lanh lien tiep
    for (int j = 0; j < m; j++) {
        long long p;
        cin >> p;
        auto it = hong.upper_bound(p);    // coc hong gan nhat ben phai p
        long long R = *it, L = *prev(it); // coc hong gan nhat ben trai p
        doan.erase(doan.find(R - L - 1)); // doan (L, R) bi cat lam hai
        doan.insert(p - L - 1);
        doan.insert(R - p - 1);
        hong.insert(p);
        cout << *doan.rbegin() << (j + 1 < m ? ' ' : '\n');
    }
    return 0;
}
