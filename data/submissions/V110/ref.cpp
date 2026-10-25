// V110 - Kiem tra day ngoac hop le bang ngan xep
#include <bits/stdc++.h>
using namespace std;

bool hopLe(const string& s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else {
            char mo = (c == ')') ? '(' : (c == ']') ? '[' : '{';
            if (st.empty() || st.top() != mo) return false;
            st.pop();
        }
    }
    return st.empty();
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        cout << (hopLe(s) ? "YES" : "NO") << "\n";
    }
    return 0;
}
