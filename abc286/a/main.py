#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N,P,Q,R,S=map(int, input().split())
A=list(map(int, input().split()))
B=[]
P -= 1
Q -= 1
R -= 1
S -= 1

#B = A[0:P] + A[P:Q+1] + A[Q+1:R] + A[R:S+1] + A[S+1:]
B = A[0:P] + A[R:S+1] + A[Q+1:R] + A[P:Q+1] + A[S+1:]
print(*B)

