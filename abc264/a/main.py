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
L,R=map(int, input().split())
s = "atcoder"
print(s[L-1:R])


#print(s[0:1])
#print(s[0:2])
#print(s[:2])
#print(s[-1])
#print(s[::-1])
#print(s[-3:-1])
