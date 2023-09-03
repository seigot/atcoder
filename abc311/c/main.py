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

N=int(input())
# graph (N頂点M辺)
#N,M=map(int, input().split())
gh = [[] for _ in range(N+1)] 
l = list(map(int,input().split()))
for ii,v in enumerate(l):
    #u,v=map(int, input().split())
    #u -= 1  # 0-indexの場合/1-indexの場合は不要
    #v -= 1  # 0-indexの場合/1-indexの場合は不要
    gh[ii+1].append(v)
    #gh[v].append(u)
error(gh)

# 幅優先探索
# (gh:グラフ)
# s: 初めの頂点番号
# n: 頂点数
# sから全頂点への距離を求める
# return
#  depth: 距離(list) もし辿り着けない頂点がある場合は-1をいれる
#  pre:   探索前の頂点番号(list)

def bfs(s, n):
    que = deque()
    l = []
    l.append(s)
    que.append((s,l))
    depth = [-1]*(n+1)
    pre = [-1]*(n+1)
    depth[s] = 0
    visited = set()
    while que:
        p = que.popleft()
        crr = p[0]
        crrl = p[1]
        visited.add(crr)
        error(crr,crrl)
        for nxt in gh[crr]:
            if nxt == s:
                print(len(crrl))
                print(*crrl)
                exit()
            if nxt in visited:
                return depth, pre, nxt
            if depth[nxt] == -1:
                depth[nxt] = depth[crr]+1
                pre[nxt] = crr
                nxtl = crrl
                nxtl.append(nxt) 
                que.append((nxt,l))
    return depth, pre, -1

for ii in range(1,N+1):
    error("---ii", ii)
    d, _, v = bfs(ii, N)
    if v != -1:
        bfs(v, N)
