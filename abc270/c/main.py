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

N,X,Y=map(int, input().split())
UV = [[] for ii in range(N+1)]
for ii in range(N-1):
    U,V = map(int, input().split())
    UV[U].append(V)
    UV[V].append(U)
#print(UV)
#print(len(UV[2]))
#print("--")

# dfs
dq = deque()
def dfs(cnum, parentnum):
    # enqueue
    dq.append(cnum)
    #print(cnum)
    for ii in range(len(UV[cnum])):
        tnum = UV[cnum][ii]
        #print(tnum)
        if tnum == Y:
            print(*dq, Y)
            exit(0)
        if tnum != parentnum:
            dfs(tnum, cnum)
    dq.pop()
    return 0

dfs(X, -1)
