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

N = int(input())
A = list(map(int, input().split()))

ans = 0
sum = 0
for ii in range(N):
    val = A[ii]
    sum += 1
    for jj in range(val):
        sum = sum << 1
        if sum >= 16:
            sum -= 16
            ans += 1
print(ans)
