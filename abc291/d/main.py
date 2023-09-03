#!/usr/bin/env python3                                                                          
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from math import gcd
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N=int(input())
AB=[list(map(int,input().split())) for i in range(N)]

# dp[N][i]: N枚並べた時、N番目がi(i=0,1)である場合に条件を満たす数
#dp = [[0]*(N+1) for _ in range(N+1)]
#dp[0][0] = 1
#dp[0][1] = 1
dp = [[0,0] for i in range(N)]
dp[0] = [1,1]

for ii in range(1, N):
    # 表裏
    for jj in range(2):
        for kk in range(2):
            if AB[ii][jj] != AB[ii-1][kk]:
                dp[ii][jj] += dp[ii-1][kk]
            dp[ii][jj] %= MOD

print(sum(dp[N-1])%MOD)
