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

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
N = int(input())
A = [0] + list(map(int, input().split()))
#print(A)
d = defaultdict(int)

# 最初の世代
d[1] = 0
gen = 0
# 世代を求める
for ii in range(1, N+1):
    a = A[ii]
#    gen += 1
#    print(a)
    gen = d[a]
    a1 = 2*(ii)
    a2 = 2*(ii) + 1
    if d[a1] == 0:
        d[a1] = gen + 1
    if d[a2] == 0:
        d[a2] = gen + 1

# 答えを出力
for ii in range(1, 2*N+1+1):
    print(d[ii])
