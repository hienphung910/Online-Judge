// V080 - So lan doi cho ke nhau it nhat = so nghich the cua day vi tri dich
#include <bits/stdc++.h>
using namespace std;

vector<int> p, tmp;

long long demNghichThe(int l, int r) {          // dem tren doan [l, r) va sap xep doan do
    if (r - l <= 1) return 0;
    int m = (l + r) / 2;
    long long res = demNghichThe(l, m) + demNghichThe(m, r);
    int i = l, j = m, k = l;
    while (i < m && j < r) {
        if (p[i] < p[j]) tmp[k++] = p[i++];
        else { res += m - i; tmp[k++] = p[j++]; }
    }
    while (i < m) tmp[k++] = p[i++];
    while (j < r) tmp[k++] = p[j++];
    for (int t = l; t < r; t++) p[t] = tmp[t];
    return res;
}

int main() {
    int n;
    cin >> n;
    vector<int> a(n), b(n);
    for (auto &x : a) cin >> x;
    for (auto &x : b) cin >> x;
    map<int, queue<int>> viTri;                 // viTri[x] = cac vi tri co ao so x trong doi hinh moi
    for (int i = 0; i < n; i++) viTri[b[i]].push(i);
    p.resize(n);
    tmp.resize(n);
    for (int i = 0; i < n; i++) {
        if (viTri[a[i]].empty()) { cout << -1 << "\n"; return 0; }
        p[i] = viTri[a[i]].front();             // ban thu k mac ao x di toi vi tri ao x thu k
        viTri[a[i]].pop();
    }
    cout << demNghichThe(0, n) << "\n";
    return 0;
}
