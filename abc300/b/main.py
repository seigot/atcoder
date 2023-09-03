#!/usr/bin/env python3                                                                          
import sys
input = sys.stdin.readline
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from math import gcd
from itertools import permutations,combinations
from copy import deepcopy
dpos2 = ((1, 0), (0, 1))
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

H,W=map(int, input().split())
mapA = [list(input()) for h in range(H)]
mapB = [list(input()) for h in range(H)]

# 移動量
for dy in range(H):
    for dx in range(W):
        # 全座標を比較
        chk = True
        for ty in range(H):
            for tx in range(W):
                if mapA[(ty+dy)%H][(tx+dx)%W] == mapB[ty][tx]:
                    continue
                chk = False
        if chk == True:
            print("Yes")
            exit(0)
print("No")