# 三次元累積和
N=int(input())
XYZ = [[] for i in range(N)]
for i in range(N):
    for j in range(N):
        l = list(map(int,input().split()))
        XYZ[i].append(l)
for j in range(N):
    for k in range(N):
        for i in range(1,N):
            XYZ[i][j][k] += XYZ[i-1][j][k]
for i in range(N):
    for k in range(N):
        for j in range(1,N):
            XYZ[i][j][k] += XYZ[i][j-1][k]
for i in range(N):
    for j in range(N):
        for k in range(1,N):
            XYZ[i][j][k] += XYZ[i][j][k-1]
error(XYZ)

# https://atcoder.jp/contests/abc366/submissions/56545220
Q=int(input())
for ii in range(Q):
    ABC=list(map(int, input().split()))
    error(ABC)
    Xl = ABC[0] - 1
    Xr = ABC[1] - 1
    Yl = ABC[2] - 1
    Yr = ABC[3] - 1
    Zl = ABC[4] - 1
    Zr = ABC[5] - 1
    v = XYZ[Xr][Yr][Zr]
    if Zl >= 1: # 1
        v -= XYZ[Xr][Yr][Zl-1]
    if Yl >= 1: # 2
        v -= XYZ[Xr][Yl-1][Zr]
    if Xl >= 1: # 3
        v -= XYZ[Xl-1][Yr][Zr]
    if Yl >= 1 and Zl >= 1: # 4
        v += XYZ[Xr][Yl-1][Zl-1]
    if Xl >= 1 and Zl >= 1: # 5
        v += XYZ[Xl-1][Yr][Zl-1]
    if Xl >= 1 and Yl >= 1: # 6
        v += XYZ[Xl-1][Yl-1][Zr] # 7
    if Xl >= 1 and Yl >= 1 and Zl >= 1:
        v -= XYZ[Xl-1][Yl-1][Zl-1]
    print(v)
