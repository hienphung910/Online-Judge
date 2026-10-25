// V032 - Ma Morse: chep san bang ma 36 ky tu, ma hoa va giai ma bang cach tra bang
#include <bits/stdc++.h>
using namespace std;

const string KYTU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
const string MA[36] = {
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
    "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
    "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."};

int main() {
    int t;
    string line;
    getline(cin, line);
    t = stoi(line);
    while (t--) {
        getline(cin, line);
        stringstream ss(line);
        string loai, w;
        ss >> loai;
        string res;
        if (loai == "MA") {
            while (ss >> w) {
                if (!res.empty()) res += " / ";
                for (int i = 0; i < (int)w.size(); i++) {
                    if (i > 0) res += " ";
                    res += MA[KYTU.find(w[i])];
                }
            }
        } else {
            while (ss >> w) {
                if (w == "/") { res += " "; continue; }
                char c = '?';
                for (int k = 0; k < 36; k++) if (MA[k] == w) c = KYTU[k];
                res += c;
            }
        }
        cout << res << "\n";
    }
    return 0;
}
