#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N,X=map(int, input().split())
l = []
for ii in range(N):
    A,B=map(int, input().split())
    for _ in range(B):
        l.append(A)

# dp[i][j] i番目までの硬貨を使った時にj円払うことができるかどうか
NN = len(l)
dp = [[False]*(X+1) for _ in range(NN+1)]
dp[0][0] = True
for ii in range(1,NN+1):
    # ii番目
    tl = l[ii-1]
    for jj in range(X+1):
        dp[ii][jj] |= dp[ii-1][jj]
        if (jj - tl) >= 0:
            dp[ii][jj] |= dp[ii-1][jj-tl]
#    print(dp[ii])

print("Yes") if dp[NN][X] == True else print("No")

