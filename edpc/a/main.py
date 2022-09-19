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
h = list(map(int, input().split()))

# ii番目に着目した時のコストの最小値
dp = [0]*N
for ii in range(1, N):
    if ii == 1:
        dp[ii] = dp[ii-1] + abs(h[ii] - h[ii-1])
    else:
        # ii >= 2
        dp[ii] = min(
            dp[ii-1] + abs(h[ii] - h[ii-1]),
            dp[ii-2] + abs(h[ii] - h[ii-2])
        )

ans = dp[N-1]
print(ans)