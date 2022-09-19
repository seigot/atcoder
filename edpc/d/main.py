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

N,W=map(int, input().split())

wv = []
wv.append((0,0))
for ii in range(N):
    w, v = map(int, input().split())
    wv.append((w,v))

# dp[i][j]
#    : i番目までのお菓子で、重さがj以下となるものの中での価値の最大値
dp = [[0]*(W+1) for ii in range(N+1)]

# 探索
# お菓子の番号
for ii in range(1,N+1):
    # 重さ
    for jj in range(1, W+1):
        if jj-wv[ii][0] >= 0:
            dp[ii][jj] = max(
                dp[ii-1][jj],                                   # 何も選択しない場合
                dp[ii-1][jj-wv[ii][0]] + wv[ii][1]          # 該当(ii)のお菓子を選択する場合
            )
        else:
            dp[ii][jj] = dp[ii-1][jj]

#print(dp)
ans = max(dp[N])
print(ans)
