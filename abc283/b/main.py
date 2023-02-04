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

N=int(input())                     # (1)数字が1つ 入力例:N
A=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An
Q=int(input())                     # (1)数字が1つ 入力例:N

for ii in range(Q):
    q = list(map(int, input().split())) 
#    print(q)
    if q[0] == 1:
        k = q[1]
        x = q[2]
        A[k-1] = x
    elif q[0] == 2:
        k = q[1]
        print(A[k-1])
