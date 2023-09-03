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

N,M=map(int, input().split())
if N*N < M:
    print(-1)
    exit()
sqrt_m = int(math.sqrt(M))
ans = float("inf")
for a in range(1,sqrt_m+10):
    if a > N:
        # 答えの範囲外
        break
    # a*b>=Mとなる、最小のbを得る
    b = (M+a-1)//a
    if b > N:
        # 答えの範囲外
        continue
    ans = min(a*b, ans)
print(ans)

