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

N,Q=map(int, input().split())
query=[list(map(int, input().split())) for q in range(Q)]
headl = [-1] * (N+1)
taill = [-1] * (N+1)
for ii in range(Q):
    q = query[ii]
    if q[0] == 1:
        x = q[1]
        y = q[2]
        taill[x] = y
        headl[y] = x
    if q[0] == 2:
        x = q[1]
        y = q[2]
        taill[x] = -1
        headl[y] = -1
    if q[0] == 3:
        x = q[1]
        # 先頭を求める
        tx = x
        while headl[tx] != -1:
            tx = headl[tx]
        # 先頭からの連結成分を求める
        ans = [tx]
        while taill[tx] != -1:
            tx = taill[tx]
            ans.append(tx)
        print(len(ans), *ans)
