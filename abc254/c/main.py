N,K=map(int, input().split())
A=list(map(int, input().split()))

# sort用
l = [[] for _ in range(K)]
# 分配
for i in range(len(A)):
    ii = i%K
    l[ii].append(A[i])
# sort
for i in range(len(l)):
    l[i].sort()

# 元に戻す
ll=[]
for i in range(len(A)):
    ii = i%K
    jj = i//K
    val = l[ii][jj]
    ll.append(val)

for i in range(len(ll)-1):
    if ll[i] > ll[i+1]:
        print("No")
        exit()

#print(ll)
print("Yes")
