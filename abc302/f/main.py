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

n,m = map(int,input().split())
a = []
s = []
# 集合N個
for i in range(n):
    a.append(int(input()))
    s.append(list(map(int,input().split())))

# 超頂点を利用して、同じ値を含む頂点に上手く移動する
graph = [[] for i in range(n+m+1)]
for i in range(n):
    # 各頂点Nに対して、Nに繋がっている辺を繋げる
    for j in range(a[i]):
        v = m+(i+1)  # 数字1~m,集合i~Nまでのグラフを作成する
        tx = s[i][j] # 数字
        graph[v].append(tx)
        graph[tx].append(v)

# 幅優先探索
# s: 初めの頂点番号
# n: 頂点数
# sから全頂点への距離を求める
# return
#  depth: 距離(list) もし辿り着けない頂点がある場合は-1をいれる
#  pre:   探索前の頂点番号(list)
def bfs(s, n):
    que = deque([s])
    depth = [-1]*(n+1)
    pre = [-1]*(n+1)
    depth[s] = 0
    while que:
        crr = que.popleft()
        error(que,crr)
        for nxt in graph[crr]:
            if depth[nxt] == -1:
                depth[nxt] = depth[crr]+1
                pre[nxt] = crr
                que.append(nxt)
    return depth, pre

d, _ = bfs(1, n+m+1)

ans = d[m]
if ans == -1:
    print(ans)
else:
    error(ans)
    # 数字-->集合-->数字、、のような探索方法なので-2して、集合-->集合の探索回数に戻してやる
    print((ans-2)//2)
