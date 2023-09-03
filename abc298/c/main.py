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
dpos4cross = ((1, 1), (1, -1), (-1, 1), (-1, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
def invmod(a):
    return pow(a,-1,MOD)
INF = float("inf")
MINF = -float("inf")

N=int(input())
Q=int(input())
box = defaultdict(list)
num = defaultdict(set)

for ii in range(Q):
    q=list(map(int, input().split()))
    if q[0] == 1:
        i = q[1]
        j = q[2]
        box[j-1].append(i)
        num[i-1].add(j)
    if q[0] == 2:
        i = q[1]
        print(*sorted(box[i-1]))
    if q[0] == 3:
        i = q[1]
        print(*sorted(num[i-1]))
