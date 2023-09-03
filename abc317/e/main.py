#!/usr/bin/env python3                                                                          
import sys
#input = lambda: sys.stdin.readline().rstrip()
input = sys.stdin.readline

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

H,W=map(int, input().split())
maze = [list(input()) for h in range(H)] # maze(###.###) のようなスペースなしの2次元配列で受け取り

block_s = set()
upper_s = set()
lowwer_s = set()
left_s = set()
right_s = set()
start = 0
goal = 0
for jj in range(H):
    for ii in range(W):
        if maze[jj][ii] == "S":
            start = (jj,ii)
            maze[jj][ii] = "."
        if maze[jj][ii] == "G":
            goal = (jj,ii)
            maze[jj][ii] = "."
        if maze[jj][ii] == "<":
            left_s.add(jj*W+ii)
            block_s.add(jj*W+ii)
        if maze[jj][ii] == ">":
            right_s.add(jj*W+ii)
            block_s.add(jj*W+ii)
        if maze[jj][ii] == "^":
            upper_s.add(jj*W+ii)
            block_s.add(jj*W+ii)
        if maze[jj][ii] == "v":
            lowwer_s.add(jj*W+ii)
            block_s.add(jj*W+ii)
        if maze[jj][ii] == "#":
            block_s.add(jj*W+ii)
#error(upper_s)
#error(lowwer_s)
#error(left_s)
#error(right_s)
#error(start,goal)

# upper_s
#error("--upper--")
for v in upper_s:
#    error(jj,ii)
    jj = v//W
    ii = v%W
    for kk in range(1,H):
#        error("add",(jj-kk,ii),kk)
        if jj-kk < 0 or maze[jj-kk][ii] != ".":
            break
        block_s.add((jj-kk)*W+ii)

# lowwer_s
#error("--lowwer--")
for v in lowwer_s:
#    error(jj,ii)
    jj = v//W
    ii = v%W
    for kk in range(1,H):
        if jj+kk >= H or maze[jj+kk][ii] != ".":
            break
        block_s.add((jj+kk)*W+ii)
# left_s
#error("--left--")
for v in left_s:
#    error(jj,ii)
    jj = v//W
    ii = v%W
    for kk in range(1,W):
#        error(ii-kk)
        if ii-kk < 0 or maze[jj][ii-kk] != ".":
            break
        block_s.add(jj*W+ii-kk)
# right_s
#error("--right--")
for v in right_s:
    jj = v//W
    ii = v%W
#    error(jj,ii)
    for kk in range(1,W):
        if ii+kk >= W or maze[jj][ii+kk] != ".":
            break
        block_s.add(jj*W+ii+kk)

# 幅優先探索
# (gh:グラフ)
# s: 初めの頂点番号
# n: 頂点数
# sから全頂点への距離を求める
# return
#  depth: 距離(list) もし辿り着けない頂点がある場合は-1をいれる
#  pre:   探索前の頂点番号(list)
def bfs(syx, n):
    que = deque()
    sidx = syx
    que.append(sidx)
    depth = [-1]*(n+1)
    depth[sidx] = 0
    while que:
        cidx = que.popleft()
        crr_y = cidx//W
        crr_x = cidx%W
        for dpos in dpos4:
            ny = crr_y + dpos[0]
            nx = crr_x + dpos[1]
            nidx = nx + ny*W
            if not (0<=ny<H and 0<=nx<W):
                continue
            if ny*W+nx in block_s:
                continue
            if maze[ny][nx] != ".":
                continue
            if depth[nidx] != -1:
                continue
            depth[nidx] = depth[cidx]+1
            que.append(nidx)
    return depth

d = bfs(start[1]+start[0]*W, H*W)
#error(d)
gidx = goal[1]+goal[0]*W
print(d[gidx])
