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

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B

N = int(input())
T = 10**5
TXA = [[0]*5 for ii in range(T+2) ]
TMax = 0
for ii in range(N):
    T,X,A,=map(int, input().split())
    TXA[T][X] = A
    TMax = max(TMax, T)
#print(TXA)
#print(TMax)

# dp[i][j]: 時刻iの時に、jの位置にいる場合の最大値
dp = [ [-INF]*5 for ii in range(T+2)]
dp[0][0] = 0 # init
for ii in range(1,TMax+1):
    for jj in range(5):
        val = -INF
        if jj >= 1:
            val = max(dp[ii-1][jj-1], val)
        val = max(dp[ii-1][jj], val)
        if jj <= 3:
            val = max(dp[ii-1][jj+1], val)
        dp[ii][jj] = val

        # snukeくんを捕まえる
        val = TXA[ii][jj]
        dp[ii][jj] += val

#print(dp)
print(max(dp[TMax]))
