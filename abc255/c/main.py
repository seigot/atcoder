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

# 6 2 3 3
#   A D N
#   [2 5 8]
ans = 0
X, A, D, N = map(int,input().split())

S = [A]

FirstVal = A
EndVal = A + D*(N-1)
if D < 0:
    FirstVal = A + D*(N-1)
    EndVal = A
#print(FirstVal,EndVal)

# 初項より小さい場合
if X <= FirstVal:
    ans = FirstVal - X
    print(ans)
    exit()
# 末項より大きい場合
if X >= EndVal:
    ans = X - EndVal
    print(ans)
    exit()
# 数列の中にある場合
Val = (X - A) % D
ans = min(abs(Val), abs(D - Val))
print(ans)