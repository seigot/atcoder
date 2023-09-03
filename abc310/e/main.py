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

import sys
sys.setrecursionlimit(5*10**5)
input = sys.stdin.readline
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
from math import gcd


n = int(input())
s = input()
dp = [[0]*2 for i in range(n+1)] # i番目の数がnumだった場合の場合の数
ans = 0
for i in range(1, n+1):
    num=int(s[i-1])
    dp[i][num] += 1

    if num == 1:
        # 1の場合は、
        # - 1つ前が1の場合は0となる場合の数が増える
        # - 1つ前が0の場合は1となる場合の数が増える
        dp[i][0] += dp[i-1][1]
        dp[i][1] += dp[i-1][0]
    else:
        # 0の場合は、
        # - 1つ前が0の場合は1となる場合の数が増える
        # - 1つ前が0の場合も1となる場合の数が増える
        dp[i][1] += dp[i-1][0]
        dp[i][1] += dp[i-1][1]
#    ans += dp[i][1]

# 1となる場合の数を加算する
for ii in range(1, n+1):
    ans += dp[ii][1]
print(ans)


