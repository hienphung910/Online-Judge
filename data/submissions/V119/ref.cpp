// V119 - Doan ngoac dung dai nhat va so doan dat do dai do, ngan xep O(n)
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n = s.size();
    vector<int> st = {0};   // vi tri, phan tu day la "moc" (vi tri ngay truoc doan dang xet)
    int best = 0, dem = 0;
    for (int i = 1; i <= n; i++) {
        if (s[i - 1] == '(') {
            st.push_back(i);
        } else {
            st.pop_back();
            if (st.empty()) {
                st.push_back(i);   // ')' thua: moc moi
            } else {
                int len = i - st.back();   // doan dung dai nhat ket thuc tai i
                if (len > best) best = len, dem = 1;
                else if (len == best) dem++;
            }
        }
    }
    cout << best << " " << (best == 0 ? 0 : dem) << "\n";
    return 0;
}
