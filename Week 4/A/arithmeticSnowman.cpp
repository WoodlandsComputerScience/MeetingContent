#include <bits/stdc++.h>
using namespace std;
const int mx=3005; 
int n, arr[mx], ans=INT_MIN;
int main() {
    cin >> n; 
    for(int i = 1; i <= n; ++i) cin >> arr[i]; 
    sort(arr,arr+n+1); 
    for(int i = 1; i <= n; ++i) {
        for(int j = i+1; j <= n; ++j) {
            int found = 0;
            int l = j+1, r = n; 
            while(l<=r) {
                int mid = (l+r)/2; 
                if(arr[mid] - arr[j] == arr[j] - arr[i]) {
                    found = mid;
                    break; 
                }
                else if (arr[mid]-arr[j] > arr[j]-arr[i]) r = mid - 1;
                else l = mid + 1;
            }
            if(found) ans = max(ans, arr[i]+arr[j]+arr[found]); 
        }
    }
    cout << ans << "\n";
}
