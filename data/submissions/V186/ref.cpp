// V186 - Doan doi xung dai nhat va so doan doi xung bang thuat toan Manacher, O(n)
// Chen '#' giua cac ky tu: t = #a#b#a#. d[i] = ban kinh doi xung lon nhat tai tam i cua t.
// Tam i ung voi (d[i] - 1) do dai lon nhat va dong gop d[i] / 2 doan doi xung cua S.
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    string t = "#";
    for (char c : s) { t += c; t += '#'; }
    int m = t.size();
    vector<int> d(m, 0);               // d[i]: so ky tu t[i-d+1..i+d-1] doi xung (tinh ca tam)
    int l = 0, r = -1;                 // [l, r] la doan doi xung xa nhat ve phai da biet
    for (int i = 0; i < m; i++) {
        int k = (i > r) ? 1 : min(d[l + r - i], r - i + 1);
        while (i - k >= 0 && i + k < m && t[i - k] == t[i + k]) k++;
        d[i] = k;
        if (i + k - 1 > r) { l = i - k + 1; r = i + k - 1; }
    }
    int best = 0;
    long long cnt = 0;
    for (int i = 0; i < m; i++) {
        best = max(best, d[i] - 1);
        cnt += d[i] / 2;
    }
    cout << best << ' ' << cnt << '\n';
    return 0;
}
