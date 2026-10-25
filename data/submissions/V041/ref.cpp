// V041 - So tu man: chi co 46 so <= 10^18, tinh truoc (duyet to hop chu so) roi chep vao bang
#include <bits/stdc++.h>
using namespace std;

const long long TU_MAN[] = {
    1LL, 2LL, 3LL, 4LL, 5LL,
    6LL, 7LL, 8LL, 9LL, 153LL,
    370LL, 371LL, 407LL, 1634LL, 8208LL,
    9474LL, 54748LL, 92727LL, 93084LL, 548834LL,
    1741725LL, 4210818LL, 9800817LL, 9926315LL, 24678050LL,
    24678051LL, 88593477LL, 146511208LL, 472335975LL, 534494836LL,
    912985153LL, 4679307774LL, 32164049650LL, 32164049651LL, 40028394225LL,
    42678290603LL, 44708635679LL, 49388550606LL, 82693916578LL, 94204591914LL,
    28116440335967LL, 4338281769391370LL, 4338281769391371LL, 21897142587612075LL, 35641594208964132LL,
    35875699062250035LL};

int main() {
    int t;
    cin >> t;
    int k = sizeof(TU_MAN) / sizeof(TU_MAN[0]);
    while (t--) {
        long long l, r;
        cin >> l >> r;
        int dem = 0;
        for (int i = 0; i < k; i++)
            if (l <= TU_MAN[i] && TU_MAN[i] <= r) dem++;
        cout << dem << "\n";
    }
    return 0;
}
