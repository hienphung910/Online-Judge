// V246 - Chat tam phan long nhau: diem co tong khoang cach Euclid nho nhat
// f(x, y) = tong sqrt((x - x_i)^2 + (y - y_i)^2) loi theo ca hai bien.
// g(x) = min theo y cua f(x, y) cung loi -> chat tam phan x, ben trong chat tam phan y.
#include <bits/stdc++.h>
using namespace std;

int n;
vector<double> X, Y;

double f(double x, double y) {
    double s = 0;
    for (int i = 0; i < n; i++) s += hypot(x - X[i], y - Y[i]);
    return s;
}

double g(double x) {                 // gia tri nho nhat khi co dinh x
    double lo = -1e4, hi = 1e4;
    for (int it = 0; it < 80; it++) {
        double m1 = lo + (hi - lo) / 3, m2 = hi - (hi - lo) / 3;
        if (f(x, m1) < f(x, m2)) hi = m2; else lo = m1;
    }
    return f(x, (lo + hi) / 2);
}

int main() {
    cin >> n;
    X.resize(n), Y.resize(n);
    for (int i = 0; i < n; i++) cin >> X[i] >> Y[i];
    double lo = -1e4, hi = 1e4;
    for (int it = 0; it < 80; it++) {
        double m1 = lo + (hi - lo) / 3, m2 = hi - (hi - lo) / 3;
        if (g(m1) < g(m2)) hi = m2; else lo = m1;
    }
    printf("%.9f\n", g((lo + hi) / 2));
    return 0;
}
