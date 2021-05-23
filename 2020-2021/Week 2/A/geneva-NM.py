n=int(input())
m=int(input())
arr=[[0 for i in range(m+1)]for j in range(n+1)]
for i in range(n):
    for j in range(m):
        ele = int(input())
        arr[i][j] = ele

