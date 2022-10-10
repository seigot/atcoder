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

A.sort(reverse=True)
Odd = []  # 奇数
Even = [] # 偶数
for ii in range(len(A)):
    val = A[ii]
    if val % 2 == 1:
        Odd.append(val)
    else:
        Even.append(val)
ans = -1
if len(Odd) >= 2:
    ans = max(ans, (Odd[0]+Odd[1]))
if len(Even) >= 2:
    ans = max(ans, (Even[0]+Even[1]))
print(ans)
