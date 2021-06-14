#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e3;
const int maxv = 1e6;

int n;
int a[maxn];
int freq[(int)1e6+1];

int main() {
    cin >> n;
    int ans = 0;
    for(int i = 0; i < n; i++) {
        cin >> a[i];
        freq[a[i]]++;

        if(freq[a[i]] > freq[ans]) {
            ans = a[i];
        }
    }
    cout << ans << endl;
}