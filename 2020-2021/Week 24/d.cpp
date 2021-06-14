#include <bits/stdc++.h>

using namespace std;

int n, k, q;
const int maxn = 200000;

int d[maxn+5];
int psa[maxn+5];

signed main() {
    cin >> n >> k >> q;
    for(int i = 1; i <= n; i++) {
        int l, r;
        cin >> l >> r;
        d[l]++;
        d[r+1]--;
    }

    for(int i = 1; i <= 200000; i++) {
        d[i] += d[i-1];
    }

    for (int i = 1; i <= 200000; i++) {
        if(d[i] >= k)
            psa[i]++;

        psa[i] += psa[i-1];
    }

    for(int i = 1; i <= q; i++) {
        int a, b;
        cin >> a >> b;

        cout << psa[b]-psa[a-1] << endl;
    }
}
