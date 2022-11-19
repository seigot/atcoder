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
N, x, y=map(int, input().split()) 
A = list(map(int, input().split()))

# p1 = (0,0)
# p2 = (Ai,0)
# pN = (Ax,0)
# pN+1 = (x,y)
# 点 piと点 pi+1の距離はAi(1≤i≤N)
# 線分pi pi+1 と線分pi+1 pi+2のなす角は 90 度 (1≤i≤N−1)

# 深さ優先探索?
def dfs(tx, ty, depth, pdx, pdy):

    cx = tx
    cy = ty
#    global cdepth 
    cdepth = depth
    #print(cx, cy, cdepth, pdx, pdy , x, y)

    if cdepth == N:
        if cx == x and cy == y:
            print("Yes")
            exit(0)
        else:
            return 0

    # search next
    cdist = A[cdepth]
    if cdepth == 0:
        # p2 = (Ai,0)の制約
        dx, dy = (1, 0)
        dfs(cx + cdist*dx , cy + cdist*dy, cdepth+1 ,dx , dy)
    else:
#        for ii in dpos4:
#            dx, dy = ii
#            if (pdx, pdy) != (dx, dy) and (pdx, pdy) != (-1*dx, -1*dy):
#                dfs(cx + cdist*dx , cy + cdist*dy, cdepth+1 ,dx , dy)
        if pdx == 1 or pdx == -1:
            dx = 0
            dy = 1
        else:
            dx = 1
            dy = 0
        dfs(cx + cdist*dx , cy + cdist*dy, cdepth+1 ,dx , dy)
        dfs(cx + cdist*dx*(-1) , cy + cdist*dy*(-1), cdepth+1 ,dx , dy)

    return 0

dfs(0, 0, 0, 0, 0)
print("No")
