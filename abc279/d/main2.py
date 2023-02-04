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

A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B

# t = g*B + A*(g**0.5)
def funct(g):
    if g < 0:
        return INF
    val = g*B + A/((g+1)**0.5)
    return val

x = (A/(2*B))**(2/3)-1
x = int(x//1)
#print(x)

mval = INF
for ii in range(x-5, x+5, 1):
    mval = min(mval, funct(ii))
print(mval)
