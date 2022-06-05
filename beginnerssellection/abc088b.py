N = int(input())
A=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An

A.sort(reverse=True)

AA = []
BB = []

#print(A)
for ii in range(len(A)):
    if ii%2 == 0:
        AA.append(A[ii])
    else:
        BB.append(A[ii])

#print(AA)
ans = sum(AA) - sum(BB)
print(ans)

