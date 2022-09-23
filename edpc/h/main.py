#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
MOD2 = 10**9+7
INF = float("inf")
MINF = -float("inf")

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
H,W=map(int, input().split())
a = []
for ii in range(H):
    s = input()
    a.append(s)

# init dp
dp = [[0]*(W+1) for ii in range(H+1)]
dp[H-1][W-1] = 1

# (H,W)から逆順に通りをカウントする
# "#"である場合は壁なのでカウントから外す
for jj in range(H-1, -1, -1):
    for ii in range(W-1, -1, -1):
        #print(jj,ii)

        # 右下の場合
        if ii == W-1 and jj == H-1:
            continue

        # 更新
        if ii+1 < W:
            dp[jj][ii] += dp[jj][ii+1]
        if jj+1 < H:
            dp[jj][ii] += dp[jj+1][ii]

        # 壁の場合
        if a[jj][ii] == "#":
            dp[jj][ii] = 0

#print(dp)
print(dp[0][0]%MOD2)
