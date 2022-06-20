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

R, C = map(int, input().split())
l = []
for ii in range(2):
    ll = list(map(int, input().split()))
    l.append(ll)
print(l[R-1][C-1])
