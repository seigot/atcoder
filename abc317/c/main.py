#!/usr/bin/env python3                                                                          
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(4100000)
import math
import os
from inspect import currentframe
ONLINE_JUDGE = os.environ["HOME"] != "/Users/seigo"
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

N,M=map(int, input().split())
ABC = [list(map(int,input().split())) for h in range(M)]
d = defaultdict(defaultdict)
gh = [[] for _ in range(N+1)] 
error(ABC)
for abc in ABC:
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    gh[a].append(b)
    gh[b].append(a)
    d[a][b] = c
    d[b][a] = c

# 幅優先探索
# (gh:グラフ)
# s: 初めの頂点番号
# n: 頂点数
# sから全頂点への距離を求める
# return
#  depth: 距離(list) もし辿り着けない頂点がある場合は-1をいれる
#  pre:   探索前の頂点番号(list)
# 深さ幅優先探索
# queueとvisitedのadd/discardを組み合わせて実装する
from collections import deque
visited = set()

def dfs(n):
    max_cost = 0
    q = deque()
    q.appendleft((~n,0))
    q.appendleft((n,0))
    while q:
        # visitedへ追加
        v = q.popleft()
        tx = v[0]
        crr_cost = v[1]
        visited.add(tx)
        if tx >= 0:
            error(tx,crr_cost)
            max_cost = max(max_cost, crr_cost)
            for dx in gh[tx]:
                if dx in visited:
                    # already visited
                    continue
                # not visited
                nxt_cost = crr_cost + d[tx][dx]
                error(tx,crr_cost,nxt_cost,d[tx][dx])
                q.appendleft((~dx,0))
                q.appendleft((dx,nxt_cost))
        else:
            # visitedから削除
            tx = ~tx
            visited.discard(tx)
    return max_cost

# 全頂点で探索
ans = 0
for ii in range(1,N+1):
    max_length = dfs(ii)
    ans = max(ans, max_length)
print(ans)

