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
N, M, X, T, D =map(int, input().split())

# 100 10 100 180 1
# 

# N歳の時にTcm
ans = 0
if M >= X:
    ans = T
else:
    zero_height = T - D * X
    ans = D * M + zero_height
print(ans)
