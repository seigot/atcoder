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


d = defaultdict(int)
d[0] = 1
d[3] = 1
d[9] = 1

print(d)
print(len(d))
print(d.keys())
print("--")
for ii in range(len(d)):
    print(d[ii])
print("--")
for ii in d.keys():
    print(ii)
#    print(d[ii])

