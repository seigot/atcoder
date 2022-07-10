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

N = int(input())
A = []
for ii in range(N):
    l = input()
    A.append(list(l))

dy = [-1, -1, 0, 1, 1,  1 , 0  , -1]
dx = [ 0,  1, 1, 1, 0, -1 , -1 , -1]
ans = []
for ii in range(N):
    for jj in range(N):
        for dd in range(8):
            # 8方向に探索
            str = ""
            for kk in range(N):
                y = (ii + dy[dd]*kk) % N
                x = (jj + dx[dd]*kk) % N
                str = str + A[y][x]
            ans.append(int(str))
print(max(ans))


