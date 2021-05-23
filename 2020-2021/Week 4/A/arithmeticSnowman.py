n=int(input())
arr=[0]+list(map(int,input().split()))
ans=0
arr.sort()
for i in range(1,n):
    for j in range(i+1,n+1):
        l = j+1
        r = n
        found = 0
        while(l<=r):
            mid = (l+r)//2
            if(arr[mid] - arr[j] == arr[j] - arr[i]):
                found = mid
                break
            elif(arr[mid] - arr[j] > arr[j] - arr[i]):r = mid - 1 
            else:l=mid + 1
        if(found):ans=max(ans, arr[i]+arr[j]+arr[found])
print(ans)
