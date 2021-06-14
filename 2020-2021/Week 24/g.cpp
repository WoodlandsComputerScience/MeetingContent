#include <bits/stdc++.h>
using namespace std;
#define int long long

const int maxn = 100050;

int v[maxn];
int t[maxn];
int tpsa[maxn];

int whole[maxn];
int rem[maxn];

signed main() {
    int N;
    cin >> N;

    for(int i = 1; i <= N; i++) {
        cin >> v[i];
    }

    for(int i = 1; i <= N; i++) {
        cin >> t[i];
    }

    for(int i = 1; i <= N; i++) {
        tpsa[i] = tpsa[i-1]+t[i];
    }

    for(int i = 1; i <= N; i++) {
        int l = i;
        int r = N;
        int lastgood = -1;

        while(l <= r) {
            int m = (l+r)/2;

            int sum = tpsa[m]-tpsa[i-1];

            if(sum <= v[i]) {
                l = m+1;
                lastgood = m;
            } else {
                r = m-1;
            }
        }

        if(lastgood == -1) {
            rem[i] += v[i];
        } else {
            whole[i]++;
            whole[lastgood+1]--;
            rem[lastgood+1] += (v[i]-(tpsa[lastgood]-tpsa[i-1]));
        }
    }

    for(int i = 1; i <= N; i++) {
        whole[i] += whole[i-1];
    }

    for(int i = 1; i <= N; i++) {
        cout << (t[i]*whole[i])+rem[i] << " ";
    }
    cout << endl;
}
