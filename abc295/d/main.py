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

S=input()

res = defaultdict(int)
res[0] = 1 # 何もない場合
bit = 0
for i in range(len(S)):
    if S[i] == "\n":
        continue
    bit ^= 1<<int(S[i])
    res[bit] += 1
  
ans = 0
for v in res.keys():
    cnt = res[v]
    ans += cnt*(cnt-1)//2
print(ans)