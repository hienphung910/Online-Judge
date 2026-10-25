// V035 - Quan ly tai khoan bang map<string, long long>; map da sap xep ten nen de tim GIAU
#include <bits/stdc++.h>
using namespace std;

int main() {
    int q;
    cin >> q;
    map<string, long long> tk;
    while (q--) {
        string op, a, b;
        long long x;
        cin >> op;
        if (op == "MO") {
            cin >> a;
            if (tk.count(a)) cout << "LOI\n";
            else { tk[a] = 0; cout << "OK\n"; }
        } else if (op == "NAP") {
            cin >> a >> x;
            if (!tk.count(a)) cout << "LOI\n";
            else { tk[a] += x; cout << "OK\n"; }
        } else if (op == "RUT") {
            cin >> a >> x;
            if (!tk.count(a) || tk[a] < x) cout << "LOI\n";
            else { tk[a] -= x; cout << "OK\n"; }
        } else if (op == "CHUYEN") {
            cin >> a >> b >> x;
            if (!tk.count(a) || !tk.count(b) || a == b || tk[a] < x) cout << "LOI\n";
            else { tk[a] -= x; tk[b] += x; cout << "OK\n"; }
        } else if (op == "XEM") {
            cin >> a;
            if (!tk.count(a)) cout << "LOI\n";
            else cout << tk[a] << "\n";
        } else {  // GIAU: duyet theo thu tu ten tang dan, chi doi khi lon hon han
            if (tk.empty()) { cout << "LOI\n"; continue; }
            string best = tk.begin()->first;
            for (auto &p : tk) if (p.second > tk[best]) best = p.first;
            cout << best << "\n";
        }
    }
    return 0;
}
