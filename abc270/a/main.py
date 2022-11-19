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
A,B=map(int, input().split())

#print(A|B)

AA = [0]*3
BB = [0]*3
CC = [0]*3

AA[0] = A // 4
AA[1] = (A % 4) //2
AA[2] = (A % 4) % 2
BB[0] = B // 4
BB[1] = (B % 4) //2
BB[2] = (B % 4) % 2
CC[0] = AA[0] | BB[0]
CC[1] = AA[1] | BB[1]
CC[2] = AA[2] | BB[2]
#print(AA)
#print(BB)
#print(CC)
print(CC[0]*4 + CC[1]*2 + CC[2]*1)
