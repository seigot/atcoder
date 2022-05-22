N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

x=[]

for i in range(N):
    if A[i]==max(A):
        x.append(i+1)

y=False
        
for j in range(len(x)):
    if x[j] in B:
        y=True

if y==True:
    print("Yes")
else:
    print("No")
