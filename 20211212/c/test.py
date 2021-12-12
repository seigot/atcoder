#!/bin/python

import sys
from bisect import bisect_left, bisect_right

def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)

N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = []
#リストAにappend()を使って格納していく
for _ in range(Q):
    X.append(int(input()))

error(N,Q)
error(A)
error(X)
A2 = sorted(A)
error(A2)
for i in range(Q):
    #r = bisect_right(A2, X[i]-1)
    l = bisect_left(A2, X[i])
    print(N - l)
