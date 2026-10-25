// V049 - Quay lui dem so cach xep hang co tong hai so ao ke nhau la so nguyen to
#include <bits/stdc++.h>
using namespace std;

int n, a[15];
bool daDung[15], ngTo[205];
long long dem = 0;

void xep(int viTri, int truoc) {          // truoc: chi so nguoi dung o vi tri viTri - 1
    if (viTri == n) { dem++; return; }
    for (int i = 0; i < n; i++) {
        if (daDung[i]) continue;
        if (viTri > 0 && !ngTo[a[truoc] + a[i]]) continue;   // cat nhanh som
        daDung[i] = true;
        xep(viTri + 1, i);
        daDung[i] = false;
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int x = 2; x <= 200; x++) {
        ngTo[x] = true;
        for (int d = 2; d * d <= x; d++)
            if (x % d == 0) ngTo[x] = false;
    }
    xep(0, -1);
    cout << dem << "\n";
    return 0;
}
