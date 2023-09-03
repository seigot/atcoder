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


def check_takcode(jj,ii):
    # (jj,ii)を基準に判定する
    # 左上#
    # 右下#
    for ty in range(3):
        for tx in range(3):
            if maze[jj+ty][ii+tx] != "#":
                return False
            if maze[jj+8-ty][ii+8-tx] != "#":
                return False
    # 左上.
    for ty in range(4):
        if maze[jj+ty][ii+3] != ".": return False
    for tx in range(4):
        if maze[jj+3][ii+tx] != ".": return False
    # 右下.
    for ty in range(4):
        if maze[jj+8-ty][ii+8-3] != ".": return False
    for tx in range(4):
        if maze[jj+8-3][ii+8-tx] != ".": return False
    return True

# 全探索
ans = []
for jj in range(N-8):
    for ii in range(M-8):
        error(jj,ii)
        if check_takcode(jj,ii) == True:
            ans.append((jj,ii))

if len(ans) == 0:
    exit()
for a in ans:
    print(a[0]+1,a[1]+1)