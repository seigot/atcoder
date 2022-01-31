h,w=map(int,input().split())
A=[list(map(int,input().split())) for i in range(h)]
for j in range(w):
    for i in range(h):
        print(A[i][j], end=' ')
    print('')
