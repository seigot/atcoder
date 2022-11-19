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

#4 2
#5 4 -1 8

N,M = map(int, input().split()) 
A = list(map(int, input().split()))

#print(A)
accum = [0] * N
for ii in range(M-1, N):
#    if ii == 0:
#        accum[ii] = A[ii]
#    else:
#        accum[ii] = A[ii] + #accum[ii-1]
    if ii == M-1:
        for jj in range(M):
            accum[ii] += A[jj]
    else:
            accum[ii] = A[ii] + accum[ii-1] - A[ii-M]

#print(accum)

# 合計を求める
ans = MINF
for ii in range(M-1, N):
    #print("---",ii)
    if ii == M-1:
        sum = 0
        for jj in range(M):
            #sum += A[ii+jj] * (jj+1)
            sum += A[jj] * (jj+1)
    else:
        sum -= accum[ii-1]
        #print(sum)
        sum += A[ii] * M 

    #print("sum",sum)
    ans = max(sum, ans)

print(ans)
