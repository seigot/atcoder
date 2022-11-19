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

N=int(input())  
ss = set()
s0 = "HDCS"
s1 = "A23456789TJQK"
for ii in range(N):
    s = input()
#    print(s)
    if s[0] not in s0 or s[1] not in s1: 
        print("No")
        exit()
    if s in ss:
#        print(s)
        print("No")
        exit()
    ss.add(s)
#    ss.append(s)
print("Yes")
