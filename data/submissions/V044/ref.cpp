// V044 - Thap Ha Noi: de quy doi n-1 khay sang ke trung gian
#include <bits/stdc++.h>
using namespace std;

vector<array<int, 3>> buoc;

void doi(int n, int tu, int den) {
    if (n == 0) return;
    int giua = 6 - tu - den;          // ke con lai (1 + 2 + 3 = 6)
    doi(n - 1, tu, giua);
    buoc.push_back({n, tu, den});
    doi(n - 1, giua, den);
}

int main() {
    int n, s, t;
    cin >> n >> s >> t;
    doi(n, s, t);
    cout << buoc.size() << "\n";
    for (auto &b : buoc) cout << b[0] << " " << b[1] << " " << b[2] << "\n";
    return 0;
}
