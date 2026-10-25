// V052 - Quay lui gan chu so cho chu cai; moi chu cai co "he so dong gop", phep cong dung khi tong = 0
#include <bits/stdc++.h>
using namespace std;

vector<char> chu;            // cac chu cai khac nhau
long long heSo[26];          // dong gop cua moi chu cai (X, Y mang dau +, Z mang dau -)
bool dauTu[26];              // chu cai dung dau mot tu thi khong duoc la 0
bool daDung[10];
long long dem = 0;

void them(const string &w, int dau) {
    long long p = 1;
    for (int i = (int)w.size() - 1; i >= 0; i--, p *= 10) heSo[w[i] - 'A'] += dau * p;
    dauTu[w[0] - 'A'] = true;
}

void gan(int i, long long tong) {
    if (i == (int)chu.size()) { if (tong == 0) dem++; return; }
    int c = chu[i] - 'A';
    for (int d = 0; d <= 9; d++) {
        if (daDung[d] || (d == 0 && dauTu[c])) continue;
        daDung[d] = true;
        gan(i + 1, tong + heSo[c] * d);
        daDung[d] = false;
    }
}

int main() {
    string x, y, z;
    cin >> x >> y >> z;
    them(x, 1); them(y, 1); them(z, -1);
    for (char ch : x + y + z)
        if (find(chu.begin(), chu.end(), ch) == chu.end()) chu.push_back(ch);
    gan(0, 0);
    cout << dem << "\n";
    return 0;
}
