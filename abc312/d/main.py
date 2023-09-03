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
from heapq import heappop, heappush, heapify
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

S=input()

#dp[i][j] i番目の?の文字をjと置いた時にあと")"が何個必要かの数
N = len(S)
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1
ans = 0
for ii in range(N):
    # 状態遷移
    for jj in range(N):
        s = S[ii]
        error(s)
        if s == "(":
            # "("が来た場合は状態遷移
            # )が1個必要な未来が加わる
            dp[ii+1][jj+1] += dp[ii][jj]
        if s == ")":
            # 先頭に")"が来た場合は対象外
            # )が必要な未来を更新する
            if jj != 0:
                dp[ii+1][jj-1] += dp[ii][jj]
        if s == "?":
            # sが"("の場合と")"の場合の２パターンの未来を更新する
            if jj != 0:
                dp[ii+1][jj-1] += dp[ii][jj]
            dp[ii+1][jj+1] += dp[ii][jj]
        dp[ii+1][jj+1] %= MOD

ans = dp[-1][0]
print(ans%MOD)
