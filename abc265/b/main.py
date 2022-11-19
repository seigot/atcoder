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
N,M,T=map(int, input().split())
A = list(map(int, input().split()))
X = defaultdict(int)
for ii in range(M):
    x, y = map(int, input().split())
    x -= 1
    X[x] = y

#print(A)
#print(N)
#print(X)
currentT = T
for ii in range(N-1):
    #print("--", ii)
    #print(currentT)
    currentT += X[ii]
    #print(currentT)
    currentT -= A[ii]
    #print(currentT)
    if currentT <= 0:
        print("No")
        exit(0)
print("Yes")
    