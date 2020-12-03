#include <bits/stdc++.h>
using namespace std;
int main() {
    long long l = 1, r=2000000000;
    while (l<=r) {
        long long mid=(l+r)/2;
        cout << mid << endl;
        string a; cin >> a;
        if (a=="SINKS") l = mid + 1;
        else if (a=="FLOATS") r = mid - 1;
        else return 0;
    }
}

