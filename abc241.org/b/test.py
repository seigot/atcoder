N, _ = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#print(N, A, B)
ans="Yes"
for i in range(len(B)):

    b = B[i]
    flag = True
    for j in range(len(A)):
        if A[j] == b:
            A.pop(j)
            flag = False
            break

    if flag == True:
        ans = "No"

print(ans)
