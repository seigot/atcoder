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

N,K=map(int, input().split())
A=list(map(int, input().split()))
Q=int(input())
lr = []
for _ in range(Q):
    l,r=map(int, input().split())
    l -= 1
    r -= 1
    lr.append((l,r))

# Kおきの累積和
comm = [0]*(N)
for ii in range(N):
    if ii < K:
        comm[ii] = A[ii]
    else:
        comm[ii] = comm[(ii-K)] + A[ii]
#print(comm)

# 区間l,rの累積和を取得して、全て同じ値かどうかをチェックする
for ii in range(len(lr)):
    l,r = lr[ii]
#    print(l,r)
    LRcomm = [0]*K
    for ti in range(K):
        lidx = l+ti
        ridx = lidx + K*((r-l)//K)
        if ridx > r:
            ridx -= K
#        print(lidx,ridx)
        LRcomm[ti] = comm[ridx] - comm[lidx] + A[lidx]
#    print(LRcomm)
    if len(set(LRcomm)) == 1:
        print("Yes")
    else:
        print("No")


