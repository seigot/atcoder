n,a,b=map(int,input().split())
p,q,r,s=map(int,input().split())

print(n,a,b,p,q,r,s)

k_min = max(1-a,1-b)
k_max = min(n-a,n-b)
k2_min = max(1-a,b-n)
k2_max = min(1-a,b-n)
#print(k_min,k_max,k2_min,k2_max)

for ii in range(p,q+1):
    st = []
    for jj in range(r,s+1):
        
        if ii+jj==a+b or ii-jj==a-b:
            st.append("#")
        else:
            st.append(".")

    #for kk in st:
    #    print(kk)
    print("".join(st))
