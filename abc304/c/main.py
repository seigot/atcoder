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

N,D=map(int, input().split())
XY = []
for ii in range(N):
    x,y=map(int, input().split())
    XY.append((x,y))

dist = [[INF]*(N) for _ in range(N)] # お互いの距離
for ii in range(N):
    for jj in range(N):
        d = ((XY[ii][0] - XY[jj][0])**2 + (XY[ii][1] - XY[jj][1])**2)**0.5
        dist[ii][jj] = d

# 幅優先探索
# (gh:グラフ)
# s: 初めの頂点番号
# n: 頂点数
# sから全頂点への距離を求める
# return
#  depth: 距離(list) もし辿り着けない頂点がある場合は-1をいれる
#  pre:   探索前の頂点番号(list)
def bfs(s, n):
    que = deque([s])
    depth = [-1]*(n)
    pre = [-1]*(n)
    depth[s] = 0
    while que:
        crr = que.popleft()
        for ii, nxt in enumerate(dist[crr]):
            if nxt > D or nxt == 0:
                # skip
                continue
            if depth[ii] == -1:
                # 未探索の場合は探索する
                depth[ii] = depth[crr]+1
                pre[ii] = crr
                que.append(ii)
    return depth, pre
d, _ = bfs(0, N)
for ii in d:
    if ii == -1:
        print("No")
    else:
        print("Yes")
