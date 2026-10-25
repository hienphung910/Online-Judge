// V133 - Danh sach lien ket doi (gop hai bao O(1)) + set cac cap ke nhau sap theo (tong, vi tri)
// Bao gop giu chi so cua bao ben trai, nen thu tu chi so trong danh sach van tang dan -> "trai nhat" = chi so nho nhat.
#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> w;          // w[i]: khoi luong bao i
vector<int> L, R;             // bao ben trai / ben phai (-1 hoac n neu khong co)
set<pair<long long, int>> cap; // (w[i] + w[R[i]], i): cap (i, R[i])

void them(int i) { if (i >= 0 && R[i] < n) cap.insert({w[i] + w[R[i]], i}); }
void bo(int i)   { if (i >= 0 && R[i] < n) cap.erase({w[i] + w[R[i]], i}); }

int main() {
    cin >> n;
    w.resize(n);
    L.resize(n);
    R.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> w[i];
        L[i] = i - 1;
        R[i] = i + 1;
    }
    for (int i = 0; i + 1 < n; i++) them(i);
    vector<long long> ans;
    while (!cap.empty()) {
        int i = cap.begin()->second, j = R[i];   // gop bao j vao bao i
        bo(L[i]); bo(i); bo(j);                  // cac cap co dung toi i hoac j se thay doi
        w[i] += w[j];
        R[i] = R[j];
        if (R[j] < n) L[R[j]] = i;
        them(L[i]); them(i);
        ans.push_back(w[i]);
    }
    for (size_t k = 0; k < ans.size(); k++) cout << ans[k] << (k + 1 < ans.size() ? " " : "");
    cout << '\n';
    return 0;
}
