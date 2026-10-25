// V126 - Danh sach lien ket (std::list) mo phong con tro soan thao: chen/xoa tai con tro O(1)
#include <bits/stdc++.h>
using namespace std;

int main() {
    string keys;
    cin >> keys;
    list<char> text;
    auto cur = text.begin();          // con tro dung ngay TRUOC phan tu *cur (end() = cuoi dong)
    for (char c : keys) {
        if (c == '<') {
            if (cur != text.begin()) cur--;
        } else if (c == '>') {
            if (cur != text.end()) cur++;
        } else if (c == '-') {
            if (cur != text.begin()) cur = text.erase(prev(cur));   // xoa ki tu ben trai con tro
        } else if (c == '[') {
            cur = text.begin();
        } else if (c == ']') {
            cur = text.end();
        } else {
            text.insert(cur, c);      // chen truoc cur, cur van tro vao phan tu cu
        }
    }
    if (text.empty()) cout << "RONG";
    for (char c : text) cout << c;
    cout << '\n';
    return 0;
}
