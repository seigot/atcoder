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

# graph (N頂点M辺)
N,M=map(int, input().split())
gh = [[] for _ in range(N+1)] 
p = list(map(int, input().split()))
XY=[list(map(int, input().split())) for _ in range(M)]
error(p)
error(XY)

for cur,parent in enumerate(p):
    u = cur+2
    v = parent
#    gh[u].append(v)
    gh[v].append(u)
error(gh)

# 保険の最大値
vmaxd = defaultdict(int)
for x,y in XY:
    if y+1 > vmaxd[x]:
        vmaxd[x] = y+1
error(vmaxd)

# MAXの値を持ってBFS

# 幅優先探索
# (gh:グラフ)
# s: 初めの頂点番号
# n: 頂点数
# sから全頂点への距離を求める
# return
#  depth: 距離(list) もし辿り着けない頂点がある場合は-1をいれる
#  pre:   探索前の頂点番号(list)
insurance = set()
def bfs(s, n):
    que = deque()
    crr_insurance = vmaxd[s]
    if crr_insurance > 0:
        insurance.add(s)
    que.append((s,crr_insurance))
    depth = [-1]*(n+1)
    pre = [-1]*(n+1)
    depth[s] = 0
    while que:
        crr, crr_insurance = que.popleft()
        error(crr,crr_insurance)
        if crr_insurance > 0:
            insurance.add(crr)
        crr_insurance -= 1
        for nxt in gh[crr]:
            if depth[nxt] == -1:
                depth[nxt] = depth[crr]+1
                pre[nxt] = crr
                nxt_insurance = crr_insurance
                if vmaxd[nxt] > nxt_insurance:
                    nxt_insurance = vmaxd[nxt]
                que.append((nxt,nxt_insurance))
    return depth, pre

d, _ = bfs(1, N+1)
error(insurance)
print(len(insurance))