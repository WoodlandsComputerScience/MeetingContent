import sys
l=1
r=2000000000
while(l<=r):
    mid=(l+r)//2
    print(mid)
    sys.stdout.flush()
    s=input()
    if(s=="SINKS"): l = mid + 1
    elif(s == "FLOATS"): r = mid - 1
    else:break
