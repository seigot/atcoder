#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, K = map(int, input().split())
A = list(map(int, input().split()))
for ii in range(len(A)):
    A[ii] -= 1
coord = []
for ii in range(N):
    x, y = map(int, input().split())
    coord.append([x,y])

# 明かりを持っているかどうか
d = defaultdict(int)
for ii in range(N):
    d[ii] = 0
for ii in range(len(A)):
    d[A[ii]] = 1
#print(d)

# 全探索
ans_dist = 0
for ii in range(N):
    # 明かりを持っていない人
    dist = INF
    if d[ii] == 0:
        tx, ty = coord[ii]
        # 明かりを持っている人との最短距離を求める
        for jj in range(len(A)):
            dx, dy = coord[A[jj]]
            tmp_dist = ((tx - dx)**2 + (ty - dy)**2)**0.5
            dist = min(dist, tmp_dist)
        ans_dist = max(ans_dist, dist)
print(ans_dist)