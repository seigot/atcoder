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
A=list(map(int, input().split()))

# dp[j]       初めにj個の石が存在した時に、先手が取ることのできる最大の個数
#             先手番がAi個の石を取ったとき、最終的に取れる石の個数は、
#             Ai+「石がn−Ai個残っている状態からゲームを始めたとき、
#                  後手が取ることのできる石の個数」のMAX
#             すなわち、 max( Ai + ((ii-Ai) - dp[ii-Ai]) )

dp = [0]*(N+1)

for ii in range(0, N+1):
    for jj in range(0, K):
        if ii-A[jj] >= 0:
            dp[ii] = max(dp[ii], A[jj] + ((ii-A[jj]) - dp[ii-A[jj]]))

#print(dp)
print(dp[N])