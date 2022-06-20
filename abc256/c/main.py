#!/usr/bin/env python3
import sys
from zlib import adler32
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
h1, h2, h3, w1, w2, w3 = map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
#print(h1, h2, h3, w1, w2, w3)

#####
# ii jj x h1
# uu vv x h2
# x  x  x h3
# w1 w2 w3

#####
# A11 A12 A13 h1
# A21 A22 A23 h2 
# A31 A32 A33 h3
# w1  w2  w3

# 30*30*30*30 = 10**6くらい
ans = 0
for ii in range(1,29):
    for jj in range(1,29):
        for uu in range(1,29):
            for vv in range(1,29):
                A11 = ii
                A12 = jj
                A21 = uu
                A22 = vv

                A13 = h1 - A11 - A12
                if A13 < 1:
                    continue
                A23 = h2 - A21 - A22
                if A23 < 1:
                    continue
                A31 = w1 - A11 - A21
                if A31 < 1:
                    continue
                A32 = w2 - A12 - A22
                if A32 < 1:
                    continue
                A33 = w3 - A13 - A23
                if A33 < 1:
                    continue
                if A31 + A32 + A33 != h3:
                    continue
                ans += 1
print(ans)
