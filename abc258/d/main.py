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

#3 4
#3 4
#2 3
#4 2

N, X = map(int,input().split())
AB = []
SumAB = []
for ii in range(N):
    A, B = map(int,input().split())
    AB.append([A,B])

    if ii == 0:
        SumAB.append(A+B)
    else:
        SumAB.append(A+B+SumAB[ii-1])
#print(SumAB)
# 全探索
ans = INF
cnt = 0
for target_i in range(min(X,N)):
    # 着目しているiのBの値
    tB = AB[target_i][1]
    # 累積和を足す
    cnt = 0
    cnt += SumAB[target_i]
    # 残り全部足す
    cnt += (tB * (X-(target_i+1)))
    # 最小を見つける
    if cnt < ans:
        ans = cnt
print(ans)
