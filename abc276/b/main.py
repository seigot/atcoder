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

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
N,M=map(int, input().split())
gh = [[] for _ in range (N+1)] 
#print("--")
for ii in range(M):
    a, b = map(int, input().split())
#    print(a,b)
    gh[a].append(b)
    gh[b].append(a)

#print(gh)
for ii in range(1, N+1):
#    print(ii)
    print(len(gh[ii]), *sorted(gh[ii]))

