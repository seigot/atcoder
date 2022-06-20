#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, Q = map(int,input().split())
A = list(map(int, input().split()))
A.sort()
#print(A)
# 累積和
commA = []
for ii in range(len(A)):
    if ii == 0:
        commA.append(A[ii])
    else:
        commA.append(commA[ii-1] + A[ii])
#print(commA)
# 5 3
# 6 11 2 5 5
# 5  X
# 20
# 0
for ii in range(Q):

    X = int(input())

    ans = 0
    leftSum = 0
    rightSum = 0

    # 境界を見つける
    idx = bisect_right(A, X)
    #print(idx) # 

    # 左側
    if idx > 0:
        leftSum = X * ((idx-1)+1) - commA[idx-1]
        #print(leftSum)
    # 右側
    if idx < len(A):
        if idx == 0:
            rightSum = (commA[len(A)-1]) - 0 - (X * (len(A)-(idx)))
        else:
            rightSum = (commA[len(A)-1] - commA[idx-1]) - (X * (len(A)-(idx)))
        #print(rightSum)
    print(leftSum + rightSum)
    #print("--")
