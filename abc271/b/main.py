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
N,Q=map(int, input().split()) 

LN = []
ST = []

for ii in range(N):
    ln = list(map(int, input().split()) )
    LN.append(ln)

for ii in range(Q):
    s,t = map(int, input().split()) 
    ST.append((s,t))

#print(LN)
#print(ST)
for ii in range(len(ST)):
    s = ST[ii][0]
    t = ST[ii][1]
#    print(s,t)
    print(LN[s-1][t])
