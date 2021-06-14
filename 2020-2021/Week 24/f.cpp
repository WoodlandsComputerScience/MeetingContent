#include <bits/stdc++.h>
using namespace std;
const int MM = 1e7; 
int t, x;
int d[MM+20], ans[MM+20];

int main() {
	for(int i=1;i<MM-1;i++) 
		for(int j=i;j<MM;j+=i) 
			d[j]+=i; 
    
	for(int i=1;i<MM-1;i++) {
		if(d[i]>MM || ans[d[i]]) continue; 
		ans[d[i]] = i; 
	}

	for(cin>>t;t--;) {
		cin >> x; 
		if(!ans[x]) cout << -1 << '\n'; 
		else cout << ans[x] << '\n'; 
	}
}
