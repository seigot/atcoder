n,a,b=map(int,input().split())
p,q,r,s=map(int,input().split())
 
for i in range(p,q+1):
    st=[]
    high=b+abs(a-i)
    low=b-abs(a-i)
 
    for j in range(r,s+1):
        
        
        if j==high or j==low:
            st.append("#")
        else:
            st.append(".")
    
    print("".join(st))
