// V120 - Tong (max - min) tren moi doan con: dem dong gop bang ngan xep don dieu, O(n)
#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> h;

// Tong max cua moi doan con. Doi dau h (h -> -h) thi ham nay cho -(tong min).
long long tongMax() {
    vector<int> L(n), R(n), st;
    for (int i = 0; i < n; i++) {               // L[i]: gan nhat ben trai co h > h[i]
        while (!st.empty() && h[st.back()] <= h[i]) st.pop_back();
        L[i] = st.empty() ? -1 : st.back();
        st.push_back(i);
    }
    st.clear();
    for (int i = n - 1; i >= 0; i--) {          // R[i]: gan nhat ben phai co h >= h[i]
        while (!st.empty() && h[st.back()] < h[i]) st.pop_back();
        R[i] = st.empty() ? n : st.back();
        st.push_back(i);
    }
    long long s = 0;
    for (int i = 0; i < n; i++) s += h[i] * (i - L[i]) * (R[i] - i);
    return s;
}

int main() {
    cin >> n;
    h.resize(n);
    for (auto& x : h) cin >> x;
    long long sumMax = tongMax();
    for (auto& x : h) x = -x;
    long long sumMin = -tongMax();
    cout << sumMax - sumMin << "\n";
    return 0;
}
