n,t=map(int,input().split())
freq = [0 for i in range(n+1)] # we are making a frequency array, so we initialize all frequencies to 0
tot=0
for i in range(n):
    ind, q = map(int,input().split())
    if(q == -1):
        tot += 1
        freq[ind] -= 1
    else:
        freq[q] += 1
 
found = False
for i in range(1,n+1):
    if(freq[i] + tot == t):
        print(i, end = " ")
        found = True
if not (found):
    print("-1")
