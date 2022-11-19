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
a, b, d =map(int, input().split())
theta = d * math.pi / 180
x = a*(math.cos(theta)) - b*(math.sin(theta))
y = a*(math.sin(theta)) + b*(math.cos(theta))
print(x,y)
