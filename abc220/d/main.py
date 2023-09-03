#!/usr/bin/env python3                                                                          
import sys
input = sys.stdin.readline
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
A=deque(map(int, input().split()))

# dp[i][j]: i回操作を行った時に、答えがjになる数
dp = [0 for i in range(10)]
dp[A[0]] = 1
# 配るdp
for ii in range(1,N):
    a = A[ii]
    nxt = [0 for i in range(10)]
    for jj in range(10): 
        # 着目している数値と答えを計算した際に答えがjjになる数
        f = (jj+a)%10
        g = (jj*a)%10
        nxt[f] += dp[jj]
#        nxt[f] %= MOD
        nxt[g] += dp[jj]
#        nxt[g] %= MOD
    dp = nxt

error(dp)
for jj in range(10):
    print(dp[jj]%MOD)
