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
st=[list(input().split()) for n in range(N)]

# graph (N頂点M辺)
gh = defaultdict(list)
for ii in range(N):
    s,t=st[ii]
    gh[s].append(t)

# bfs
#visited_all = set()
resultd = defaultdict(int)
def bfs(k):
#    if k in visited_all:
#        return
    if resultd[k] != 0:
        return
    q = deque()
    q.append(k)
    visited = set()
    visited.add(k)
    while q:
        tx = q.popleft()
        if tx not in keys:
            break
        if resultd[tx] != 0:
            break
        for dx in gh[tx]:
            if dx in visited:
                # already visited
                print("No")
                exit(0)
            # not visited
            q.append(dx)
            visited.add(dx)
    resultd[k] = 1
#    visited_all.union(visited)

keys = gh.keys()
for key in keys:
    bfs(key)
print("Yes")