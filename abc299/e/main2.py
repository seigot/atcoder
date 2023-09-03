#!/usr/bin/env python3                                                                          
import sys
input = sys.stdin.readline
sys.setrecursionlimit(4100000)
import math
import os
ONLINE_JUDGE = os.environ["HOME"] == "/home/contestant"
def error(*args, end="\n"):
    if not ONLINE_JUDGE: print("[stderr]", *args, end=end, file=sys.stderr)
#def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
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

N,M=map(int, input().split())
#uv=[list(map(int, input().split())) for h in range(M)]
gh = [[] for _ in range(N)] 
for ii in range(M):
    u,v=map(int, input().split())
    u -= 1  # 0-indexの場合/1-indexの場合は不要
    v -= 1  # 0-indexの場合/1-indexの場合は不要
    gh[u].append(v)
    gh[v].append(u)
K=int(input())
pd=[]
for ii in range(K):
    p,d=map(int, input().split())
    p -= 1  # 0-indexの場合/1-indexの場合は不要
    pd.append((p,d))

# 全頂点からの距離を求める
# 制約のある頂点から、それが成立するパターンを探索する

# 全頂点からの距離を求める
# bfs
def bfs(tx, d):
    dict = defaultdict(list)
    q = deque()
    q.append((tx,d))
    visited.add(tx)
    while q:
        tx,d = q.popleft()
        dict[d].append(tx)
#        error(tx,d)
        for dx in gh[tx]:
            if dx in visited:
                # already visited
                continue
            # not visited
            q.append((dx,d+1))
            visited.add(dx)
    return dict
dd = []
for ii in range(N):
    error("---")
    visited = set()
    dict = bfs(ii, 0)
    error(dict)
    dd.append(dict)
#error(dd)

# 制約のある頂点から、それが成立するパターンを探索する
error("---")
ansS=defaultdict(int)
for ii in range(len(pd)):
    p, d = pd[ii]
    print(dd[p])
    # 距離がdの頂点は黒(1)にしてみる、距離がd以内の頂点は全て白(0)にする
