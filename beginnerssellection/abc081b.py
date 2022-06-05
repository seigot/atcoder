N = int(input())
A=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An

cnt = 0
while True:
    oddflag = False
    for ii in range(len(A)):
        val = A[ii]
        if val%2 == 0:
            A[ii] = A[ii]//2
        else:
            oddflag = True
    if oddflag == True:
        break
    cnt += 1
print(cnt)
