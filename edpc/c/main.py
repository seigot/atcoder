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
abc = []
abc.append((0,0,0))                  # 0日目
for ii in range(N):
    a,b,c=map(int, input().split())
    abc.append((a,b,c))              # 1日目以降


# dp[ii][jj] ii日目にjjを選択する場合のMAXの幸福度
# jj 0: umi
# jj 1: yama
# jj 2: HomeWork
dp = [[0]*3 for ii in range(N+1)]

for ii in range(1, N+1):             # 1日目〜N日目までをカウント
    for jj in range(3):              # 3種類
        idx1 = (jj+1)%3
        idx2 = (jj+2)%3
        dp[ii][jj] = max(            # 前日の別のやつをカウントする
            dp[ii-1][idx1] + abc[ii][idx1],
            dp[ii-1][idx2] + abc[ii][idx2]
        )
ans = max(dp[N])
print(ans)
