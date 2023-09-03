#!/usr/bin/env python3                                                                          
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(4100000)
import math
import os
from inspect import currentframe
ONLINE_JUDGE = os.environ["HOME"] == "/home/contestant"
def error1(*args, end="\n"): # 変数のみ表示
    if ONLINE_JUDGE: return
    print("[stderr]", *args, end=end, file=sys.stderr)
def error(*args): # 変数の名前と値をまとめて表示
    if ONLINE_JUDGE: return
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print("[stderr]",' '.join([names.get(id(arg), '???') + ' = ' + repr(arg) for arg in args]), file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from math import gcd
from itertools import permutations,combinations
from copy import deepcopy
dpos2 = ((1, 0), (0, 1))
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos4cross = ((1, 1), (1, -1), (-1, 1), (-1, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
def invmod(a):
    return pow(a,-1,MOD)
INF = float("inf")
MINF = -float("inf")

N=int(input())
XY = [list(map(int,input().split())) for _ in range(N)]
error(N)
error(XY)

dp = [[0]*2 for _ in range(N+1)]
for ii in range(1,N+1):
    x = XY[ii-1][0]
    y = XY[ii-1][1]

    # 下げてもらう
    dp[ii][0] = dp[ii-1][0]
    dp[ii][1] = dp[ii-1][1]
    # 食べる
    if x == 0:
        dp[ii][0] = max(dp[ii][0],
                        dp[ii-1][0] + y,
                        dp[ii-1][1] + y)
    if x == 1:
        dp[ii][1] = max(dp[ii][1],
                        dp[ii-1][0] + y)
error(dp)
print(max(dp[N]))

