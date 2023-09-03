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

N,M,K=map(int, input().split())
gh = [[] for _ in range(N)] 
for ii in range(M):
    u,v=map(int, input().split())
    u -= 1  # 0-indexの場合/1-indexの場合は不要
    v -= 1  # 0-indexの場合/1-indexの場合は不要
    gh[u].append(v)
    gh[v].append(u)
PH=[list(map(int, input().split())) for k in range(K)]

# 幅優先探索
# (gh:グラフ)
# s: 初めの頂点番号
# n: 頂点数
# sから全頂点への距離を求める
# return
#  depth: 距離(list) もし辿り着けない頂点がある場合は-1をいれる
#  pre:   探索前の頂点番号(list)
hp = [-1]*(N)
def bfs(s, h):
    que = deque()
    que.append((s,h))
#    if h < hp[s]:
#        return
    while que:
        crr,crr_h = que.popleft()
        if crr_h == 0:
            continue
        for nxt in gh[crr]:
#            if hp[nxt] == -1:
            if hp[nxt] < crr_h - 1:
                hp[nxt] = crr_h - 1
                que.append((nxt,crr_h - 1))
#              if crr_h - 1 > 0:
#                   que.append((nxt,crr_h - 1))


# init
for ii in range(K):
    p = PH[ii][0]-1
    h = PH[ii][1]
    hp[p] = h

# 探索
_PH = sorted(PH, key=lambda x:(x[1]),reverse=True)
for ii in range(K):
    p = _PH[ii][0]-1
    h = _PH[ii][1]
    error(p,h)
    bfs(p, h)

ans = []
for ii in range(N):
    if hp[ii] == -1:
        continue
    ans.append(ii+1)
print(len(ans))
print(*ans)