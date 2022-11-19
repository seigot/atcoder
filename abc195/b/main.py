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

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
A,B,W=map(int, input().split())  

W *= 1000

minV=INF
maxV=0
# 可能性を全探索する(10**6+1)
for ii in range(1,10**6+1):
    val = W / ii
    if A <= val <= B:
        minV = min(minV, ii)
        maxV = max(maxV, ii)

if minV != INF:
    print(minV, maxV)
else:
    print("UNSATISFIABLE")
