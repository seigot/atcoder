#!/usr/bin/env python3                                                                          
import sys
input = sys.stdin.readline # 文字列Sの場合は最後に"¥n"が付くので注意
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
q=[]
for ii in range(Q):
    l = list(map(int, input().split()))
    q.append(l)

gh = defaultdict(set)
ans = N
for ii in range(Q):
    if q[ii][0] == 1:
        # union
        u = q[ii][1]
        v = q[ii][2]
        u -= 1  # 0-indexの場合/1-indexの場合は不要
        v -= 1  # 0-indexの場合/1-indexの場合は不要
        # u
        if len(gh[u]) == 0:
            ans -= 1
        gh[u].add(v)
        # v
        if len(gh[v]) == 0:
            ans -= 1
        gh[v].add(u)
    if q[ii][0] == 2:
        # delete
        v = q[ii][1]
        v -= 1  # 0-indexの場合/1-indexの場合は不要
        for g in gh[v]:
            gh[g].discard(v)
            if len(gh[g]) == 0:
                ans += 1
        if len(gh[v]) != 0:
            gh[v].clear()
            ans += 1
    print(ans)
