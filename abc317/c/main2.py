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
error(gh)
error(d)
#error(d[1][4])

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
    crr_length = 0
    visited_bit = 0
    que.append((s,visited_bit,crr_length)) # 現在の点、集合, 長さ
    max_length = 0
    mcost = [[0]*(2**(N+2)+1) for _ in range(N+1)]

    while que:
        crr = que.popleft()
        crr_n = crr[0]
        crr_visited_bit = crr[1]
        crr_length = crr[2]
#        error(crr_n,crr_visited,crr_visited_bit,crr_length)
        max_length = max(max_length, crr_length)

        for nxt_n in gh[crr_n]:
            nxt_length = int(crr_length) + int(d[crr_n][nxt_n])

            error(crr_n,nxt_n,crr_visited_bit,nxt_length)
            if nxt_length < mcost[nxt_n][crr_visited_bit]:
                 continue
            mcost[nxt_n][crr_visited_bit] = nxt_length
            nxt_visited_bit = crr_visited_bit
            for jj in range(1,N+1):
                if jj == nxt_n:
                    # 該当のビットがたっていなければ立てる
                    if (nxt_visited_bit // (2<<nxt_n)) % 2 == 0:
                        nxt_visited_bit += 2<<nxt_n
#            error(nxt_length,crr_length,d[crr_n][nxt_n],crr_n,nxt_n)
            que.append((nxt_n,nxt_visited_bit,nxt_length))

    return max_length

ans = 0
for ii in range(1,N+1):
    max_length = bfs(ii, N+1)
    ans = max(ans, max_length)

print(ans)
