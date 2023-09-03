#!/usr/bin/env python3                                                                          
import sys
#input = sys.stdin
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

H,W=map(int, input().split())
maze = [list(input()) for h in range(H)]
error(maze)

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
    que.append((0,0,0))
    max_depth = 0
    visited = set()
    while que:
        crr = que.popleft()
        tx = crr[0]
        ty = crr[1]
        depth = crr[2]
        for nxt in dpos2:
            nx = tx + nxt[0] # dx
            ny = ty + nxt[1] # dy
            error(nx,ny)
            if (0 <= nx < W) and (0 <= ny < H):
                pass
            else:
                max_depth = max(max_depth,depth)
                continue
            error()
            if maze[ny][nx] == "#":
                # 壁の場合は探索終了
                max_depth = max(max_depth,depth)
                continue
            if (nx,ny,depth+1) not in visited:
                que.append((nx,ny,depth+1))
                visited.add((nx,ny,depth+1))
    return max_depth

ans = bfs(0,H*W)
print(ans+1)
