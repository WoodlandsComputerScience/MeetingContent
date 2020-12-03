n=int(input())
orig=[0] # 1-indexed, add element at start of array
for i in range(n):
    orig.append(int(input()))
PSA=[0]
for i in range(1, n+1):
    PSA.append(PSA[i-1] + orig[i]) 
for i in range(int(input())): # loop through each query
    a,b=map(int,input().split())
    a+=1 # add one since queries are 0-indexed 
    b+=1 # but PSA should be 1 indexed
    print(PSA[b]-PSA[a-1])
