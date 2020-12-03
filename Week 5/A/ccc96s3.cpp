#include <bits/stdc++.h>
using namespace std;
void recur(string s, int ones, int length) {
    // current string, 1s remaining, # of characters remaining
    if(length == 0) cout << s << "\n"; // base case 
    if(ones > 0) recur(s+'1',ones-1,length-1);
    if(length > ones) recur(s+'0',ones,length-1);
}
int main() {
    int t; cin >> t;
    while(t--) {
        int n, k; cin >> n >> k;
        string s="";
        cout << "The bit patterns are\n";
        recur(s,k,n);
        cout << "\n"; 
    } 
}


