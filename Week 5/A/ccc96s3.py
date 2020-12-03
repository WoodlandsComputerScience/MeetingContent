def recur(s, ones, length): 
    # current string, 1s left, remaining characters
    if(length==0):print(s) # base case
    if(ones > 0):recur(s+'1',ones-1,length-1) 
    if(length > ones):recur(s+'0',ones,length-1)

for i in range(int(input())):
    n,k=map(int,input().split())
    print("The bit patterns are")
    recur("",k,n)
    print()
