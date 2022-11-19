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
A = list(map(int, input().split()))

import itertools

length = ""
for ii in range(N):
    length = length + str(ii)
#print(length)

for ii in range(N):
    A[ii] = str(A[ii] - 1)
#print(A)

prev = None
for x in itertools.permutations(length):
    print(list(x))
    if list(x) == A:
#        print("same")
        ans = [0] * N
        for ii in range(N):
            ans[ii] = int(prev[ii]) + 1
        print(*ans)
        exit(0)
    prev = x
