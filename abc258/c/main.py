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

#3 3
#abc
#2 2
#1 1
#2 2

N, Q = map(int, input().split())
S = input()
#print(S)
#print(len(S))
cnt = 0
for ii in range(Q):
    q1, q2 = map(int, input().split())

    if q1 == 1:
        cnt += q2
    if q1 == 2:
        # 0-index
        q2 -= 1
        idx = (q2-cnt)%len(S)
        print(S[idx])

