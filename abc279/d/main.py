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

def funct(g):
    if g < 0:
        return INF
    val = g*B + A/((g+1)**0.5)
    return val

# 三分探索
upper = 10**18
lowwer = 0
while upper - lowwer > 2:
    tl = (lowwer*2 + upper)//3
    tr = (lowwer + upper*2)//3
    val_tl = funct(tl)
    val_tr = funct(tr)

    # 傾きを求めて値を進める
    if val_tl < val_tr:
        upper = tr
    else:
        lowwer = tl

# 極小値
val = INF
for ii in range(lowwer-10**3, upper+10**3, 1):
    val = min(val, funct(ii))
print(val)
