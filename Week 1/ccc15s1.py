n=int(input())
st=[]
for i in range(n):
    num=int(input())
    if(num!=0):
        st.append(num)
    else:
        st.pop()
print(sum(st))
