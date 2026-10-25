// V114 - Phan tu lon hon gan nhat ben phai bang ngan xep don dieu, O(n)
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> t(n), cho(n, 0);
    for (int i = 0; i < n; i++) cin >> t[i];
    vector<int> st;   // cac ngay chua tim duoc ngay am hon, nhiet do khong tang tu day len dinh
    for (int i = 0; i < n; i++) {
        while (!st.empty() && t[st.back()] < t[i]) {
            cho[st.back()] = i - st.back();
            st.pop_back();
        }
        st.push_back(i);
    }
    for (int i = 0; i < n; i++) cout << cho[i] << (i + 1 < n ? ' ' : '\n');
    return 0;
}
