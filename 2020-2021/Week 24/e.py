for i in range(int(input())):
    n = int(input())
    if(n <= 3): 
        print(-1)
        continue 

    start = [n,n-1][n&1]
    for x in range(start, 4, -2): 
        print(x, end = " ")
    print(2, 4, end = " ")
    for x in range(1, n+1, 2):
        print(x, end = " ")
    print()
