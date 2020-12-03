#include <bits/stdc++.h>
using namespace std;
set<int> nums; 
int main() {
    int n; cin >> n; 
    for(int i=0;i<n;i++){
        int num; cin >> num;
        nums.insert(num); 
    }
    cout << nums.size(); 
}

