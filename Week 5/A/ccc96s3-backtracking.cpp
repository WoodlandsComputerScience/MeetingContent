#include <bits/stdc++.h>
using namespace std;
int arr[100], ans, k, n; 
void recur(int curr, int idx) {
    if(idx == n) {
        if(curr < k) ans = max(ans, curr); 
        return; 
    }
    recur(curr*arr[idx],idx+1); 
    recur(curr+arr[idx],idx+1);
    recur(curr-arr[idx],idx+1);
}

int main() {
    cin >> n >> k; 
    for(int i = 0; i < n; i++) cin >> arr[i]; 
    recur(arr[0], 1); 
    cout << ans << "\n"; 
}


