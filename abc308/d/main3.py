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

H,W=map(int, input().split())
maze = [list(input()) for h in range(H)]
snuke = "snuke"
#error(snuke)

# 幅優先探索(2次元座標を座標圧縮して探索する)
# s:始点座標(座標圧縮済)
# n:座標の数(width*height)
# mat:二次元座標
# return: depth
def bfs(s, n, mat, width, height):
    que = deque([(s,0)])
    INF = 10**15
    depth = [INF]*(n)
    pre = [-1]*(n)
    depth[s] = 0
    while que:
        crr,step = que.popleft()
        y, x  = crr//width, crr % width
        for dx, dy in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            if mat[ny][nx] != snuke[(step+1)%5]:
                continue
            if (ny,nx) == (height-1,width-1):
                print("Yes")
                exit()
            nxt = ny*width+nx
            if depth[nxt] == INF:
                # 未探索
                depth[nxt] = depth[crr]+1
                pre[nxt] = crr
                que.append((nxt,step+1))
    return depth

# 全頂点で探索
if maze[0][0] == "s":
    bfs(0, W*H, maze, W, H)
print("No")
