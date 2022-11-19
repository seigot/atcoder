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
N, X, Y = map(int, input().split())

# red, blue
red = [0] * (N+1)
blue = [0] * (N+1)

# init
red[N] = 1

# print(red)
# level N毎に段階的に処理する
for ii in range(N, 1, -1):
    lv = ii
    if red[lv] > 0:
        red[lv-1] += red[lv]
        blue[lv] += red[lv] * X
    if blue[lv] > 0:
        red[lv-1] += blue[lv]
        blue[lv-1] += blue[lv] * Y

#print(red)
#print(blue)
print(blue[1])
