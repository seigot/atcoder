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
HW=[list(map(int, input().split())) for h in range(H)] # 1 2 3 4 のようなスペースありの2次元配列を受け取り, HW[ty][tx]
#print(HW)

for jj in range(H):
    l = HW[jj]
    ans = []
    for ii in l:
        if ii == 0:
            c = "."
        else:
            c = chr(ord("A") + ii - 1)
        ans.append(c)
    print(*ans, sep="")
