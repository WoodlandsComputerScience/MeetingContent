#include <bits/stdc++.h>
using namespace std;
const int mx=1e5+5; 
int sus[mx]; 
int tot = 0; 
int main() {
    int n, t; cin >> n >> t;
    for(int i = 1; i <= n; i++) {
        int ind, q; cin >> ind >> q; 
        if(q == -1) {
            tot++; 
            sus[ind]--; 
        } 
        else {
            sus[q]++; 
        }
    }
    int ans=0; 
    for(int i = 1; i <= n; i++) {
        if(sus[i]+tot==t) {
            cout << i << " "; 
            ans++; 
        }
    }
    if(!ans) cout << "-1"; 
}
