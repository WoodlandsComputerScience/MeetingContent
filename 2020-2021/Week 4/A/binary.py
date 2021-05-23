L = 1 
R = N
ans = 0 
while(L<=R): # while there are still subarrays
    mid = (L+R)//2 # rounded down 
    if(arr[mid]<K):
        ans = arr[mid]
        L = mid + 1 
    else:
        R = mid - 1
