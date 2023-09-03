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

N,M=map(int, input().split())
maze = [list(input()) for h in range(N)]
error(maze)
wall_v = []
wall_h = []
visited = set()
# 縦横方向の壁検出
# 横
for jj in range(N):
    l = []
    for ii in range(M):
        if maze[jj][ii] == "#":
            l.append(ii)
    wall_h.append(l)
# 縦
for ii in range(M):
    l = []
    for jj in range(N):
        if maze[jj][ii] == "#":
            l.append(jj)
    wall_v.append(l)
error(wall_h)
error(wall_v)
#exit()


# 探索
# 幅優先探索
# (gh:グラフ)
# s: 初めの頂点番号
# n: 頂点数
# sから全頂点への距離を求める
# return
#  depth: 距離(list) もし辿り着けない頂点がある場合は-1をいれる
#  pre:   探索前の頂点番号(list)

ans = set()
visited = set()

def bfs(s, n):
    que = deque()
    que.append(s)
#    visited.add(s)
    ans = set()
    while que:
        crr = que.popleft()
        y = crr[0]
        x = crr[1]
        error("---",crr)
        # 上下左右探索候補
        gh = []
        # lowwer
        nyi = bisect_left(wall_v[x],y)
        ny = wall_v[x][nyi] - 1
        nx = x
        gh.append((ny,nx))
        # upper
        nyi = bisect_left(wall_v[x],y)
        ny = wall_v[x][nyi-1] + 1
        nx = x
        gh.append((ny,nx))
        # right
        ny = y
        nxi = bisect_left(wall_h[y],x)
        nx = wall_h[y][nxi] - 1
        gh.append((ny,nx))
        # left
        ny = y
        nxi = bisect_left(wall_h[y],x)
        nx = wall_h[y][nxi-1] + 1
        gh.append((ny,nx))
        error(gh)
        for nxt in gh:
            ny = nxt[0]
            nx = nxt[1]
            if (y,x,ny,nx) not in visited:
                # 未探索の場合は探索
                visited.add((y,x,ny,nx))
                visited.add((ny,nx,y,x))
                ans.add((y,x))
                ans.add((ny,nx))
                # update ans
                if y == ny and x > nx:
                    for ii in range(nx, x+1):
                        ans.add((y,ii))
                if y == ny and x < nx:
                    for ii in range(x, nx+1):
                        ans.add((y,ii))
                if y > ny and x == nx:
                    for jj in range(ny, y+1):
                        ans.add((jj,x))
                if y < ny and x == nx:
                    for jj in range(y, ny+1):
                        ans.add((jj,x))
                #ans += abs(x - nx) + abs(y - ny)
                error("next---", ans, (y,x), (ny,nx))
                que.append((ny,nx))
#        error(visited)
#        exit()
    return visited, ans

d, ans = bfs((1,1), N*M)
print(len(ans))

