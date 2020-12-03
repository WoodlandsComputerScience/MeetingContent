#include <bits/stdc++.h>
using namespace std;
stack<int> st; 
int main() {
    int n; cin >> n; 
    for(int i=0;i<n;i++) {
        int num; cin >> num;
        if(num!=0) {
            st.push(num);
        } else {
            st.pop(); 
        }
    }
    int sum=0; 
    while(!st.empty()) {
        sum+=st.top();
        st.pop(); 
    }
    cout << sum; 
}

