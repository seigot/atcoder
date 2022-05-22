import sys
input = lambda: sys.stdin.readline().rstrip()
INF=float('INF')

def addS(a):
    if a<=W:S.add(a)


N,W=map(int,input().split())
A=list(map(int, input().split()))

while len(A)<=3:
    A.append(INF)
    N+=1

S=set()
for i in range(N-2):
    addS(A[i])
    for j in range(i+1,N-1):
        addS(A[i]+A[j])
        addS(A[j])
        for k in range(j+1,N):
            addS(A[k])
            addS(A[i]+A[k])
            addS(A[j]+A[k])
            addS(A[i]+A[j]+A[k])
print(len(S))
