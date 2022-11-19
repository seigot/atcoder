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
N,P,Q,R=map(int, input().split())
A=list(map(int, input().split()))

SumA = [0] * (N)
for ii in range(N):
    if ii == 0:
        SumA[ii] = A[ii]
    else:
        SumA[ii] = SumA[ii-1] + A[ii]
SumA += [INF] # banpei
#print(SumA)

# SumAは必ず昇順になる
for xx in range(N):
    if xx == 0:
        offsetx = 0
    else:
        offsetx = SumA[xx-1] # 1つ前までの和
    X = offsetx + P
    Y = X + Q
    Z = Y + R
    # 値がちょうどX,Y,Zになるものを見つける
    idx_x = bisect_left(SumA, X)
    idx_y = bisect_left(SumA, Y)
    idx_z = bisect_left(SumA, Z)
    #print("---")
    #print(X,Y,Z)
    #print(idx_x,idx_y,idx_z)
    if SumA[idx_x] == X and SumA[idx_y] == Y and SumA[idx_z] == Z:
        print("Yes")
        exit(0)
print("No")