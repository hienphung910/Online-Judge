// V007 - Hinh chu nhat lon nhat trong bieu do cot bang ngan xep don dieu, O(n)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> h(n + 1, 0);   // them cot cao 0 o cuoi de day het ngan xep
    for (int i = 0; i < n; i++) cin >> h[i];
    vector<int> st;                  // chi so cac cot, chieu cao tang dan
    long long best = 0;
    for (int i = 0; i <= n; i++) {
        while (!st.empty() && h[st.back()] >= h[i]) {
            long long cao = h[st.back()];
            st.pop_back();
            int trai = st.empty() ? -1 : st.back();   // cot thap hon gan nhat ben trai
            best = max(best, cao * (i - trai - 1));
        }
        st.push_back(i);
    }
    cout << best << "\n";
    return 0;
}
