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
X, Y, Z = map(int, input().split()) 

# X: goal
# Y: wall
# Z: hammer

# ゴールを常に正の位置に置く
if Y < 0:
    X *= -1
    Y *= -1
    Z *= -1

ans = 0
#1. goalが壁の向こうにない場合 --> 直接goalへ向かう
#2. goalが壁の向こうにある場合 --> hammerをとってからgoalへ向かう
##2.1  hammerが壁の向こうにある場合 --> NG
##2.2  hammerが壁の向こうにない場合 --> hammerをとってからgoalへ向かう

#1. goalが壁の向こうにない場合 --> 直接goalへ向かう
if X < Y:
    ans = abs(X)
    print(ans)
    exit(0)

#2. goalが壁の向こうにある場合 --> hammerをとってからgoalへ向かう
##2.1  hammerが壁の向こうにある場合 --> NG
if Y < Z:
    ans = -1
    print(ans)
    exit(0)

##2.2  hammerが壁の向こうにない場合 --> hammerをとってからgoalへ向かう
ans += abs(Z)
ans += X - Z
print(ans)
