int L = 1, R = N, ans = 0;
while(L<=R) {
    int mid = (L+R)/2; 
    if(arr[mid] < K) {
        ans = arr[mid]; 
        L = mid+1; 
    }
    else {
        R = mid-1; 
    }
}

