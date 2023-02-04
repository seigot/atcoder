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

N,K=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
A=deque(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An

for ii in range(K):
    A.popleft()
    A.append(0)
print(*A)

