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

N,X,Y,Z=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

# 合格したフラグ
passed = [0] * N

# math
_A = [ [-A[i], i] for i in range(N) if passed[i] == 0]  # 絶対にsortを降順にしたくない
_A.sort() # lamda使いたくない
for ii in range(X):
    passed[_A[ii][1]] += 1

# english
_B = [ [-B[i], i] for i in range(N) if passed[i] == 0]  # 絶対にsortを降順にしたくない
_B.sort() # lamda使いたくない
for ii in range(Y):
    passed[_B[ii][1]] += 1

# math + english
_C = [ [-(A[i]+B[i]), i] for i in range(N) if passed[i] == 0]  # 絶対にsortを降順にしたくない
_C.sort() # lamda使いたくない
for ii in range(Z):
    passed[_C[ii][1]] += 1

# result
[print(ii+1) for ii in range(N) if passed[ii] == 1]

