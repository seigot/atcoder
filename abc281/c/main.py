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

N,T=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
A=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An

sumA = sum(A)

# 周期の余りを取得
T = T%sumA
for ii in range(len(A)):
    val = A[ii]
    if T < val:
        print(ii+1, T)
        exit()
    T -= val
