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
A=[0] + list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An
Q=int(input())                     # (1)数字が1つ 入力例:N

# 1 xq ： A のすべての要素に xq を代入する。
# 2 i q xq ： Aiq に xq  を加える。
# 3 i q： Ai q の値を出力する。

addall = 0
Query = []

d = defaultdict(int)
for ii in range(len(A)):
    d[ii] = A[ii]
for ii in range(Q):
    q = list(map(int, input().split()))
    Query.append(q)

for ii in range(Q):
    q = Query[ii]
    if q[0] == 1:
        d = defaultdict(int)
        addall = q[1]
    if q[0] == 2:
        d[q[1]] = d[q[1]] + q[2]
    if q[0] == 3:
        val = d[q[1]] + addall
        print(val)
