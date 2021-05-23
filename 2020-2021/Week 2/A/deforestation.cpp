#include <bits/stdc++.h>
using namespace std;
int orig[1000005], PSA[1000005], N, Q, a, b; 
int main() {
    cin >> N; 
    for(int i = 1; i <= N; i++) {
        cin >> orig[i]; 
    }
    for(int i = 1; i <= N; i++) {
        PSA[i] = PSA[i-1] + orig[i]; 
    }
    cin >> Q; 
    for(int i = 1; i <= Q; i++) {
        cin >> a >> b;
        a++; // add one since queries are 0-indexed 
        b++; 
        cout << PSA[b] - PSA[a-1] << "\n"; 
    }
}

