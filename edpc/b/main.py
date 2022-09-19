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
N,K=map(int, input().split())
h = list(map(int, input().split()))

# ii番目に着目した時のコストの最小値
dp = [INF]*N
dp[0] = 0
for ii in range(1, N):

    ## (ii - jj)番目から飛んでくることを考える
    for jj in range(1, K+1):
        if ii-jj >= 0:
            dp[ii] = min(
                dp[ii],
                dp[ii-jj] + abs(h[ii] - h[ii-jj])
            )

ans = dp[N-1]
print(ans)